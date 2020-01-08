from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Title


def index(request):
    latest_post_list = Title.objects.order_by('-pub_date')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'posts/index.html', context)

def detail(request, post_id):
    return HttpResponse("You're looking at question %s." % post_id)

def results(request, post_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % post_id)

def like(request, post_id):
    return HttpResponse("You're voting on question %s." % post_id)