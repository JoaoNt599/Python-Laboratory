from rest_framework import serializers
from .models import Cliente, TelefoneCliente, EmailCliente, Venda, Produto, Fornecedor, TelefoneFornecedor, EmailFornecedor, Compra, PedidoEstaCompra, VendaContemProduto
# from .models import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class TelefoneClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelefoneCliente
        fields = '__all__'


class EmailClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailCliente
        fields = '__all__'


class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'


class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'


class TelefoneFornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelefoneFornecedor
        fields = '__all__'


class EmailFornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailFornecedor
        fields = '__all__'


class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__'


class PedidoEstaCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoEstaCompra
        fields = '__all__'


class VendaContemProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendaContemProduto
        fields = '__all__'
