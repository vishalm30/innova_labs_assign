import cv2
import subprocess
import json


def face_detection(video):

    # Load the pre-trained face detection model
    face_cascade = cv2.CascadeClassifier('face_detector.xml')


    # Check if the video file was successfully opened
    if not video.isOpened():
        print("Error opening video file")
        exit()

    frame_count = 0

    while True:
        # Read a single frame from the video
        ret, frame = video.read()

        # Break the loop if no more frames are available
        if not ret:
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Perform face detection
        faces = face_cascade.detectMultiScale(gray,1.1, 4)

        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('Video with Face Detection', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close the windows
    video.release()
    cv2.destroyAllWindows()


def audio_detection(input_video_path):


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