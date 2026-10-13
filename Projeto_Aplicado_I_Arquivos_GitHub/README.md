# Projeto Aplicado I — Itaú Unibanco

## Tema
Análise da evolução das operações de crédito selecionadas e da inadimplência entre 2024 e 2026.

## Pergunta de pesquisa
Como a expansão do indicador de operações de crédito selecionado se relacionou com a evolução da inadimplência entre 2024 e 2026?

## Integrantes
- Camila Miranda De Almeida
- Gabriel Freitas Vieira
- Mônica Farias Alves
- Nicolas dos Santos Varnier Mota

## Fonte dos dados
Itaú Unibanco — Relações com Investidores, Planilha de Séries Históricas do 2º trimestre de 2026:  
https://www.itau.com.br/relacoes-com-investidores/resultados-e-relatorios/central-de-resultados/

## Estrutura
- `dados/`: planilha original e tabelas exportadas.
- `notebooks/`: análise exploratória em Jupyter Notebook.
- `scripts/`: script Python complementar.
- `figuras/`: gráficos exportados para uso no relatório.

## Como executar
1. Instale Python 3, pandas, openpyxl, matplotlib e Jupyter.
2. Abra `notebooks/01_analise_exploratoria.ipynb` no VS Code ou Jupyter.
3. Execute as células na ordem, começando pela primeira.

Instalação das bibliotecas:
```bash
pip install pandas openpyxl matplotlib jupyter
```

## Nota metodológica
O indicador de crédito utilizado é o item identificado na planilha como “Total de Operações de Crédito com Garantias Financeiras Prestadas e Títulos Privados”. Não se deve tratá-lo automaticamente como medida de toda a carteira de crédito. A correlação indica associação, não causalidade. A planilha também informa alterações de classificação/composição dos dados ao longo da série.

## Principais resultados

No período analisado, de 1T24 a 2T26, o indicador selecionado de operações de crédito aumentou aproximadamente 24,55%. No mesmo intervalo, a inadimplência de 90 dias caiu de 2,70% para aproximadamente 1,95%, uma redução de 0,75 ponto percentual.

A correlação de Pearson entre as duas séries foi de aproximadamente -0,847, indicando uma associação linear negativa forte na amostra analisada. Entretanto, esse resultado não permite concluir que o aumento das operações de crédito causou a redução da inadimplência.
