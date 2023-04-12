<script>
import Lenguages from '@/assets/config/lenguages';

export default {
  data() {
    return {
      Lenguages: Lenguages
    }
  }
}
</script>

<template>
  <div class="w-50 p-5 row mx-auto">
    <h1 class="text-center m-3 p-2">
      {{ this.Lenguages[this.Lenguages.selected].general.great }}
    </h1>
    <div class="col-auto mx-auto">
      <h4 class="text-muted text-center">
        {{ this.Lenguages[this.Lenguages.selected].menu.modules.tablet }}
      </h4>
      <br>
      <RouterLink to="/tablet" class="btn h1 m-3 p-3 text-light btn-dark">
        {{ this.Lenguages[this.Lenguages.selected].menu.modules.tablet }}
      </RouterLink>
    </div>
    <div class="col-auto mx-auto">
      <h4 class="text-muted text-center">
        {{ this.Lenguages[this.Lenguages.selected].general.restaurants }}
      </h4>
      <br>
      <RouterLink to="/trucks" class="btn h1 m-3 p-3 text-light btn-dark">
        {{ this.Lenguages[this.Lenguages.selected].menu.modules.trucks }}
      </RouterLink>
      <br>
      <RouterLink to="/foods" class="btn h1 m-3 p-3 text-light btn-dark">
        {{ this.Lenguages[this.Lenguages.selected].menu.modules.foods }}
      </RouterLink>
      <br>
      <RouterLink to="/orders" class="btn h1 m-3 p-3 text-light btn-dark">
        {{ this.Lenguages[this.Lenguages.selected].menu.modules.orders }}
      </RouterLink>
    </div>
    <div class="col-auto mx-auto">
      <h4 class="text-muted text-center">
        {{ this.Lenguages[this.Lenguages.selected].menu.modules.screen }}
      </h4>
      <br>
      <RouterLink to="/screen" class="btn h1 m-3 p-3 text-light btn-dark">
        {{ this.Lenguages[this.Lenguages.selected].menu.modules.screen }}
      </RouterLink>
    </div>
  </div>
</template>

<style></style>