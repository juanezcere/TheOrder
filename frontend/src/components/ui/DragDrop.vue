<script>
import PageGenerator from '@/components/table/PageGenerator.vue';
import BackendConnection from '@/components/BackendConnection.vue';
import Lenguages from '@/assets/config/lenguages';
import Fields from '@/assets/config/fields';

export default {
  props: ['token', 'user', 'models', 'hasPermission'],
  emits: ['showMessage', 'uploadFile'],
  data() {
    return {
      moduleName: 'files',
      Lenguages: Lenguages,
      Fields: Fields,
      active: false,
      timeout: null
    };
  },
  created() {
    this.Model = this.Fields[this.moduleName].Model;
  },
  computed: {
    display() {
      if (this.models.length) return this.$refs.PageGenerator.paginate(this.models);
      else return [];
    }
  },
  methods: {
    showMessage(_text, _type) {
      this.$emit('showMessage', _text, _type);
    },
    generateId(length) {
      let result = '';
      const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
      const charactersLength = characters.length;
      for (var i = 0; i < length; i++) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
      }
      return result;
    },
    getScale(value, transparency = '49') {
      return '#00FF00' + transparency;
    },
    setActive() {
      this.active = true;
      clearTimeout(this.timeout);
    },
    setInactive() {
      this.timeout = setTimeout(() => {
        this.active = false;
      }, 100);
    },
    onDrop(e) {
      this.setInactive();
      [...e.dataTransfer.files].forEach((f) => {
        //const found = this.models.find(model => model.name === f.name && model.extension === f.type && model.size === f.size);
        //if (found) return this.showMessage(f.name + this.Lenguages[this.Lenguages.selected][this.moduleName].err_exists, 'warning');
        if (f.size > 24 * 1024 * 1024) return this.showMessage(f.name + this.Lenguages[this.Lenguages.selected][this.moduleName].err_big, 'warning');
        const model = {
          id: URL.createObjectURL(f).split('/').slice(-1)[0].replaceAll('-', ''),
          file: f,
          resource: URL.createObjectURL(f),
          extension: f.type,
          size: f.size,
          code: this.generateId(7),
          name: f.name,
          description: (f.size / 1024).toFixed(2).toString() + ' KiB - ' + new Date(f.lastModified).toString(),
          enabled: true,
          status: 0.0
        }
        this.createFile(model);
      });
    },
    async createFile(model) {
      try {
        const data = await this.$refs.BackendConnection.uploadFile(this.moduleName, model);
        this.showMessage(this.Lenguages[this.Lenguages.selected].general.created_file, 'success');
        const file = new this.Model(data.data);
        this.$emit('uploadFile', file);
      } catch (err) {
        console.log(err);
      }
    },
    async downloadFile(model, name) {
      try {
        const data = await this.$refs.BackendConnection.downloadFile(this.moduleName, model);
        const link = document.createElement('a');
        link.href = URL.createObjectURL(data);
        link.download = name;
        link.click();
        URL.revokeObjectURL(link.href);
      } catch (err) {
        console.log(err);
      }
    }
  },
  components: {
    PageGenerator,
    BackendConnection
  },
  mounted() {
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach((n) => {
      document.body.addEventListener(n, (e) => e.preventDefault());
    });
  },
  unmounted() {
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach((n) => {
      document.body.removeEventListener(n, (e) => e.preventDefault());
    });
  }
}
</script>

<template>
  <div class="row mt-1 drop-area">
    <div :data-active="active" @dragenter.prevent="setActive" @dragover.prevent="setActive"
      @dragleave.prevent="setInactive" @drop.prevent="onDrop" class="col-xl my-1 mx-4 rounded bg-light">
      <div class="card-deck row mt-1">
        <slot :dropZoneActive="active" style="min-height: 350px"></slot>
        <div v-for="element in display" class="card text-center m-2 bg-dark">
          <div class="card-body">
            <a ref="#" role="button" @click="downloadFile(element.id, element.name)"
              class="card-title text-light text-decoration-none">
              <h6>{{ element.code }}</h6>
              <h3>{{ element.name }}</h3>
              <h5>{{ element.description }}</h5>
              <div class="row w-100 text-center px-3">
                <div class="col-auto rounded-circle py-auto mx-auto" data-bs-toggle="tooltip" data-bs-placement="bottom"
                  :title="Lenguages[Lenguages.selected].general.status + ': ' + (element.status * 100).toFixed() + '%'"
                  :style="{ 'height': '20px', 'width': '20px', 'background': getScale(element.status * 100.0) }">
                </div>
              </div>
            </a>
          </div>
        </div>
        <h5 v-if="models.length == 0" class="w-100 text-center text-muted p-5">
          {{ this.Lenguages[this.Lenguages.selected].general.not_data }}
        </h5>
      </div>
    </div>
  </div>
  <PageGenerator ref="PageGenerator" />
  <BackendConnection :token="token" :user="user" ref="BackendConnection" @showMessage="showMessage" />
</template>

<style>
.card {
  width: 350px;
}

@media (max-width: 350px) {
  .card {
    width: 100%;
  }
}
</style>
