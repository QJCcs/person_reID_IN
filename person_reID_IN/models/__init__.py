from __future__ import absolute_import

from .ResNet_IN import *
from .ResNet_o import *
from .MobileNet_IN import *
from .MobileNet_o import *



__factory = {  
    'resnet50': resnet50,
    'resnet50_in': resnet50_IN,
	'mobilenet':MobileNetV2,
    'mobilenet_in': MobileNetV2_IN,
    

}

def get_names():
    return __factory.keys()

def init_model(name, *args, **kwargs):
    if name not in __factory.keys():
        raise KeyError("Unknown model: {}".format(name))
    return __factory[name](*args, **kwargs)