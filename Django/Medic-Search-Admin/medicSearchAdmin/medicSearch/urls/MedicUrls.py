from django.urls import path
from medicSearch.views.MedicView import list_medics_view


urlpatterns = [
    path("", list_medics_view, name='medics'),
]