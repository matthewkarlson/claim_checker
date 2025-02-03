from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from claim_extraction import extract_claims

video_id = "PmmAOWUczVw"
transcript = YouTubeTranscriptApi.get_transcript(video_id)
formatter = TextFormatter()

# .format_transcript(transcript) turns the transcript into a JSON string.
text_formatted_transcript = formatter.format_transcript(transcript)

# Now we can write it out to a file.
with open('transcript.txt', 'w', encoding='utf-8') as json_file:
    json_file.write(json_formatted)
