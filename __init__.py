from . import detector
from . import featurevectors
from . import video_functions
from . import evaluation

def detect(*args, **kwargs):
    return detector.detect(*args, **kwargs)

def construct_feature_vectors(url, feature_vectors_dir_name, feature_vector_function, framejump):
    return featurevectors.construct_feature_vectors(url, feature_vectors_dir_name, feature_vector_function, framejump)

def query_episodes_with_faiss(videos, vectors_dir):
    return detector.query_episodes_with_faiss(videos, vectors_dir)

def get_framerate(video_fn):
    return video_functions.get_framerate(video_fn)

def fill_gaps(sequence, lookahead):
    return detector.fill_gaps(sequence, lookahead)

def get_two_longest_timestamps(timestamps):
    return detector.get_two_longest_timestamps(timestamps)

def to_time_string(seconds):
    return detector.to_time_string(seconds)





