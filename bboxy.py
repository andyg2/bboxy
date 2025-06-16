import cv2
import numpy as np

def draw_rounded_bounding_box(image, top_left, bottom_right, color, thickness=2, border_radius=10, arm_length=10):
    x1, y1 = top_left
    x2, y2 = bottom_right
    r = border_radius
    arm = arm_length

    # Sanity clamp
    r = min(r, (x2 - x1) // 2, (y2 - y1) // 2)
    arm = min(arm, (x2 - x1) // 2 - r, (y2 - y1) // 2 - r)

    # Corner Centers
    corners = {
        'tl': (x1 + r, y1 + r),
        'tr': (x2 - r, y1 + r),
        'br': (x2 - r, y2 - r),
        'bl': (x1 + r, y2 - r),
    }

    # Arcs at each corner with anti-aliasing
    cv2.ellipse(image, corners['tl'], (r, r), 180, 0, 90, color, thickness, lineType=cv2.LINE_AA)
    cv2.ellipse(image, corners['tr'], (r, r), 270, 0, 90, color, thickness, lineType=cv2.LINE_AA)
    cv2.ellipse(image, corners['br'], (r, r), 0, 0, 90, color, thickness, lineType=cv2.LINE_AA)
    cv2.ellipse(image, corners['bl'], (r, r), 90, 0, 90, color, thickness, lineType=cv2.LINE_AA)

    # Horizontal arms with anti-aliasing
    cv2.line(image, (x1 + r, y1), (x1 + r + arm, y1), color, thickness, lineType=cv2.LINE_AA)
    cv2.line(image, (x2 - r, y1), (x2 - r - arm, y1), color, thickness, lineType=cv2.LINE_AA)
    cv2.line(image, (x1 + r, y2), (x1 + r + arm, y2), color, thickness, lineType=cv2.LINE_AA)
    cv2.line(image, (x2 - r, y2), (x2 - r - arm, y2), color, thickness, lineType=cv2.LINE_AA)

    # Vertical arms with anti-aliasing
    cv2.line(image, (x1, y1 + r), (x1, y1 + r + arm), color, thickness, lineType=cv2.LINE_AA)
    cv2.line(image, (x1, y2 - r), (x1, y2 - r - arm), color, thickness, lineType=cv2.LINE_AA)
    cv2.line(image, (x2, y1 + r), (x2, y1 + r + arm), color, thickness, lineType=cv2.LINE_AA)
    cv2.line(image, (x2, y2 - r), (x2, y2 - r - arm), color, thickness, lineType=cv2.LINE_AA)

    return image

# Example Usage
if __name__ == "__main__":
    
    # Create a sample image with NumPy
    img = np.ones((300, 400, 3), dtype=np.uint8) * 255  # white background
    
    box1 = draw_rounded_bounding_box(
        img.copy(),               # Input Image
        top_left=(50, 50),        # Top Left x, y
        bottom_right=(350, 250),  # Bottom Right x, y
        color=(0, 0, 255),        # Red Box
        thickness=3,              # 3 Pixels Thick
        border_radius=20,         # 20 Pixels Radius
        arm_length=20             # 20 Pixels Arm
    )
    cv2.imwrite("example_1.png", box1)

    box2 = draw_rounded_bounding_box(
        img.copy(),
        top_left=(50, 50),
        bottom_right=(350, 250),
        color=(150, 50, 204),     # Purple
        thickness=40,              
        border_radius=10,
        arm_length=250
    )
    cv2.imwrite("example_2.png", box2)

    box3 = draw_rounded_bounding_box(
        img.copy(),
        top_left=(100, 100),
        bottom_right=(300, 200),
        color=(0, 255, 0),  # Green
        thickness=10,
        border_radius=35,
        arm_length=0
    )
    cv2.imwrite("example_3.png", box3)

    box4 = draw_rounded_bounding_box(
        img.copy(),
        top_left=(120, 60),
        bottom_right=(280, 240),
        color=(255, 0, 0),  # Blue
        thickness=4,
        border_radius=0,
        arm_length=25
    )
    cv2.imwrite("example_4.png", box4)
