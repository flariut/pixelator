import cv2
import glob

SIZE = (1920, 1080)

img_array = []

for image_path in glob.glob('sources/*.jpg'):

    src = cv2.imread(image_path)
    img_array.append(src)

    if src.shape[1] == SIZE[0] and src.shape[0] == SIZE[1]: 
        for tier in range(1, 4):
            for res in range(10, 0 if tier == 3 else 1, -1):
                width = int(SIZE[0] * res / 10 ** tier)
                height = int(SIZE[1] * res / 10 ** tier)
                dim = (width, height)
                
                # Reduce the resolution
                resized = cv2.resize(src, dim, interpolation = cv2.INTER_AREA)
                # Back to 1080 to create the video frame
                resized = cv2.resize(resized, SIZE, interpolation = 
                
                cv2.INTER_AREA)
                img_array.append(resized)


out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 2, SIZE)

for img in img_array:
    out.write(img)

out.release()
