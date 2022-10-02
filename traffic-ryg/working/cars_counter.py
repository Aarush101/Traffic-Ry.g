import cv2
import numpy as np
import time as time

def traffic_density():
    #cap = cv2.VideoCapture('Road traffic video for object recognition.mp4')
    cap = cv2.VideoCapture('cars.mp4')

    length_lane=3.5     #to be detected using edge detection

    frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.CAP_PROP_FPS)

    seconds = round(frames / fps)
    fps = cap.set(cv2.CAP_PROP_FPS,1)+100

    min_contour_width=40  

    min_contour_height=40  
    offset=10   
    line_height=550  
    matches =[]
    cars=0

    def get_centroid(x, y, w, h):

        x1 = int(w / 2)
        y1 = int(h / 2)

        cx = x + x1
        cy = y + y1
        return cx,cy
        return [cx, cy] 


    cap.set(3,1920)
    cap.set(4,1080)

    if cap.isOpened():
        ret,frame1 = cap.read()
    else:
        ret = False
    ret,frame1 = cap.read()
    ret,frame2 = cap.read()

    while ret:
        d = cv2.absdiff(frame1,frame2)
        grey = cv2.cvtColor(d,cv2.COLOR_BGR2GRAY)

        blur = cv2.GaussianBlur(grey,(5,5),0)

        ret , th = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
        dilated = cv2.dilate(th,np.ones((3,3)))
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
        closing = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)
        contours,h = cv2.findContours(closing,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for(i,c) in enumerate(contours):
            (x,y,w,h) = cv2.boundingRect(c)
            contour_valid = (w >= min_contour_width) and (
                    h >= min_contour_height)

            if not contour_valid:
                continue
            cv2.rectangle(frame1,(x-10,y-10),(x+w+10,y+h+10),(255,0,0),2)

            cv2.line(frame1, (0, line_height), (1200, line_height), (0,255,0), 2)
            centroid = get_centroid(x, y, w, h)
            matches.append(centroid)
            cv2.circle(frame1,centroid, 5, (0,255,0), -1)
            cx,cy= get_centroid(x, y, w, h)
            for (x,y) in matches:
                if (line_height + offset) > y > (line_height - offset):
                    cars=cars+1
                    matches.remove((x,y))
        cv2.putText(frame1, "Total Vehicles Detected: " + str(cars), (10, 90), cv2.FONT_HERSHEY_DUPLEX, 1,
                    (0, 170, 0), 2)


        cv2.imshow("OUTPUT" , frame1)
        if (cv2.waitKey(1) == ord('q')):
            break
        frame1 = frame2
        ret , frame2 = cap.read()
        
    cv2.imwrite('new.png',frame1)
    cv2.destroyAllWindows()
    cap.release()

    den=cars/(seconds)
    return den

def traffic_light():
    start_time = time.time()
    seconds = 20
    n1,n2=1,2
    print("n1:",n1,"n2:",n2)
    
    A='R'
    B='G'

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        A_l,B_l=[],[]
        if (elapsed_time < seconds ):
            if(n1>n2):
                A='Y'
                print(A,B)
                time.sleep(3)
                B='R'
                A='G'
            elif(n1<n2):
                A='Y'
                print(A,B)
                time.sleep(3)
                B='G'
                A='R'
            A_l.append(A)
            B_l.append(B)
        else:
            break

    return A_l,B_l
        
print(traffic_density())
traffic_light()
