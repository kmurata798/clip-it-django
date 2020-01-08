from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:post_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:post_id>/likes/', views.like, name='like'),
]