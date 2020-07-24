import cv2
import dlib

# Load the detector
detector = dlib.get_frontal_face_detector()

# Load the predictor
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# read the image
img = cv2.imread(r"C:\Users\Josiah\Documents\GitHub\Describe-Me\abba.png")

# Convert image into grayscale because the detector only works with grayscale
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

# Use detector to find landmarks
faces = detector(gray)

for face in faces:
    x1 = face.left() # left point
    y1 = face.top() # top point
    x2 = face.right() # right point
    y2 = face.bottom() # bottom point

    """
    Uncomment to draw rect around faces
    # Draw a rectangle
    cv2.rectangle(img=img, pt1=(x1, y1), pt2=(x2, y2), color=(0, 255, 0), thickness=4)
    """

    # Look for the landmarks
    landmarks = predictor(image=gray, box=face)
    
    #finds the 27th point (refer to point map.png)
    x = landmarks.part(27).x
    y = landmarks.part(27).y
    
    # Draw a circle
    cv2.circle(img=img, center=(x, y), radius=5, color=(0, 255, 0), thickness=-1)

# show the image
cv2.imshow(winname="Face", mat=img)

# Wait for a key press to exit
cv2.waitKey(delay=0)

# Close all windows
cv2.destroyAllWindows()
