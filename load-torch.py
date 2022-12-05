import torch

model = torch.hub.load('ultralytics/yolov5', 'custom', path='model/best-5.pt')
x = 0

while x <= 9:
    x += 1
    file = f'data/data-for-test/h{x}.jpg'
    result = model(file)
    result.save(save_dir='data/test-result')
print('Done')