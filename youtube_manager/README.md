# 🎥 YouTube Video Manager (CLI App)

A simple command-line interface (CLI) application in Python to manage your personal list of YouTube videos. You can add, update, delete, and view video entries stored in a local JSON-formatted text file (`youtube.txt`).

---

## 📂 Features

- 📄 List all YouTube videos
- ➕ Add a new video with name and duration
- ✏️ Update details of an existing video
- ❌ Delete a video by its number
- 💾 Data stored persistently in a `youtube.txt` file using JSON

---

## 🛠️ How It Works

- Videos are stored in a list of dictionaries with fields: `name` and `time`.
- The data is saved in `youtube.txt` in JSON format.
- Menu options are handled using Python 3.10+ `match-case` syntax.

---

## ▶️ Usage

```bash
python main.py
```
