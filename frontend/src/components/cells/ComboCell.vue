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
    this.validation = properties.validation;
    this.format = properties.format;
    this.required = properties.required;
    this.target = properties.target;
    this.default = properties.default;
    this.index = document.getElementsByName(this.name).length;
  },
  computed: {
    show() {
      if (this.original != null) {
        const value = this.auxiliar[this.target].filter((val) => val.id == this.original);
        return value[0].name;
      } else return this.default
    },
    getTarget() {
      if (this.auxiliar[this.target]) return this.auxiliar[this.target];
      else return [];
    }
  },
  methods: {
    update(ev) {
      //this.element = ev.target;
      this.$emit('cellChange', this.name, ev);
    },
    focusout() {
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
      return true;
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
    },
    checkSelected(id) {
      return id == this.original;
    },
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
      data-bs-toggle="dropdown" aria-expanded="false" @change="update" @focusout="focusout">

    <div class="dropdown">
      <ul class="dropdown-menu">
        <li v-for="val in getTarget">
          <a href="#" @click="update(val.id)"
            :class="{ 'dropdown-item': true, 'py-1': true, 'bg-dark': checkSelected(val.id), 'text-light': checkSelected(val.id), 'dropdown-item': true }">
            {{ val.name }}
          </a>
        </li>
      </ul>
    </div>
    <!-- <select :id="id + index" :name="name" :index="index" data-toggle="tooltip" data-placement="bottom"
            :title="placeholder" class="rounded border border-dark" @focusout="update">
            <option value="" selected>
              {{ this.Lenguages[this.Lenguages.selected].general.none }}
            </option>
            <option v-for="val in getTarget" :value="val.id" :selected="checkSelected(val.id)">
              {{ val.name || val.username }}
            </option>
          </select> -->
  </div>
</template>

<style>
select {
  width: 250px;
  height: 35px;
}
</style>
