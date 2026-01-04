import pandas as pd
import glob

files = glob.glob("data/raw/ddinter_downloads_code_*.csv")

dfs = []
for file in files:
    df = pd.read_csv(file)
    dfs.append(df)

df = pd.concat(dfs, ignore_index=True)

df = df.drop_duplicates()

df = df[["DDInterID_A", "Drug_A", "DDInterID_B", "Drug_B"]]


df = df.dropna(subset=["Drug_A", "Drug_B"])


df["Drug_A"] = df["Drug_A"].str.lower().str.strip()
df["Drug_B"] = df["Drug_B"].str.lower().str.strip()

df.to_csv("data/processed/processed_ddinter.csv", index=False)

print("Processed rows:", df.shape[0])


import networkx as nx
import pickle
import pandas as pd


df = pd.read_csv("data/processed/processed_ddinter.csv")

G = nx.Graph()

for _, row in df.iterrows():
    drug_a = row["Drug_A"]
    drug_b = row["Drug_B"]

    if drug_a != drug_b:
        G.add_edge(
            drug_a,
            drug_b,
            source="DDInter"
        )

with open("graph/drug_interaction_graph.pkl", "wb") as f:
    pickle.dump(G, f)

print("Graph created successfully")
print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())


import networkx as nx

assert nx.number_of_selfloops(G) == 0
print("Graph validation passed")
