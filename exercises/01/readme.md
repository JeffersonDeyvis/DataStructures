## Instruções

Pilhonaldo é um empacotador muito suspeito. Durante o dia trabalha em um armazém, empilhando caixas da shopee, mas sonha
em ser professor de matemática no ensino fundamental.

Para isso, ele teve um ideia de atividade enquanto empilhava as caixas. Pilhonaldo percebeu que poderia trabalhar com
seus alunos a subtração e a paridade de números com um jogo.

Cada rodada do jogo consiste em empilhar as caixas uma em cima da outra, na ordem em que vierem. Mas existe uma
complicação: cada vez que uma caixa é empilhada em cima de uma que tem número com paridade igual (ambas ímpares ou ambas
pares), as duas são substituídas por uma única caixa com número igual à diferença (em absoluto) entre as duas.

Exemplo:

Dada uma pilha em que foram empilhadas caixas com 3,2 e 1 pacotes, nessa ordem (sendo 1 o topo):

````Bash
1
2
3
````

Ao adicionar uma caixa com 7 pacotes em cima de uma de número 1, a operação de subtração deve ser realizada:

````Bash
7
1    6
2 -> 2 -> 4
3    3    3
````

**Observações:**

- Note que, no caso de ter sido adicionada uma caixa de número 1 em cima de uma de número 7, ambas as caixas também
  seria substituídas por uma caixa contendo <span style="color:red;">|7-1| = 6</span> pacotes. Assim, a subtração é dada em absoluto, não importando a
  ordem das caixas.
- A operação de subtração é sucessiva, e continuará acontecendo entre a caixa no topo e a caixa imediatamente adjacente
  ao topo até que a paridade delas seja diferente, como pode ser visto no exemplo.

## Input Specification

Inicialmente, uma linha contendo um número <span style="color:red;">t</span> de casos é dada:

````Bash
t
````

Implicando que <span style="color:red;">t</span> rodadas do jogo serão jogadas, com pilhas numeradas de 1
a <span style="color:red;">t</span>.

Em seguida, <span style="color:red;">t</span> casos são dados. Cada caso é imediatamente precedido por uma **linha vazia
**, em seguida são dadas
várias
linhas da forma:

````Bash
n
````

onde <span style="color:red;">n</span> representa um número (não nulo) de pacotes dentro da caixa a ser adicionada na
pilha. (O número com o qual
deverão ser feitas as operações do jogo). A última caixa, com valor <span style="color:red;">0</span>, marcará o **fim
da partida**, quando uma pilha
atinge
seu estado final. A caixa vazia **não** é adicionada à pilha

## Output Specification

````Bash
Pilha i: tamanho top
````

**Onde:**

- <span style="color:red;">i</span> é o número da Pilha em questão (valor de 1 a <span style="color:red;">t</span>)
- <span style="color:red;">tamanho</span> indica o número de caixas na Pilha (ou seja, a **quantidade** de elementos
  empilhados, não o valor deles)
- <span style="color:red;">top</span> indica o **valor** da caixa no topo ao final do jogo, presumindo que as operações
  de subtração foram feitas de acordo
  com as regras do jogo

No caso em que não haja caixas ao final do jogo, o valor de top deve ser substituído por <span style="color:red;">
-1</span>.