from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('history/', views.history, name="history"),
    path('chapter/', views.chapter, name="chapter"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
]
