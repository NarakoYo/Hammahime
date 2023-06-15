// server.js
// 引入模块
const express = require("express");
const fs = require("fs");
const path = require("path");

// 读取ApplicationConfig.yaml文件内容，并返回键值关系的json
function readConfigFile() {
  return new Promise((resolve, reject) => {
    fs.readFile(path.join(__dirname, "./ApplicationConfig.yaml"), "utf8", (error, data) => {
      if (error) {
        reject(error);
      } else {
        try {
          const config = yaml.safeLoad(data);
          resolve(config);
        } catch (error) {
          reject(error);
        }
      }
    });
  });
}

// 创建服务器
const app = express();

// 定义变量
// const port = 3000; // 端口号
 
// 读取ApplicationConfig.yaml文件内容，并返回键值关系的json
const config = await readConfigFile();
const port = config.port || 3001; // 如果yaml文件中没有定义端口，则使用默认端口3001
console.log(port)

const musicDir = path.join(__dirname, "./Script/Music"); // 音乐目录
// const musicFiles = require.context("./Script/Music", false, /\.(mp3|wav|ogg)$/);

// 定义函数
// 获取音乐列表
function getMusicList() {
  return new Promise((resolve, reject) => {
    fs.readdir(musicDir, (error, files) => {
      if (error) {
        reject(error);
      } else {
        resolve(
          files.filter((file) => /\.(mp3|wav|ogg)$/.test(file)) // 过滤出音乐格式的文件
        );
      }
    });
  });
}

// 定义路由
// 静态资源托管
app.use(express.static(__dirname));

// 获取音乐列表接口
app.get("/music", async (req, res) => {
  try {
    let musicList = await getMusicList(); // 获取音乐列表
    res.json(musicList.map((file) => "/Script/Music/" + file)); // 返回json格式的数据，添加相对路径前缀
  } catch (error) {
    res.status(500).send(error.message); // 返回错误信息
  }
});

// // 设置静态资源目录为打包后的dist目录
// app.use(express.static(__dirname + "/dist")); 
// // 返回json格式的数据，去掉相对路径前缀
// app.get("/music", (req, res) => {
//   res.json(musicFiles.keys().map((file) => file.slice(1))); 
// });

// 启动服务器
app.listen(port, () => console.log(`Server listening on port ${port}`));
