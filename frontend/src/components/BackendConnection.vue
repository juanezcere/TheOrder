<script>
import pkg from '../../package.json';
import Backend from '@/assets/config/backend';
import Lenguages from '@/assets/config/lenguages';

export default {
  props: ['token', 'user'],
  emits: ['showMessage'],
  data() {
    return {
      Lenguages: Lenguages,
      moduleServer: Backend.url
    }
  },
  methods: {
    async getAll(moduleName) {
      try {
        const options = {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'x-client': 'web-' + pkg.version,
          }
        };
        const res = await fetch(this.moduleServer + moduleName + '/', options);
        const data = await res.json();
        console.log(data)
        if (data.code != '000') return this.$emit('showMessage', data.message, 'error');
        return data;
      } catch (error) {
        console.log(error);
        this.$emit('showMessage', this.Lenguages[this.Lenguages.selected].general.get_err + ' ' + error, 'error');
      }
    },
    async getOne(moduleName, id) {
      try {
        const options = {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'x-client': 'web-' + pkg.version,
          }
        };
        const res = await fetch(this.moduleServer + moduleName + '/' + id, options);
        const data = await res.json();
        console.log(data)
        if (data.code != '000') return this.$emit('showMessage', data.message, 'error');
        return data;
      } catch (error) {
        console.log(error);
        this.$emit('showMessage', this.Lenguages[this.Lenguages.selected].general.get_err + ' ' + error, 'error');
      }
    },
    async createOne(moduleName, model) {
      try {
        const options = {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'x-client': 'web-' + pkg.version,
          },
          body: JSON.stringify(model)
        };
        const res = await fetch(this.moduleServer + moduleName + '/', options);
        const data = await res.json();
        console.log(data)
        if (data.code != '000') return this.$emit('showMessage', data.message, 'error');
        return data;
      } catch (error) {
        console.log(error);
        this.$emit('showMessage', this.Lenguages[this.Lenguages.selected].general.create_err + ' ' + error, 'error');
      }
    },
    async updateOne(moduleName, model) {
      try {
        const options = {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'x-client': 'web-' + pkg.version,
          },
          body: JSON.stringify(model)
        };
        console.log(options, model)
        const res = await fetch(this.moduleServer + moduleName + '/' + model.id, options);
        const data = await res.json();
        console.log(data)
        if (data.code != '000') return this.$emit('showMessage', data.message, 'error');
        return data;
      } catch (error) {
        console.log(error);
        this.$emit('showMessage', this.Lenguages[this.Lenguages.selected].general.update_err + ' ' + error, 'error');
      }
    },
    async deleteOne(moduleName, model) {
      try {
        const options = {
          method: 'DELETE',
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'x-client': 'web-' + pkg.version,
          },
          body: JSON.stringify(model)
        };
        const res = await fetch(this.moduleServer + moduleName + '/' + model.id, options);
        const data = await res.json();
        console.log(data)
        if (data.code != '000') return this.$emit('showMessage', data.message, 'error');
        return data;
      } catch (error) {
        console.log(error);
        this.$emit('showMessage', this.Lenguages[this.Lenguages.selected].general.delete_err + ' ' + error, 'error');
      }
    },
  },
}
</script>

<template></template>
