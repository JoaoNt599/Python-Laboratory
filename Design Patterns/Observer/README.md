# Observer: By GPT


### O padrão Observer é um padrão de design comportamental que estabelece uma relação de dependência "um-para-muitos" entre objetos. Quando o estado de um objeto (o sujeito) muda, todos os seus observadores (ou assinantes) são automaticamente notificados e atualizados.


## Como funciona:

1. Sujeito (Subject): O objeto principal que mantém uma lista de observadores e notifica-os sobre mudanças de estado.
2. Observadores (Observers): Objetos que "observam" o sujeito e reagem a suas mudanças.


## Vantagens:

1. Desacoplamento: O sujeito não precisa conhecer os detalhes dos observadores.
2. Escalabilidade: Fácil adicionar ou remover observadores sem alterar o código do sujeito.