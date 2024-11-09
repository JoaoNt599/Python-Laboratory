from django.http import HttpResponse


def list_profile_view(request, id=None):
    if id is None and request.user.is_authenticated:
      id = request.user.id
    elif not request.user.is_authenticated:
       id = 0

    return HttpResponse('<h1>Usuário de id %s!</h1>' % id)