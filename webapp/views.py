from django.shortcuts import render
import pathlib


this_dir = pathlib.Path(__file__).resolve().parent
def home(request):
    home_html = "home.html"
    return render(request, home_html)
