from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('<album_id>/', views.detail, name='detail'),
    path('', views.IndexView.as_view(), name='index'),
    path('album/add/', views.create_album, name='album_add')
]
