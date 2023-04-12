import Lenguages from '../lenguages';

const screen = {
  title: Lenguages[Lenguages.selected].menu.modules.orders,
  Model: class Model {
    constructor(element) {
      this.food_id = element.food_id;
      this.food_name = element.food_name;
      this.food_value = element.food_value;
    }
  },
  fields: [
    {
      id: 'id',
      name: 'order_id',
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
      id: 'food',
      name: 'food_name',
      type: 1,
      properties: JSON.stringify({
        placeholder: Lenguages[Lenguages.selected].general.name,
        validation: '',
        format: '',
        required: false,
        target: '',
        default: '',
      }),
    }, {
      id: 'quantity',
      name: 'food_quantity',
      type: 1,
      properties: JSON.stringify({
        placeholder: Lenguages[Lenguages.selected].general.quantity,
        validation: '',
        format: '',
        required: false,
        target: '',
        default: '',
      }),
    }, {
      id: 'where_eat',
      name: 'where_eat',
      type: 1,
      properties: JSON.stringify({
        placeholder: Lenguages[Lenguages.selected].general.where_eat,
        validation: '',
        format: 'checkbox',
        required: false,
        target: '',
        default: '',
      }),
    }, {
      id: 'status',
      name: 'status',
      type: 1,
      properties: JSON.stringify({
        placeholder: Lenguages[Lenguages.selected].general.status,
        validation: '',
        format: '',
        required: false,
        target: '',
        default: '',
      }),
    }
  ]
};

export default screen;
