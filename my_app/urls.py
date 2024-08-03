from django.conf.urls import url, include
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url(r'information/(?P<game>\w+?)/(?P<venue>\w+?)/$',views.info,name="info"),
    url(r'volleyball/(?P<venue>\w+?)/$',views.Volley,name="volleyball"),
    url(r'cricket/(?P<venue>\w+?)/$',views.Cricket,name="cricket"),
    url(r'football/(?P<venue>\w+?)/$',views.Football,name="football"),
    url(r'basketball/(?P<venue>\w+?)/$',views.Basketball,name="basketball"),
    url(r'hockey/(?P<venue>\w+?)/$',views.Hockey,name="hockey"),
    url(r'kabaddi/(?P<venue>\w+?)/$',views.Kabaddi,name="kabaddi"),
    path(r'register_event/',views.Register_event,name='register_event'),
    url(r'search/(?P<game>\w+?)/$',views.Search,name='search'),
    path(r'college/',views.College,name='college'),
    path(r'student/',views.Student,name='student'),
    url(r'badminton/(?P<venue>\w+?)/$',views.Badminton,name="badminton"),
    url(r'tabletennis/(?P<venue>\w+?)/$',views.Tabletennis,name="tabletennis"),
    path(r'institute/',views.Institute,name='institute'),
    path(r'events/',views.Events,name='events'),
    path(r'eventsRegistered/',views.EventsRegistered,name='registered_events'),
    #path(r'logout/',auth_views.LogoutView.as_view(template_name='my_app/stud_logout.html'),name='student'),
    path(r'instpasschange/',views.Institutepasschange,name='instpasschange'),
    path(r'institute_profile/',views.Institute_profile,name='institute_profile'),
    path(r'studentprofile/',views.Student_profile,name='student_profile'),
    path(r'studentpasschange/',views.Studentpasschange,name='studentpasschange'),
    path(r'student/logout/',auth_views.LogoutView.as_view(template_name='my_app/stud_logout.html'),name='stud_logout'),
    path(r'institute/logout/',auth_views.LogoutView.as_view(template_name='my_app/inst_logout.html'),name='inst_logout'),

]
