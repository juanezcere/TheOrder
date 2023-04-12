import English from "./lenguages/english";

const Lenguages = {};

Lenguages.english = English;

Lenguages.spanish = {};
Lenguages.latin = {};
Lenguages.french = {};
Lenguages.portuguese = {};
Lenguages.dutch = {};

Lenguages.lenguages = ['english', 'spanish', 'latin', 'french', 'portuguese', 'dutch'];

Lenguages.selected = 'english';

Lenguages.update = (lenguage) => {
  Lenguages.selected = Lenguages.lenguages[lenguage];
};

export default Lenguages;