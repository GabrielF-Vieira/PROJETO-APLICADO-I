from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

arquivo = Path(__file__).resolve().parents[1] / "dados" / "Planilha_Series_Historicas_2T26.xlsx"
sumario = pd.read_excel(arquivo, sheet_name="Sumário_PRO FORMA", header=None)
periodos = sumario.iloc[1, 3:13].astype(str).tolist()
rotulos = sumario.iloc[:, 1].astype(str)

linha_npl = sumario[
    rotulos.str.contains("Índice de Inadimplência", case=False, regex=False, na=False)
]
linha_npl = linha_npl[
    linha_npl.iloc[:, 1].astype(str).str.contains("Total", case=False, regex=False, na=False)
].iloc[0]
npl = pd.DataFrame({
    "Trimestre": periodos,
    "Inadimplência (%)": pd.to_numeric(linha_npl.iloc[3:13], errors="coerce").values * 100
})

mascara_credito = rotulos.str.contains(
    "Total de Operações de Crédito com Garantias Financeiras Prestadas e Títulos Privados",
    case=False, regex=False, na=False
)
linha_credito = sumario[mascara_credito].iloc[0]
credito = pd.DataFrame({
    "Trimestre": periodos,
    "Operações de crédito (R$ milhões)": pd.to_numeric(linha_credito.iloc[3:13], errors="coerce").values
})
comparacao = credito.merge(npl, on="Trimestre").dropna()

print("Inadimplência — estatísticas descritivas")
print(npl["Inadimplência (%)"].describe())
print("\nCorrelação de Pearson:", round(comparacao[["Operações de crédito (R$ milhões)", "Inadimplência (%)"]].corr().iloc[0, 1], 4))

plt.figure(figsize=(9, 4.5))
plt.plot(npl["Trimestre"], npl["Inadimplência (%)"], marker="o")
plt.title("Índice de inadimplência de 90 dias — total")
plt.xlabel("Trimestre"); plt.ylabel("Inadimplência (%)")
plt.grid(True, alpha=.3); plt.xticks(rotation=45); plt.tight_layout(); plt.show()
