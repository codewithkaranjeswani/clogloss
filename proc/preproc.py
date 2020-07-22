import pandas as pd
import numpy as np
import cv2
import requests
from requests.exceptions import MissingSchema
import tarfile
import os
from tqdm import tqdm

def download_from_url(url, dst):
	try:
		r = requests.get(url, stream=True)
	except requests.exceptions.MissingSchema:
		print(f"requests.exceptions.MissingSchema, maybe Invalid URL {url}.")
		return -1

	if r.status_code != 200:
		print("No response from URL, maybe. r = {}".format(r))
		return -1
	file_size = int(requests.head(url).headers["Content-Length"])
	
	if os.path.exists(dst):
		first_byte = os.path.getsize(dst)
	else:
		first_byte = 0
	if first_byte >= file_size:
		return file_size
	header = {"Range": "bytes=%s-%s" % (first_byte, file_size)}
	pbar = tqdm(total=file_size, initial=first_byte,
		unit='B', unit_scale=True) # , desc=url.split('/')[-1])
	req = requests.get(url, headers=header, stream=True)
	with(open(dst, 'ab')) as f:
		for chunk in req.iter_content(chunk_size=1024):
			if chunk:
				f.write(chunk)
				pbar.update(1024)
	pbar.close()
	return file_size

train = pd.read_csv("metadata/train_metadata.csv", sep=",")
# print(train.head())
# print(len(train))

trainlabels = pd.read_csv("metadata/train_labels.csv", sep=",");
# print(len(trainlabels)) # 573048

assert len(train) == len(trainlabels), "lengths of trainlabels.csv and train_metadata.csv differ"

nanotrain = train.loc[train['nano'] == True]
# print(len(nanotrain)) # 1413

nanotrainlabels = trainlabels.loc[train['nano'] == True]
# print(len(nanotrainlabels) == len(nanotrain))

url = 'https://s3.amazonaws.com/drivendata-public-assets/nano_vessels.tar'
os.makedirs('../input/', exist_ok=True)
target_path = '../input/nano_vessels.tar'

fs = download_from_url(url, target_path)

# Untar file
mytar = tarfile.open(target_path)
mytar.extractall(target_path)
mytar.close()

# how to read video like Videoreader in matlab

# load pretrained googlenet from pytorch to extract embeddings (ROIDetector)

# make BiLSTM model and add Fully Connected layer and classification layer

# Make prediction by training and enjoy!

# Test too!

