from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from information import views
from information.views import register, activation_sent_view, activate, contact, studprofile, instprofile
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', register, name='register'),
    url(r'contact/', contact, name='contact'),
    path('information/activation_sent/', activation_sent_view, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
    # url(r'login/', Login, name='login'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='institute/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetView.as_view(template_name='institute/password_reset_done.html'),
         name='password_reset_done'),
    # path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='institute/password_reset_confirm.html'),name='password_reset_confirm'),
    url(r'password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',
                                                    success_url='/accounts/password_reset_complete/')),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='institute/password_reset_complete.html'),
         name='password_reset_complete'),


    url(r'stud_profile/', studprofile, name='stud_profile'),
    url(r'inst_profile/', instprofile, name='inst_profile'),
    path('update_profile/', views.update_profile, name = 'update_profile'),
    path('update_pass/', views.update_pass, name = 'update_pass'),
]