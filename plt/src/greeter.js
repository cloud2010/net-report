// Greeter.js
var dataset = require('../public/info.json');
module.exports = function() {
    var greet = document.createElement('div');
    console.log(dataset.greetText);
    greet.textContent = dataset.greetText;
    return greet;
  };