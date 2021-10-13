import cv2
import os, sys

# haar cascading folder path
haarcascade = "/Users/USER10/AppData/Local/Programs/Python/Python39/Lib/site-packages/cv2/data/"
# face recognition file
face = f"{haarcascade}haarcascade_frontalface_default.xml"

# image file path - terminal
img_path = sys.argv[1]


def face_detector(img_path):
  """face detector program"""

  if os.path.exists(face):
    
    # classifier
    face_cascade = cv2.CascadeClassifier(face)

    
    img = cv2.imread(img_path)

    faces = face_cascade.detectMultiScale(
      img,
      scaleFactor=1.3,
      minNeighbors=5,
      flags=cv2.CASCADE_SCALE_IMAGE
    )

    for (x, y, w, h) in faces:
      cv2.rectangle(
        img=img,
        pt1=(x, y),
        pt2=(x+w, y+h),
        color=(0, 255, 255),
        thickness=2
      )
    cv2.imshow("Faces Detector", img)
    cv2.waitKey(0)

    return "Found {0} faces!".format(len(faces))


  else:
    print("File not found")


if __name__ == "__main__":
  print(face_detector(img_path=img_path))