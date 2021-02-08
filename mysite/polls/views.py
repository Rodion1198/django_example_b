import math

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from polls.forms import ContactFrom

from .forms import UserModelForm

from .models import Choice, Question, User   # noqa: I202


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
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


def contact_form(request):
    if request.method == "GET":
        form = ContactFrom()
    else:
        form = ContactFrom(request.POST)
        if form.is_valid():
            first_cathetus = form.cleaned_data['first_cathetus']
            second_cathetus = form.cleaned_data['second_cathetus']
            if first_cathetus and second_cathetus > 0:
                hypotenuse = math.sqrt(first_cathetus ** 2 + second_cathetus ** 2)
            else:
                raise AssertionError
            return render(request, "polls/contact.html", {'hypotenuse': hypotenuse})

    return render(request, "polls/contact.html", context={"form": form, })


def user_create(request):
    if request.method == 'POST':
        form = UserModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_create')
    else:
        form = UserModelForm()
    return render(request, 'polls/user_create.html', {'form': form})


def user_edit(request, pk=None):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserModelForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_create')
    else:
        form = UserModelForm(instance=user)
    return render(request, 'polls/user_edit.html', {'form': form,
                                                    'user': user})
