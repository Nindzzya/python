import cv2


my_file = r'D:\stas_vasylev\!temp\2022-10-24-4d3dcde6c7df0bf57e35aaeca875bff9.mp4' 
my_folder = r'D:\stas_vasylev\!temp\!png\2022-10-24-4d3dcde6c7df0bf57e35aaeca875bff9\2022-10-24-4d3dcde6c7df0bf57e35aaeca875bff9'

haar_face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + '\haarcascade_frontalface_alt.xml')


vidcap = cv2.VideoCapture(my_file)
count = 163380
vidcap.set(cv2.CAP_PROP_POS_MSEC, count)
success,image = vidcap.read()

frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
print('frame_count =', frame_count)

while success:
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    print('count=', count)

    faces = haar_face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)
    print('Faces found:', len(faces))

    for (x, y, w, h) in faces:
        print(w, h)

        if(h >= 958):
            cv2.imwrite(my_folder + ' - %06d.png' % count, image)     # save frame as JPEG file 

    vidcap.set(cv2.CAP_PROP_POS_FRAMES, count)     
    success,image = vidcap.read()
    ('Read a new frame: ', success)

    # print("count =",count)
    count += 5 
