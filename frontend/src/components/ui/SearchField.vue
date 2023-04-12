<script>
import Lenguages from '@/assets/config/lenguages';

export default {
  props: ['original'],
  emits: ['searchData'],
  data() {
    return {
      Lenguages: Lenguages
    }
  },
  methods: {
    searchData(ev) {
      const value = ev.target.value.toLowerCase();
      if (value.length) {
        const models = [];
        this.original.forEach(element => {
          for (const key in element) {
            const val = element[key].toString();
            if (val.toLowerCase().indexOf(value) != -1) {
              console.log(element, value, key, val)
              models.push(element);
              break;
            }
          }
        });
        this.$emit('searchData', models);
      } else this.$emit('searchData', this.original);
    }
  }

}
</script>

<template>
  <input id="searchText" type="text" :placeholder="Lenguages[Lenguages.selected].general.search" @input="searchData"
    data-toggle="tooltip" data-placement="bottom" :title="Lenguages[Lenguages.selected].general.search"
    class="rounded px-4 py-1 border-dark">
  <i class="fa fa-magnifying-glass position-absolute" style="margin-left: 7px; margin-top: 10px;"></i>
</template>
