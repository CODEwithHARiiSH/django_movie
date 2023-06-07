from django.conf.urls.static import static

from . import views
from movieproject import settings
from django.conf.urls.static import static
from django.urls import path
app_name='movie'
urlpatterns = [


    path('', views.home, name='home'),
    path('movie/<int:movie_id>/', views.detail, name='detail'),
    path('add/', views.add_movie,name='add_movie'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]

