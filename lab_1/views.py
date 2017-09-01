from django.shortcuts import render
from datetime import date

# Enter your name here
mhs_name = 'Fari Qodri Andana' # TODO Implement this

# Create your views here.
def index(request):
    response = {'name': mhs_name, 'age' : calculate_age(1999)}
    return render(request, 'index.html', response)

# TODO Implement this to complete last checklist
def calculate_age(birth_year):
    current = date.today().year
    return current - birth_year