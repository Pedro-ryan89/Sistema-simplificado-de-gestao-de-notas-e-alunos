# PROJECT_BRIEF.md — Resumo do Projeto Final

## Nome do projeto

Sistema Simplificado de Gestão de Alunos e Notas

## Contexto

Este projeto pertence à disciplina de Introdução à Programação e Laboratório de Programação.

O objetivo é desenvolver um sistema simples em Python, executado pelo terminal, para gerenciar alunos e suas notas.

O sistema deve permitir cadastrar alunos, calcular médias, editar dados, excluir registros, listar informações, buscar alunos, aplicar filtros, gerar estatísticas e salvar/carregar dados.

## Objetivo principal

Criar um programa em Python capaz de armazenar e manipular informações de alunos de uma turma.

Cada aluno deve possuir:

- nome
- nota N1
- nota N2
- média

A média deve ser calculada automaticamente a partir das notas.

## Limite de alunos

O sistema deve permitir cadastrar até 20 alunos.

Se o limite for atingido, o programa deve impedir novos cadastros e informar o usuário.

## Funcionalidades principais

O sistema deve permitir:

1. Cadastrar aluno.
2. Informar N1 e N2.
3. Calcular a média do aluno.
4. Listar todos os alunos.
5. Mostrar os dados em formato organizado.
6. Editar dados de um aluno.
7. Excluir aluno.
8. Buscar aluno pelo nome.
9. Filtrar alunos aprovados.
10. Filtrar alunos reprovados.
11. Filtrar alunos por intervalo de média.
12. Ordenar alunos por média.
13. Mostrar estatísticas da turma.
14. Salvar dados em arquivo.
15. Carregar dados salvos ao iniciar o programa.

## Regra de aprovação

Um aluno pode ser considerado aprovado se sua média for maior ou igual a 7.0.

Um aluno pode ser considerado reprovado se sua média for menor que 7.0.

Caso o professor tenha definido outro critério, ajustar essa regra no código e na explicação.

## Estatísticas da turma

O sistema deve conseguir mostrar informações como:

- quantidade total de alunos cadastrados
- maior média
- menor média
- média geral da turma
- quantidade de aprovados
- quantidade de reprovados

## Persistência de dados

O sistema deve salvar os dados para que eles não sejam perdidos ao fechar o programa.

A biblioteca sugerida para isso é `shelve`.

A ideia é:

- carregar os alunos salvos quando o programa iniciar
- salvar os dados quando houver alterações ou ao sair do programa

## Interface

A interface será pelo terminal.

O programa deve exibir um menu com opções numeradas.

Exemplo de opções:

1. Cadastrar aluno
2. Listar alunos
3. Editar aluno
4. Excluir aluno
5. Buscar aluno por nome
6. Filtrar aprovados
7. Filtrar reprovados
8. Filtrar por intervalo de média
9. Mostrar estatísticas
10. Salvar dados
11. Sair

## Organização sugerida

O projeto pode ser organizado em funções simples.

Exemplos de funções possíveis:

- mostrar_menu
- cadastrar_aluno
- listar_alunos
- calcular_media
- editar_aluno
- excluir_aluno
- buscar_aluno
- filtrar_aprovados
- filtrar_reprovados
- filtrar_por_media
- mostrar_estatisticas
- salvar_dados
- carregar_dados

Esses nomes são apenas sugestões. A implementação final deve ser feita por mim.

## Estrutura de dados sugerida

Uma forma simples de representar os alunos é usar uma lista de dicionários.

Cada aluno pode ser representado como um dicionário contendo:

- nome
- n1
- n2
- media

A lista principal guarda todos os alunos cadastrados.

## Cuidados importantes

O programa precisa lidar com:

- nome vazio
- nota inválida
- nota menor que 0
- nota maior que 10
- tentativa de cadastrar mais de 20 alunos
- tentativa de editar aluno inexistente
- tentativa de excluir aluno inexistente
- busca sem resultado
- listagem quando não há alunos cadastrados
- arquivo de dados ainda inexistente

## Ordem recomendada de desenvolvimento

1. Criar o menu principal.
2. Criar a lista de alunos.
3. Implementar cadastro simples.
4. Implementar cálculo de média.
5. Implementar listagem.
6. Implementar validação de notas.
7. Implementar busca por nome.
8. Implementar edição.
9. Implementar exclusão.
10. Implementar filtros.
11. Implementar estatísticas.
12. Implementar salvamento.
13. Implementar carregamento.
14. Testar o sistema inteiro.
15. Preparar explicação para apresentação.

## Critério pessoal de qualidade

Eu preciso conseguir explicar:

- por que escolhi listas e dicionários
- como o menu funciona
- como o cadastro funciona
- como a média é calculada
- como a busca percorre os alunos
- como os filtros funcionam
- como os dados são salvos
- como os dados são carregados
- quais validações foram feitas
- quais limitações o sistema possui

## Restrições

Não transformar em sistema web nesta primeira versão.

Não usar banco de dados externo.

Não usar frameworks.

Não usar código complexo além do necessário.

Priorizar clareza, funcionamento e capacidade de explicação.
