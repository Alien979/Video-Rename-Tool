# Video-Rename-Tool
---
# Video Rename Tool

This tool uses optical character recognition (OCR) to rename video files based on text visible in the first 10 seconds of the video. It uses OpenCV to handle video files and Tesseract-OCR to extract text from frames of the video.

## Setup

### Dependencies

- OpenCV
- PyTesseract
- Python 3

The dependencies can be installed using pip:

```sh
pip install opencv-python pytesseract
```

### Tesseract-OCR

This program uses Tesseract-OCR to extract text from video frames. You will need to install Tesseract on your system and provide the path to the executable in the script.

For Windows, you can download Tesseract from the [GitHub releases](https://github.com/UB-Mannheim/tesseract/wiki) page.

## Usage

To use the tool, modify the `folder_path` at the end of the script to the directory containing the videos you want to rename.

Then, simply run the script:

```sh
python app.py
```

The script will iterate over all video files (currently .mp4 and .avi files are supported) in the provided directory, extract text from the first 10 seconds of each video, and rename the video files based on the extracted text.

## Notes

This script only keeps the first 3 lines of the extracted text to rename the files. You can adjust the number of lines in the `get_video_text` function.

Also, it's important to note that this method may not work perfectly if the text you need is not within the first few lines of the extracted text. In that case, you might have to use more complex text processing techniques.

---

