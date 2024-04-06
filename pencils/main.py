import cv2
from scipy.spatial import distance #библиотека для вычисления евликового расстояния

count = 0

for i in range(1, 13):
    pencils = cv2.imread(f"images/img ({i}).jpg")
    image = cv2.cvtColor(pencils, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(image, 120, 255, 0)
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    pencil_number = 0

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt) #координаты для контура.
        points = cv2.boxPoints(cv2.minAreaRect(cnt)) #углы
        w_euc = distance.euclidean(points[0], points[1]) #длина одной стороны  прямоугольника
        h_euc = distance.euclidean(points[0], points[3]) #длина другой стороны прямоугольника
        if (h_euc > 3 * w_euc and h_euc > 1000) or (w_euc > 3 * h_euc and w_euc > 1000): #условие, при котором это карандаш
            pencil_number += 1
            count += 1

    print(f"Количество карандашей на изображении {i} изображении:{pencil_number}")

    #cv2.imshow(f"Image {i}", image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

print("Общее количество карандашей:", count)
