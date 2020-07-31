# USAGE
# python human_activity_reco.py --model resnet-34_kinetics.onnx --classes action_recognition_kinetics.txt --input example_activities.mp4
# python human_activity_reco.py --model resnet-34_kinetics.onnx --classes action_recognition_kinetics.txt

# import the necessary packages
import numpy as np
import imutils
import cv2

def activity_detector(path):
        # construct the argument parser and parse the arguments
        model = "resnet-34_kinetics.onnx"
        classes = "action_recognition_kinetics.txt"

        # load the contents of the class labels file, then define the sample
        # duration (i.e., # of frames for classification) and sample size
        # (i.e., the spatial dimensions of the frame)
        CLASSES = open(classes).read().strip().split("\n")
        SAMPLE_DURATION = 16
        SAMPLE_SIZE = 112

        # load the human activity recognition model
        #print("[INFO] loading human activity recognition model...")
        net = cv2.dnn.readNet(model)

        # grab a pointer to the input video stream
        #print("[INFO] accessing image file...")
        frame = cv2.imread(path)

        # initialize the batch of frames that will be passed through the
        # model
        frames = []

        # loop over the number of required sample frames
        for i in range(0, SAMPLE_DURATION):
                # otherwise, the frame was read so resize it and add it to
                # our frames list
                frame = imutils.resize(frame, width=400)
                frames.append(frame)

        # now that our frames array is filled we can construct our blob
        blob = cv2.dnn.blobFromImages(frames, 1.0,
                (SAMPLE_SIZE, SAMPLE_SIZE), (114.7748, 107.7354, 99.4750),
                swapRB=True, crop=True)
        blob = np.transpose(blob, (1, 0, 2, 3))
        blob = np.expand_dims(blob, axis=0)

        # pass the blob through the network to obtain our human activity
        # recognition predictions
        net.setInput(blob)
        outputs = net.forward()
        label = CLASSES[np.argmax(outputs)]

        """# loop over our frames
        for frame in frames:
                
        # draw the predicted activity on the frame
        cv2.rectangle(frame, (0, 0), (300, 40), (0, 0, 0), -1)
        cv2.putText(frame, label, (10, 25), cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, (255, 255, 255), 2)
        """
        return label

        """# display the frame to our screen
        cv2.imshow("Activity Recognition", frame)
        break
                
        cv2.waitKey(0)
        cv2.destroyAllWindows()"""
