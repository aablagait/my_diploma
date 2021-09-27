import cv2 as cv


img = 'images/images/sign2.png'
try:
    while True:
        image = cv.imread(img)
        spisok = []

        frame_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

        frame_mask = cv.inRange(frame_hsv, (0, 162, 67), (255, 255, 255))

        frame_dilate = cv.dilate(frame_mask, None, iterations=2)

        contours, hierarchy = cv.findContours(frame_dilate.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        sort = spisok
        for i in contours:
            area = cv.contourArea(i)

            if 400 < area < 100000:  # можно регулировать дальность
                sort.append(i)

        cv.drawContours(image, sort, -1, (0, 23, 44), 2)





        cv.imshow('frame', image)

        if cv.waitKey(1) == 27:
            break


except:
    print('error')

