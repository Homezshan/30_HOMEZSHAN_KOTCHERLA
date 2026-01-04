# PharmaVision AI  
### A Safety-First Graph-RAG Clinical Intelligence System

<p align="center">
  <img src="https://img.shields.io/badge/Domain-Healthcare%20AI-blue" />
  <img src="https://img.shields.io/badge/Architecture-Graph%20%2B%20RAG%20%2B%20LLM-success" />
  <img src="https://img.shields.io/badge/Safety-Hallucination--Controlled-critical" />
  <img src="https://img.shields.io/badge/API-FastAPI-teal" />
  <img src="https://img.shields.io/badge/Status-Hackathon%20Ready-brightgreen" />
</p>

<p align="center">
  <strong>Graph-Grounded · Evidence-Driven · LLM-Assisted · Clinically Responsible</strong>
</p>

---

## Overview

**PharmaVision AI** is a clinical safety intelligence system designed to identify and explain **drug–drug interactions** using a **deterministic knowledge graph**, **evidence-aware retrieval**, and a **guarded language model for human-readable explanations**.

Unlike conventional AI chatbots, PharmaVision AI strictly separates **clinical truth**, **supporting evidence**, and **natural-language explanation**, ensuring **zero hallucination of medical facts**, **traceable outputs**, and **responsible AI usage**.

---

## Problem Statement

Drug–drug interactions are a major source of preventable adverse events in healthcare.  
Many existing AI systems suffer from:

- Hallucinated medical explanations  
- Opaque decision logic  
- Unsafe reliance on generative reasoning  
- Lack of traceable evidence  

**PharmaVision AI** addresses these challenges by enforcing **data-first reasoning**, while using language models **only for explanation**, never for medical decision-making.

---

## System Philosophy

PharmaVision AI follows a **Safety-First Intelligence Architecture**:

| Layer | Responsibility |
|------|----------------|
| Knowledge Graph | Determines whether an interaction exists |
| Evidence Retrieval | Retrieves factual supporting context |
| Safety Agent | Enforces deterministic logic and guardrails |
| Language Model | Converts verified facts into human-readable explanations |
| API Layer | Exposes validated results |

At no point does the system allow a language model to invent, infer, or override clinical facts.

---

## High-Level Architecture

```
User Query
│
▼
Knowledge Graph (Verified Interactions)
│
├─ Interaction Exists? ── No ──► Safe Exit
│
▼
Evidence Retrieval (Curated Sources)
│
▼
Safety Agent (Rule-Bound Logic)
│
▼
LLM Explanation Layer (Fact-Preserving)
│
▼
API Response (Structured & Explainable)
```

---

## Key Features

### Deterministic Interaction Detection
- Interaction existence is resolved exclusively via a structured knowledge graph
- No probabilistic guessing or inference

### Evidence-Aware Retrieval
- Supporting clinical context is retrieved from curated sources
- Absence of evidence is explicitly surfaced, not hidden

### Guarded LLM Usage
- Language models are used **only to explain verified facts**
- No medical reasoning or decision-making is delegated to the LLM
- Strict prompts prevent hallucination and advice generation

### Medical Safety Guardrails
- Severity is never inferred without data
- Clear disclaimers prevent misuse as medical advice

### Explainability by Design
- Every output is traceable to data and evidence
- Clear separation of reasoning and language generation

---

## Example Output

```json
{
  "drug_pair": ["warfarin", "erythromycin"],
  "interaction_exists": true,
  "severity": "unknown",
  "explanation": "These two drugs are known to interact according to curated drug-interaction databases. While no detailed mechanism was retrieved, clinicians typically monitor patients closely when such combinations are prescribed.",
  "source": "DDInter + Evidence Retrieval",
  "disclaimer": "This information is for educational purposes only and is not medical advice."
}
```

---

## Technology Stack

| Category | Tools |
|--------|------|
| Data Processing | Pandas |
| Knowledge Graph | NetworkX |
| Evidence Retrieval | Vector Database (Local Embeddings) |
| Language Model | Guarded LLM (Explanation-Only Role) |
| API Framework | FastAPI |
| Validation | Pydantic |

---

## Project Structure

```
pharmavision-ai/
├── data/          # Raw and processed datasets
├── graph/         # Knowledge graph construction & queries
├── rag/           # Evidence retrieval layer
├── agent/         # Safety logic & LLM explanation orchestration
├── api/           # FastAPI application
└── README.md
```

---

## Getting Started

```bash
pip install -r requirements.txt
python -m uvicorn api.main:app --reload
```

Interactive API documentation:

```
http://127.0.0.1:8000/docs
```

---

## Live Demo Flow (Hackathon)

1. Submit a drug pair query via the API  
2. Knowledge Graph verifies interaction existence  
3. Evidence Retrieval attempts to fetch clinical context  
4. Safety Agent enforces deterministic reasoning  
5. LLM produces a **fact-preserving explanation only**  
6. Structured response is returned with disclaimers  

This entire flow can be demonstrated in under **60 seconds**.

---

## Disclaimer

PharmaVision AI is intended for **educational and research purposes only**.  
It does **not** provide medical advice, diagnosis, or treatment recommendations.

All clinical decisions must be made by qualified healthcare professionals.

---

## Why PharmaVision AI Stands Out

- Explicit separation of **facts**, **evidence**, and **language**
- Controlled and responsible use of language models
- Zero hallucination tolerance for clinical data
- Designed for trust, auditability, and safety-critical environments

**PharmaVision AI demonstrates how Graph-RAG and LLMs can be combined responsibly in healthcare AI systems.**

---

*Because in healthcare, correctness matters more than creativity.*
