<script>
import TableHeaders from './TableHeaders.vue';
import TableFirstRow from './TableFirstRow.vue';
import TableRow from './TableRow.vue';
import PageGenerator from './PageGenerator.vue';
import Lenguages from '@/assets/config/lenguages';

export default {
  props: ['token', 'user', 'moduleName', 'modulesAlt', 'fields', 'models', 'auxiliar', 'hasPermission'],
  emits: ['showMessage', 'createOne', 'updateOne', 'deleteOne', 'sortBy'],
  data() {
    return {
      Lenguages: Lenguages,
      model: {},
      submodels: {},
      editable: true,
    };
  },
  created() {
    if (this.moduleName == 'screen') this.editable = false;
    for (const key in this.modulesAlt) this.submodels[key] = [];
  },
  computed: {
    display() {
      if (this.models.length) return this.$refs.PageGenerator.paginate(this.models);
      else return [];
    }
  },
  methods: {
    showMessage(_text, _type) {
      this.$emit('showMessage', _text, _type);
    },
    createOne(model) {
      this.$emit('createOne', model);
    },
    updateOne(index, model) {
      this.$emit('updateOne', index, model);
    },
    deleteOne(index, model) {
      this.$emit('deleteOne', index, model);
    },
    duplicateOne(index, model) {
      this.$refs.FirstRow.setModel(model);
    },
    sortBy(field, type, desc = false) {
      this.$emit('sortBy', field, type, desc);
    },

    format(value, format, target) {
      if (format) {
        if (format == 'datetime') return new Date(value).toLocaleString();
        else if (format == 'date') return new Date(value).toLocaleDateString();
        else if (format == 'time') return new Date(value).toLocaleTimeString();
        else if (format == 'checkbox') return value ? this.Lenguages[this.Lenguages.selected].general.yes : this.Lenguages[this.Lenguages.selected].general.not;
        else if (format == 'combobox' || format == 'status') {
          const found = this.auxiliar[target].find(aux => aux._id === value);
          if (found) return found.name;
          else return value;
        }
        else if (format == 'multiple') {
          let values = '';
          value.forEach(val => {
            const found = this.auxiliar[target].find(aux => aux._id === val);
            if (found) values += found.name + '\n';
          });
          return values;
        }
      } else return value;
    },
  },
  components: {
    TableHeaders,
    TableFirstRow,
    TableRow,
    PageGenerator
  }
}
</script>

<template>
  <div class="row mt-1">
    <table class="table table-striped mt-3 m-2">
      <TableHeaders :editable="editable" :fields="fields" @sortBy="sortBy" />
      <tbody>
        <TableFirstRow :moduleName="moduleName" :fields="fields" :auxiliar="auxiliar" :editable="editable"
          :hasPermission="hasPermission" @showMessage="showMessage" @createOne="createOne" ref="FirstRow" />
        <template v-for="(element, index) in display" :key="index">
          <TableRow :token="token" :user="user" :moduleName="moduleName" :modulesAlt="modulesAlt" :fields="fields"
            :auxiliar="auxiliar" :editable="editable" :index="index" :original="element" :hasPermission="hasPermission"
            @showMessage="showMessage" @updateOne="updateOne" @deleteOne="deleteOne" @duplicateOne="duplicateOne" />
        </template>
      </tbody>
    </table>
  </div>
  <PageGenerator ref="PageGenerator" />
</template>

<style>
@media (max-width: 500px) {

  input[type=text],
  input[type=email],
  input[type=date],
  input[type=password],
  input[type=number],
  td select {
    width: 100%;
  }

  input[type=checkbox] {
    width: 30px;
    height: 30px;
  }
}
</style>
