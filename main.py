from audio_face import face_detection, audio_detection

import cv2
import multiprocessing


# Open the video file
input_video_path = 'test.gif'
video = cv2.VideoCapture(input_video_path)


# face_detection(video)
# audio_detection(input_video_path)


if __name__ == '__main__':
    # Create separate processes for each function
    process1 = multiprocessing.Process(target=face_detection(video))
    process2 = multiprocessing.Process(target=audio_detection(input_video_path))

    # Start both processes
    process1.start()
    process2.start()

    # Wait for both processes to finish
    process1.join()
    process2.join()

    print("Both functions completed")