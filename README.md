# Agricorn


## Tech Stack
- PyTorch
- YOLOv5
- OpenCV
- Google Colab
- PyQT5


## Instalation
- Firstly create virtualenvironment then activate and install the dependencies

- If you don't have CUDA on your machine skip this one and install dependencies from `requirements.txt`

ROCM 5.1.1 (Linux only)
```
pip install torch==1.12.1+rocm5.1.1 torchvision==0.13.1+rocm5.1.1 torchaudio==0.12.1 --extra-index-url  https://download.pytorch.org/whl/rocm5.1.1
```
CUDA 11.6
```
pip install torch==1.12.1+cu116 torchvision==0.13.1+cu116 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu116
```
CUDA 11.3
```
pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113
```
CUDA 10.2
```
pip install torch==1.12.1+cu102 torchvision==0.13.1+cu102 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu102
```

- Install from `requirements.txt`

```
pip install -r requirements.txt
```

