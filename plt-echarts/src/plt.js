/**
 * 绘图代码
 */
// 引入 ECharts 主模块
import echarts from 'echarts/lib/echarts'
// var echarts = require('echarts/lib/echarts') // 旧版写法
// 引入柱状图
// require('echarts/lib/chart/bar')
import 'echarts/map/js/china'
import 'echarts/lib/chart/line'
import 'echarts/lib/chart/map'
// 引入提示框和标题组件
import 'echarts/lib/component/tooltip'
import 'echarts/lib/component/toolbox'
import 'echarts/lib/component/title'
import 'echarts/lib/component/legend'
import 'echarts/lib/component/dataZoom'
import 'echarts/lib/component/geo'
import 'echarts/lib/component/visualMap'

// 导出SVG
const svgBtn = window.document.querySelector('#download')
svgBtn.addEventListener('click', () => {
  const content = document.querySelector('svg').outerHTML
  const blob = new Blob([content], { type: 'xml/svg' })
  svgBtn.href = URL.createObjectURL(blob)
  svgBtn.download = option.title.text + '.svg'
})
// 基于准备好的dom，初始化echarts实例
var divRender = document.querySelector('#main')
divRender.setAttribute('style', 'width:1000px; height:800px;')
// 基于准备好的dom，初始化echarts实例（渲染模式为SVG）
var myChart = echarts.init(divRender, null, { renderer: 'svg' })
// 绘制图表
var yiban = [
  {
    name: '南海诸岛',
    value: 0
  },
  {
    name: '北京',
    value: 54
  },
  {
    name: '天津',
    value: 13
  },
  {
    name: '上海',
    value: 40
  },
  {
    name: '重庆',
    value: 75
  },
  {
    name: '河北',
    value: 13
  },
  {
    name: '河南',
    value: 83
  },
  {
    name: '云南',
    value: 11
  },
  {
    name: '辽宁',
    value: 19
  },
  {
    name: '黑龙江',
    value: 15
  },
  {
    name: '湖南',
    value: 69
  },
  {
    name: '安徽',
    value: 60
  },
  {
    name: '山东',
    value: 39
  },
  {
    name: '新疆',
    value: 4
  },
  {
    name: '江苏',
    value: 31
  },
  {
    name: '浙江',
    value: 104
  },
  {
    name: '江西',
    value: 36
  },
  {
    name: '湖北',
    value: 1052
  },
  {
    name: '广西',
    value: 33
  },
  {
    name: '甘肃',
    value: 7
  },
  {
    name: '山西',
    value: 9
  },
  {
    name: '内蒙古',
    value: 7
  },
  {
    name: '陕西',
    value: 22
  },
  {
    name: '吉林',
    value: 4
  },
  {
    name: '福建',
    value: 18
  },
  {
    name: '贵州',
    value: 5
  },
  {
    name: '广东',
    value: 98
  },
  {
    name: '青海',
    value: 1
  },
  {
    name: '西藏',
    value: 0
  },
  {
    name: '四川',
    value: 44
  },
  {
    name: '宁夏',
    value: 4
  },
  {
    name: '海南',
    value: 22
  },
  {
    name: '台湾',
    value: 3
  },
  {
    name: '香港',
    value: 5
  },
  {
    name: '澳门',
    value: 5
  }
]

var option = {
  title: {
    text: '易班各省市自治区注册人数',
    subtext: '来源：易班网',
    left: 'center',
    textStyle: {
      fontSize: 26
    }
  },
  tooltip: {
    trigger: 'item',
    showDelay: 0,
    transitionDuration: 0.2,
    formatter: function(params) {
      var value = (params.value + '').split('.')
      value = value[0].replace(/(\d{1,3})(?=(?:\d{3})+(?!\d))/g, '$1,')
      return params.seriesName + '<br/>' + params.name + ': ' + value
    }
  },
  toolbox: {
    feature: {
      // dataView: { readOnly: false },
      // restore: {},
      saveAsImage: { pixelRatio: 3 } // 图片保存比例
    }
  },
  visualMap: {
    min: 0,
    max: 1000,
    // left: 26,
    // bottom: 40,
    top: '55%',
    left: '10%',
    showLabel: true,
    text: ['高', '低'],
    // pieces: [
    //   {
    //     gt: 100,
    //     label: '> 100 人',
    //     color: '#7f1100'
    //   },
    //   {
    //     gte: 10,
    //     lte: 100,
    //     label: '10 - 100 人',
    //     color: '#ff5428'
    //   },
    //   {
    //     gte: 1,
    //     lt: 10,
    //     label: '1 - 9 人',
    //     color: '#ff8c71'
    //   },
    //   {
    //     gt: 0,
    //     lt: 1,
    //     label: '其它',
    //     color: '#ffd768'
    //   },
    //   {
    //     value: 0,
    //     color: '#dddddd'
    //   }
    // ],
    show: true,
    // orient: 'horizontal',
    inRange: {
      // color: ['#3B5077', '#031525'] // 蓝黑
      // color: ['#ffc0cb', '#800080'] // 红紫
      // color: ['#3C3B3F', '#605C3C'] // 黑绿
      // color: ['#0f0c29', '#302b63', '#24243e'] // 黑紫黑
      // color: ['#23074d', '#cc5333'] // 紫红
      // color: ['#F6CED8', '#D90505'] //蓝红
      // color: ['#00467F', '#A5CC82'] // 蓝绿
      color: ['#ffffff', '#1488CC', '#00467F', '#2B32B2'] // 浅蓝
      // color: ['#00467F', '#A5CC82'] // 蓝绿
    }
  },
  geo: {
    name: '中国地图',
    map: 'china',
    roam: false, // 缩放移动
    scaleLimit: {
      min: 1,
      max: 2
    },
    zoom: 1.0,
    top: 'auto',
    label: {
      normal: {
        show: true,
        fontSize: '15',
        color: '#000000'
      }
    },
    itemStyle: {
      normal: {
        // shadowBlur: 10,
        shadowColor: 'rgba(0, 0, 0, 0.2)',
        borderWidth: 1,
        opacity: 0.85,
        borderColor: '#666666'
      },
      emphasis: {
        areaColor: '#f2d5ad',
        shadowOffsetX: 0,
        shadowOffsetY: 0,
        borderWidth: 0
      }
    }
  },
  series: [
    {
      name: '易班各省市自治区注册人数',
      type: 'map',
      geoIndex: 0,
      data: yiban
    }
  ]
}

myChart.setOption(option)
