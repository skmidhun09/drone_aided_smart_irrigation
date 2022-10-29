from vidstab import VidStab
import numpy as np
import cv2


def stabilize():
    stabilizer = VidStab()
    stabilizer.stabilize(input_path='Input/Thermal2.mp4', output_path='Output/Stable2.avi')


def crop():
    cap = cv2.VideoCapture('Output/Stable2.avi')
    cnt = 0
    w_frame, h_frame = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps, frames = cap.get(cv2.CAP_PROP_FPS), cap.get(cv2.CAP_PROP_FRAME_COUNT)
    xinit = int(w_frame / 10)
    yinit = int(h_frame / 10)
    x, y, h, w = xinit, yinit, h_frame - 2 * yinit, w_frame - 2 * xinit
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('Output/result2.avi', fourcc, fps, (w, h))
    while (cap.isOpened()):
        ret, frame = cap.read()
        cnt += 1
        if ret == True:
            # Croping the frame
            crop_frame = frame[y:y + h, x:x + w]
            xx = cnt * 100 / frames
            print(int(xx), '%')
            out.write(crop_frame)
            cv2.imshow('croped', crop_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()


stabilize()
crop()
