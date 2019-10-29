from django.shortcuts import get_object_or_404, render, redirect
from .models import Data, Watson, image
from django.http import HttpResponse
from .forms import PostForm
from django.utils import timezone
from watson_developer_cloud import VisualRecognitionV3
import json
import os
import glob

import subprocess

def watsons():
    visual_recognition = VisualRecognitionV3(
        '2018-03-19',
        iam_apikey='QqxdXjczZdxurw2AYAh0KZepHq05TcOI3w9qvSxLlVV5'
    )

    files_Path = "media/"
    file_name_and_time = []

    for f_name in os.listdir(f"{files_Path}"):
        written_time = os.path.getctime(f"{files_Path}{f_name}")
        file_name_and_time.append((f"{files_Path}{f_name}", written_time))

    sorted_files = sorted(file_name_and_time, key=lambda x: x[1], reverse=True)

    recent_file = sorted_files[0]
    recent_file_name = recent_file[0]

    # media = os.path.join(os.getcwd(), 'media')
    # jpg_files = [file for file in glob.glob(os.path.join(media, '*.jpg'))]
    # jpg_files.sort(key=os.path.getmtime)

    # with open(jpg_files[-1], 'rb') as images_file:
    with open(recent_file_name, 'rb') as images_file:
        classes = visual_recognition.classify(
            images_file,
            threshold='0.6',
            classifier_ids='Chilipepper_1417755566').get_result()

    return classes, recent_file_name
  #  return json.dumps(classes, indent=2)

def index(request):
    return render(request, 'seedofr/index.html')

# 아래에 api 입력 및 로직 구현합니다.
def post_new(request):
    try:
        subprocess.call('ls -a ', shell=True) #명령어 넣기
    except OSError:
        pass
    # visual_recognition = VisualRecognitionV3(
    #     '2018-03-19',
    #     iam_apikey='QqxdXjczZdxurw2AYAh0KZepHq05TcOI3w9qvSxLlVV5'
    # )
    #
    # with open('./fruitbowl.jpg', 'rb') as images_file:
    #     classes = visual_recognition.classify(
    #         images_file,
    #         threshold='0.6',
    #         classifier_ids='Chilipepper_1417755566').get_result()
    #
    # print(json.dumps(classes, indent=2)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', seq=post.seq)
    else:
        form = PostForm()
    return render(request, 'seedofr/post_edit.html', {'form': form})

def post_detail(request, seq):
    data = get_object_or_404(Data, seq=seq)
    _watson = watsons()
    ibm = Watson()
    ibm.jsonToClass(_watson[0])
    img = image()
    img.name = _watson[1]

    return render(request, 'seedofr/post_detail.html', {'data': data,'ibm':ibm, "image" : img })

def post_compare(request):
    form = PostForm()
    return render(request, 'seedofr/post_compare.html', {'form': form})

def post_list(request):
    datas = Data.objects.filter(published_date__lte=timezone.now()).order_by('publis_date')
    return render(request, 'seedofr/post_list.html', {'datas' : datas})

# def post_list(request):
#     posts = Data.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'seedofr/post_list.html', {'posts': posts})

#
def post_edit(request, pk):
    post = get_object_or_404(Data, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'seedofr/post_edit.html', {'form': form})