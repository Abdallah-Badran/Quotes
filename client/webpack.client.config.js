const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    mode: 'development',
 	entry: './src/index.js',
 	module: {
 		rules: [
 			{
 			    test: /\.js$/,
 			    exclude: /node_modules/,
 			    use: {
                        loader: 'babel-loader'
                    }
 			},
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader']
            }
            ]
        },
        devServer: {
                        port: 3000,
                        open: true,
                        historyApiFallback: true,
                    },
        plugins: [
                    new HtmlWebpackPlugin({ template: './public/index.html' })
                ]
};