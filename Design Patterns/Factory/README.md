# Factory: By GPT


## O padrão Factory é um padrão de projeto criacional que fornece uma interface para criar objetos sem expor a lógica de criação ao cliente. Ele permite que subclasses decidam qual tipo de objeto será instanciado, promovendo flexibilidade e encapsulamento.

### Principais características:

    1. Encapsulamento da criação: A lógica de criação de objetos é centralizada em um método ou classe.
    2. Flexibilidade: Permite criar objetos de diferentes tipos sem modificar o código cliente.
    3. Desacoplamento: O cliente não precisa conhecer os detalhes das classes concretas que está usando.