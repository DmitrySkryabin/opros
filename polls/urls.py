from django.urls import path, include

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('poll/<int:pk>/', views.detailview, name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('login/', include('log.urls')),
    path('admin_page/', views.adminview, name="admin_page"),
]
#path('<int:pk>/', views.DetailView.as_view(), name='detail'),
