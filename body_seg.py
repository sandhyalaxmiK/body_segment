import scipy.misc as smi 
import numpy as np
import sys,os
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
			mask[mask!=0]=1 
			new_img=np.multiply(img,mask)
			smi.imsave(output_dirs+'/'+sub_dir+'/'+input_path,new_img)	
		except:
			print sub_dir,input_path

