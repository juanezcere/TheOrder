<script>
import Lenguages from '@/assets/config/lenguages';

export default {
  props: ['id', 'name', 'properties', 'auxiliar', 'original'],
  emits: ['cellChange', 'showMessage'],
  data() {
    return {
      Lenguages: Lenguages,
      index: 0,
      element: null,
    }
  },
  created() {
    const props = this.properties.replaceAll("'", '"');
    const properties = JSON.parse(props);
    this.placeholder = properties.placeholder;
    this.validation = properties.validation.length ? new RegExp(properties.validation) : '';
    this.format = properties.format;
    this.required = properties.required;
    this.target = properties.target;
    this.default = properties.default;
    this.index = document.getElementsByName(this.name).length;
  },
  computed: {
    show() {
      if (this.original != null) return this.original;
      else return this.default
    },
  },
  methods: {
    update(ev) {
      this.element = ev.target;
      this.$emit('cellChange', this.name, this.element.value);
    },
    focusout(){
      Array.from(this.element.classList).filter((el) => el.startsWith('border-')).forEach((el) => {
        this.element.classList.remove(el);
      });
      if (this.validate()) this.element.classList.add('border-warning');
      else {
        this.element.classList.add('border-danger');
        this.$emit('showMessage', this.Lenguages[this.Lenguages.selected].general.validation_err, 'warning');
      }
    },
    validate() {
      if (this.id.length != 32) return true;
      if (!this.required) return true;
      if (this.required && (this.original == null || this.original.length == 0)) return false;
      if (!this.validation.length && this.required && this.original.length) return true;
      if (this.validation.length && this.original.length) return !!String(this.original).toLowerCase().match(this.validation);
    },
    restore() {
      if (this.element) {
        Array.from(this.element.classList).filter((el) => el.startsWith('border-')).forEach((el) => {
          this.element.classList.remove(el);
        });
        this.element.classList.add('border-dark');
      }
    },
    clear() {
      Array.from(this.element.classList).filter((el) => el.startsWith('border-')).forEach((el) => {
        this.element.classList.remove(el);
      });
    }
  },
  mounted() {
    this.element = document.getElementById(this.id + this.index);
  }
}
</script>

<template>
  <div>
    <input type="text" :placeholder="placeholder" :id="id + index" :name="name" :value="show"
      class="rounded border p-1 border-dark" data-toggle="tooltip" data-placement="bottom" :title="placeholder"
      @change="update" @focusout="focusout">
  </div>
</template>

<style>
input[type=text] {
  width: 250px;
  height: 35px;
}
</style>
