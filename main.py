import torch
import cv2
from PIL import Image

model = torch.hub.load('ultralytics/yolov5', 'custom', path='Agricorn/agricorn.pt')

img = 'data/zsehat6.jpg'

result = model(img, size=640)
result.save(save_dir='result/', filename='result.png')

print(result.xyxy[0])
print(result.pandas().xyxy[0])