from django.urls import path
from django.views.decorators.cache import cache_page

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('triangle', views.contact_form, name="contact"),
    path('send_email', views.test_form, name='test-form'),
    path('quotes/', cache_page(5)(views.QuotesListView.as_view()), name='quot-list'),
]
