<script>
import Lenguages from '@/assets/config/lenguages';

export default {
  emits: ['exportData'],
  data() {
    return {
      Lenguages: Lenguages
    }
  },
  methods: {
    exportFile(models, fields, filename) {
      const data = [];
      const headers = [];
      fields.forEach((field) => {
        const props = field.properties.replaceAll("'", '"');
        const properties = JSON.parse(props);
        headers.push(properties.placeholder);
      });
      data.push(headers.join('\t') + '\n');
      models.forEach((element) => {
        const row = [];
        fields.forEach((field) => {
          if (element[field.name]) row.push(element[field.name]);
          else row.push('');
        });
        data.push(row.join('\t') + '\n');
      });
      const blob = new Blob(data, { type: 'application/text' });
      const link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      link.download = filename + '_export.csv';
      link.click();
      URL.revokeObjectURL(link.href);
    }
  }
}
</script>

<template>
  <button type="button" data-bs-toggle="dropdown" aria-expanded="false" data-toggle="tooltip" data-placement="bottom"
    :title="Lenguages[Lenguages.selected].general.export" class="btn bg-dark text-light dropdown-toggle">
    <i class="fa fa-file-export"></i>
  </button>
  <ul class="dropdown-menu">
    <li>
      <a class="dropdown-item" href="#" @click="$emit('exportData', 0)">
        {{ this.Lenguages[this.Lenguages.selected].general.export_view }}
      </a>
    </li>
    <li>
      <a class="dropdown-item" href="#" @click="$emit('exportData', 1)">
        {{ this.Lenguages[this.Lenguages.selected].general.export_all }}
      </a>
    </li>
  </ul>
</template>
