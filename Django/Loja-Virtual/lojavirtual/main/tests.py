from django.test import TestCase
from django.urls import reverse
from django.core import mail
from main import forms



class TestarPaginas(TestCase):
    def testar_se_pagina_pricipal_carrega_completamente(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertContains(response, 'Loja Virtual')
    

    def testar_se_pagina_ajuda_carrega_completamente(self):
        response = self.client.get(reverse("ajuda"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertContains(response, '<h2>Ajuda</h2>')


class TestarForms(TestCase):
    def testar_formulario_fale_conosco_corretamente_preechido(self):
        formulario = forms.FormFaleConosco(
            {
                'nome': 'João Vieira',
                'email_origem': 'joao@teste.com',
                'mensagem': 'Testando nova funcionalidade'
            }
        )
        self.assertTrue(formulario.is_valid())
        formulario.enviar_mensagem_por_email()
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'FALE CONOSCO: Mensagem recebida.')

    
    def testar_formulario_fale_conosco_invalido(self):
        formulario = forms.FormFaleConosco(
            {
                'mensagem': 'Testando nova funcionalidade'
            }
        )
        self.assertFalse(formulario.is_valid())