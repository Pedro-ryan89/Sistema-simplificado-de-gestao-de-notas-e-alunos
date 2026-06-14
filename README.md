# Sistema Simplificado de Gestao de Alunos e Notas

Projeto final da disciplina de Introducao a Programacao.

O sistema funciona pelo terminal e permite gerenciar alunos, notas, medias, buscas, filtros, estatisticas e persistencia de dados em arquivo JSON.

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
│   ├── menus.py
│   ├── alunos.py
│   ├── consultas.py
│   ├── estatisticas.py
│   ├── armazenamento.py
│   └── validacoes.py
├── dados/
│   └── alunos.json
├── docs/
└── rascunhos/
```

## Organizacao dos modulos

- `main.py`: inicia o programa e carrega os dados salvos.
- `sistema/menus.py`: controla o menu principal e os submenus.
- `sistema/alunos.py`: cadastro, listagem, busca, edicao, exclusao e calculo de media.
- `sistema/consultas.py`: filtros de aprovados/reprovados, intervalo de media e ordenacao.
- `sistema/estatisticas.py`: estatisticas gerais da turma.
- `sistema/armazenamento.py`: salvar e carregar dados em JSON.
- `sistema/validacoes.py`: validacoes de entrada, como nota valida e texto obrigatorio.
- `dados/alunos.json`: arquivo onde os alunos ficam salvos.

## Funcionalidades

- Cadastrar aluno com N1 e N2.
- Calcular media automaticamente.
- Limitar cadastro a 20 alunos.
- Listar alunos em formato tabular.
- Buscar aluno por nome.
- Editar nome, N1 ou N2.
- Excluir aluno com confirmacao.
- Filtrar aprovados e reprovados.
- Filtrar alunos por intervalo de media.
- Ordenar alunos por media, da maior para a menor.
- Mostrar estatisticas da turma em tabela.
- Salvar e carregar dados usando JSON.

## Estrutura dos dados

Os alunos sao armazenados em uma lista de dicionarios.

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

## Regras usadas

- A media e calculada por `(N1 + N2) / 2`.
- Aluno aprovado: media maior ou igual a `7.0`.
- Aluno reprovado: media menor que `7.0`.
- As notas devem estar entre `0` e `10`.
- O nome do aluno nao pode ficar vazio.

## Observacoes

O arquivo `dados/alunos.json` ja possui alunos cadastrados para facilitar testes e demonstracao durante a apresentacao.
