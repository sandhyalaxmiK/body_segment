import scipy.misc as smi 
import numpy as np
import sys,os
import cv2
input_dirs=sys.argv[1]
mask_dirs=sys.argv[2]
output_dirs=sys.argv[3]
if not os.path.exists(output_dirs):
	os.mkdir(output_dirs)
	
for sub_dir in os.listdir(input_dirs):
	if not os.path.exists(output_dirs+'/'+sub_dir):
		os.mkdir(output_dirs+'/'+sub_dir)
	for input_path in os.listdir(input_dirs+'/'+sub_dir):
		try:
			img = smi.imread(input_dirs+'/'+sub_dir+'/'+input_path) 
			if img.shape[2]==4:
				img=img[:,:,:3]
			mask = smi.imread(mask_dirs+'/'+sub_dir+'/'+input_path[:-4]+'.png')
			mask1=np.zeros(mask.shape[:2])
			try:
				face_pts=np.where(mask==13)
				face=[[face_pts[0][i],face_pts[1][i]] for i in range(len(face_pts[0]))]
				for i in face:
					mask1[i[0]][i[1]]=255
				kernel = np.ones((5,5),np.uint8)
				face_erode = cv2.erode(mask1,kernel,iterations = 2)
				ymin=max(np.where(face_erode==255)[0])+10
			except:
				neck_pts=np.where(mask==10)
				neck=[[neck_pts[0][i],neck_pts[1][i]] for i in range(len(neck_pts[0]))]
				for i in neck:
					mask1[i[0]][i[1]]=255
				kernel = np.ones((5,5),np.uint8)
				neck_erode = cv2.erode(mask1,kernel,iterations = 3)
				ymin=min(np.where(neck_erode==255)[0])+10
			mask[mask!=0]=1 
			full_body=np.multiply(img,mask)
			without_head=full_body[ymin:,:]
			smi.imsave(output_dirs+'/'+sub_dir+'/'+input_path,without_head)	
		except:
			print sub_dir,input_path
			pass

