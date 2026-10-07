# Gerenciador de Lojas - Lista Ligada em Python 🔗📦

Este projeto é uma implementação em Python de uma **Lista Ligada (Singly Linked List)** desenvolvida com o objetivo de aprofundar conhecimentos em Estruturas de Dados. 

A aplicação conta com um menu de linha de comando (CLI) interativo que permite ao usuário realizar operações completas de CRUD (Criar, Ler, Atualizar e Deletar) em um cadastro fictício de lojas.

---

## 📌 Funcionalidades

- **Inserção de Dados:**
  - Inserir no início da lista (complexidade $O(1)$)
  - Inserir no fim da lista
  - Inserir em uma posição específica
- **Consulta e Pesquisa:**
  - Listar todos os elementos cadastrados
  - Consultar item por índice/posição
  - Pesquisar loja por nome ou termo parcial
- **Remoção e Limpeza:**
  - Remover elemento do início
  - Remover elemento de posição específica
  - Limpar toda a lista
- **Tratamento de Exceções:** Validações de limites e índices válidos para evitar falhas durante a execução.

---

## 🛠️ Estrutura do Projeto

O projeto é dividido em dois arquivos principais:

- `classes.py`: Contém a implementação das classes `Celula` (os nós da lista) e `ListaLigada` (a estrutura de dados em si e seus métodos).
- `main.py`: Contém a classe `Loja` e a interface do usuário (menu interativo via terminal).

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Python 3.8 ou superior instalado.

### Passos

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

2. **Acesse a pasta do projeto:**
   ```bash
   cd seu-repositorio
   ```

3. **Execute o programa:**
   ```bash
   python main.py
   ```

---

## 💻 Exemplo de Uso

Ao iniciar a aplicação, você verá o seguinte menu interativo:

```text
====================================
      GERENCIADOR DE LOJAS          
====================================
1. Inserir no início
2. Inserir no fim
3. Inserir em posição específica
4. Listar todas as lojas
5. Consultar item por posição
6. Pesquisar loja por nome
7. Remover do início
8. Remover de posição específica
9. Limpar toda a lista
0. Sair
====================================
```

---

## 📚 Conceitos Aprendidos

- **Ponteiros/Referências:** Conexão entre nós (`Celula.proximo`).
- **Encapsulamento:** Uso de `@property` para proteção de atributos internos.
- **Manipulação de Memória e Posições:** Busca sequencial para inserções e remoções genéricas.
- **Tratamento de Erros:** Manipulação de exceções como `IndexError` e `ValueError`.

---

## 📝 Licença

Este projeto é de uso livre para fins de estudo e aprendizado.
