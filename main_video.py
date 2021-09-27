import cv2 as cv


video = cv.VideoCapture('images/video/traffic.mp4')
try:
    while True:
        ret, frame = video.read()
        spisok = []

        frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        frame_mask = cv.inRange(frame_hsv, (0, 162, 67), (255, 255, 255))

        frame_dilate = cv.dilate(frame_mask, None, iterations=2)

        contours, hierarchy = cv.findContours(frame_dilate.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        sort = spisok
        for i in contours:
            area = cv.contourArea(i)

            if 400 < area < 10000:  # можно регулировать дальность
                sort.append(i)

        cv.drawContours(frame, sort, -1, (0, 23, 44), 2)





        cv.imshow('frame', frame)
        if cv.waitKey(1) == 27:
            break


except:
    print('error')

    video.release()
    cv.destroyAllWindows()