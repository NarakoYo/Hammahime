// server.js
// 引入模块
const express = require("express");
const fs = require("fs");
const path = require("path");

// 读取ApplicationConfig.yaml文件内容，并返回json格式的参数值，如果没有文件或文件内无内容则提示报错无内容或文件丢失
async function readConfigFile() {
  return new Promise((resolve, reject) => {
    fs.readFile(path.join(__dirname, "./ApplicationConfig.yaml"), "utf8", (error, data) => {
      if (error) {
        reject(error);
      } else {
        try {
          const config = JSON.parse(data);
          resolve(config);
        } catch (error) {
          reject(new Error("文件内容格式错误"));
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
console.log(config);
const port = config.port;
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
// app.listen(port, () => console.log(`Server listening on port ${port}`));
// 判断服务器是否启动
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
  console.log('server open');
}).on('error', (err) => {
  console.log('no start');
  console.log(err);
});

