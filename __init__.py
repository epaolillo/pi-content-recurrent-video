from . import detector, 
from . import featurevectors
from . import video_functions
from . import evaluation

def detect(*args, **kwargs):
    return detector.detect(*args, **kwargs)

def construct_feature_vectors(url, feature_vectors_dir_name, feature_vector_function, framejump):
    return featurevectors.construct_feature_vectors(url, feature_vectors_dir_name, feature_vector_function, framejump)