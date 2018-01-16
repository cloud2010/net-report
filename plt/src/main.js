
// const greeter = require('./greeter.js');
import output from './greeter.js'

console.log(output())

document.querySelector('#header').appendChild(output()[0])

document.querySelector('#header').appendChild(output()[1])
