import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')

main_img = cv2.imread('background.jpg')
overlay_img = cv2.imread('mask_pattern.png')


results = model(main_img)


count = 0
for r in results:
    for box in r.boxes:
        if count >= 2:
            break
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        w, h = x2 - x1, y2 - y1
        resized_overlay = cv2.resize(overlay_img, (w, h))
        main_img[y1:y2, x1:x2] = resized_overlay
        count += 1

cv2.imwrite('result.jpg', main_img)
cv2.imshow('Result', main_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
