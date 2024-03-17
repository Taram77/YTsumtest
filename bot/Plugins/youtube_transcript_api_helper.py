from youtube_transcript_api import YouTubeTranscriptApi
import re

def get_video_id(youtube_url):
    # Regular expression patterns for different YouTube URL formats
    patterns = [
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/watch\?v=([0-9A-Za-z_-]{11})',  # Standard watch URL
        r'(?:https?:\/\/)?youtu\.be\/([0-9A-Za-z_-]{11})',  # Shortened URL
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/embed\/([0-9A-Za-z_-]{11})',  # Embedded URL
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/v\/([0-9A-Za-z_-]{11})',  # Legacy embed URL
    ]

    for pattern in patterns:
        match = re.search(pattern, youtube_url)
        if match:
            return match.group(1)

    return None  # If no pattern matches

def get_youtube_transcription(video_id):
    try:
        # Fetching the transcript
        list_of_languages = get_youtube_list_transctipt_languages(video_id)
        # Assuming the original language might have the most comprehensive transcript
        default_transcript = max(set(list_of_languages), key=list_of_languages.count)

        transcripted_text = ""
        if(default_transcript):
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[default_transcript])
            # Printing the transcript
            for entry in transcript:
                transcripted_text += entry['text'] + "\n"
        return transcripted_text
    except Exception as e:
        return None

def get_youtube_list_transctipt_languages(video_id):
    # Fetching all available transcripts for the video
    transcripts = YouTubeTranscriptApi.list_transcripts(video_id)
    YouTubeTranscriptApi
    list_of_languages = []
    # Listing all available transcripts
    for transcript in transcripts:
        list_of_languages.append(transcript.language_code)

    return list_of_languages

def youtube_transcript_video(video_id):
    video_id = get_video_id(video_id)
    transcripted_text = get_youtube_transcription(video_id)
    return transcripted_text