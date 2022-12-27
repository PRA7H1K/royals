from django.shortcuts import render
from django.http import HttpResponse
from .models import StaffRoster, SoccerRoster, BasketballRoster, Injuries, Transactions, Schedule

# Create your views here.

def main(request):
    return render(request, 'app/index.html')

def roster(request):
    context = {
        'staff' : StaffRoster.objects.all,
        'soccer' : SoccerRoster.objects.all,
        'basketball' : BasketballRoster.objects.all,
    }
    return render(request, 'app/roster.html', context)

def schedule(request):
    context = {
        'schedule' : Schedule.objects.all,
    }
    return render(request, 'app/schedule.html', context)

def injuries(request):
    context = {
        'injuries' : Injuries.objects.all,
    }
    return render(request, 'app/injuries.html', context)

def transactions(request):
    context = {
        'transactions' : Transactions.objects.all,
    }
    return render(request, 'app/transactions.html', context)

def about(request):
    return render(request, 'app/about.html')
