import cv2
import pytesseract
import os
import re

# Provide path to tesseract executable
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe' # modify this path accordingly

def get_video_text(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if video opened successfully
    if not cap.isOpened():
        print("Error opening video stream or file")

    # Read the first 10 seconds (assuming 30 fps)
    frames = []
    for i in range(300):
        ret, frame = cap.read()
        if ret and i % 10 == 0:  # Only process every 10th frame
            frames.append(frame)
        else:
            continue

    # Use Tesseract to extract text
    text = ''
    for frame in frames:
        text += pytesseract.image_to_string(frame)

    # Cleanup
    cap.release()

    # Only keep the first 3 lines
    lines = text.split('\n')
    text = '\n'.join(lines[:3])

    return text

def sanitize_filename(filename):
    # Remove invalid characters
    filename = re.sub(r'[\\/*?:"<>|]', "", filename)

    # Replace newlines with spaces
    filename = filename.replace('\n', ' ')

    # Limit the length of the filename
    if len(filename) > 250:  # Leaving some space for the path
        filename = filename[:250]

    return filename

def rename_videos_in_folder(folder_path):
    # List all files in folder
    files = os.listdir(folder_path)

    # Filter out non-video files
    video_files = [f for f in files if f.endswith('.mp4') or f.endswith('.avi')] # add more formats if needed

    # Iterate over all video files
    for video_file in video_files:
        # Get full path to video file
        full_path = os.path.join(folder_path, video_file)

        # Extract text from video
        text = get_video_text(full_path)

        # Use the text to create a new name
        new_name = sanitize_filename(text.strip()).replace(' ', '_') + os.path.splitext(video_file)[1]

        # Get full path to new file name
        new_full_path = os.path.join(folder_path, new_name)

        # Rename file
        os.rename(full_path, new_full_path)

# Use the function
rename_videos_in_folder('C:\\Users\\User\\Desktop\\video')
