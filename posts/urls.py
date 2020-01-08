from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:post_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:post_id>/like/', views.like, name='like'),
]