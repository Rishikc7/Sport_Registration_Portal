from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string

from my_app.forms import VolleyballForm, Registration
from my_app.forms import CricketForm
from my_app.forms import FootballForm
from my_app.forms import BasketballForm
from my_app.forms import HockeyForm
from my_app.forms import KabaddiForm
from my_app.models import RegistrationModel, CollegeModel, CricketModel, VolleyModel, FootballModel, BasketballModel, \
    HockeyModel, KabaddiModel, BadmintonModel, TabletennisModel
from my_app.forms import CollegeForm
from my_app.forms import BadmintonForm
from my_app.forms import TabletennisForm
from information.models import Profile
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import  send_mail

def Events(request):
    # return HttpResponse('<h1>hello guys</h1>')
    college = CollegeModel.objects.all()
    sport = RegistrationModel.objects.all()
    cricket = CricketModel.objects.all()
    volley = VolleyModel.objects.all()
    football = FootballModel.objects.all()
    basketball = BasketballModel.objects.all()
    hockey = HockeyModel.objects.all()
    kabaddi = KabaddiModel.objects.all()
    badminton = BadmintonModel.objects.all()
    tabletennis = TabletennisModel.objects.all()
    context = {
        'college': college,
        'sport': sport,
        'cricket': cricket,
        'volley': volley,
        'football': football,
        'basketball': basketball,
        'hockey': hockey,
        'kabaddi': kabaddi,
        'badminton': badminton,
        'tabletennis': tabletennis
    }
    return render(request, 'my_app/events.html', context)

def EventsRegistered(request):
    # return HttpResponse("Hiiii")
    cricket = CricketModel.objects.all()
    sport = RegistrationModel.objects.all()
    college = CollegeModel.objects.all()
    volley = VolleyModel.objects.all()
    football = FootballModel.objects.all()
    basketball = BasketballModel.objects.all()
    hockey = HockeyModel.objects.all()
    kabaddi = KabaddiModel.objects.all()
    badminton = BadmintonModel.objects.all()
    tabletennis = TabletennisModel.objects.all()
    context = {
        'cricket': cricket,
        'sport': sport,
        'college': college,
        'volley': volley,
        'football': football,
        'basketball': basketball,
        'hockey': hockey,
        'kabaddi': kabaddi,
        'badminton': badminton,
        'tabletennis': tabletennis
    }
    return render(request, 'my_app/eventRegistered.html', context)

def Volley(request,venue):
    if request.method == 'POST':
        form = VolleyballForm(data=request.POST)
        if form.is_valid():
            data = form.save()
            data.venue = venue
            data.inst = RegistrationModel.objects.get(instituteName=venue, game='volleyball')
            data.save()

            guest = User.objects.get(username = data.p1)
            subject = 'Registration done successfully'
            message = render_to_string('my_app/mails.html',{'data':data})
            receiver = guest.email
            send_mail(subject,message,settings.EMAIL_HOST_USER,[receiver ],fail_silently=False)

            return redirect('student')
        else:
            print("Form is not valid!!")
    form = VolleyballForm()
    return render(request,'my_app/volley.html',{'form':form})

def Cricket(request,venue):
    if request.method == 'POST':
        cricket = CricketForm(data=request.POST)
        print(cricket)
        if cricket.is_valid():
            data = cricket.save()
            data.venue = venue
            data.inst = RegistrationModel.objects.get(instituteName = venue , game = 'cricket')
            data.save()

            guest = User.objects.get(username=data.p1)
            subject = 'Registration done successfully'
            message = render_to_string('my_app/mails.html', {'data': data})
            receiver = guest.email
            send_mail(subject, message, settings.EMAIL_HOST_USER, [receiver], fail_silently=False)

            return redirect('student')
        else:
            print("Form is not valid!!")
    cricket = CricketForm()
    return render(request,'my_app/cricket.html',{'form':cricket})

def Football(request,venue):
    if request.method == 'POST':
        football = FootballForm(data=request.POST)
        print(football)
        if football.is_valid():
            data = football.save()
            data.venue = venue
            data.inst = RegistrationModel.objects.get(instituteName=venue, game='football')
            data.save()

            guest = User.objects.get(username=data.p1)
            subject = 'Registration done successfully'
            message = render_to_string('my_app/mails.html', {'data': data})
            receiver = guest.email
            send_mail(subject, message, settings.EMAIL_HOST_USER, [receiver], fail_silently=False)

            return redirect('student')
        else:
            print("Form is not valid!!")
    football = FootballForm()
    return render(request,'my_app/football.html',{'form':football})

def Basketball(request,venue):
    if request.method == 'POST':
        basketball = BasketballForm(data=request.POST)
        print(basketball)
        if basketball.is_valid():
            data = basketball.save()
            data.venue = venue
            data.inst = RegistrationModel.objects.get(instituteName=venue, game='basketball')
            data.save()

            guest = User.objects.get(username=data.p1)
            subject = 'Registration done successfully'
            message = render_to_string('my_app/mails.html', {'data': data})
            receiver = guest.email
            send_mail(subject, message, settings.EMAIL_HOST_USER, [receiver], fail_silently=False)

            return redirect('student')
        else:
            print("Form is not valid!!")
    basketball = BasketballForm()
    return render(request,'my_app/basketball.html',{'form':basketball})


def Hockey(request,venue):
    if request.method == 'POST':
        hockey = HockeyForm(data=request.POST)
        print(hockey)
        if hockey.is_valid():
            data = hockey.save()
            data.venue = venue
            data.inst = RegistrationModel.objects.get(instituteName=venue, game='hockey')
            data.save()

            guest = User.objects.get(username=data.p1)
            subject = 'Registration done successfully'
            message = render_to_string('my_app/mails.html', {'data': data})
            receiver = guest.email
            send_mail(subject, message, settings.EMAIL_HOST_USER, [receiver], fail_silently=False)

            return redirect('student')
        else:
            print("Form is not valid!!")
    hockey = HockeyForm()
    return render(request,'my_app/hockey.html',{'form':hockey})

def Kabaddi(request,venue):
    if request.method == 'POST':
        kabaddi = KabaddiForm(data=request.POST)
        print(kabaddi)
        if kabaddi.is_valid():
            data = kabaddi.save()
            data.venue = venue
            data.inst = RegistrationModel.objects.get(instituteName=venue, game='kabaddi')
            data.save()

            guest = User.objects.get(username=data.p1)
            subject = 'Registration done successfully'
            message = render_to_string('my_app/mails.html', {'data': data})
            receiver = guest.email
            send_mail(subject, message, settings.EMAIL_HOST_USER, [receiver], fail_silently=False)

            return redirect('student')
        else:
            print("Form is not valid!!")
    kabaddi = KabaddiForm()
    return render(request,'my_app/kabaddi.html',{'form':kabaddi})

def Register_event(request):
    if request.method == "POST":
        instance = RegistrationModel.objects.create(instituteName=request.POST['venue'].lower().strip().replace(" ","_"))
        instance.game = request.POST['game'].lower().strip().replace(" ","_")
        instance.date = request.POST['from']
        instance.teams = request.POST['teams']
        instance.fee = request.POST['fee']
        instance.oneplace = request.POST['oneplace']
        instance.twoplace = request.POST['twoplace']
        instance.fest = CollegeModel.objects.last()
        instance.save()

    return render(request, 'my_app/register.html')

def Search(request, game):
    if request.method == "POST":
        institute = request.POST['instituteName']
        game = request.POST['game']

        if institute!='':
            details = RegistrationModel.objects.filter(instituteName=institute)
            return render(request, 'my_app/search.html',{'details':details})
        elif game!='':
            details = RegistrationModel.objects.filter(game=game)
            return render(request, 'my_app/search.html',{'details':details})

    details = RegistrationModel.objects.filter(game=game)
    return render(request, 'my_app/search.html',{'details':details})

def College(request):
    if request.method == 'POST':
        college = CollegeForm(data=request.POST)
        print(college)
        if college.is_valid():
            # data = college.save()
            data = college.save(commit=False)
            data.created_by = request.user
            data.save()
            return redirect('/my_app/register_event')
        else:
            print("Form is not valid!!")
    college= CollegeForm()
    return render(request,'my_app/college.html',{'form':college})

def Student(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request,'my_app/student.html')

def Badminton(request,venue):
    if request.method == 'POST':
        print(request.POST)
        badminton = BadmintonForm(data=request.POST)
        print(badminton)
        if badminton.is_valid():
            data = badminton.save()
            data.venue = venue
            data.inst = RegistrationModel.objects.get(instituteName=venue, game='badminton')
            data.save()

            if (data.p1 == ''):
                guest = User.objects.get(username=data.p21)
            else:
                guest = User.objects.get(username=data.p1)

            subject = 'Registration done successfully'
            message = render_to_string('my_app/mails_2.html', {'data': data})
            receiver = guest.email
            send_mail(subject, message, settings.EMAIL_HOST_USER, [receiver], fail_silently=False)

            return redirect('student')
        else:
            print("Form is not valid!!")
    badminton = BadmintonForm()
    return render(request,'my_app/bad2.html',{'form':badminton})

def Tabletennis(request,venue):
    if request.method == 'POST':
        print(request.POST)
        tabletennis = TabletennisForm(data=request.POST)
        print(tabletennis)
        if tabletennis.is_valid():
            data = tabletennis.save()
            data.venue = venue
            data.inst = RegistrationModel.objects.get(instituteName=venue, game='tabletennis')
            data.save()

            if (data.p1 == ''):
                guest = User.objects.get(username=data.p21)
            else:
                guest = User.objects.get(username=data.p1)

            subject = 'Registration done successfully'
            message = render_to_string('my_app/mails_2.html', {'data': data})
            receiver = guest.email
            send_mail(subject, message, settings.EMAIL_HOST_USER, [receiver], fail_silently=False)

            return redirect('student')
        else:
            print("Form is not valid!!")
    tabletennis = TabletennisForm()
    return render(request,'my_app/bad2.html',{'form':tabletennis})


def Institute(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request,'my_app/institute.html')

def Login(request):
    print("FFF")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        print(username)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
          if user.is_active:
            login(request, user)
            print("user authenticated")
            profile = Profile.objects.get(user=user)
            if profile.group == 'institute':
                print("i am institute")
                return redirect('institute')
            elif profile.group == 'student':
                print("i am student")
                return redirect('student')
            form = login(request, user)
        else:
            messages.error(request, 'In-correct Password or Username!! Please login again.')
            return redirect('login')
    form = AuthenticationForm()
    return render(request, 'home/homepage.html', {'form': form})

def Institute_profile(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request,'my_app/institute_profile.html')

def Institutepasschange(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request,'my_app/instpasschange.html')

def Student_profile(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request,'my_app/studentprofile.html')

def Studentpasschange(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request,'my_app/studentpasschange.html')

def info(request,game, venue):
    details = CollegeModel.objects.filter(college__iexact=venue.lower())
    if request.method == "POST":
        return HttpResponseRedirect("/my_app/{}/{}/".format(game,venue))
    return render(request, 'my_app/info.html', {"details" : details, "game" : game, "venue" : venue})