var webpack = require('webpack');
var path = require('path');
var uglifyJsPlugin = webpack.optimize.UglifyJsPlugin;
var CopyWebpackPlugin = require('copy-webpack-plugin');

module.exports = {
  devtool: 'cheap-module-source-map',
  entry: [
    path.resolve(__dirname, 'src/main.js'),
  ],
  output: {
    path: __dirname + '/dist',
    publicPath: '',
    filename: 'bundle.js'
  },
  module: {
    loaders:[
      { 
        test: /\.css$/, 
        include: path.resolve(__dirname, 'src'), 
        loader: 'style-loader!css-loader' 
      },
      { 
        test: /\.js[x]?$/, 
        include: path.resolve(__dirname, 'src'), 
        exclude: /node_modules/, 
        loader: 'babel',
        query: {
            presets: ['es2015', 'stage-1', 'react']
        }
      },
    ]
  },
  resolve: {
    extensions: ['', '.js', '.jsx'],
  },
  plugins: [
    new webpack.optimize.DedupePlugin(),
    new uglifyJsPlugin({
      compress: {
        warnings: false
      }
    }),
    new CopyWebpackPlugin([
      { from: './src/index.html', to: 'index.html' },
      { from: './src/css', to: 'css'}
    ]),
    new webpack.DefinePlugin({
      "process.env": { 
         NODE_ENV: JSON.stringify("production") 
       }
    })
  ]
};
