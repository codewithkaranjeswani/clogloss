import random
import os
import numpy as np
import cv2

import torch
from torch.utils.data import Dataset

class Nano_Dataset(Dataset):
	def __init__(self, root):

		# vcap = cv2.VideoCapture(url)
		# if not vcap.isOpened():
		# 	print("File can not be opened.")
		# 	exit(1)

		# while True:
		# 	# Capture frame-by-frame
		# 	ret, frame = vcap.read()
		# 	if ret:
		# 		# Display the resulting frame
		# 		cv2.imshow('frame',frame)
		# 		# Press q to close the video windows before it ends if you want
		# 		if cv2.waitKey(22) & 0xFF == ord('q'):
		# 			break
		# 	else:
		# 		break

		# # When everything done, release the capture
		# vcap.release()
		# cv2.destroyAllWindows()


	def __getitem__(self, index):
		pass

	def __len__(self):
		pass
		# return len(self.datalist)
