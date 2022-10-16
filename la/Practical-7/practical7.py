# Practical 7 : Title: Rotate & crop
# Q1 Write a python program to rotate a image by 45, 90, 18
# Q2 Write a python program to crop a picture.

def Rotate(IM_1,t):
    from PIL import Image
    a1=Image.open(IM_1)
    a1.show()
    rot_a1=a1.rotate(t)
    rot_a1=a1.show()
    rot.a1.save('F:/22SCS021/Linear-Algebra/Practical-7/rot_FACE_1.jpg')

def Crop(IM_1,cords):
    from PIL import Image
    a1=Image.open(IM_1)
    a1.show()
    croped=a1.crop(cords)
    croped.show()
    croped.save('F:/22SCS021/Linear-Algebra/Practical-7/crop_FACE_1.jpg')
    

