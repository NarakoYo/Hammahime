// 定义一个全局变量，用于存储音乐列表
var musicList = [];

// 定义一个回调函数，用于处理JSONP请求返回的数据
function handleData(data) {
  // 将返回的数据赋值给音乐列表
  musicList = data;
  // 调用播放音乐的函数
  playMusic();
}

// 定义一个函数，用于发送JSONP请求
function sendRequest() {
  // 创建一个script标签
  var script = document.createElement("script");
  // 设置script的src属性为目标URL，注意要加上回调函数的参数
  script.src = "Music/music.json?callback=handleData";
  // 将script插入到文档中
  document.body.appendChild(script);
}

// 定义一个函数，用于播放音乐
function playMusic() {
  // 获取audio元素和player元素
  var audio = document.getElementById("audio");
  var player = document.getElementById("player");
  // 设置一个变量，用于记录当前播放的音乐的索引
  var index = 0;
  // 设置audio的src属性为音乐列表中第一个音乐的路径
  audio.src = "Music/" + musicList[index];
  // 设置player的内容为音乐列表中第一个音乐的名称
  player.innerHTML = musicList[index];
  // 调用audio的play方法，开始播放音乐
  audio.play();
  
  // 监听audio的ended事件，当音乐播放结束时触发
  audio.addEventListener("ended", function() {
    // 将当前播放的音乐的索引加一，如果超过音乐列表的长度，则重置为零
    index++;
    if (index >= musicList.length) {
      index = 0;
    }
    // 设置audio的src属性为下一个音乐的路径
    audio.src = "Music/" + musicList[index];
    // 设置player的内容为下一个音乐的名称
    player.innerHTML = musicList[index];
    // 调用audio的play方法，继续播放音乐
    audio.play();
    // 设置audio的volume属性为零，表示静音
    audio.volume = 0;
    // 设置一个变量，用于记录淡入淡出的时间间隔（毫秒）
    var interval = 100;
    // 设置一个变量，用于记录淡入淡出的步长（0到1之间）
    var step = 0.1;
    // 定义一个函数，用于实现淡入效果
    function fadeIn() {
      // 如果音量小于1，则递增音量，并在一定时间后再次调用自身
      if (audio.volume < 1) {
        audio.volume += step;
        setTimeout(fadeIn, interval);
      }
    }
    // 定义一个函数，用于实现淡出效果
    function fadeOut() {
      // 如果音量大于0，则递减音量，并在一定时间后再次调用自身
      if (audio.volume > 0) {
        audio.volume -= step;
        setTimeout(fadeOut, interval);
      } else {
        // 如果音量等于0，则调用淡入效果的函数
        fadeIn();
      }
    }
    // 调用淡出效果的函数
    fadeOut();
  });
}

// 调用发送请求的函数
sendRequest();
