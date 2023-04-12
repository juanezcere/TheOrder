<script>
import Lenguages from '@/assets/config/lenguages';

export default {
  props: {
    tabList: {
      type: Array,
      required: true,
    },
    variant: {
      type: String,
      required: false,
      default: () => "vertical",
      validator: (value) => ["horizontal", "vertical"].includes(value),
    },
    index: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      activeTab: 1,
      Lenguages: Lenguages
    };
  }
};
</script>

<template>
  <div :class="{ flex: variant === 'horizontal', }">
    <div :class="{ flex: variant === 'vertical', }">
      <div v-for="(tab, i) in tabList" :key="i" class="px-3 py-1">
        <input :id="'tab_' + index + '_' + i" type="radio" :name="'tab_' + index + '_' + i" :value="i + 1"
          v-model="activeTab" class="btn-check mx-3" autocomplete="off">
        <label :for="'tab_' + index + '_' + i" class="btn btn-outline-dark">
          {{ this.Lenguages[this.Lenguages.selected].menu.submodules[tab] }}
        </label>
      </div>
    </div>
    <template v-for="(tab, i) in tabList">
      <div :key="i" v-if="i + 1 === activeTab">
        <slot :name="tab + index" />
      </div>
    </template>
  </div>
</template>

<style>
.flex {
  display: flex;
}
</style>