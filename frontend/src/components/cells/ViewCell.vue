<script>
export default {
  props: ['id', 'name', 'properties', 'auxiliar', 'original'],
  created() {
    const props = this.properties.replaceAll("'", '"');
    const properties = JSON.parse(props);
    this.placeholder = properties.placeholder;
    this.validation = properties.validation;
    this.format = properties.format;
    this.required = properties.required;
    this.target = properties.target;
    this.default = properties.default;
  },
  computed: {
    show() {
      if (this.original != null) return this.original;
      else return this.default
    },
  },
  methods: {
    validate() {
      return true;
    },
    restore() {
      return true;
    },
    clear() {
      return true;
    }
  }
}
</script>

<template>
  <div class="p-1">
    <p data-toggle="tooltip" data-placement="bottom" :title="placeholder">{{ show }}</p>
  </div>
</template>

<style>

</style>
