import matplotlib.pyplot as plt 
import torch
from torchvision import datasets, transforms
import os

class Load_Dataset:

	def __init__(self, path):

		self.train_transforms = transforms.Compose([transforms.Resize(32),
													transforms.RandomRotation(30),
													transforms.RandomHorizontalFlip(),
													transforms.ToTensor(),
													transforms.Normalize([0.5, 0.5, 0.5],
																		[0.5, 0.5, 0.5])])


		self.val_test_transforms = transforms.Compose([transforms.Resize(32),
													trnsforms.ToTensor(),
													transforms.Normalize([0.5, 0.5, 0.5],
																		[0.5, 0.5, 0.5])])	

	def getLoader(self, path, step):

		if step == 'validation' or step =='test':
			transform = self.val_test_transforms
		elif step == 'train':
			transform = self.train_transforms

		data_load_path = os.path.join(path,step)
		
		data = datasets.ImageFolder(data_load_path, transform = transform)
		dataloader = torch.utils.data.DataLoader(train_data, batch_size=32)

		return dataloader