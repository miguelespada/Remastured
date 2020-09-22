import os
os.system("mkdir 'models'")
os.system("wget https://www.dropbox.com/s/zkehq1uwahhbc2o/ColorizeArtistic_gen.pth?dl=0 -O ./models/ColorizeArtistic_gen.pth")
os.system("gdown --id '1GwKMXS1B6kFHmr1e3ArTzZClXx_hv2tm'")
os.system("mv PornArtisticModel2_gen_6.pth ./models/ColorizePorn_gen.pth")