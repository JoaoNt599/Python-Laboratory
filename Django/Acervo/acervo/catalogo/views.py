from django.shortcuts import render, redirect
from .models import Livro
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


def index(request):
    """ Listagem e Pesquisa de Livros """
    query = request.GET.get('q')
    if query:
        livros = Livro.objects.filter(titulo__icontains=query)
    else:
        livros = Livro.objects.all()
    return render(request, 'catalogo/index.html', {'livros': livros})


def login_view(request):
    """ View para login """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            # next_url = request.GET.get('next', 'index')
            return render(request, 'catalogo/index.html')
        else:
            return JsonResponse({'success': False})
    return render(request, 'catalogo/login.html')


@login_required()
def admin_dashboard(request):
    user = request.user
    if user.is_authenticated and user.is_superuser:
        return render(request, 'admin_dashboard.html')
    return redirect('login')