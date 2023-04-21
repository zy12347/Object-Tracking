import cv2
import os


def main():
    dir = "./image/processed/"
    filenames = os.listdir(dir)
    for name in filenames:
        path = os.path.join(dir, name)
        img = cv2.imread(path)
        cv2.imshow("frame",img)
        if cv2.waitKey(1)& 0xFF==ord("q"):
            break
    
    cv2.destroyAllWindows()
    
if __name__=="__main__":
    main()