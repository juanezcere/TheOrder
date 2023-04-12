import Lenguages from '../lenguages';

const foods = {
  title: Lenguages[Lenguages.selected].menu.modules.foods,
  Model: class Model {
    constructor(element) {
      this.food_id = element.food_id;
      this.food_name = element.food_name;
      this.food_value = element.food_value;
      this.truck_id = element.truck_id;
    }
  },
  fields: [
    {
      id: 'id',
      name: 'food_id',
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
      name: 'food_name',
      type: 4,
      properties: JSON.stringify({
        placeholder: Lenguages[Lenguages.selected].general.name,
        validation: '',
        format: '',
        required: false,
        target: '',
        default: '',
      }),
    }, {
      id: 'value',
      name: 'food_value',
      type: 3,
      properties: JSON.stringify({
        placeholder: Lenguages[Lenguages.selected].general.value,
        validation: '',
        format: '',
        required: false,
        target: '',
        default: '',
      }),
    }, {
      id: 'truck',
      name: 'truck_id',
      type: 4,
      properties: JSON.stringify({
        placeholder: Lenguages[Lenguages.selected].general.truck,
        validation: '',
        format: '',
        required: false,
        target: '',
        default: '',
      }),
    }
  ]
};

export default foods;
