# E-Stock
Sistema de gestão de estoque para e-commerce desenvolvido em ``Python``, com interface gráfica construída utilizando a biblioteca ``Graphics``.

>O projeto foi desenvolvido em grupo na disciplina de Algoritmos e Estruturas de Dados, com foco na aplicação prática de algoritmos e estruturas de dados no desenvolvimento de um sistema de controle de estoque. A aplicação permite cadastrar e consultar produtos, controlar quantidades disponíveis e atualizar o estoque conforme as operações realizadas. Como principal desafio, foi necessário desenvolver a interface utilizando a biblioteca Graphics, trabalhando com recursos gráficos básicos para criar a interação e a experiência do usuário.

**Conceitos utilizados:**
 ``Estruturas de dado`` ``Listas e dicionário`` ``Manipulação de arquivos CS`` ``Modularizaçã`` ``Desenvolvimento de interfaces gráfica`` ``Organização de códig`` ``Manipulação e atualização de dado``
## Funcionalidades
``Leitura de dados de estoque a partir de arquivos CSV`` ``Cadastro de novos produtos`` ``Consulta da quantidade disponível de produtos`` ``Visualização dos itens em estoque`` ``Atualização do estoque após uma compra`` ``Interface gráfica para interação com o sistema``

## Minha contribuição
Durante o desenvolvimento, atuei principalmente na estruturação da aplicação e construção da interface gráfica, além da correção e organização do projeto.

* Definição da arquitetura e organização geral do projeto
* Desenvolvimento do design das telas
* Implementação da tela inicial
* Correção de problemas nas telas de compra
* Modularização das telas
* Remoção de arquivos duplicados
* Reorganização da estrutura do projeto
* Ajustes finais para preparação da entrega

## Estrutura do projeto

O projeto foi organizado de forma modular, separando a interface gráfica, as funcionalidades do sistema e os dados utilizados pela aplicação.

* ``Telas``: organizadas de acordo com as diferentes funcionalidades do sistema, facilitando a navegação e manutenção da interface.
* ``Funcionalidades``: responsáveis pelas operações de cadastro, consulta e atualização do estoque.
* ``Dados``: arquivos CSV utilizados para armazenar e consultar as informações dos produtos.
* ``Estrutura modular``: divisão do código em diferentes componentes para evitar duplicação e facilitar a manutenção.

## Como executar

### Pré-requisitos

* Python 3 instalado

### Executando o projeto

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/e-stock.git
cd e-stock
```

2. Execute o arquivo principal da aplicação:

```bash
python main.py
```

A interface gráfica será aberta para interação com as funcionalidades do sistema.

> **Observação:** o sistema utiliza arquivos CSV para armazenar os dados de estoque. Os arquivos devem permanecer na estrutura esperada pelo projeto para que a leitura e atualização dos produtos funcionem corretamente.