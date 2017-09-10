from django.shortcuts import render
from lab_1.views import mhs_name, birth_date

#TODO Implement
#Create a content paragraph for your landing page:
landing_page_content = 'Welcome to my website. Please excuse any sort of flaws or imperfection. I\'m still learning'

def index(request):
    response = {'name': mhs_name, 'content': landing_page_content}
    return render(request, 'index_lab2.html', response)
