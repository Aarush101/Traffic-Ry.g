import cv2
import numpy as np
from .call import Call
from .whatsapp import Whatsapp


class FireDetect:
      def __init__(self) -> None:
            vid=cv2.VideoCapture(0)

            while True:
                  ret, frame=vid.read()
                  frame=cv2.resize(frame,(1000,600))
                  blur=cv2.GaussianBlur(frame,(15,15),0)
                  hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)

                  lower_red=[161,155,84]
                  upper_red=[179,255,255]
                  lower_red=np.array(lower_red,dtype='uint8')
                  upper_red=np.array(upper_red,dtype='uint8')
                  mask_red=cv2.inRange(hsv,lower_red,upper_red)
                  outputRed=cv2.bitwise_and(frame,hsv,mask=mask_red)
                  size=cv2.countNonZero(mask_red)


                  lower_orange=[255,211,0]
                  upper_orange=[252,232,131]
                  lower_orange=np.array(lower_orange,dtype='uint8')
                  upper_orange=np.array(upper_orange,dtype='uint8')
                  mask_orange=cv2.inRange(hsv,lower_orange,upper_orange)
                  outputOrange=cv2.bitwise_and(frame,hsv,mask=mask_orange)
                  size=cv2.countNonZero(mask_orange)

                  if int(size) > 15000:
                        # print("fire detected")
                        c = Call()
                        msg = Whatsapp()

                  cv2.imshow("Output",outputRed)
                  if cv2.waitKey(1) & 0xFF==ord("q"):
                        break 
            cv2.destroyAllWindows()
            vid.release()