// Greeter.js
import './style/style.css'
var dataset = require('../public/info.json')
/**
 * 返回两个DOM元素
 * @returns a 元素1 b 元素2
 * @version ver 1.00
 */
export default function output() {
  var greet = document.createElement('div')
  var hello = document.createElement('h1')
  greet.textContent = dataset.greetText
  hello.innerHTML = dataset.helloText
  hello.classList.add('test')
  return [greet, hello]
}
