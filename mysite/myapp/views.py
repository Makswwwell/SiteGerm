from django.shortcuts import render
from .models import Blog, Section, PartyService, DishGallery, Impressum
from docx import Document
from django.conf import settings
import os


# Create your views here.

def home(request):
    return render(request, "html_temp/index.html")


def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'html_temp/blog.html', {'blogs': blogs})


def menu(request):
    sections = Section.objects.all()
    return render(request, 'html_temp/menu.html', {'sections': sections})


def party_service_list(request):
    party_services = PartyService.objects.all()
    return render(request, 'html_temp/party_service_list.html', {'party_services': party_services})


def dish_gallery(request):
    dishes = DishGallery.objects.all()
    return render(request, 'html_temp/dish_gallery.html', {'dishes': dishes})


def impressum_view(request):
    data = Impressum.objects.all()
    return render(request, 'html_temp/Impressum.html', {'data': data})


def privacy_policy_view(request):
    # Путь к вашему Word-документу
    docx_path = os.path.join('static', 'src', 'Datenschutzerklärung.docx')

    # Чтение содержимого Word-документа
    doc = Document(docx_path)
    content = []

    for paragraph in doc.paragraphs:
        content.append(paragraph.text)

    return render(request, 'html_temp/privacy_policy.html', {'content': content})
