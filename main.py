import torch

model = torch.hub.load('ultralytics/yolov5', 'custom', path='model/agricorn.pt')

img = 'data/zsehat6.jpg'

result = model(img)

print(result.pandas().xyxy[0])