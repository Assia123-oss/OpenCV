import cv2

image =  cv2.imread("assignment-001-given.jpg")

cv2.rectangle(image, (266, 195), (990, 922), (0, 255, 0), 8)

# Text properties
text, font, scale, thickness, color = 'RAH972U', cv2.FONT_HERSHEY_SIMPLEX, 3, 7, (0, 255, 0)
(x, y), (w, h) = (800, 170), cv2.getTextSize(text, font, scale, thickness)[0]

# Padding for the background rectangle
padding_x, padding_y = 4, 20

# Draw transparent background and text
overlay = image.copy()
cv2.rectangle(overlay, (x - padding_x, y - h - padding_y), (x + w + padding_x, y + padding_y), (0, 0, 0), -1)
cv2.addWeighted(overlay, 0.5, image, 0.6, 0, image)
cv2.putText(image, text, (x, y), font, scale, color, thickness)

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.imwrite('assignment-001-given-rectangle.jpg', image)
cv2.destroyAllWindows()
