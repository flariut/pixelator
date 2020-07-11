import cv2
import glob

def main():
    SIZE = (1920, 1080)
    ASP = SIZE[0] / SIZE[1]

    img_array = []

    for image_path in sorted(glob.glob('sources/*.jpg')):

        src = cv2.imread(image_path)
        img_array.append(src)

        if src.shape[:2][::-1] == SIZE:
            for tier in range(1, 4):
                for step in range(9, 0, -1):

                    height = round(SIZE[1] * step / 10 ** tier)
                    width = round(height * ASP)
                    dim = (width, height)
                    
                    # Reduce the resolution
                    resized = cv2.resize(src, dim,
                                         interpolation = cv2.INTER_AREA)
                    # Back to 1080 to create the video frame
                    frame = cv2.resize(resized, SIZE,
                                         interpolation = cv2.INTER_AREA)
                    
                    img_array.append(frame)
            
            # Last single "pixel" frame
            resized = cv2.resize(src, (1,1),
                                 interpolation = cv2.INTER_AREA)
            frame = cv2.resize(resized, SIZE,
                               interpolation = cv2.INTER_AREA)
            img_array.append(frame)

    out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 2,
                          SIZE)

    for img in img_array:
        out.write(img)

    out.release()

if __name__ == '__main__':
    main()
