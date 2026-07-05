import json
import pandas as pd

# chargement du JSON + dataframe
with open("benchmark_data.json", "r", encoding="utf-8") as f:
    dataset = json.load(f)
df = pd.DataFrame(dataset)

# nettoyer les colonnes pour une meilleure lisibilité
df["copie_texte"] = df["copie"].apply(lambda x: "; ".join(x))
df["attendu_texte"] = df["attendu"].apply(lambda x: "; ".join(x))
df["est_correcte_texte"] = df["est_correcte"].apply(lambda x: "VRAI" if x else "FAUX")

# réorganiser les colonnes
df = df[[
    "theoreme_id",
    "nom",
    "copie_texte",
    "attendu_texte",
    "est_correcte",
    "est_correcte_texte",
    "raison",
    "type_erreur"
]]

# renommage des colonnes
df.columns = [
    "ID",
    "Théorème",
    "Copie",
    "Attendu",
    "Correct (bool)",
    "Correct (texte)",
    "Raison",
    "Type_erreur"
]

# Export en CSV (pour Excel / tableur)
df.to_csv("benchmark_data_tab.csv", index=False, encoding="utf-8-sig")
print("CSV exporté: benchmark_data_tab.csv")

# Export en Markdown (pour documentation)
with open("benchmark_data_tab.md", "w", encoding="utf-8") as f:
    f.write("# Benchmark des théorèmes mathématiques\n\n")
    f.write(f"**Total:** {len(df)} copies\n\n")
    f.write(f"**Correctes:** {df['Correct (bool)'].sum()}\n\n")
    f.write(f"**Fausses:** {len(df) - df['Correct (bool)'].sum()}\n\n")
    f.write("## Détail des copies\n\n")
    
    # Tableau markdown
    f.write("| # | Théorème | Copie | Attendu | Verdict | Raison | Type_erreur |\n")
    f.write("|---|----------|-------|---------|---------|--------|-------------|\n")
    
    for i, row in df.iterrows():
        # Tronquer les textes trop longs pour le markdown
        copie = row["Copie"][:60] + "..." if len(row["Copie"]) > 63 else row["Copie"]
        attendu = row["Attendu"][:60] + "..." if len(row["Attendu"]) > 63 else row["Attendu"]
        raison = row["Raison"][:40] + "..." if len(row["Raison"]) > 43 else row["Raison"]
        
        f.write(f"| {i+1} | {row['Théorème']} | {copie} | {attendu} | {row['Correct (texte)']} | {raison} | {row['Type_erreur']} |\n")

print("Markdown exporté: benchmark_data_tab.md")

# Statistiques dans le terminal (optionnel, mais utile)
print("\n" + "="*60)
print("STATISTIQUES DU BENCHMARK")
print("="*60)
print(f"Total: {len(df)} copies")
print(f"Correctes: {df['Correct (bool)'].sum()}")
print(f"Fausses: {len(df) - df['Correct (bool)'].sum()}")

print("\nTypes d'erreurs:")
type_counts = df["Type_erreur"].value_counts()
for t, count in type_counts.items():
    print(f"  - {t}: {count}")

print("\nRaisons d'échec (top 5):")
raison_counts = df[df["Correct (bool)"] == False]["Raison"].value_counts().head(5)
for r, count in raison_counts.items():
    print(f"  - {r}: {count}")