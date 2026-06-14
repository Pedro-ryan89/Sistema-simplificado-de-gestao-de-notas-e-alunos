# Melhorias Futuras

Este arquivo registra pontos que podem ser melhorados depois que a versao principal estiver funcionando.

## Prioridade para terminar o projeto

- Melhorar a listagem de alunos para mostrar nome, N1, N2 e media.
- Criar a funcao de excluir aluno.
- Criar filtros de aprovados e reprovados.
- Criar filtro por intervalo de media.
- Criar ordenacao por media.
- Criar estatisticas da turma: total de alunos, maior media, menor media, media geral, aprovados e reprovados.
- Criar salvamento e carregamento dos dados com `shelve`.

## Validacoes importantes

- Impedir nome vazio no cadastro.
- Validar notas entre 0 e 10.
- Evitar erro se o usuario digitar letra no lugar da nota.
- Tratar entradas invalidas nos menus.
- Confirmar antes de excluir um aluno.

## Melhorias de organizacao e apresentacao

- Padronizar acentos e textos exibidos no terminal.
- Corrigir pequenos erros de digitação nos menus, como "Cadrastar" para "Cadastrar".
- Melhorar a formatacao da media para uma ou duas casas decimais.
- Evitar repeticao de codigo entre buscar, editar e excluir aluno.
- Criar testes manuais documentados para apresentar o funcionamento.

## Observacoes para explicacao

- Cada dicionario representa um aluno individual.
- A lista `alunos` representa a turma inteira.
- O menu principal chama submenus.
- O submenu de gestao trabalha com cadastro, listagem, busca, edicao e exclusao.
- O submenu de filtros e estatisticas trabalha com analise da turma.
