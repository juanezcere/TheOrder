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
import Lenguages from '@/assets/config/lenguages';

export default {
  props: ['moduleName', 'fields', 'auxiliar', 'editable', 'hasPermission'],
  emits: ['showMessage', 'createOne'],
  data() {
    return {
      Lenguages: Lenguages,
      index: -1,
      model: {},
    };
  },
  methods: {
    showMessage(_text, _type) {
      this.$emit('showMessage', _text, _type);
    },
    createOne() {
      const errors = [];
      this.fields.forEach((field) => {
        if (!this.$refs[field.id][0].validate()) errors.push(field);
      });
      if (!errors.length) this.$emit('createOne', this.model);
      else this.showMessage(this.Lenguages[this.Lenguages.selected].general.validation_err, 'warning');
    },
    clearFields(){
      this.fields.forEach((field) => {
        this.$refs[field.id][0].clear();
      });
      this.model = {};
    },
    cellChange(name, value) {
      this.model[name] = value;
    },
    setModel(model){
      this.model = model;
      this.fields.forEach((field) => {
        this.$refs[field.id][0].value = model[field.name];
      });
    }
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
  }
}
</script>

<template>
  <tr v-if="editable && hasPermission(moduleName, 'create')">
    <td>
      <div class="btn-group">
        <button v-if="hasPermission(moduleName, 'create')" type="button" data-toggle="tooltip" data-placement="bottom"
          :title="Lenguages[Lenguages.selected].general.save" class="btn btn-success" @click="createOne">
          <i class="fa-solid fa-floppy-disk"></i>
        </button>
        <button type="button" data-toggle="tooltip" data-placement="bottom"
          :title="Lenguages[Lenguages.selected].general.clear" class="btn btn-warning" @click="clearFields">
          <i class="fa-solid fa-delete-left"></i>
        </button>
      </div>
    </td>
    <td v-for="(field, i) in fields" :key="i" scope="row">
      <ViewCell v-if="field.type == 1" :id="field.id" :name="field.name" :properties="field.properties"
        :auxiliar="auxiliar" :index="index" :original="model[field.name]" :ref="field.id" />
      <CheckCell v-if="field.type == 2" :id="field.id" :name="field.name" :properties="field.properties"
        :auxiliar="auxiliar" :index="index" :original="model[field.name]" :ref="field.id" @cellChange="cellChange"
        @showMessage="showMessage" />
      <NumberCell v-if="field.type == 3" :id="field.id" :name="field.name" :properties="field.properties"
        :auxiliar="auxiliar" :index="index" :original="model[field.name]" :ref="field.id" @cellChange="cellChange"
        @showMessage="showMessage" />
      <TextCell v-if="field.type == 4" :id="field.id" :name="field.name" :properties="field.properties"
        :auxiliar="auxiliar" :index="index" :original="model[field.name]" :ref="field.id" @cellChange="cellChange"
        @showMessage="showMessage" />
      <DateCell v-if="field.type == 5" :id="field.id" :name="field.name" :properties="field.properties"
        :auxiliar="auxiliar" :index="index" :original="model[field.name]" :ref="field.id" @cellChange="cellChange"
        @showMessage="showMessage" />
      <EmailCell v-if="field.type == 6" :id="field.id" :name="field.name" :properties="field.properties"
        :auxiliar="auxiliar" :index="index" :original="model[field.name]" :ref="field.id" @cellChange="cellChange"
        @showMessage="showMessage" />
      <PasswordCell v-if="field.type == 7" :id="field.id" :name="field.name" :properties="field.properties"
        :auxiliar="auxiliar" :index="index" :original="model[field.name]" :ref="field.id" @cellChange="cellChange"
        @showMessage="showMessage" />
      <ComboCell v-if="field.type == 8" :id="field.id" :name="field.name" :properties="field.properties"
        :auxiliar="auxiliar" :index="index" :original="model[field.name]" :ref="field.id" @cellChange="cellChange"
        @showMessage="showMessage" />
      <MultipleCell v-if="field.type == 9" :id="field.id" :name="field.name" :properties="field.properties"
        :auxiliar="auxiliar" :index="index" :original="model[field.name]" :ref="field.id" @cellChange="cellChange"
        @showMessage="showMessage" />
    </td>
  </tr>
</template>

<style>

</style>
