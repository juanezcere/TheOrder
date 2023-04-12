<script>
import Lenguages from '@/assets/config/lenguages';

export default {
  data() {
    return {
      page: 1,
      size: 10,
      pages: [],
      total: 0,
      Lenguages: Lenguages
    }
  },
  methods: {
    paginate(elements) {
      this.calculate(elements);
      const from = (this.page * this.size) - this.size;
      const to = (this.page * this.size);
      return elements.slice(from, to);
    },
    calculate(elements) {
      this.pages = [];
      this.total = elements.length;
      const number = Math.ceil(this.total / this.size);
      for (let i = 1; i <= number; i++) this.pages.push(i);
      if (this.page > this.pages.length) this.page = 1;
    },
    getIndex(index) {
      return parseInt(index) + ((this.page - 1) * this.size);
    }
  }
}
</script>

<template>
  <div class="row w-100">
    <div class="col">
      <p class="text-muted py-3">
        {{ this.Lenguages[this.Lenguages.selected].general.showing }}
        {{ this.Lenguages[this.Lenguages.selected].general.page }}
        {{ page }}
        {{ this.Lenguages[this.Lenguages.selected].general.of }}
        {{ pages.length }}
        {{ this.Lenguages[this.Lenguages.selected].general.pages }}.
      </p>
    </div>
    <div class="col py-2">
      <div class="btn-group py-2">
        <button type="button" v-if="page != 1" @click="page--" class="btn bg-dark text-light">
          <i class="fa fa-angles-left"></i>
        </button>
        <button v-for="number in pages.slice(page - 1, page + 5)" :key="number" @click="page = number"
          class="btn bg-dark text-light">
          {{ number }}
        </button>
        <button v-if="page < pages.length" @click="page++" class="btn bg-dark text-light">
          <i class="fa fa-angles-right"></i>
        </button>
      </div>
    </div>
    <div class="col">
      <p class="text-muted py-3">
        {{ this.Lenguages[this.Lenguages.selected].general.showing }}
        <select v-model="size" id="limitSelector" class="rounded">
          <option value="10" :selected="size == 10">10</option>
          <option value="25" :selected="size == 25">25</option>
          <option value="50" :selected="size == 50">50</option>
          <option value="100" :selected="size == 100">100</option>
          <option value="100000" :selected="size >= 101">Todos</option>
        </select>
        {{ this.Lenguages[this.Lenguages.selected].general.of }}
        {{ total }}
        {{ this.Lenguages[this.Lenguages.selected].general.registers }}.
      </p>
    </div>
  </div>
</template>

<style>
#limitSelector {
  width: 60px;
  height: 30px;
}
</style>
