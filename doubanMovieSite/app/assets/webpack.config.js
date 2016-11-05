var webpack = require('webpack');
var path = require('path');
var OpenBrowserPlugin = require('open-browser-webpack-plugin');

var output = path.join(__dirname, '..');
var publicDistPath = '/static/js/dist/';

module.exports = {
    entry: [
        'webpack/hot/dev-server',
        'webpack-dev-server/client?http://localhost:3000',
        path.resolve(__dirname, 'src/main.js')
    ],
    output: {
        path: path.join(output, publicDistPath),
        publicPath: '/',
        filename: './bundle.js'
    },
    devServer: {
        historyApiFallback: true,
        hot: true,
        inline: true,
        progress: true,
        contentBase: './src',
        port: 3000,
        proxy: {
          '/api': {
            target: 'http://localhost:8100',
            secure: false
          }
        }
    },
    devtool: 'source-map',
    module: {
        loaders: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                include: path.resolve(__dirname, 'src'),
                loader: 'babel',
                query: {
                    presets: ['es2015', 'stage-1', 'react']
                }
            },
            {
                test: /\.css$/,
                loader: 'style-loader!css-loader?modules',
                include: path.resolve(__dirname, 'src')
            }
        ]
    },
    plugins: [
        new webpack.HotModuleReplacementPlugin(),
        new OpenBrowserPlugin({ url: 'http://localhost:3000' })
    ]
}
