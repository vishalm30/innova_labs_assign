from audio_face import face_detection, audio_detection

import cv2
import multiprocessing


# Open the video file
input_video_path = 'test.gif'
video = cv2.VideoCapture(input_video_path)


face_detection(video)
audio_detection(input_video_path)