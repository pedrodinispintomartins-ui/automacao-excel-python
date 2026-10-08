import pandas as pd

# 1. Simulação de uma base de dados de clientes/vendas
dados = {
    "Cliente": ["Loja Alfa", "Café Central", "Loja Alfa", "Oficina Silva", "Café Central"],
    "Categoria": ["Software", "Manutenção", "Hardware", "Software", "Software"],
    "Valor (€)": [350, 80, 1200, 450, 150],
    "Estado": ["Pago", "Pendente", "Pago", "Pago", "Pendente"]
}

# 2. Criar o DataFrame
df = pd.DataFrame(dados)

# 3. Processamento de Dados (Métricas e Filtros)
vendas_pagas = df[df["Estado"] == "Pago"]
total_recebido = vendas_pagas["Valor (€)"].sum()
pendentes = df[df["Estado"] == "Pendente"]
total_pendente = pendentes["Valor (€)"].sum()

print("=== RELATÓRIO EXECUTIVO DE VENDAS ===")
print("\n--- Todas as Transações ---")
print(df)

print(f"\n[+] Total Efetivamente Recebido: {total_recebido}€")
print(f"[!] Total em Atraso / Pendente: {total_pendente}€")

# 4. Exportar relatório limpo de pagamentos pendentes para cobrança
pendentes.to_excel("Cobracas_Pendentes.xlsx", index=False)
print("\n[SUCESSO] Ficheiro 'Cobracas_Pendentes.xlsx' gerado para envio ao cliente!")