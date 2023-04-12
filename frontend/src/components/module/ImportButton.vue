<script>
import Lenguages from '@/assets/config/lenguages';

export default {
  props: ['moduleName'],
  emits: ['importFile'],
  data() {
    return {
      Lenguages: Lenguages,
    }
  },
  methods: {
    importFile() {
      return this.$emit('importFile');
      const reader = new FileReader();
      reader.onload = (ev) => {
        try {
          
          const headers = ev.target.result.split('\n')[0].split(',');
          const dataset = ev.target.result.split('\n').slice(1);
          for (const row of dataset) {
            const r = row.split('","');
            if (headers.length <= row.length) {
              let data = {}
              for (let i = 0; i < headers.length; i++) data[headers[i]] = r[i].replace('"', '');
              if (this.moduleName == 'places') data = this.place_converter(data);
              const model = new this.Fields[this.moduleName].Model(data);
              this.$emit('importData', model);
            }
          }
        } catch (err) {
          console.log(err);
        }
      };
      reader.readAsText(files[0]);
    },
    downloadFile() {
      const data = [];
      const headers = [];
      Fields[this.moduleName].fields.forEach((field) => headers.push(field.placeholder));
      data.push(headers.join(',') + '\n');
      const blob = new Blob(data, { type: 'application/text' });
      const link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      link.download = this.moduleName + '_template.csv';
      link.click();
      URL.revokeObjectURL(link.href);
    },
    place_converter(data) {
      const newData = {
        code: data['ID'],
        name: data['Sitio'],
        country: 'Colombia',
        region: data['Region'],
        state: data['Departamento'],
        municipality: data['Municipio'],
        dane_municipality: data['DANE_Municipio'],
        poblation: data['Centro_Poblado'],
        dane_poblation: data['DANE_CP'],
        zone: data['Zona'],
        objetive: data['Objetivo_Cobertura'],
        locality: data['Localidad__CRC_'],
        address: data['Ubicacion'],
        latitude: data['Latitud'],
        longitude: data['Longitud'],
        altitude: '0',
        structure: data['Estructura'],
        structure_detail: data['Detalle_Estructura'],
        height: data['Altura_Estructura'],
        real_owner: data['Propietario_Estructura']
      };
      return newData;
    }
  },
}
</script>

<template>
  <input ref="FileUpload" type="file" accept=".csv" @change="importFile" hidden>
  <button type="button" data-bs-toggle="dropdown" aria-expanded="false" data-toggle="tooltip" data-placement="bottom"
    :title="Lenguages[Lenguages.selected].general.import" class="btn bg-dark text-light dropdown-toggle">
    <i class="fa fa-file-import"></i>
  </button>
  <ul class="dropdown-menu">
    <li>
      <a class="dropdown-item" href="#" @click="downloadFile">
        {{ this.Lenguages[this.Lenguages.selected].general.import_template }}
      </a>
    </li>
    <li>
      <a class="dropdown-item" href="#" @click="importFile">
        {{ this.Lenguages[this.Lenguages.selected].general.import_file }}
      </a>
    </li>
  </ul>
</template>

