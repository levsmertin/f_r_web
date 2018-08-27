import face_recognition
from matplotlib import pyplot as plt
import glob
import pickle

def get_path_to_image (path_and_embedding, unknown_img_face):
    image_unknown = face_recognition.load_image_file(unknown_img_face)
    unknown_encoding = face_recognition.face_encodings(image_unknown)
    path_list=[]
    for biden_embeding in path_and_embedding:
        results = face_recognition.compare_faces(biden_embeding[1], unknown_encoding)
        if results[0] :
            path_list.append(biden_embeding[0])
    return path_list

with open('embedings.pickle', 'rb') as f:
    path_and_embedding = pickle.load(f)

def show_image (images_path_list):
    for image_path in images_path_list:
        image = face_recognition.load_image_file(image_path)
        plt.imshow(image)
        plt.title (image_path.split('/')[2])
        plt.show()

#image_input = face_recognition.load_image_file("1.bmp")
images_path_list = get_path_to_image (path_and_embedding, "Женя.jpg")
print (images_path_list)
show_image (images_path_list)
