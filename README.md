<<<<<<< HEAD
# YouTube Video Downloader 📺

![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/license-GPL--3.0-green.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
![Downloads](https://img.shields.io/badge/downloads-1k%2Fmonth-blue)
![Build Status](https://img.shields.io/badge/build-passing-success)

🎬 High-performance YouTube video and playlist downloader with customizable quality settings.

## ⭐ Key Features

- 🎥 **Video Downloads**
  - Resolution: 144p to 4K
  - Format: MP4 (H.264)
  - Quality Selection

<<<<<<< HEAD
- 🎵 **Audio Downloads**
  - High Quality (320kbps)
  - Format: M4A
=======
- Python 3.x
- FFmpeg (required for video processing)
- in window you need to install menually FFmpeg
>>>>>>> 39cfe7cb57e683ec7c045ba89de52aeeba295cfa

- 📑 **Advanced Features**
  - Playlist Support
  - Auto-Resume
  - Progress Tracking
  - Custom Output Path

<<<<<<< HEAD
---

## 🚀 Installation

### Prerequisites

- **Python 3.8** or higher
- **FFmpeg**
- **Internet Connection**
- **100MB free disk space**

---

### Windows Installation

1. **Install Python:**

   Download and install Python from the [official website](https://www.python.org/downloads/windows/). During installation, make sure to check the box **"Add Python to PATH"**.

2. **Install FFmpeg:**

   - Using **winget** (Windows Package Manager):

     ```powershell
     winget install ffmpeg
     ```

   - Or download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html) and add the `bin` folder to your system PATH.

3. **Clone the Repository:**

   Open Command Prompt or PowerShell:

   ```bash
   git clone https://github.com/myselfayush010/youtube-playlist-downloader.git
   cd youtube-playlist-downloader
   ```

4. **Create and Activate Virtual Environment:**

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

5. **Install Dependencies:**

```bash
pip install -r requirements.txt
```

### Linux Installation

1. **Install Python and FFmpeg:**

   For Debian/Ubuntu-based distributions:

   ```bash
   sudo apt update
   sudo apt install python3 python3-venv python3-pip ffmpeg git
   ```

2. **Clone the Repository:**

   ```bash
   git clone https://github.com/myselfayush010/youtube-playlist-downloader.git
   cd youtube-playlist-downloader
   ```

3. **Create and Activate Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

---

### macOS Installation

1. **Install Homebrew** (if not already installed):

   ```bash
   /bin/bash -c "$(curl -fsSL https://github.com/myselfayush010/youtube-playlist-downloader.git/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python and FFmpeg:**

   ```bash
   brew install python@3.9 ffmpeg git
   ```

3. **Clone the Repository:**

   ```bash
   git clone https://github.com/myselfayush010/youtube-playlist-downloader.git
   cd youtube-playlist-downloader
   ```

4. **Create and Activate Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

5. **Install Dependencies:**

```bash
pip install -r requirements.txt
```

## 💻 Usage Examples

- **Download Video (1080p):**

  ```bash
  python y.py "https://youtube.com/watch?v=..."
  ```

- **Download Playlist (720p):**

  ```bash
  python y.py "https://youtube.com/playlist?list=..." -r 720
  ```

- **Download Audio Only:**

  ```bash
  python y.py "https://youtube.com/watch?v=..." -a
  ```

---

## ⚙️ Options

| Flag | Description      | Default        |
|------|------------------|----------------|
| `-r` | Resolution       | `1080p`        |
| `-a` | Audio Only       | `False`        |
| `-o` | Output Directory | `./downloads`  |

---

## 🔧 Troubleshooting

- **FFmpeg not found:**

  Ensure FFmpeg is installed and added to your system PATH.

- **Permission Error:**

  Run the command with administrative privileges or adjust folder permissions.

- **SSL Certificate Error (macOS):**

  Install certificates:

  ```bash
  /Applications/Python\ 3.x/Install\ Certificates.command
  ```

- **Command Not Found:**

  Verify that Python and FFmpeg are correctly installed and accessible in your PATH.

---

## 🤝 Contributing

1. **Fork the Repository**

2. **Create a Feature Branch:**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Your Changes:**

   ```bash
   git commit -am "Add new feature"
   ```

4. **Push to the Branch:**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request**

---

## 📝 License

This project is licensed under the **GNU General Public License v3.0** - see the LICENSE file for details.

---

## 💬 Support

For support, open an issue on the [GitHub repository](https://github.com/yourusername/youtube-downloader/issues).

---

Happy downloading! 🎉
=======
1. Clone the repository:
```bash
git clone https://github.com/yourusername/youtube-downloader.git
cd youtube-downloader
>>>>>>> 39cfe7cb57e683ec7c045ba89de52aeeba295cfa
=======
# YouTube Video Downloader 📺

![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/license-GPL--3.0-green.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
![Downloads](https://img.shields.io/badge/downloads-1k%2Fmonth-blue)
![Build Status](https://img.shields.io/badge/build-passing-success)

🎬 High-performance YouTube video and playlist downloader with customizable quality settings.

## ⭐ Key Features

- 🎥 **Video Downloads**
  - Resolution: 144p to 4K
  - Format: MP4 (H.264)
  - Quality Selection

<<<<<<< HEAD
- 🎵 **Audio Downloads**
  - High Quality (320kbps)
  - Format: M4A
=======
- Python 3.x
- FFmpeg (required for video processing)
- in window you need to install menually FFmpeg
>>>>>>> 39cfe7cb57e683ec7c045ba89de52aeeba295cfa

- 📑 **Advanced Features**
  - Playlist Support
  - Auto-Resume
  - Progress Tracking
  - Custom Output Path

<<<<<<< HEAD
---

## 🚀 Installation

### Prerequisites

- **Python 3.8** or higher
- **FFmpeg**
- **Internet Connection**
- **100MB free disk space**

---

### Windows Installation

1. **Install Python:**

   Download and install Python from the [official website](https://www.python.org/downloads/windows/). During installation, make sure to check the box **"Add Python to PATH"**.

2. **Install FFmpeg:**

   - Using **winget** (Windows Package Manager):

     ```powershell
     winget install ffmpeg
     ```

   - Or download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html) and add the `bin` folder to your system PATH.

3. **Clone the Repository:**

   Open Command Prompt or PowerShell:

   ```bash
   git clone https://github.com/yourusername/youtube-downloader.git
   cd youtube-downloader
   ```

4. **Create and Activate Virtual Environment:**

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

5. **Install Dependencies:**

```bash
pip install -r requirements-prod.txt
pip install -r requirements-dev.txt
pip install -r requirements.txt
pip install -r requirements-docs.txt
pip install -r requirements-optional.txt
```

### Linux Installation

1. **Install Python and FFmpeg:**

   For Debian/Ubuntu-based distributions:

   ```bash
   sudo apt update
   sudo apt install python3 python3-venv python3-pip ffmpeg git
   ```

2. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/youtube-downloader.git
   cd youtube-downloader
   ```

3. **Create and Activate Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

---

### macOS Installation

1. **Install Homebrew** (if not already installed):

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python and FFmpeg:**

   ```bash
   brew install python@3.9 ffmpeg git
   ```

3. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/youtube-downloader.git
   cd youtube-downloader
   ```

4. **Create and Activate Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

5. **Install Dependencies:**

```bash
pip install -r requirements-prod.txt
pip install -r requirements-dev.txt
pip install -r requirements.txt
pip install -r requirements-docs.txt
pip install -r requirements-optional.txt
```

## 💻 Usage Examples

- **Download Video (1080p):**

  ```bash
  python y.py "https://youtube.com/watch?v=..."
  ```

- **Download Playlist (720p):**

  ```bash
  python y.py "https://youtube.com/playlist?list=..." -r 720
  ```

- **Download Audio Only:**

  ```bash
  python y.py "https://youtube.com/watch?v=..." -a
  ```

---

## ⚙️ Options

| Flag | Description      | Default        |
|------|------------------|----------------|
| `-r` | Resolution       | `1080p`        |
| `-a` | Audio Only       | `False`        |
| `-o` | Output Directory | `./downloads`  |

---

## 🔧 Troubleshooting

- **FFmpeg not found:**

  Ensure FFmpeg is installed and added to your system PATH.

- **Permission Error:**

  Run the command with administrative privileges or adjust folder permissions.

- **SSL Certificate Error (macOS):**

  Install certificates:

  ```bash
  /Applications/Python\ 3.x/Install\ Certificates.command
  ```

- **Command Not Found:**

  Verify that Python and FFmpeg are correctly installed and accessible in your PATH.

---

## 🤝 Contributing

1. **Fork the Repository**

2. **Create a Feature Branch:**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Your Changes:**

   ```bash
   git commit -am "Add new feature"
   ```

4. **Push to the Branch:**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request**

---

## 📝 License

This project is licensed under the **GNU General Public License v3.0** - see the LICENSE file for details.

---

## 💬 Support

For support, open an issue on the [GitHub repository](https://github.com/yourusername/youtube-downloader/issues).

---

Happy downloading! 🎉
=======
1. Clone the repository:
```bash
git clone https://github.com/yourusername/youtube-downloader.git
cd youtube-downloader
>>>>>>> 39cfe7cb57e683ec7c045ba89de52aeeba295cfa
>>>>>>> origin/main
