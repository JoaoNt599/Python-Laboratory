from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from django.conf import settings
from apirestful.models import (
    Cliente, TelefoneCliente, EmailCliente, Venda, Produto, Fornecedor,
    TelefoneFornecedor, EmailFornecedor, Compra, PedidoEstaCompra, VendaContemProduto
)

from apirestful.serializers import (
    ClienteSerializer, TelefoneClienteSerializer, EmailClienteSerializer,
    VendaSerializer, ProdutoSerializer, FornecedorSerializer, TelefoneFornecedorSerializer,
    EmailFornecedorSerializer, CompraSerializer, PedidoEstaCompraSerializer, VendaContemProdutoSerializer
)

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()


class ClienteView(APIView):
    def get(self, request, pk=None):
        try:
            if pk:
                cliente = session.query(Cliente).filter_by(cod_cliente=pk).first()
                if not cliente:
                    return Response({'error': 'Cliente não encontrado'}, status=status.HTTP_404_NOT_FOUND)
                serializer = ClienteSerializer(cliente)
            else:
                clientes = session.query(Cliente).all()
                serializer = ClienteSerializer(clientes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as erro:
            return Response({'error': f'Erro interno do servidor: {str(erro)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response({'error': 'Autenticação necessária'}, status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            serializer = ClienteSerializer(data=request.data)
            if serializer.is_valid():
                cliente = Cliente(**serializer.validated_data)
                session.add(cliente)
                session.commit()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
        except Exception as erro:
            return Response({'error': f'Erro interno do servidor: {str(erro)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self, request, pk):
        if not request.user.is_authenticated:
            return Response({'error': 'Autenticação necessária'}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            cliente = session.query(Cliente).filter_by(cod_cliente=pk).first()
            if not cliente:
                # Criando novo cliente
                serializer = ClienteSerializer(data=request.data)
                if serializer.is_valid():
                    cliente = Cliente(**serializer.validated_data)
                    session.add(cliente)
                    session.commit()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
            
            # Atualizando cliente existente
            serializer = ClienteSerializer(cliente, data=request.data)
            if serializer.is_valid():
                for key, value in serializer.validated_data.items():
                    setattr(cliente, key, value)
                session.commit()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
        except Exception as erro:
            return Response({'error': f'Erro interno do servidor: {str(erro)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def patch(self, request, pk):
        if not request.user.is_authenticated:
            return Response({'error': 'Autenticação necessária'}, status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            cliente = session.query(Cliente).filter_by(cod_cliente=pk).first()
            if not cliente:
                return Response({'error': 'Cliente não encontrado'}, status=status.HTTP_404_NOT_FOUND)

            serializer = ClienteSerializer(cliente, data=request.data, partial=True)
            if serializer.is_valid():
                for key, value in serializer.validated_data.items():
                    setattr(cliente, key, value)
                session.commit()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
        except Exception as erro:
            return Response({'error': f'Erro interno do servidor: {str(erro)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request, pk):
        if not request.user.is_authenticated:
            return Response({'erro': 'Autenticação necessária'}, status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            cliente = session.query(Cliente).filter_by(cod_cliente=pk).first()
            if not cliente:
                return Response({'error': 'Cliente não encontrado'}, status=status.HTTP_404_NOT_FOUND)
            session.delete(cliente)
            session.commit()
            return Response({'message': 'Cliente deletado com sucesso'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as erro:
            return Response({'error': f'Erro interno do servidor: {str(erro)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


