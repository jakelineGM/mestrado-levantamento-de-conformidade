# levantamento-de-conformidade

Levantamento de conformidade entre enunciados e códigos de alunos aceitos pelo juiz online (CodeBench) (dataset `../cb-dataset`, disciplinas AED, AED I e AED II). O juiz só confere a saída; aqui se verifica, com um LLM, se o código também cumpre o que o enunciado exige (método, algoritmo, estrutura de dados, restrições). O objetivo é obter dados númericos a cerca de "desvios" que os alunos podem cometer e o juiz online não identificar. Além disso, avaliar a LLM como agente desse papel.

## Pipeline

```
indexar_exercicios -> classificar_exercicios -> selecionar_amostra -> verificar_conformidade -> relatorio_conformidade
```

Os scripts leem o dataset de `../cb-dataset` (ou da variável de ambiente `CB_DATASET`) e gravam nas pastas deste diretório. Podem ser rodados de qualquer pasta, por exemplo `python scripts/selecionar_amostra.py --categorias ...`.

## Estrutura

```
levantamento-de-conformidade/
├── diario-de-pesquisa.md
├── scripts/
├── prompt/
├── classificacao/
├── selecao/
└── conformidade/
```

### `diario-de-pesquisa.md`
Diário de pesquisa (arquivo atualmente vazio).

### `scripts/`
| Arquivo | O que faz |
|---|---|
| `indexar_exercicios.py` | Percorre o dataset e gera o índice de exercícios e a lista de enunciados únicos (saída em `classificacao/`). |
| `classificar_exercicios.py` | Classifica cada enunciado único em categoria/subtema com a API da Anthropic, em lotes. Retomável; precisa de `ANTHROPIC_API_KEY`. |
| `selecionar_amostra.py` | Sorteia 200 códigos por disciplina, alternando categorias e subtemas (semente fixa), e monta a pasta `selecao/`. |
| `verificar_conformidade.py` | Envia cada item da amostra (um enunciado + um código) ao Claude Code (`claude -p`) com o prompt escolhido e grava os resultados em `conformidade/<versao>/`. Retomável; exige `ANTHROPIC_API_KEY` **não** definida. |
| `relatorio_conformidade.py` | Gera relatórios: proporção de desvios (com IC95 e ponderação pela população), comparação entre versões do prompt e concordância com a revisão manual. |

### `prompt/`
Prompts usados na verificação de conformidade.

| Arquivo | Conteúdo |
|---|---|
| `prompt_conformidade_V1.txt` | Primeira versão do prompt. Veredito: `conforme` / `nao_conforme`. |
| `prompt_conformidade_V2.txt` | Versão atual (padrão do script). Veredito: `sem_desvio` / `desvio` / `indeterminado`, com tipos de desvio. |

### `classificacao/`
Resultado da indexação e da classificação dos enunciados.

| Arquivo | Conteúdo |
|---|---|
| `indice_exercicios.csv` | Uma linha por exercício (caminho no dataset, disciplina, turma, avaliação, linguagem, título, nº de alunos, hash e texto do enunciado). |
| `enunciados_unicos.jsonl` | Um registro por enunciado único (é o que vai ao LLM). |
| `classificacao.csv` | Categoria, subtema, categoria secundária, confiança e justificativa por enunciado único. |
| `exercicios_classificados.csv` | O índice completo com a classificação anexada. |
| `resumo_por_categoria.csv` | Enunciados, exercícios e códigos de alunos por categoria/subtema. |
| `para_revisar.csv` | Itens com confiança média/baixa ou rótulo fora da taxonomia, para revisão manual. |
| `execucao.json` | Modelo, data, tamanho do lote e prompt usados na classificação. |

### `selecao/`
Amostra sorteada para a verificação.

| Item | Conteúdo |
|---|---|
| `amostra.csv` | Uma linha por código sorteado (uid, categoria, subtema, caminhos no dataset), sem textos longos. |
| `amostra.jsonl` | O mesmo, com enunciado, código e casos de teste. É a entrada de `verificar_conformidade.py`. |
| `resumo_categorias.csv` | Por disciplina, categoria e subtema: exercícios, códigos disponíveis e sorteados. Usado na ponderação do relatório. |
| `resumo.md` | O resumo acima em texto legível. |
| `parametros.json` | Semente, nº por disciplina, categorias e subtemas, data do sorteio. |
| `AED/`, `AED1/`, `AED2/` | 200 pastas por disciplina, no formato `<ordem>_<categoria>-<subtema>_<exercicio>_<aluno>/`, cada uma com `enunciado.md`, `metadados.json`, `codigo/` (código do aluno) e `test-cases/` (`N.input.txt` / `N.output.txt`). |

### `conformidade/`
Resultados da verificação, uma subpasta por versão do prompt (hoje só `v2/`).

| Arquivo (em `v2/`) | Conteúdo |
|---|---|
| `resultados.jsonl` | Resposta bruta do LLM por item, com metadados. |
| `itens.csv` | Uma linha por item, ordenada por prioridade de revisão. As colunas `revisao_manual_desvio` e `revisao_manual_comentario` são preenchidas à mão e preservadas ao refazer. |
| `desvios.csv` | Uma linha por desvio apontado (exigência, tipo, linhas, evidência, descrição). |
| `execucao.json` | Modelo, datas, hash e texto exato do prompt (para a metodologia). |
| `erros.jsonl` | Itens sem resposta válida (só existe se houver falhas). |

Cada versão aceita um único prompt e modelo; para testar outro prompt, use outra `--versao`.
