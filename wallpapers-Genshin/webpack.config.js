// webpack.config.js
const path = require("path");
module.exports = {
  entry: "./server.js",
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "server.bundle.js",
  },
  module: {
    rules: [
      {
        test: /\.(mp3|wav|ogg)$/,
        use: "file-loader",
      },
    ],
  },
};
