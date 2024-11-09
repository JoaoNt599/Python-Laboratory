from main.models import Produto

produto = Produto.objects.filter(slug='python').first()
if produto is None:
    print("O produto com o slug 'python' não foi encontrado.")
else:
    print("Produto encontrado:", produto.nome)