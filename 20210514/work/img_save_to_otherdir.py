import os,shutil
import cv2
for a,b,c in os.walk("c://"):
    for file in c:
        if file.endswith(".jpg"):
            try:
                    file1=os.path.join(a,file)
                    print(file)
                    newpath="999/"+file
                    print(newpath)
                    img=cv2.imread(file1)
                    cv2.imshow("bai",img)
                    if cv2.waitKey(1000)&0xFF==ord("q"):
                        shutil.copy(file1,newpath)
                        break
            except:
                print("dfdf")

