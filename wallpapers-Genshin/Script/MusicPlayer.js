// script.js
// 获取元素
const player = document.getElementById("player");
const play = document.getElementById("play");
const volume = document.getElementById("volume");
const name = document.getElementById("name");
const status = document.getElementById("status");

// 定义变量
let musicList = []; // 音乐列表
let currentIndex = -1; // 当前音乐索引
let isPlaying = false; // 是否正在播放

// 定义函数
// 获取音乐列表
function getMusicList() {
  fetch("/Music")
    .then((response) => response.json())
    .then((data) => {
      musicList = data; // 赋值给音乐列表
      if (musicList.length > 0) {
        // 如果有音乐，加载第一首
        loadMusic(0);
      }
    })
    .catch((error) => console.error(error));
}

// 加载音乐
function loadMusic(index) {
  currentIndex = index; // 更新当前索引
  player.src = musicList[index]; // 设置音乐源
  name.textContent = musicList[index].split("/").pop(); // 显示音乐名称
}

// 播放/暂停音乐
function togglePlay() {
  if (isPlaying) {
    // 如果正在播放，暂停音乐
    player.pause();
    isPlaying = false; // 更新状态
    play.textContent = "Play"; // 更新按钮文本
    status.textContent = "Paused"; // 更新状态文本
    player.volume = volume.value; // 恢复音量
    player.style.transition = "none"; // 取消过渡效果
    player.style.opacity = "1"; // 恢复不透明度
  } else {
    // 如果没有播放，播放音乐
    player.play();
    isPlaying = true; // 更新状态
    play.textContent = "Pause"; // 更新按钮文本
    status.textContent = "Playing"; // 更新状态文本
  }
}

// 切换下一首音乐
function switchMusic() {
  if (musicList.length > 0) {
    // 如果有音乐，计算下一首索引
    let nextIndex = (currentIndex + 1) % musicList.length;
    loadMusic(nextIndex); // 加载下一首音乐
    if (isPlaying) {
      // 如果正在播放，继续播放
      player.play();
    }
  }
}

// 调整音量
function changeVolume() {
  player.volume = volume.value; // 设置音乐音量
}

// 添加事件监听器
window.addEventListener("load", getMusicList); // 窗口加载时，获取音乐列表
play.addEventListener("click", togglePlay); // 点击播放/暂停按钮，切换播放状态
volume.addEventListener("input", changeVolume); // 拖动音量滑块，调整音量
player.addEventListener("ended", switchMusic); // 音乐结束时，切换下一首音乐

// 添加淡入淡出效果
player.addEventListener("play", () => {
  player.style.transition = "opacity 2s"; // 设置过渡效果
  player.style.opacity = "1"; // 设置不透明度为1
});

player.addEventListener("pause", () => {
  player.style.transition = "opacity 2s"; // 设置过渡效果
  player.style.opacity = "0"; // 设置不透明度为0
});
