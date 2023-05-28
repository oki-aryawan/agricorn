import torch

model = torch.hub.load('ultralytics/yolov5', 'custom', path='model/yuvicho.pt')
file = f'data/data-for-test/bawang.jpg'
result = model(file)
result.print()
result.save()
print(result.xyxy[0])  # im1 predictions (tensor)
print(result.pandas().xyxy[0])