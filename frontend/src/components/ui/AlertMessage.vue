<script>
export default {
  data() {
    return {
      text: '',
      type: '',
      time: 0,
    }
  },
  methods: {
    show(_text, _type = 'info', _time = 5000) {
      this.text = _text;
      this.type = _type;
      this.time = new Date().getTime() + _time;
      if (this.text.length) document.getElementById('notification').classList.remove('hidden');
    },
    hide() {
      this.text = '';
      this.time = 0;
      if (!this.text.length) document.getElementById('notification').classList.add('hidden');
    }
  },
  mounted() {
    setInterval(() => {
      if (this.text) {
        const t = new Date().getTime();
        if ((t - this.time) >= 0) this.hide();
      }
    }, 100);
  }
}
</script>

<template>
  <div id="notification" class="m-3 p-2 rounded bg-dark text-light hidden" @click="hide">
    <div class="row m-1">
      <h5 class="col p-1">The Order</h5>
      <a role="button" data-toggle="tooltip" data-placement="bottom" title="Close"
        class="col-auto p-1 text-decoration-none text-danger text-center fw-bold" @click="hide">X</a>
    </div>
    <div class="alert alert-success" role="alert" v-if="type == 'success'">{{ this.text }}</div>
    <div class="alert alert-danger" role="alert" v-if="type == 'error'">{{ this.text }}</div>
    <div class="alert alert-warning" role="alert" v-if="type == 'warning'">{{ this.text }}</div>
    <div class="alert alert-info" role="alert" v-if="type == 'info'">{{ this.text }}</div>
    <div class="row m-1">
      <hp class="col p-1 text-muted">{{ new Date() }}</hp>
    </div>
</div>
</template>

<style>
.hidden {
  display: none;
}

#notification {
  position: absolute;
  z-index: 10000;
  bottom: 0px;
  right: 0px;
  width: 20rem;
  height: auto;
}
</style>
