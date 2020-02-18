import numpy as numpy
import cv2
import os

# configs
output_dir = 'output'
input_dir = 'video'
frame_skip = 30

def main():
    video_files = os.listdir(input_dir)

    for file in video_files:
        cap = cv2.VideoCapture(input_dir+"/"+file)
        video_file_name = file
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        print('Processing file:'+ video_files[0])
        print('Frame count: ', frame_count)
        
        # index
        i = 0
        while(cap.isOpened()):
            # skip frames
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_skip*i)
            # read next frame
            ret, frame = cap.read()

            if ret == False:
                break

            # write frame
            cv2.imwrite(output_dir+"/"+video_file_name+"_"+str(i)+".jpg", frame)
            
            # step
            i+=1
            
        # cleanup    
        cap.release()
        cv2.destroyAllWindows()

def writeFrame(frame):
    pass

if __name__ == "__main__":
    main()