<script setup>
import { RouterView } from 'vue-router';
import TopBar from './components/TopBar.vue';


const hasPermission = (moduleName, _permission) => {
  return true;
  if (user.value) {
    const permission = moduleName + '.' + _permission;
    const found = user.value.permissions.find(element => element.resource === permission);
    if (found) return true;
  }
  return false;
};
</script>

<template>
  <TopBar />
  <div class="container-fluid pt-5">
    <div class="row flex-nowrap">
      <div class="col">
        <RouterView :token="'token'" :user="'user'" :hasPermission="hasPermission" :updateToken="updateToken"
          class="col-auto mx-1 py-3 pt-5" />
      </div>
    </div>
  </div>
</template>

<style scoped>
@font-face {
  font-family: 'Roboto';
  src: url('./assets/webfonts/Roboto-Regular.ttf');
}

* {
  font-family: 'Roboto', sans-serif;
  font-size: 14px;
}
</style>
