from catalog.models import Human

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.cache import cache_page

from .forms import ContactForm, TestForm
from .models import Quot
from .tasks import send_mail as celery_send_mail


def index(request):
    return HttpResponse("First page")


class HumanCreate(LoginRequiredMixin, generic.CreateView):
    model = Human
    fields = ['first_name', 'last_name', 'mobile', 'interests']
    login_url = '/login/'
    template_name = 'catalog/human_form.html'
    success_url = reverse_lazy('human-create')
    redirect_field_name = 'admin'


class HumanUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Human
    fields = ['first_name', 'last_name', 'mobile', 'interests']
    login_url = '/login/'
    template_name = 'catalog/human_update_form.html'
    success_url = reverse_lazy('human-list')
    redirect_field_name = 'admin'


class HumanDelete(LoginRequiredMixin, generic.DeleteView):
    fields = ['first_name', 'last_name', 'mobile', 'interests']
    login_url = '/login/'
    success_url = reverse_lazy('human-list')
    redirect_field_name = 'admin'
    queryset = Human.objects


@method_decorator(cache_page(5), name='dispatch')
class HumanListView(generic.ListView):
    model = Human
    paginate_by = 10


@method_decorator(cache_page(5), name='dispatch')
class HumanDetailView(generic.DetailView):
    model = Human


@method_decorator(cache_page(5), name='dispatch')
class QuotesListView(generic.ListView):
    model = Quot
    paginate_by = 100

    queryset = Quot.objects.select_related('author').all()


def test_form(request):
    if request.method == "GET":
        form = TestForm()
    else:
        form = TestForm(request.POST)
        if form.is_valid():
            subject = 'Напоминание'
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            time_to_send = form.cleaned_data['time_to_send']
            celery_send_mail.apply_async((subject, message, from_email), eta=time_to_send)
            return redirect('catalog:test-form')
    return render(request, "catalog/testform.html", context={"form": form})


def contact_form_ajax(request):
    data = dict()
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            celery_send_mail.delay(subject, message, from_email)
            messages.add_message(request, messages.SUCCESS, 'Message sent')
            return redirect('human-list')
        else:
            data['form_is_valid'] = False
    data['html_form'] = render_to_string(
        template_name='include/contact_ajax.html',
        context={'form': form},
        request=request
    )
    return JsonResponse(data)
