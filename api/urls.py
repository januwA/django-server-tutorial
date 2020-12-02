from django.urls import path, include
from . import views

app_name = 'api'
urlpatterns = [

  # after
  # path('', views.main, name='main'),

  # before
  path('', views.MainView.as_view(), name='main'),


  # ex: /api/5/
  path('<int:pk>/', views.DetailView.as_view(), name='detail'),
  # ex: /api/5/results/
  path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
  # ex: /api/5/vote/
  path('<int:question_id>/vote/', views.vote, name='vote'),
]