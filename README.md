# Video to GIF Converter

This repository contains a simple web application built with Streamlit that converts video files into GIFs. The application allows users to upload a video, and it generates GIFs at regular intervals from the video.

## Features

- Upload videos in formats like MP4, MOV, and AVI.
- Generate GIFs at regular intervals (default: every 5 seconds, each lasting 3 seconds).
- Preview and download the generated GIFs.
- Automatically cleans up temporary files after processing.

## Requirements

- Python 3.7+
- FFmpeg installed and added to your system PATH

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/video-to-gif-converter.git
   cd video-to-gif-converter
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```

3. Install the required Python packages:
   ```bash
   pip install streamlit moviepy
   ```

4. Install FFmpeg:
   - Download FFmpeg from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html).
   - Add the FFmpeg `bin` directory to your system's PATH.

5. Verify FFmpeg installation:
   ```bash
   ffprobe -version
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app3.py
   ```

2. Open your web browser and navigate to the provided URL (usually `http://localhost:8501`).

3. Upload a video file and click the **Generate GIFs** button.

4. Preview and download the generated GIFs.

## File Details

- **`app3.py`**: Main script for the Streamlit application.

## Dependencies

The application uses the following libraries:

- [Streamlit](https://streamlit.io/): For creating the web application.
- [MoviePy](https://zulko.github.io/moviepy/): For video processing and GIF creation.

## Notes

- The application generates temporary files (videos and GIFs) during processing, which are cleaned up automatically after use.
- FFmpeg is required for video duration detection and must be installed separately.

## Contributions

Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit a pull request.

## Acknowledgments

Special thanks to the developers of Streamlit and MoviePy for their excellent tools.

