from django.conf.urls import url, include
from home import views as home_views

app_name = 'home'

urlpatterns = [
    url(r'^$', home_views.index, name='index'),
    # url(r'signup/', home_views.register, name='register'),

]