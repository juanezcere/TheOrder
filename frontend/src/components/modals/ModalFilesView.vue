<script>
import DragDrop from '@/components/ui/DragDrop.vue';
import Lenguages from '@/assets/config/lenguages';

export default {
  props: ['token', 'user', 'moduleName', 'models', 'hasPermission'],
  emits: ['showMessage', 'closeModal', 'uploadFile'],
  data() {
    return {
      element: null,
      Lenguages: Lenguages,
    };
  },
  methods: {
    showMessage(_text, _type) {
      this.$emit('showMessage', _text, _type);
    },
    uploadFile(_file) {
      this.$emit('uploadFile', _file);
    },
    showModal() {
      this.element.classList.remove('hidden');
    },
    closeModal() {
      this.element.classList.add('hidden');
      this.$emit('closeModal');
    },
  },
  components: {
    DragDrop
  },
  mounted() {
    this.element = document.getElementById('modalView');
  }
}
</script>

<template>
  <Transition name="modal">
    <div id="modalView" class="hidden modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container w-75 rounded my-1 p-3 mx-auto bg-light">
          <div class="modal-header">
            <slot name="header">
              <div class="row m-1 w-100">
                <h5 class="col p-1">{{ Lenguages[Lenguages.selected].general.import_file }}</h5>
                <a role="button" data-toggle="tooltip" data-placement="bottom" title="Close"
                  class="col-auto p-1 text-decoration-none text-danger text-center fs-5 fw-bold" @click="closeModal">X</a>
              </div>
            </slot>
          </div>
          <div class="modal-body">
            <slot name="body">
              <DragDrop :token="token" :user="user" :moduleName="moduleName" :models="models" @showMessage="showMessage"
                @uploadFile="uploadFile" />
            </slot>
          </div>
        </div>
      </div>
    </div>
  </Transition>
</template>

<style>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
}

.hidden {
  display: none;
}
</style>
