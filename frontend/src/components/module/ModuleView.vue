<script>
import AlertMessage from '@/components/ui/AlertMessage.vue';
import SearchField from '@/components/ui/SearchField.vue';
import TableStructure from '@/components/table/TableStructure.vue';
import BackendConnection from '@/components/BackendConnection.vue';
import ExportButton from './ExportButton.vue';
import ImportButton from './ImportButton.vue';
import ModalFilesView from '@/components/modals/ModalFilesView.vue';
import Lenguages from '@/assets/config/lenguages';
import Fields from '@/assets/config/fields';

export default {
  props: ['token', 'user', 'moduleName', 'modulesAlt', 'hasPermission', 'updateToken'],
  data() {
    return {
      Lenguages: Lenguages,
      Fields: Fields,
      original: [],
      models: [],
      auxiliar: [],
    };
  },
  created() {
    if (!this.token) this.$router.push('/logout');
    else if (!this.user) this.$router.push('/logout');
    else if (!this.hasPermission(this.moduleName, 'access')) this.$router.push('/');
    this.title = this.Lenguages[this.Lenguages.selected].menu.modules[this.moduleName];
  },
  methods: {
    showMessage(_text, _type) {
      this.$refs.AlertMessage.show(_text, _type);
    },
    searchData(models) {
      this.models = models;
    },
    exportData(model = 0) {
      if (model == 1) this.$refs.ExportButton.exportFile(this.original, this.fields, this.moduleName);
      else this.$refs.ExportButton.exportFile(this.models, this.fields, this.moduleName);
    },
    sortBy(field, type, desc = false) {
      this.models.sort((a, b) => {
        let x = a[field];
        let y = b[field];
        if (typeof x == 'string') x = x.toLowerCase();
        if (typeof y == 'string') y = y.toLowerCase();
        if (!desc) {
          if (x < y) return -1;
          if (x > y) return 1;
          return 0;
        } else {
          if (x < y) return 1;
          if (x > y) return -1;
          return 0;
        }
      });
    },
    showModal() {
      this.$refs.ModalImport.showModal();
    },
    uploadFile(file) {
      this.processFile(file.extension, file.resource);
      this.$refs.ModalImport.closeModal();
    },
    async getData() {
      try {
        const modName = this.moduleName == 'screen' ? 'orders' : this.moduleName;
        const data = await this.$refs.BackendConnection.getAll(modName);
        this.fields = this.Fields[this.moduleName].fields;
        this.original = this.models = data.data.map((d) => new this.Fields[this.moduleName].Model(d));
      } catch (error) {
        console.log(error);
      }
    },
    async createOne(model) {
      try {
        const data = await this.$refs.BackendConnection.createOne(this.moduleName, model);
        this.showMessage(this.Lenguages[this.Lenguages.selected].general.create_ok, 'success');
        this.original.push(new this.Fields[this.moduleName].Model(data.data));
      } catch (error) {
        console.log(error);
      }
    },
    async updateOne(index, model) {
      try {
        if (this.moduleName == 'trucks') model.id = model.truck_id;
        else if (this.moduleName == 'foods') model.id = model.food_id;
        else if (this.moduleName == 'orders') model.id = model.order_id;
        const data = await this.$refs.BackendConnection.updateOne(this.moduleName, model);
        this.showMessage(this.Lenguages[this.Lenguages.selected].general.update_ok, 'success');
        this.original[index] = new this.Fields[this.moduleName].Model(data.data);
      } catch (error) {
        console.log(error);
      }
    },
    async deleteOne(index, model) {
      try {
        if (this.moduleName == 'trucks') model.id = model.truck_id;
        else if (this.moduleName == 'foods') model.id = model.food_id;
        else if (this.moduleName == 'orders') model.id = model.order_id;
        await this.$refs.BackendConnection.deleteOne(this.moduleName, model);
        this.showMessage(this.Lenguages[this.Lenguages.selected].general.delete_ok, 'success');
        this.getData()
      } catch (error) {
        console.log(error);
      }
    },
    async processFile(type, file) {
      try {
        const data = await this.$refs.BackendConnection.processFile(this.moduleName, type, file);
        data.data.forEach((d) => {
          this.original.push(d);
          this.models.push(d);
        });
        this.showMessage(this.Lenguages[this.Lenguages.selected].general.import_ok, 'success');
      } catch (error) {
        console.log(error);
      }
    },
  },
  components: {
    AlertMessage,
    SearchField,
    ExportButton,
    ImportButton,
    ModalFilesView,
    TableStructure,
    BackendConnection,
  },
  mounted() {
    if (this.hasPermission(this.moduleName, 'access')) this.getData();
    else this.$router.push('/');
  }
}
</script>

<template>
  <div class="row pt-3 w-100">
    <div class="col">
      <h1 id="moduleTitle">{{ title }}</h1>
    </div>
    <div v-if="moduleName != 'screen'" class="col py-2">
      <div class="btn-group">
        <SearchField :original="original" @searchData="searchData" />
        <ExportButton v-if="hasPermission(moduleName, 'export')" ref="ExportButton" @exportData="exportData" />
        <ImportButton v-if="hasPermission(moduleName, 'import')" :moduleName="moduleName" @importFile="showModal" />
      </div>
    </div>
  </div>
  <AlertMessage ref="AlertMessage" class="row pt-1" />
  <TableStructure :token="token" :user="user" :moduleName="moduleName" :modulesAlt="modulesAlt" :fields="fields"
    :models="models" :auxiliar="auxiliar" :hasPermission="hasPermission" @showMessage="showMessage" @createOne="createOne"
    @updateOne="updateOne" @deleteOne="deleteOne" @sortBy="sortBy" />
  <ModalFilesView :token="token" :user="user" :moduleName="moduleName" :models="[]" :hasPermission="hasPermission"
    ref="ModalImport" @showMessage="showMessage" @uploadFile="uploadFile" />
  <BackendConnection :token="token" :user="user" ref="BackendConnection" @showMessage="showMessage" />
</template>

<style></style>
