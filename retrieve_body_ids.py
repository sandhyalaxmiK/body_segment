import cv2
img=cv2.imread('/home/narendrachintala/Desktop/beard/temp_seg/img/1897890_2018_10_31_4.png',0)
img1=img.copy()

for i in range(20):
	print i
	img2=img.copy()
	img2[img==i]=255
	img2[img2<255]=0
	cv2.namedWindow('',cv2.WINDOW_NORMAL)
	cv2.imshow('',img2)
	cv2.waitKey(0)
	
