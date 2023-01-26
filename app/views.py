from django.shortcuts import render
from django.http import HttpResponse
from .models import StaffRoster, SoccerRoster, BasketballRoster, Injuries, Schedule

# Create your views here.

def main(request):
    context = {
        'schedule' : Schedule.objects.all().order_by('order'),
        'injuries' : Injuries.objects.all,
    }
    return render(request, 'app/index.html', context)

def roster(request):
    context = {
        'staff' : StaffRoster.objects.all().order_by('id'),
        'soccer' : SoccerRoster.objects.all().order_by('-position'),
        'basketball' : BasketballRoster.objects.all().order_by('-position'),
        'injuries' : Injuries.objects.all,
    }
    return render(request, 'app/roster.html', context)

def schedule(request):
    context = {
        'schedule' : Schedule.objects.all().order_by('order'),
    }
    return render(request, 'app/schedule.html', context)

def injuries(request):
    context = {
        'injuries' : Injuries.objects.all,
    }
    return render(request, 'app/injuries.html', context)

# def transactions(request):
#     context = {
#         'transactions' : Transactions.objects.all().order_by('-id'),
#     }
#     return render(request, 'app/transactions.html', context)

def about(request):
    return render(request, 'app/about.html')
