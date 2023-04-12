import Lenguages from '../lenguages';

const trucks = {
  title: Lenguages[Lenguages.selected].menu.modules.trucks,
  Model: class Model {
    constructor(element) {
      this.truck_id = element.truck_id;
      this.truck_name = element.truck_name;
    }
  },
  fields: [
    {
      id: 'id',
      name: 'truck_id',
      type: 1,
      properties: JSON.stringify({
        placeholder: Lenguages[Lenguages.selected].general.id,
        validation: '',
        format: '',
        required: false,
        target: '',
        default: '',
      }),
    }, {
      id: 'name',
      name: 'truck_name',
      type: 4,
      properties: JSON.stringify({
        placeholder: Lenguages[Lenguages.selected].general.name,
        validation: '',
        format: '',
        required: false,
        target: '',
        default: '',
      }),
    }
  ]
};

export default trucks;
