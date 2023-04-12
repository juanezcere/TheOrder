import Lenguages from '../lenguages';

const files = {
  title: Lenguages[Lenguages.selected].menu.modules.files,
  Model: class Model {
    constructor(element) {
      this.id = element.id;
      this.code = element.code;
      this.name = element.name;
      this.description = element.description;
      this.resource = element.resource;
      this.extension = element.extension;
      this.size = element.size;
      this.file = element.file;
      this.admit = element.admit || true;
      this.status = 1.0;
      this.enabled = element.enabled;
      this.created_at = element.created_at;
      this.created_by = element.created_by;
      this.updated_at = element.updated_at;
      this.updated_by = element.updated_by;
    }
  },
  fields: []
};

export default files;
