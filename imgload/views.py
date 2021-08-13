from django.shortcuts import render, redirect
from .models import Image_model
from .forms import ImageForm, ResizeForm
from .utils import resize1, resize_by_width, resize_by_height
from django.conf import settings
from django.core.files import File
import os

def homepage_view(request):
    context = {
        'images': Image_model.objects.all(),
    }
    return render(request, 'imgload/home.html', context)


def upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ImageForm()
    return render(request, 'imgload/upload.html', {'form': form})


def resize_view(request, img_id):
    image = Image_model.objects.get(id=img_id)
    if image.img:
        name = (str(image.img)).replace('/', '\\')
    else:
        name = (image.url)
    # test = Image_model.objects.create()
    # test.img = File(open('media/images/index.jpg'), 'rb')
    # test.save()
    if request.method == 'POST':
        form = ResizeForm(request.POST)
        if form.is_valid():
            height = form.cleaned_data['height']
            width = form.cleaned_data['width']
            f = resize1(width, height, name)
            print(os.path.abspath(f))
            #Image_model.img(os.path.abspath(f), File().read())
            return redirect('home')
    else:
        form = ResizeForm()
    context = {
        'image': image,
        'form': form,
    }
    return render(request, 'imgload/resize.html', context)
