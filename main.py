from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
video_id = "IvOJSpcbX3A"

transcript = YouTubeTranscriptApi.get_transcript(video_id)

formatter = TextFormatter()

# .format_transcript(transcript) turns the transcript into a JSON string.
json_formatted = formatter.format_transcript(transcript)


# Now we can write it out to a file.
with open('transcript.txt', 'w', encoding='utf-8') as json_file:
    json_file.write(json_formatted)

# Now should have a new JSON file that you can easily read back into Python.