from catalog.models import Human

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic


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


class HumanListView(generic.ListView):
    model = Human
    paginate_by = 10


class HumanDetailView(generic.DetailView):
    model = Human
