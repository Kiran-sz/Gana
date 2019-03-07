from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('<pk>/', views.DetailView.as_view(), name='detail'),
    path('', views.IndexView.as_view(), name='index'),
    path('album/add/', views.AlbumCreate.as_view(), name='album_add')
]
