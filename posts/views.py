from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.template import loader

from .models import Title


def index(request):
    latest_post_list = Title.objects.order_by('-pub_date')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'posts/index.html', context)

def detail(request, post_id):
    try:
        post = Title.objects.get(pk=post_id)
    except Title.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'posts/detail.html', {'post': post})

def results(request, post_id):
    response = "You're looking at the results of post %s."
    return HttpResponse(response % post_id)

def like(request, post_id):
    post = get_object_or_404(Title, pk=post_id)
    try:
        selected_choice = post.choice_set.get(pk=request.POST['body'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))