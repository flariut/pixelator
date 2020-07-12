import cv2
import glob
from math import log

def main():
    size = (1920, 1080)
    fps = 30
    duration = 15
    output_path = 'project.avi'
    pixelator(size, fps, duration, output_path)

def pixelator(size, fps, duration, output_path):

    asp = size[0] / size[1]
    steps = duration * fps
    decr = (1/size[1]) ** (1/steps)
    print('##', size, fps, duration, round(asp,2), steps, round(decr,2))
    print('## Starting...')
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'DIVX'), fps,
                          size)

    for image_path in sorted(glob.glob('sources/*.jpg')):

        src = cv2.imread(image_path)
        out.write(src)
        _res = size
        
        print(f'### Pixelating {image_path}...')
        
        if src.shape[:2][::-1] == size:
            for step in range(0, steps, 1):
                
                height = int(size[1] * decr ** step)
                width = round(height * asp)
                _res = (width, height)

                # Reduce the resolution
                resized = cv2.resize(src, _res,
                                     interpolation = cv2.INTER_AREA)
                # Back to original resolution to create the video frame
                frame = cv2.resize(resized, size,
                                   interpolation = cv2.INTER_AREA)
                
                out.write(frame)
                
    out.release()

if __name__ == '__main__':
    print('# Pixelator')
    main()
