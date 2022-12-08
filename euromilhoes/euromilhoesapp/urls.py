from django.urls import path
from . import views

app_name = 'euromilhoesapp'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('statistics/', views.stats_view, name='statistics'),
    path('contacts/', views.contact_view, name='contacts'),
    # path('main/', views.main, name='main'),
    # path('user_info/', views.user_info, name='user_info'),

]