import cv2

def face_detect():
    cam = cv2.VideoCapture(0) # to open web cam

    face_clf = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

    while True:
        ret, frame = cam.read()

        if ret == False:
            continue;

        # gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_clf.detectMultiScale(frame, 1.3, 5) #image, scale, neighnours

        for x,y,w,h in faces:
        	cv2.putText(frame, "Person", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
        	cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow("faces", frame)
        # cv2.imshow("gray_faces", gray_frame)

        key = cv2.waitKey(1) & 0xff

        if key == ord('q'):
        	cam.release()
        	break

if __name__ == '__main__':
    face_detect()
    cv2.destroyAllWindows()