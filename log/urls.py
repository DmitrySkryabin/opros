from django.urls import path, include

from . import views

app_name = 'login'
urlpatterns = [
    path('', views.login, name='index'),
    path('logout/', views.logout, name='index'),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
