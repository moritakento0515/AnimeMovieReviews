from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
     path('',views.IndexView.as_view(),name='index'),
     path('movie/<int:pk>/',views.MovieDetailView.as_view(),name='movie_detail'), #viewsディレクトリ｜のMoviewDetailView｜を関数として使う
     path('register/director/', views.RegisterDirectorView.as_view(), name='registerdirector'), 
     path('register/movie/', views.RegisterMovieView.as_view(), name='registermovie'), 
     path('writing/log/', views.WritingLogView.as_view(), name='writinglog'),
     path('edit/<int:pk>/',views.EditMovieView.as_view(),name='editmovie'),
     path('update/log/<int:pk>/',views.UpdateLogView.as_view(), name='updatelog'),
     path('delete/movie/<int:pk>/',views.DeleteMovieView.as_view(), name='deletemovie'),
]
