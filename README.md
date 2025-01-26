# Instagram Automation

## Project Overview
This project, **Instagram Automation**, is a Python-based tool that generates short motivational videos. It uses random images and audio files, combines them with generated text from the Gemini API, and outputs a final video. The tool is designed to streamline the process of creating engaging Instagram content.

---

## Features
- **Gemini API Integration**: Generates motivational quotes based on user prompts.
- **Random Media Selection**: Picks random images and audio from specified directories.
- **Custom Video Creation**: Combines images, text, and audio into a polished video.
- **Text Effects**: Adds captions with customizable fonts, colors, and stroke effects.
- **Fade Effects**: Smooth fade-in and fade-out transitions for a professional look.

---

## Prerequisites
Before setting up the project, ensure the following are installed:

### Windows
1. [Python](https://www.python.org/downloads/) (version 3.7 or later)
2. [FFmpeg](https://ffmpeg.org/download.html)
   - Add FFmpeg to your system PATH.
3. [PIP](https://pip.pypa.io/en/stable/installation/)

### Ubuntu
1. Install Python:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```
2. Install FFmpeg:
   ```bash
   sudo apt install ffmpeg
   ```

---

## Setup

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd instagram-automation
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Set Up Directories
Ensure the following directories exist:
- `images/` (for image files)
- `sounds/` (for audio files)
- `video/` (for output videos)

### Step 4: Configure the API Key
Replace `<your-api-key>` in `main.py` with your Gemini API key.

---

## Running the Script
1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the script:
   ```bash
   python main.py
   ```
4. Enter a prompt when asked, e.g., `"Motivational quotes about success"`.
5. The generated video will be saved in the `video/` directory.

---

## Tips for Customization
- **Change Video Duration**: Modify `VIDEO_DURATION` in `main.py` to adjust the length of the videos.
- **Update Text Style**:
  - Font size: Change `FONT_SIZE`.
  - Font color: Update `FONT_COLOR`.
  - Font style: Change `FONT_STYLE` (ensure the font is installed on your system).
- **Adjust Text Position**: Modify `TEXT_VERTICAL_OFFSET` to move the text up or down.
- **Change Fade Duration**: Update `FADE_DURATION` for smoother or quicker transitions.

---

## Troubleshooting
### Common Issues
1. **No Images or Sounds Found**:
   - Ensure the `images/` and `sounds/` directories contain valid media files.
   - Supported image formats: `.png`, `.jpg`, `.jpeg`.
   - Supported audio formats: `.mp3`, `.wav`.

2. **FFmpeg Not Found**:
   - Verify FFmpeg is installed and added to your system PATH.
   - On Ubuntu, run `which ffmpeg` to confirm installation.

3. **API Errors**:
   - Ensure the Gemini API key is valid.
   - Check your internet connection.

4. **Python Errors**:
   - Ensure all dependencies are installed.
   - Run `pip install -r requirements.txt` again to verify.

---

## License
This project is open-source and available under the MIT License.

---

## Contribution
Feel free to fork the repository and submit pull requests. Suggestions and improvements are always welcome!

