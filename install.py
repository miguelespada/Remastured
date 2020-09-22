print("Installing dependecies")

import os
#NOTE:  This must be the first call in order to work properly!
from deoldify import device
from deoldify.device_id import DeviceId
#choices:  CPU, GPU0...GPU7
device.set(device=DeviceId.GPU0)

import torch

if not torch.cuda.is_available():
  print('[ERROR] GPU not available.')
else:
  os.system("!pip install -r colab_requirements.txt")
  import fastai
  from deoldify.visualize import *
  import warnings
  warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")
  os.system("mkdir 'models'")
  os.system("wget https://www.dropbox.com/s/zkehq1uwahhbc2o/ColorizeArtistic_gen.pth?dl=0 -O ./models/ColorizeArtistic_gen.pth")
  os.system("gdown --id '1NT_A5FmdUkgh--anMWkon2VRbCG-ym3z")
  os.system("mv /content/PornModel_gen_1_0_400.pth ./models/ColorizePorn_gen.pth")