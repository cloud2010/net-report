import './style/style.css';
const greeter = require('./greeter.js');
document.querySelector("#chart").appendChild(greeter());

var h1_test = document.createElement('h1');
h1_test.textContent = 'hello webpack world';
h1_test.classList.add('test');

document.querySelector("#chart").appendChild(h1_test);

var echarts = require('echarts');

// 引入 ECharts 主模块
var echarts = require('echarts/lib/echarts');
// 引入柱状图
require('echarts/lib/chart/bar');
// 引入提示框和标题组件
require('echarts/lib/component/tooltip');
require('echarts/lib/component/title');

// 基于准备好的dom，初始化echarts实例
var divRender = document.querySelector("#main");
divRender.setAttribute('style', 'width:800px; height:600px;');

var myChart = echarts.init(divRender);
// 绘制图表
myChart.setOption({
    title: {
        text: 'ECharts 入门示例'
    },
    tooltip: {},
    xAxis: {
        data: ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
    },
    yAxis: {},
    series: [{
        name: '销量',
        type: 'bar',
        data: [5, 20, 36, 10, 10, 20]
    }]
});