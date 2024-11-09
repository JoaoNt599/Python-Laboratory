from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse


class CriarPerfil(View):
    def get(self, *args, **kwargs):
        return HttpResponse('CriarPerfil')


class AtualizarPerfil(View):
    def get(self, *args, **kwargs):
        return HttpResponse('AtualizarPerfil')


class Login(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Login')


class Logout(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Logout')

