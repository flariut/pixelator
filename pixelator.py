import cv2
import glob
from math import log

def main():
    size = (1920, 1080)
    fps = 30
    duration = 5
    pixelator(size, fps, duration)

def pixelator(size, fps, duration):

    asp = size[0] / size[1]
    steps = duration * fps
    decr = (1/size[1]) ** (1/steps)
    
    out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps,
                          size)

    for image_path in sorted(glob.glob('sources/*.jpg')):

        src = cv2.imread(image_path)
        out.write(src)
        _res = size
        
        if src.shape[:2][::-1] == size:
            for step in range(0, steps, 1):
                
                height = int(size[1] * decr ** step)
                width = round(height * asp)
                _res = (width, height)

                # Reduce the resolution
                resized = cv2.resize(src, _res,
                                        interpolation = cv2.INTER_AREA)
                # Back to 1080 to create the video frame
                frame = cv2.resize(resized, size,
                                        interpolation = cv2.INTER_AREA)
                
                out.write(frame)
                
    out.release()

if __name__ == '__main__':
    main()
