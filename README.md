
# LLM-Based Application for YouTube Transcript Summarization and Learning

This project is an AI-powered tool designed to summarize YouTube video transcripts, focusing on educational content. It leverages Large Language Models (LLMs) to extract key concepts, definitions, and explanations from lengthy video transcripts, providing concise and structured summaries. The tool simplifies the learning process by converting YouTube videos into easily digestible notes, helping users to quickly grasp the core ideas of educational content.

## Features

- **YouTube Transcript Extraction**: Automatically extracts transcripts from YouTube videos.
- **LLM-Based Summarization**: Uses advanced LLM (Google Gemini) to generate insightful and concise summaries.
- **Simple and User-Friendly Interface**: A streamlined, intuitive interface for ease of use.
- **Dark Mode**: Switch between light and dark modes for a comfortable viewing experience.
- **Progress Bar for Processing**: Visual feedback through a progress bar during transcript fetching.

## Installation

### Prerequisites

- Python 3.7+
- [Streamlit](https://streamlit.io)
- Google Gemini API Key
- YouTube Transcript API

### Clone the Repository

```bash
git clone https://github.com/atharv2001j/LLM-YouTube-Transcript-Summarizer.git
cd LLM-YouTube-Transcript-Summarizer
```

### Install Required Libraries

```bash
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root and add your Google Gemini API key:

```
GOOGLE_API_KEY=your_google_gemini_api_key
```

## Usage

1. **Run the Application**:
    ```bash
    streamlit run app.py
    ```

2. **Input YouTube Video URL**: Enter the YouTube video link into the text box.

3. **View Transcript and Summary**: The app will display the video thumbnail, fetch the transcript, and generate a summarized version of the transcript.

## Project Structure

```
├── app.py                  # Main Streamlit app file
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (API Key)
└── README.md               # Project documentation
```

## Example

1. Input YouTube URL:
   `https://www.youtube.com/watch?v=dQw4w9WgXcQ`

2. Output:
   - Video thumbnail
   - Full video transcript
   - Summarized key points and explanations

## Future Enhancements

- Support for multiple languages in transcript summarization.
- Summarization customization based on word limits or topics.
- Export summary as PDF or text file.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.

## For more details 

For more details of the project contact me on joshiatharv67@gmail.com

## Demo link 

https://www.loom.com/share/ead72d63ad8a4cd985e80e2076b98622?sid=cefc7536-42e6-4354-8295-c8d89eca1e49
