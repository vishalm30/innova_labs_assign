# import subprocess
# import json

# # Input video file path
# input_video_path = 'audio.mp4'

# # FFprobe command to get audio stream information
# ffprobe_cmd = f'C:/PATH_Programs/ffprobe -v error -select_streams a:0 -show_entries stream=channels -of json {input_video_path}'

# # Run FFprobe command and capture the output
# output = subprocess.check_output(ffprobe_cmd, shell=True)

# # Parse the JSON output
# json_data = json.loads(output.decode('utf-8'))

# # Get the count of audio channels
# channel_count = json_data['streams'][0]['channels']

# print("Number of audio channels:", channel_count)


import subprocess
import json

# Input video file path
input_video_path = 'test.gif'

# FFprobe command to get audio stream information
ffprobe_cmd = f'C:/PATH_Programs/ffprobe -v error -select_streams a:0 -show_entries stream=channels -of json {input_video_path}'


# Run FFprobe command and capture the output
output = subprocess.check_output(ffprobe_cmd, shell=True)

# Parse the JSON output
json_data = json.loads(output.decode('utf-8'))
if len(json_data['streams']) > 0:
    # Get the count of audio channels
    channel_count = json_data['streams'][0]['channels']

    print("Number of audio channels:", channel_count)

else:
    print("No audio detected")


