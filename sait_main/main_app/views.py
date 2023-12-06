from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')


# def view_input_html(request):
#     user_input = "Data from somewhere" 
#     return render(request, 'your_template.html', {'user_input': user_input})