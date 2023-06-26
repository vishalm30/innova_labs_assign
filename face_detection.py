# import cv2

# face_cascade = cv2.CascadeClassifier('face_detector.xml')


# img = cv2.imread('test.jpg')
# faces = face_cascade.detectMultiScale(img,1.1, 4) #this will do all the regonication part
# for(x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2) #draw rectangle on the face

# cv2.imwrite("face_detected.png", img)
# print('Photo successfully exported')


import cv2

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier('face_detector.xml')

# Open the video file
video = cv2.VideoCapture('test.gif')

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
