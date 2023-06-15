// webpack.dev.js
const webpack = require("webpack");
const config = require("./webpack.config.js");
config.entry.app.unshift("webpack-hot-middleware/client");
config.plugins.push(new webpack.HotModuleReplacementPlugin());
const compiler = webpack(config);
const express = require("express");
const app = express();
app.use(
  require("webpack-dev-middleware")(compiler, {
    publicPath: config.output.publicPath,
  })
);
app.use(require("webpack-hot-middleware")(compiler));
app.listen(3000, () => console.log("Dev server listening on port 3000"));
