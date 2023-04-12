<script>
import ViewCell from '@/components/cells/ViewCell.vue';
import CheckCell from '@/components/cells/CheckCell.vue';
import NumberCell from '@/components/cells/NumberCell.vue';
import TextCell from '@/components/cells/TextCell.vue';
import DateCell from '@/components/cells/DateCell.vue';
import EmailCell from '@/components/cells/EmailCell.vue';
import PasswordCell from '@/components/cells/PasswordCell.vue';
import ComboCell from '@/components/cells/ComboCell.vue';
import MultipleCell from '@/components/cells/MultipleCell.vue';
import TabsStructure from '@/components/table/TabsStructure.vue';
import BackendConnection from '@/components/BackendConnection.vue';
import SubTableStructure from './subtable/SubTableStructure.vue';
import Lenguages from '@/assets/config/lenguages';

export default {
  props: ['token', 'user', 'moduleName', 'modulesAlt', 'fields', 'auxiliar', 'editable', 'index', 'original', 'hasPermission'],
  emits: ['showMessage', 'updateOne', 'deleteOne', 'duplicateOne'],
  data() {
    return {
      Lenguages: Lenguages,
      model: {},
      models: {},
      change: false,
    };
  },
  created() {
    this.model = this.original;
  },
  computed: {
    cells() {
      return this.fields;
    },
  },
  methods: {
    showMessage(_text, _type) {
      this.$emit('showMessage', _text, _type);
    },
    updateOne() {
      const errors = [];
      this.fields.forEach((field) => {
        if (!this.$refs[field.id][0].validate()) errors.push(field);
      });
      if (!errors.length) this.$emit('updateOne', this.index, this.model);
      else this.showMessage(this.Lenguages[this.Lenguages.selected].general.validation_err, 'warning');
      this.fields.forEach((field) => {
        this.$refs[field.id][0].restore();
      });
      this.change = false;
    },
    deleteOne() {
      this.model.reason = window.prompt(this.Lenguages[this.Lenguages.selected].general.delete_ask, '');
      if (this.model.reason == null || this.model.reason == '') return;
      this.$emit('deleteOne', this.index, this.model);
      this.change = false;
    },
    duplicateOne() {
      this.$emit('duplicateOne', this.index, this.model);
    },
    cellChange(name, value) {
      this.change = true;
      this.model[name] = value;
    },
    cellValue(field) {
      this.model = this.original;
      return this.model[field];
    },
    sortBy(modAlt, field, type, desc = false) {
      this.models[modAlt].data.sort((a, b) => {
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
    getAlts(index) {
      const alts = [];
      for (const key in this.modulesAlt) alts.push(key + index);
      return alts;
    },
    getModule(mod) {
      return mod.replace(/[0-9]/, '');
    },
    expandTable() {
      const el = document.getElementById('subtable' + this.index);
      if (el.classList.contains('hidden')) {
        Object.entries(this.modulesAlt).forEach(async ([modAlt, patern]) => {
          try {
            const data = await this.$refs.BackendConnection.getAll(modAlt + '/' + this.moduleName + '/' + this.model.id);
            this.models[modAlt] = data;
            if (this.moduleName == 'humans') this.models[modAlt].auxiliar['users'] = [this.model];
            else this.models[modAlt].auxiliar[this.moduleName] = [this.model];
          } catch (error) {
            console.log(error)
          }
        });
      }
      el.classList.toggle('hidden');
    },
    getInformation(slotName, type) {
      const name = this.getModule(slotName);
      if (!this.models || !this.models[name]) return [];
      if (this.models[name][type]) return this.models[name][type];
      else return [];
    },
    async createRelation(moduleName, model) {
      try {
        const data = await this.$refs.BackendConnection.createOne(moduleName, model);
        this.models[moduleName].data.push(data.data);
      } catch (error) {
        console.log(error)
      }
    },
    async updateRelation(moduleName, index, model) {
      try {
        const data = await this.$refs.BackendConnection.updateOne(moduleName, model);
        this.models[moduleName].data[index] = data.data;
      } catch (error) {
        console.log(error)
      }
    },
    async deleteRelation(moduleName, index, model) {
      try {
        await this.$refs.BackendConnection.deleteOne(moduleName, model);
        this.models[moduleName].data.slice(index, 1);
      } catch (error) {
        console.log(error)
      }
    },
  },
  components: {
    ViewCell,
    CheckCell,
    NumberCell,
    TextCell,
    DateCell,
    EmailCell,
    PasswordCell,
    ComboCell,
    MultipleCell,
    TabsStructure,
    SubTableStructure,
    BackendConnection,
  }
}
</script>

<template>
  <tr :id="'row-' + index" :class="{ 'bg-warning': change }">
    <td v-if="editable">
      <div class="btn-group">
        <button v-if="hasPermission(moduleName, 'update') && change" type="button" data-toggle="tooltip"
          data-placement="bottom" :title="Lenguages[Lenguages.selected].general.save" class="btn btn-success"
          @click="updateOne">
          <i class="fa-solid fa-floppy-disk"></i>
        </button>
        <button v-if="editable && hasPermission(moduleName, 'create')" type="button" data-toggle="tooltip"
          data-placement="bottom" :title="Lenguages[Lenguages.selected].general.duplicate" class="btn btn-primary"
          @click="duplicateOne">
          <i class="fa-solid fa-copy"></i>
        </button>
        <button v-if="hasPermission(moduleName, 'delete')" type="button" data-toggle="tooltip" data-placement="bottom"
          :title="Lenguages[Lenguages.selected].general.delete" class="btn btn-danger" @click="deleteOne">
          <i class="fa-solid fa-trash"></i>
        </button>
        <button v-if="Object.keys(modulesAlt).length" type="button" data-toggle="tooltip" data-placement="bottom"
          :title="Lenguages[Lenguages.selected].general.expand" class="btn btn-dark" @click="expandTable">
          <i class="fa-solid fa-caret-down"></i>
        </button>
      </div>
    </td>
    <td v-for="(field, i) in cells" :key="i" scope="row">
      <ViewCell v-if="field.type == 1" :id="field.id" :name="field.name" :properties="field.properties"
        :auxiliar="auxiliar" :index="index" :original="cellValue(field.name)" :ref="field.id" />
      <CheckCell v-if="field.type == 2" :id="field.id" :name="field.name" :properties="field.properties"
        :auxiliar="auxiliar" :index="index" :original="cellValue(field.name)" :ref="field.id" @cellChange="cellChange"
        @showMessage="showMessage" />
      <NumberCell v-if="field.type == 3" :id="field.id" :name="field.name" :properties="field.properties"
        :auxiliar="auxiliar" :index="index" :original="cellValue(field.name)" :ref="field.id" @cellChange="cellChange"
        @showMessage="showMessage" />
      <TextCell v-if="field.type == 4" :id="field.id" :name="field.name" :properties="field.properties"
        :auxiliar="auxiliar" :index="index" :original="cellValue(field.name)" :ref="field.id" @cellChange="cellChange"
        @showMessage="showMessage" />
      <DateCell v-if="field.type == 5" :id="field.id" :name="field.name" :properties="field.properties"
        :auxiliar="auxiliar" :index="index" :original="cellValue(field.name)" :ref="field.id" @cellChange="cellChange"
        @showMessage="showMessage" />
      <EmailCell v-if="field.type == 6" :id="field.id" :name="field.name" :properties="field.properties"
        :auxiliar="auxiliar" :index="index" :original="cellValue(field.name)" :ref="field.id" @cellChange="cellChange"
        @showMessage="showMessage" />
      <PasswordCell v-if="field.type == 7" :id="field.id" :name="field.name" :properties="field.properties"
        :auxiliar="auxiliar" :index="index" :original="cellValue(field.name)" :ref="field.id" @cellChange="cellChange"
        @showMessage="showMessage" />
      <ComboCell v-if="field.type == 8" :id="field.id" :name="field.name" :properties="field.properties"
        :auxiliar="auxiliar" :index="index" :original="cellValue(field.name)" :ref="field.id" @cellChange="cellChange"
        @showMessage="showMessage" />
      <MultipleCell v-if="field.type == 9" :id="field.id" :name="field.name" :properties="field.properties"
        :auxiliar="auxiliar" :index="index" :original="cellValue(field.name)" :ref="field.id" @cellChange="cellChange"
        @showMessage="showMessage" />
    </td>
  </tr>
  <tr v-if="Object.keys(modulesAlt).length" :id="'subtable' + index" class="hidden">
    <td :colspan="fields.length + editable">
      <TabsStructure :tabList="Object.keys(modulesAlt)" :index="index">
        <template v-for="slotName in getAlts(index)" v-slot:[slotName]>
          <template v-if="hasPermission(getModule(slotName), 'access')">
            <SubTableStructure :moduleName="getModule(slotName)" :fields="getInformation(slotName, 'fields')"
              :models="getInformation(slotName, 'data')" :auxiliar="getInformation(slotName, 'auxiliar')"
              :editable="editable" :hasPermission="hasPermission" @showMessage="showMessage" @createOne="createRelation"
              @updateOne="updateRelation" @deleteOne="deleteRelation" @sortBy="sortBy" />
          </template>
        </template>
      </TabsStructure>
    </td>
  </tr>
  <tr v-if="Object.keys(modulesAlt).length" class="hidden"></tr>
  <BackendConnection v-if="Object.keys(modulesAlt).length" :token="token" :user="user" :moduleName="moduleName"
    ref="BackendConnection" @showMessage="showMessage" />
</template>

<style>
.hidden {
  display: none;
}
</style>
