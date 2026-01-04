import pickle

with open("graph/drug_interaction_graph.pkl", "rb") as f:
    G = pickle.load(f)

def get_interaction(drug_a, drug_b):
    drug_a = drug_a.lower().strip()
    drug_b = drug_b.lower().strip()

    if G.has_edge(drug_a, drug_b):
        return G[drug_a][drug_b]
    return None

def get_all_interactions(drug_list):
    interactions = []

    for i in range(len(drug_list)):
        for j in range(i + 1, len(drug_list)):
            result = get_interaction(drug_list[i], drug_list[j])
            if result:
                interactions.append({
                    "drug_pair": (drug_list[i], drug_list[j]),
                    "details": result
                })
    return interactions
