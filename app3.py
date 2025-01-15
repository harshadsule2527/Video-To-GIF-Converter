import streamlit as st
import os
from moviepy.editor import VideoFileClip

def create_gif(input_file, start_time, duration, output_file):
    clip = VideoFileClip(input_file).subclip(start_time, start_time + duration)
    clip.write_gif(output_file, fps=10)
    clip.close()

def process_video(video_file):
    # Save uploaded video temporarily
    temp_video_path = "temp_video.mp4"
    with open(temp_video_path, "wb") as f:
        f.write(video_file.read())

    # Use moviepy to get video duration
    with VideoFileClip(temp_video_path) as clip:
        duration = clip.duration

    # Create GIFs at regular intervals (every 5 seconds for this example)
    interval = 5
    gif_files = []
    for i in range(0, int(duration), interval):
        output_file = f"output_{i}.gif"
        create_gif(temp_video_path, i, min(3, duration - i), output_file)
        gif_files.append(output_file)

    # Clean up temporary video file
    os.remove(temp_video_path)

    return gif_files

st.title("Video to GIFs Converter")

uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    st.video(uploaded_file)

    if st.button("Generate GIFs"):
        with st.spinner("Processing video and generating GIFs..."):
            gif_files = process_video(uploaded_file)

        st.success(f"Generated {len(gif_files)} GIFs!")

        for gif_file in gif_files:
            st.image(gif_file)
            # Optionally, provide download buttons for each GIF
            with open(gif_file, "rb") as file:
                btn = st.download_button(
                    label=f"Download {gif_file}",
                    data=file,
                    file_name=gif_file,
                    mime="image/gif"
                )

        # Clean up GIF files
        for gif_file in gif_files:
            os.remove(gif_file)