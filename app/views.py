from django.shortcuts import render
from django.http import HttpResponse
from .models import StaffRoster, SoccerRoster, BasketballRoster, Injuries, Schedule, Player

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
    for scorer in Schedule.objects.values_list('highest_goal_scorer'):
        name = scorer
        names = name[0]
    context = {
        'schedule' : Schedule.objects.all().order_by('order'),
    }
    return render(request, 'app/schedule.html', context)

def injuries(request):
    context = {
        'injuries' : Injuries.objects.all,
    }
    return render(request, 'app/injuries.html', context)

def player(request):
    name = request.GET.get('name', 'None')

    name = Player.objects.filter(name__icontains = name)

    try:
        photo = Player.objects.filter(name__icontains = name[0]).values_list('photo', flat=True)
        bio = Player.objects.filter(name__icontains = name[0]).values_list('bio', flat=True)
        weight = Player.objects.filter(name__icontains = name[0]).values_list('weight', flat=True)
        height = Player.objects.filter(name__icontains = name[0]).values_list('height', flat=True)
        birthdate = Player.objects.filter(name__icontains = name[0]).values_list('birthdate', flat=True)
        signed = Player.objects.filter(name__icontains = name[0]).values_list('signed', flat=True)
    except (IndexError, UnboundLocalError):
            name = ""
            photo = ""
            bio = ""
            weight = ""
            height = ""
            birthdate = ""
            signed = ""

    try:
        get_staff_position = StaffRoster.objects.filter(name__icontains = name[0]).values_list('position', flat=True)
    except IndexError:
        staff_position = ""
    try:
        get_soccer_position = SoccerRoster.objects.filter(name__icontains = name[0]).values_list('position', flat=True)
        goals = SoccerRoster.objects.filter(name__icontains = name[0]).values_list('goals', flat=True)
        goals = goals[0]
    except IndexError:
        staff_position = ""
        goals = ""
    try:
        get_basketball_position = BasketballRoster.objects.filter(name__icontains = name[0]).values_list('position', flat=True)
        points = BasketballRoster.objects.filter(name__icontains = name[0]).values_list('points', flat=True)
        points = points[0]
        cft = BasketballRoster.objects.filter(name__icontains = name[0]).values_list('completed_ft', flat=True)
        cft = cft[0]
        aft = BasketballRoster.objects.filter(name__icontains = name[0]).values_list('attempted_ft', flat=True)
        aft = aft[0]
        ftp = BasketballRoster.objects.filter(name__icontains = name[0]).values_list('ft_percent', flat=True)
        ftp = ftp[0]
    except IndexError:
        staff_position = ""
        points = ""
        cft = ""
        aft = ""
        ftp = ""

    try:
        staff_position = get_staff_position[0]
    except (IndexError, UnboundLocalError):
        staff_position = ""
    try:
        soccer_position = get_soccer_position[0]
    except (IndexError, UnboundLocalError):
        soccer_position = ""
    try:
        basketball_position = get_basketball_position[0]
    except (IndexError, UnboundLocalError):
        basketball_position = ""

    try:
        status = Injuries.objects.filter(name__icontains = name[0]).values_list('status', flat=True)
        reason = Injuries.objects.filter(name__icontains = name[0]).values_list('reason', flat=True)
        if status[0] != "":
            status = status[0]
        if reason[0] != "":
            reason = reason[0]
    except (IndexError, UnboundLocalError):
        status = ""
        reason = ""

    try:
        name = name[0]
        photo = photo[0]
        bio = bio[0]
        weight = weight[0]
        height = height[0]
        birthdate = birthdate[0]
        signed = signed[0]
    except (IndexError, UnboundLocalError):
        name = ""
        photo = ""
        bio = ""
        weight = ""
        height = ""
        birthdate = ""
        signed = ""

    context = {
        'player' : name,
        'photo' : photo,
        'bio' : bio,
        'weight' : weight,
        'height' : height,
        'birthdate' : birthdate,
        'signed' : signed,
        'staff_position' : staff_position,
        'soccer_position' : soccer_position,
        'basketball_position' : basketball_position,
        'goals' : goals,
        'points' : points,
        'cft' : cft,
        'aft' : aft,
        'ftp' : ftp,
        'status' : status,
        'reason' : reason,
    }

    return render(request, 'app/player.html', context)

# def transactions(request):
#     context = {
#         'transactions' : Transactions.objects.all().order_by('-id'),
#     }
#     return render(request, 'app/transactions.html', context)

def about(request):
    return render(request, 'app/about.html')
