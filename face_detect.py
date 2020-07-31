import cv2

# Get user supplied values
#imagePath = sys.argv[1]
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

def detect_faces(path):
    # Read the image
    image = cv2.imread(path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    return len(faces)
"""
def find_bg(x1, y1, x2, y2, image):
    colors = {}
    colour = []
    temp = 0
    key = ""

    area = (x2-x1) * (y2-y1)
    half = area//2
    print(image.size)
    print(area)
    for i in range(x1, x2):
        for j in range(y1, y2):
            if str(image[i, j]) in colors:
                color = str(image[i, j])
                colors[color] += 1
                
                if temp < colors[color]:
                    temp = colors[color]
                    key = color
                    colour = image[i, j]
                    print(colour)
                if colors[color] == half:
                    temp = colors[color]
                    key = color
                    colour = image[i, j]
                    break         
            elif str(image[i, j]) not in colors:
                color = str(image[i, j])
                colors[color] = 1

    if temp == 0:
            for color in colors:
                if temp < colors[color]:
                    temp = colors[color]
                    key = color

    return colour

def face_colour(path):
    print("Read the image")
    image = cv2.imread(path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    print("Detect faces in the image")
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    print("Get x and y values")
    
    array = faces[0]
    print(array)
    
    x, y, w, h = array
    #cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    x1, y1, x2, y2 = x, y, x+w, y+h
    print("Find face colour")
    print(find_bg(x1, y1, x2, y2, image))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Faces found", image)
    cv2.waitKey(0)
"""

#face_colour("face.png")





