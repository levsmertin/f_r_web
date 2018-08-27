from django.shortcuts import render
from FRW.models import PhotoBase
from FRW.forms import PhotoBaseForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

import face_recognition
import glob
import pickle

def get_path_to_image (path_and_embedding, unknown_img_face):
    image_unknown = face_recognition.load_image_file(unknown_img_face)
    unknown_encoding = face_recognition.face_encodings(image_unknown)
    path_list=[]
    for biden_embeding in path_and_embedding:
        results = face_recognition.compare_faces(biden_embeding[1], unknown_encoding)
        if results[0] :
            path_list.append('/media/'+biden_embeding[0][2:])
    return path_list



def main_page(request):
    return render(request, 'FRW/main_page.html', {})

def add_photo(request):
    form = PhotoBaseForm()
    images_path_list = []
    if request.method == 'POST':
        form = PhotoBaseForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            print(request.FILES)
            if 'photo' in request.FILES:
                form.photo = request.FILES['photo']
            form.save(commit=True)
            with open('embedings.pickle', 'rb') as f:
                path_and_embedding = pickle.load(f)
            print(request.FILES['photo'])
            images_path_list = get_path_to_image (path_and_embedding, 'media/Photos1/' + str(request.FILES['photo']))
            print (images_path_list)
        else:
            print(form.errors)
    return render(request, 'FRW/main_page.html', locals())
