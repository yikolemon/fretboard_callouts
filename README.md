# 吉他弦音播报练习器

设置间隔时间，自动播报「弦号 + 音名」（如「1弦G」「3弦F」），帮助吉他练习者按指板位置找音。纯前端单页应用，无需后端。

## 功能

- **间隔播报**：自定义间隔秒数，按节奏自动播报下一组「弦号 + 音名」
- **音频拼接**：预生成中文音频片段，用 Web Audio API 拼接成连续音频无缝播放
- **自定义品位范围**：全局设置起止品位（如 0~7 品），据此计算每根弦上可出现的音
- **随机不重复**：可选近 N 个不重复，避免短时间出现相同组合
- **升降号开关**：默认仅自然音（C D E F G A B），可在设置中开启升号
- **小窗悬浮**：支持 Document Picture-in-Picture，练琴时小窗置顶不挡视线
- **控制**：开始 / 暂停 / 停止，实时倒计时、已播报数量、最近播报历史

## 快速开始

```bash
# 1. 生成音频片段（需要联网，首次运行）
pip install edge-tts
python generate_audio.py

# 2. 启动本地服务器
python -m http.server 8000

# 3. 浏览器打开
#    http://localhost:8000
```

## 音频生成

使用 [edge-tts](https://github.com/rany2/edge-tts)（微软免费中文 TTS）预生成音频片段到 `audio/` 目录：

- 弦号：中文音色念「一弦」~「六弦」
- 音名：英文音色念字母（C D E F G A B）
- 升号音：英文音色念「C sharp」等

运行 `generate_audio.py` 即可重新生成全部片段。

## 技术栈

- HTML / CSS / 原生 JavaScript
- Web Audio API（音频预解码与拼接播放）
- Document Picture-in-Picture API（小窗悬浮，需 Chrome / Edge 116+）
- edge-tts（音频片段预生成）

## 文件结构

```
guitar-nota/
├── index.html          # 单页应用
├── generate_audio.py   # 音频片段生成脚本
├── app.py              # 桌面应用启动脚本（pywebview）
├── audio/              # 预生成的音频片段
│   ├── 1.mp3 ~ 6.mp3   # 弦号
│   └── C.mp3 ... Gs.mp3# 音名（含升号）
└── .gitignore
```

## 打包成可执行程序

使用 PyWebView + PyInstaller 打包成 Windows 单 exe（双击即用，无需安装 Python）：

```bash
pip install pywebview pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "guitar-nota" ^
  --add-data "index.html;." --add-data "audio;audio" app.py
```

生成的可执行文件位于 `dist/guitar-nota.exe`（约 18MB）。

## 浏览器要求

- Chrome / Edge 116+（小窗功能需要 Document PiP API）
- 其他浏览器可正常使用除小窗外的功能
