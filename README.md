# Sistema Simplificado de Gestão de Alunos e Notas

Projeto de terminal desenvolvido para a disciplina de Introdução à Programação.

O sistema permite gerenciar alunos e notas, fazer buscas e filtros, gerar estatísticas da turma e manter os dados salvos em um arquivo JSON.

## Como executar

No terminal, dentro da pasta do projeto, execute:

```bash
python3 main.py
```

## Estrutura do projeto

```text
.
├── main.py
├── sistema/
│   ├── gestao/
│   │   ├── alunos.py
│   │   └── auxiliares.py
│   ├── interface/
│   │   └── menus.py
│   ├── persistencia/
│   │   └── armazenamento.py
│   ├── relatorios/
│   │   ├── consultas.py
│   │   └── estatisticas.py
│   ├── tipos.py
│   └── validacoes.py
├── dados/
│   └── alunos.json
└── README.md
```

## Organização dos módulos

- `main.py`: ponto de entrada; carrega os dados e inicia o menu principal.
- `sistema/interface/menus.py`: controla o menu principal e os submenus.
- `sistema/gestao/alunos.py`: cadastro, listagem, busca, edição e exclusão de alunos.
- `sistema/gestao/auxiliares.py`: funções reutilizáveis para buscar, selecionar e exibir alunos.
- `sistema/relatorios/consultas.py`: filtros de aprovados, reprovados, intervalo de média e ordenação.
- `sistema/relatorios/estatisticas.py`: estatísticas gerais da turma.
- `sistema/persistencia/armazenamento.py`: leitura e gravação dos dados em JSON.
- `sistema/validacoes.py`: validações de notas, nomes e termos de busca.
- `sistema/tipos.py`: define o tipo `Aluno`, usado nos type hints do projeto.
- `dados/alunos.json`: arquivo em que os alunos são salvos.

## Funcionalidades

- Cadastrar aluno com nome completo, N1 e N2.
- Calcular média automaticamente.
- Limitar cadastro a 20 alunos.
- Listar alunos em formato tabular.
- Buscar aluno por nome ou parte do nome.
- Cancelar uma busca ou seleção de aluno digitando `0`.
- Editar nome, N1 ou N2 com recálculo da média.
- Excluir aluno com confirmação.
- Filtrar aprovados e reprovados.
- Filtrar alunos por intervalo de média.
- Ordenar alunos por média, da maior para a menor.
- Mostrar estatísticas da turma em tabela.
- Salvar e carregar dados usando JSON.

## Estrutura dos dados

Os alunos são armazenados em uma lista de dicionários. O tipo `Aluno`, definido em `sistema/tipos.py`, documenta as chaves esperadas.

Exemplo:

```python
[
    {
        "nome": "Ana Clara",
        "n1": 8.0,
        "n2": 9.0,
        "media": 8.5
    }
]
```

## Regras de negócio

- A média é calculada por `(N1 + N2) / 2`.
- Aluno aprovado: média maior ou igual a `7.0`.
- Aluno reprovado: média menor que `7.0`.
- As notas devem estar entre `0` e `10`.
- O cadastro exige nome e sobrenome, usando apenas letras e espaços.
- A busca aceita nome completo ou parte do nome.
- Durante uma busca ou seleção de aluno, digite `0` para cancelar e voltar ao menu.

## Observacoes

O arquivo `dados/alunos.json` já possui alunos cadastrados para facilitar testes e demonstrações durante a apresentação.
