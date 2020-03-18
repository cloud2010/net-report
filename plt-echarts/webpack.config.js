const path = require('path')
const webpack = require('webpack')
const HtmlWebpackPlugin = require('html-webpack-plugin') // 加载HTML插件
const { CleanWebpackPlugin } = require('clean-webpack-plugin') // 清理dist文件夹
const MiniCssExtractPlugin = require('mini-css-extract-plugin') // webpack 4.x CSS和JS分离插件
// const ExtractTextPlugin = require('extract-text-webpack-plugin') // 分离CSS和JS文件 webpack 4.x 移除

module.exports = {
  devtool: 'inline-npsource-map',
  entry: {
    main: './src/main.js',
    charts: './src/plt.js'
  },
  output: {
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, 'dist')
  },
  module: {
    rules: [
      {
        // test: /\.css$/,
        // use: ExtractTextPlugin.extract({
        //   fallback: 'style-loader',
        //   use: 'css-loader'
        // })
        /**
         * 编译后用什么loader来提取css文件
         * 需要什么样的loader去编译文件
         */
        test: /\.css$/i,
        // use: ['style-loader', 'css-loader']
        use: [MiniCssExtractPlugin.loader, 'css-loader']
      },
      {
        test: /\.m?js$/,
        exclude: /(node_modules|bower_components)/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env']
          }
        }
      },
      {
        test: /\.(png|jpe?g|gif)$/i,
        use: [
          {
            loader: 'file-loader'
          }
        ]
      }
    ]
  },
  devServer: {
    contentBase: path.resolve(__dirname, 'dist'), // 本地服务器所加载的页面所在的目录
    historyApiFallback: true, // 不跳转
    inline: true // 实时刷新
  },
  plugins: [
    new CleanWebpackPlugin({
      cleanAfterEveryBuildPatterns: ['dist']
    }), // 清理dist文件夹
    new webpack.BannerPlugin('Author: capt.liu@foxmail.com'),
    new HtmlWebpackPlugin({
      // new一个这个插件的实例，并传入相关的参数
      template: path.resolve(__dirname, './src/view/index.tmpl.html')
    }),
    new webpack.optimize.OccurrenceOrderPlugin(),
    new MiniCssExtractPlugin()
    // new ExtractTextPlugin('style.css') // 加载插件
    // 压缩JS
    // new webpack.optimize.UglifyJsPlugin()
  ]
}
