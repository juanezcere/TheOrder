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
  props: ['token', 'user', 'moduleName', 'modulesAlt', 'fields', 'auxiliar', 'editable', 'index', 'original', 'hasPermission'],
  emits: ['showMessage', 'updateOne', 'deleteOne', 'duplicateOne'],
  data() {
    return {
      Lenguages: Lenguages,
      model: {},
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
  },
  mounted() {
    this.model = this.original;
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
  <tr>
    <td v-if="editable">
      <div class="btn-group">
        <button v-if="hasPermission(moduleName, 'update') && change" type="button" data-toggle="tooltip"
          data-placement="bottom" :title="Lenguages[Lenguages.selected].general.save" class="btn btn-success"
          @click="updateOne">
          <i class="fa-solid fa-floppy-disk"></i>
        </button>
        <!-- <button v-if="editable && hasPermission(moduleName, 'create')" type="button" data-toggle="tooltip"
              data-placement="bottom" :title="Lenguages[Lenguages.selected].general.duplicate" class="btn btn-primary"
              @click="duplicateOne">
              <i class="fa-solid fa-copy"></i>
            </button> -->
        <button v-if="hasPermission(moduleName, 'delete')" type="button" data-toggle="tooltip" data-placement="bottom"
          :title="Lenguages[Lenguages.selected].general.delete" class="btn btn-danger" @click="deleteOne">
          <i class="fa-solid fa-trash"></i>
        </button>
      </div>
    </td>
    <td v-for="(field, i) in fields" :key="i" scope="row">
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
</template>

<style>
.hidden {
  display: none;
}
</style>
