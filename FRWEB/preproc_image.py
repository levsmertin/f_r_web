import face_recognition
from matplotlib import pyplot as plt
import glob
import pickle

def get_embedding_faces_in_dir (path):
    paths = glob.glob( path +'*.jpg')
    N = len(paths)
    i = 1
    path_and_embedding = []
    for path_img in paths:
        print (str(i) +' / ' + str(N))
        image = face_recognition.load_image_file(path_img)
        embeddings = face_recognition.face_encodings(image)
        for embedding in embeddings:
            path_and_embedding.append ([path_img, embedding])
        i = i + 1
    return path_and_embedding

path_and_embedding = get_embedding_faces_in_dir ('./base/')


with open('embedings.pickle', 'wb') as f:
    pickle.dump(path_and_embedding, f)
