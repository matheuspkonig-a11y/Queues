# Implementação de classe Queue em Python
O objetivo desse repositório é documentar minha abordagem para criar um algoritmo de Queues implementadas do zero em Python --- Atividade proposta pelo professor Luis Claudio Leite Pereira, na disciplina Estrutura de Dados.

O código foi desenvolvido utilizando listas nativas do Python, sem o uso de arrays ou da biblioteca 'collections.deque'

## Utilização e Métodos

A seguir estão os exemplos de como utilizar os métodos presentes na classe `Queue`.

#### Criar uma Fila

Ao instanciar a fila, você pode optar entre definir um limite máximo de elementos ou deixá-lo sem limite.
```python

# Instanciar uma fila com limite máximo de 20 elementos:
    lista_limitada = Queue(20)

# Instanciar uma fila ilimitada:
    lista_ilimitada = Queue()

```

#### Adicionar Elementos

Adiciona um novo elemento ao final da fila utilizando o método `enqueue()`. 
Se a fila estiver cheia irá disparar a excessão `OverflowError`.
```python

    lista_limitada.enqueue("nome_elemento01")
    lista_limitada.enqueue("nome_elemento02")

```

#### Remover Elementos

Remove o elemento no início da fila utilizando o método `dequeue()`.
Se a fila estiver vazia irá disparar a excessão `IndexError`.
```python

removido = lista_limitada.dequeue()

```

#### Visualizar o Primeiro Elemento

Retorna o valor do elemento que está no início da fila sem removê-lo, utilizando o método `peek()`.
Se a fila estiver vazia irá disparar a excessão `IndexError`.
```python

primeiro = lista_limitada.peek()

```

#### Verificadores de Estado

Métodos utilizados para checar o status da fila

```python

# Retorna a quantidade de elementos na lista
tamanho_atual = lista_limitada.size()

# Retorna Verdadeiro se a lista estiver vazia
estah_vazia = lista_limitada.is_empty()

# Retorna Verdadeiro se a lista estiver cheia
estah_cheia = lista_limitada.is_full()

```

#### Limpar a Fila

Remove todos os elementos da fila utilizando o método `clear()`

```python

lista_limitada.clear()

```

## Links

[Atividade no Google Classroom](https://classroom.google.com/c/ODI1MjIzMzA5OTEx/a/ODY1MTUyOTE2OTAy/details) 
