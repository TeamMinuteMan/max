# prac 06 Title:- Resize and Merge
# Q1 Write a python program to resize a picture.
# Q2 Write a python program to merge two pictures.

def RESIZE(IM_1,m,n):
    from PIL import Image
    a1 =Image.open(IM_1)
    a1.show()
    new_a1= a1.resize((m,n))
    new_a1.save('D:/Practicals/Linear-Algebra/Practical-6/RE_FACE_1.PNG')
    new_a1.show()

def MERGE(IM_1,IM_2,a,b):
    from PIL import Image
    import numpy as np
    a1 =Image.open(IM_1)
    a2 =Image.open(IM_2)
    a1.show()
    a2.show()
    new_a1= a1.resize((300, 300))
    new_a2= a2.resize((300, 300))
    new_a1.save('D:/Practicals/Linear-Algebra/Practical-6/ME_FACE_2.jpg')
    new_a2.save('D:/Practicals/Linear-Algebra/Practical-6/ME_FACE_3.jpg')
    p=np.array(new_a1)+np.array(new_a2)
    a=Image.fromarray(p)
    a.save('D:/Practicals/Linear-Algebra/Practical-6/ME_FACE.jpg')
    a.show()
    print(np.array(a))

#RESIZE('D:/Practicals/Linear-Algebra/Practical-6/face1.jpg',100,100)

MERGE('D:/Practicals/Linear-Algebra/Practical-6/face1.jpg','D:/Practicals/Linear-Algebra/Practical-6/face2.jpg',300,300)
