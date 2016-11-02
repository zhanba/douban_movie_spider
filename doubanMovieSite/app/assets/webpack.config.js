var webpack = require('webpack');
var path = require('path');
var OpenBrowserPlugin = require('open-browser-webpack-plugin');

module.exports = {
    entry: [
        'webpack/hot/dev-server',
        'webpack-dev-server/client?http://localhost:3000',
        path.resolve(__dirname, 'src/main.js')
    ],
    output: {
        path: __dirname + '/dist',
        publicPath: '/',
        filename: './bundle.js'
    },
    devServer: {
        historyApiFallback: true,
        hot: true,
        inline: true,
        progress: true,
        contentBase: './src',
        port: 3000
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
                loader: 'style-loader!css-loader',
                // include: path.resolve(__dirname, 'app')
            }
        ]
    },
    plugins: [
        new webpack.HotModuleReplacementPlugin(),
        new OpenBrowserPlugin({ url: 'http://localhost:3000' })
    ],
}
