import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from time import sleep

# Load environment variables
load_dotenv()

# Configure Google Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Prompt for generating the summary
prompt = """
Summarize the following YouTube transcript intended for educational purposes. Highlight key concepts, definitions, and important explanations. Ensure that the summary is structured in a way 
that makes it easy to understand for someone who may not be familiar with the topic. 
Keep the summary under [number] words.  
"""

# Function to extract transcript from YouTube video
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        raise e

# Function to generate summary using Google Gemini API
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

# Custom CSS to make the interface visually appealing
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
        font-family: 'Montserrat', sans-serif;
    }
    .main {
        background-color: white;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    h1 {
        color: #333;
        font-size: 3rem;
        text-align: center;
        margin-bottom: 20px;
        font-weight: 700;
    }
    .input {
        margin: 20px 0;
        font-size: 1.2rem;
        border-radius: 8px;
        border: 2px solid #ccc;
        padding: 10px;
    }
    button {
        border-radius: 10px;
        padding: 10px;
        font-size: 1.2rem;
        background-color: #4CAF50;
        color: white;
        transition: background-color 0.3s ease;
        border: none;
    }
    button:hover {
        background-color: #45a049;
    }
    .stImage {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    .stMarkdown {
        color: #333;
        font-size: 1.2rem;
        background: rgba(0, 0, 0, 0.05);
        padding: 10px;
        border-radius: 10px;
    }
    .summary-section {
        background-color: #f9f9f9;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
    }
    .progress-bar {
        width: 100%;
        background-color: #f3f3f3;
    }
    .progress-bar-fill {
        height: 24px;
        background-color: #4CAF50;
        transition: width 0.5s;
    }
    .dark-mode {
        background-color: #2c2c2c;
        color: #fff;
    }
    </style>
""", unsafe_allow_html=True)

# Title and YouTube input
st.title("📚 YouTube Transcript to Detailed Notes Converter")

youtube_link = st.text_input("Enter YouTube Video Link:", placeholder="Paste YouTube URL here")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

# Button to get the summary with a progress bar simulation
if st.button("Get Detailed Notes"):
    with st.spinner('Fetching Transcript...'):
        for progress in range(0, 101, 10):
            st.markdown(f'<div class="progress-bar"><div class="progress-bar-fill" style="width: {progress}%"></div></div>', unsafe_allow_html=True)
            sleep(0.1)
    
    transcript_text = extract_transcript_details(youtube_link)
    
    if transcript_text:
        summary = generate_gemini_content(transcript_text, prompt)
        st.markdown("<div class='summary-section'><h2>Detailed Notes:</h2></div>", unsafe_allow_html=True)
        st.write(summary)

# Dark mode toggle (optional)
dark_mode = st.checkbox("Enable Dark Mode")
if dark_mode:
    st.markdown("<style>.main { background-color: #2c2c2c; color: white; }</style>", unsafe_allow_html=True)
