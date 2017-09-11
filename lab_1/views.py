from django.shortcuts import render
from datetime import datetime, date
# Enter your name here
mhs_name = 'Fari Qodri Andana' # TODO Implement this
curr_year = int(datetime.now().strftime("%Y"))
birth_date = date(1999, 9, 21) #TODO Implement this, format (Year, Month, Date)
# Create your views here.
def index(request):
    response = {'name': mhs_name, 'age': calculate_age(birth_date.year)}
    return render(request, 'index_lab1.html', response)
