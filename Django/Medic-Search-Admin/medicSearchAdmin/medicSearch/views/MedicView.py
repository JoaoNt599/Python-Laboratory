from django.http import HttpResponse

from django.db.models import Q

from medicSearch.models import Profile


def list_medics_view(request):
    name = request.GET.get("name")
    speciality = request.GET.get("speciality")
    neighborhood = request.GET.get("neighborhood")
    city = request.GET.get("city")
    state = request.GET.get("state")

    medics = Profile.objects.filter(role=2)

    medics = medics.filter(Q(user__first_name__contains=name) | Q(user__username__contains=name))
    
    if speciality is not None:
        medics = medics.filter(specialties__id=speciality)

    if neighborhood is not None:
        medics = medics.filter(addresses__neighborhood=neighborhood)

    else: 
        if city is not None:
            medics = medics.filter(addresses__neighborhood__city=city)
        elif state is not None:
            medics = medics.filter(addresses__neighborhood__city__state=state)

    print(medics.all())
    return HttpResponse('Listagem de 1 ou mais médicos')