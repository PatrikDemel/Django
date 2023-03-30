from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, 'birthday/index.html', {
        "birthdayDate": now.month == 11 and now.day == 7,
        "currentDate": now.strftime("%d.%m.%Y")
    },)
