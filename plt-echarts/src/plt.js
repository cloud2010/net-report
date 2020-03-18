/**
 * 绘图代码
 */

var dataset = require('../public/09-m-1-app-t20.json')
// 构建数据
var pltData = []
var pltValue = []
dataset.forEach(element => {
  pltData.push(element[1])
  pltValue.push(element[6])
})
var echarts = require('echarts')

// 引入 ECharts 主模块
var echarts = require('echarts/lib/echarts')
// 引入柱状图
require('echarts/lib/chart/bar')
// 引入提示框和标题组件
require('echarts/lib/component/tooltip')
require('echarts/lib/component/title')

// 基于准备好的dom，初始化echarts实例
var divRender = document.querySelector('#main')
divRender.setAttribute('style', 'width:1200px; height:600px;')

var myChart = echarts.init(divRender)
// 绘制图表
myChart.setOption({
  title: {
    text: '临港大学城9月份大一男生APP情况'
  },
  tooltip: {},
  xAxis: {
    data: pltData
  },
  yAxis: {},
  series: [
    {
      name: 'UV值',
      type: 'bar',
      data: pltValue
    }
  ]
})
