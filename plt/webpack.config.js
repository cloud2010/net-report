const path = require('path');
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin'); // 加载HTML插件

module.exports = {
  devtool: 'source-map',
  entry: './src/main.js',
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist')
  },
  module: {
    rules: [{
      test: /\.css$/,
      use: [
        'style-loader', 'css-loader'
      ]
    }]

  },
  devServer: {
    contentBase: "./dist", //本地服务器所加载的页面所在的目录
    historyApiFallback: true, //不跳转
    inline: true //实时刷新
  },
  plugins: [
    new webpack.BannerPlugin('Author: capt.liu@foxmail.com'),
    new HtmlWebpackPlugin({
      // new一个这个插件的实例，并传入相关的参数
      template: __dirname + "/src/view/index.tmpl.html"
    }),
    new webpack.optimize.OccurrenceOrderPlugin(),
    // 压缩JS
    // new webpack.optimize.UglifyJsPlugin()
  ],
};