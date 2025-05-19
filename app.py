import streamlit as st
from video_utils import download_youtube_video, extract_audio
from transcript_utils import transcribe_audio
from summarize_utils import summarize_with_chapters
from visual_utils import extract_keyframes, get_best_frame

st.title("🎞️ Video to Documentary Generator")

url = st.text_input("Enter YouTube Video URL")

if st.button("Generate Documentary"):
    with st.spinner("Downloading and processing video..."):
        video_path = download_youtube_video(url)
        audio_path = extract_audio(video_path)
        transcript = transcribe_audio(audio_path)
        summary = summarize_with_chapters(transcript)

    st.header("📝 Documentary Summary")
    st.markdown(summary)

    with st.spinner("Extracting visuals..."):
        frames = extract_keyframes(video_path)
        best_image = get_best_frame(summary, frames)

    st.header("📷 Representative Visual")
    st.image(best_image, use_column_width=True)
