import cv2
import numpy as np


def find_area(img, color_lower, color_upper):
    # convert to HSV space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # create a mask for the color range
    mask = cv2.inRange(hsv, color_lower, color_upper)

    # find the contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # draw a boundary box around the found area
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # create a new image for only greean area
    extracted_img = cv2.bitwise_and(img, img, mask=mask)

    return img, extracted_img


if __name__=="__main__":
    fname = 'PXL_20230324_025235345.jpg'
    green_lower = np.array([45, 100, 50])
    green_upper = np.array([75, 255, 255])

    img = cv2.imread(fname)

    img, extracted_img = find_area(img, green_lower, green_upper)
    cv2.imshow('original with boundary', img)
    cv2.imshow('extracted', extracted_img)

    # Save the new image containing only the green screen
    cv2.imwrite('extracted_img.jpg', extracted_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
