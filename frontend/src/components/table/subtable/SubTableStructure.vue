<script>
import TableHeaders from '@/components/table/TableHeaders.vue';
import TableFirstRow from '@/components/table/TableFirstRow.vue';
import SubTableRow from './SubTableRow.vue';

import Lenguages from '@/assets/config/lenguages';

export default {
  props: ['moduleName', 'fields', 'models', 'auxiliar', 'editable', 'hasPermission'],
  emits: ['showMessage', 'createOne', 'updateOne', 'deleteOne', 'sortBy'],
  data() {
    return {
      Lenguages: Lenguages,
    };
  },
  methods: {
    showMessage(_text, _type) {
      this.$emit('showMessage', _text, _type);
    },
    createOne(model) {
      this.$emit('createOne', this.moduleName, model);
    },
    updateOne(index, model) {
      this.$emit('updateOne', this.moduleName, index, model);
    },
    deleteOne(index, model) {
      this.$emit('deleteOne', this.moduleName, index, model);
    },
    duplicateOne(index, model) {
      console.log(this.$refs, model)
      this.$refs.FirstRow.setModel(model);
    },
    sortBy(field, type, desc = false) {
      this.$emit('sortBy', this.moduleName, field, type, desc);
    },

  },
  components: {
    TableHeaders,
    TableFirstRow,
    SubTableRow,
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
        <template v-for="(element, index) in models" :key="index">
          <SubTableRow :token="token" :user="user" :moduleName="moduleName" :modulesAlt="modulesAlt" :fields="fields"
            :auxiliar="auxiliar" :editable="editable" :index="index" :original="element" :hasPermission="hasPermission"
            @showMessage="showMessage" @updateOne="updateOne" @deleteOne="deleteOne" @duplicateOne="duplicateOne" />
        </template>
      </tbody>
    </table>
  </div>
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
