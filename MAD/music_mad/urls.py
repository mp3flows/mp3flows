from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('free_beat/', views.free_beat, name='free_beat'),
    path('download/<str:id>', views.download, name='download'),
    path('free_beat_download/<str:id>', views.free_beat_download, name='free_beat_download'),
    path('see_all/', views.see_all, name='see_all')


]
