import cv2
from engine.Video_proccesor.get_frames import get_frames

def convert_video(VFILE):

    fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', 'V')
    VFILE = VFILE + "Convert"
    video_out = cv2.VideoWriter(VFILE, fourcc, 20, (640,480))

    if video_out:
        
            counter = 0
            for frame in get_frames(VFILE):
                if frame is None:
                    break
                cv2.putText(frame, 
                            text=str(counter),
                            org=(100,100),
                            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                            fontScale=1,
                            color=(0,255,0),
                            thickness=3)
                video_out.write(frame)    
                counter += 1
            video_out.release()
            
    else:
        return "fail"
