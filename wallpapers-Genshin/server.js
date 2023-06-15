// server.js
// 引入模块
const express = require("express");
const fs = require("fs");
const path = require("path");

// 创建服务器
const app = express();

// 定义变量
const port = 3000; // 端口号
const musicDir = path.join(__dirname, "./Script/Music"); // 音乐目录

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

// 启动服务器
app.listen(port, () => console.log(`Server listening on port ${port}`));
