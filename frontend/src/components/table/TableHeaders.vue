<script>

export default {
  props: ['editable', 'fields'],
  emits: ['sortBy', 'filterBy'],
  methods: {
    getPlaceholder(element) {
      const props = element.properties.replaceAll("'", '"');
      const properties = JSON.parse(props);
      return properties.placeholder;
    },
  },
}
</script>

<template>
  <thead>
    <tr>
      <th v-if="editable"></th>
      <th v-for="(element, index) in fields" :key="index" scope="col">
        <div class="btn-group-vertical">
          <button @click="$emit('sortBy', element.name, element.type, false)" class="btn btn-secundary btn-sm"
            data-toggle="tooltip" data-placement="bottom" title="Sort alphabetically">
            <i class="fa-solid fa-arrow-up-a-z"></i>
          </button>
          <button @click="$emit('sortBy', element.name, element.type, true)" class="btn btn-secundary btn-sm"
            data-toggle="tooltip" data-placement="bottom" title="Sort alphabetically inverse">
            <i class="fa-solid fa-arrow-down-z-a"></i>
          </button>
        </div>
        {{ getPlaceholder(element) }}
      </th>
    </tr>
  </thead>
</template>

<style>
th {
  min-width: 250px;
}
</style>
