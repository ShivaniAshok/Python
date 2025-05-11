# 🎥 YouTube Video Manager (SQLite App)

A command-line interface (CLI) application in Python that allows you to manage your personal list of YouTube videos, with data stored in a local SQLite database (`youtube_videos.db`). You can add, update, delete, and view video entries.

---

## 📂 Features

- 📄 List all YouTube videos from the SQLite database
- ➕ Add a new video with name and duration
- ✏️ Update details of an existing video
- ❌ Delete a video by its ID
- 💾 Data is stored persistently in an SQLite database (`youtube_videos.db`)

---

## 🛠️ How It Works

- The data is stored in a **SQLite database** (`youtube_videos.db`) with a table `videos`, which has columns: `id`, `name`, and `time`.
- SQLite is used to store and manage the data persistently, ensuring that the video list is saved between app launches.
- Menu options are handled using Python’s built-in SQLite module (`sqlite3`).

---

## ▶️ Usage

1. Clone the repo or navigate to the folder where the `youtube_manager_sqlite.py` script is located.

2. Make sure you have Python installed (version 3.x+).

3. Run the script:
```bash
python youtube_manager_sqlite.py
