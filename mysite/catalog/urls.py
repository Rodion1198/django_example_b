from django.urls import path

from . import views


urlpatterns = [
    path('', views.HumanListView.as_view(), name='human-list'),
    path('human/create/', views.HumanCreate.as_view(), name='human-create'),
    path('human/<int:pk>/update/', views.HumanUpdate.as_view(), name='human-update'),
    path('human/<int:pk>/delete/', views.HumanDelete.as_view(), name='human-delete'),
    path('human/<int:pk>/', views.HumanDetailView.as_view(), name='human-detail'),
    path('quotes/', views.QuotesListView.as_view(), name='quot-list'),

    path('send_email/', views.test_form, name='test-form'),
    path('contact_ajax/', views.contact_form_ajax, name='contact-ajax'),

]
