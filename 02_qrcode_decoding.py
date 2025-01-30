import cv2

# Initialize QR code detector
detector = cv2.QRCodeDetector()

# Read the image
image = cv2.imread("qrcode.png")

# Detect and decode the QR code
data, points, _ = detector.detectAndDecode(image)

if data:
    print(f"QR Code Data: {data}")
    # Draw the bounding box around the QR code
    if points is not None:
        points = points.astype(int)
        cv2.polylines(image, [points], True, (0, 255, 0), 2)
    
    # Annotate the QR code data next to the bounding box
    x, y = points[0][0]  # Top-left corner of the bounding box
    cv2.putText(image, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)  # Green text

    # Save the annotated image
    output_file = "decoded_qrcode.png"
    cv2.imwrite(output_file, image)
    print(f"Annotated QR code image saved as {output_file}")
else:
    print("No QR code detected.")

# Display the image with the QR code highlighted and annotated
cv2.imshow("QR Code", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
