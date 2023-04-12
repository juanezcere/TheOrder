<script>
import ModuleView from '@/components/module/ModuleView.vue';

export default {
  props: ['token', 'user', 'hasPermission', 'updateToken'],
  data() {
    return {
      moduleName: 'foods',
      modulesAlt: {}
    };
  },
  components: {
    ModuleView
  }
}
</script>

<template>
  <ModuleView :token="token" :user="user" :moduleName="moduleName" :modulesAlt="modulesAlt"
    :hasPermission="hasPermission" :updateToken="updateToken" />
</template>
