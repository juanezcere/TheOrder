<script>
import BackendConnection from '@/components/BackendConnection.vue';
import AlertMessage from '@/components/ui/AlertMessage.vue';
import Lenguages from '@/assets/config/lenguages';
import Fields from '@/assets/config/fields';

export default {
  props: ['token', 'user', 'hasPermission', 'updateToken'],
  data() {
    return {
      moduleName: 'tablet',
      Lenguages: Lenguages,
      Fields: Fields,
      original: [],
      models: [],
      auxiliar: [],
    };
  },
  created() {
    if (!this.token) this.$router.push('/logout');
    else if (!this.user) this.$router.push('/logout');
    else if (!this.hasPermission(this.moduleName, 'access')) this.$router.push('/');
    this.title = this.Lenguages[this.Lenguages.selected].menu.modules[this.moduleName];
  },
  methods: {
    showMessage(_text, _type) {
      this.$refs.AlertMessage.show(_text, _type);
    },
    searchData(models) {
      this.models = models;
    },
    async getData() {
      try {
        const data = await this.$refs.BackendConnection.getAll('foods');
        console.log(data.data)
        this.fields = this.Fields[this.moduleName].fields;
        this.original = this.models = data.data.map((d) => new this.Fields[this.moduleName].Model(d));
      } catch (error) {
        console.log(error);
      }
    },
    async createOne(model) {
      try {
        model.food_quantity = window.prompt(this.Lenguages[this.Lenguages.selected].general.quantity, '');
        model.customer = window.prompt(this.Lenguages[this.Lenguages.selected].general.customer, '');
        model.where_eat = window.prompt(this.Lenguages[this.Lenguages.selected].general.where_eat, '');
        const data = await this.$refs.BackendConnection.createOne('orders', model);
        this.showMessage(this.Lenguages[this.Lenguages.selected].general.create_ok, 'success');
      } catch (error) {
        console.log(error);
      }
    },
  },
  components: {
    AlertMessage,
    BackendConnection,
  },
  mounted() {
    if (this.hasPermission(this.moduleName, 'access')) this.getData();
    else this.$router.push('/');
  }
}
</script>

<template>
  <AlertMessage ref="AlertMessage" class="row pt-1" />
  <div class="row mt-1">
    <div class="col-xl m-1">
      <div class="card-deck row mt-1">
        <div class="card text-center m-2 bg-dark" v-for="element in models">
          <div class="card-body">
            <a href="#" @click="createOne(element)" class="card-title text-light text-decoration-none">
              <h3>{{ element.food_name }}</h3>
              <h5>$ {{ element.food_value }}</h5>
              <p class="text-muted m-3">{{ element.food_id }}</p>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
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
