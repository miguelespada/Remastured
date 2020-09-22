import fastai
from deoldify.visualize import *

def get_porn_image_colorizer():
    artistic = get_artistic_image_colorizer(render_factor=35)
    porn = get_artistic_image_colorizer(weights_name = "ColorizePorn_gen", render_factor=20)
    return  (artistic, porn)

def colorize_image(colorizer, path):
    a = colorizer[0].get_transformed_image(path)
    p = colorizer[1].get_transformed_image(path)
    return Image.blend(a, p, 0.5) 