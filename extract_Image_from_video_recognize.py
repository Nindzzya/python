import cv2
import face_recognition
from PIL import Image

my_file = r'D:\stas_vasylev\!temp\2023-11-04-fc116370b4d9de6feb44dc794c0d905e.mp4'
my_folder = r'D:\stas_vasylev\!temp\!png\2023-11-04-fc116370b4d9de6feb44dc794c0d905e\2023-11-04-fc116370b4d9de6feb44dc794c0d905e'

vidcap = cv2.VideoCapture(my_file)
count = 0 # 16500 0 4125 8250 12375
vidcap.set(cv2.CAP_PROP_POS_MSEC, count)
success,image = vidcap.read()
# print(type(image))
frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
print('frame_count =', frame_count)
# print('frame_xxx =', ((frame_count*5)/60)/60)

while success:
    face_locations = face_recognition.face_locations(image) # batch_face_locations
    # face_locations = face_recognition.batch_face_locations(image,)
    
    if(len(face_locations) > 0):
        for face_location in face_locations:
            # Print the location of each face in this image
            top, right, bottom, left = face_location

            # print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
            # You can access the actual face itself like this:
            face_image = image[top:bottom, left:right]
            pil_image = Image.fromarray(face_image)

            height_img = bottom - top
            width_img = right - left

            print('Высота', height_img)
            # print('Ширина', width_img)

            # pil_image.show()

    if(height_img >= 958):
        # while success:
        cv2.imwrite(my_folder + ' - %06d.png' % count, image)     # save frame as JPEG file 

    vidcap.set(cv2.CAP_PROP_POS_FRAMES, count)     
    success,image = vidcap.read()
    ('Read a new frame: ', success)

    print("count =",count)
    count += 5 


# import time    
# for i in progressbar(range(15), "Computing: ", 40):
#     time.sleep(0.1) # any code you need
