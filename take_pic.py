import cv2
import os
import time
import uuid

# Set the path where the images will be stored
IMAGES_PATH = 'Tensorflow/workspace/images'

# Define the labels for the images you want to collect
labels = ['hello', 'thanks', 'yes', 'no', 'iloveyou']

# Number of images to collect for each label
number_img = 15

# Loop through each label to collect images
for label in labels:
    # Create a new directory for the current label if it doesn't exist
    new_dir_path = os.path.join(IMAGES_PATH, label)
    if not os.path.exists(new_dir_path):
        os.makedirs(new_dir_path)
        print(f"Directory '{new_dir_path}' created successfully.")
    else:
        print(f"Directory '{new_dir_path}' already exists.")
    
    # Start video capture. Change '1' to '0' for the default camera if needed
    cap = cv2.VideoCapture(1)
    print(f'Collecting images for {label}')
    
    # Wait for 5 seconds before starting to capture to adjust the camera or pose
    time.sleep(5)
    
    # Capture and save the specified number of images
    for imgnum in range(number_img):
        ret, frame = cap.read()
        if ret:
            imagename = os.path.join(new_dir_path, f'{label}.{uuid.uuid1()}.jpg')
            cv2.imwrite(imagename, frame)
            cv2.imshow('frame', frame)
            
            # Wait for 2 seconds before capturing the next image
            time.sleep(2)
            
            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Release the camera
    cap.release()

# Make sure all windows are closed
cv2.destroyAllWindows()
