# System Architecture


```mermaid
graph TD

USER[Utilisateur]

USER --> UI[Interfaces]

UI --> CORE[Aura Core]

CORE --> SERVICES[Services]

SERVICES --> MEMORY[Memory]

SERVICES --> SECURITY[Security]

SERVICES --> LLM[LLM Service]

LLM --> OLLAMA[Ollama]

MEMORY --> SQLITE[SQLite]

MEMORY --> QDRANT[Qdrant]

---

# 8) Premier ADR

Créer :

```text
docs/decisions/ADR-0001-memory.md
# ADR-0001

## Choix

Architecture mémoire hybride.


## Statut

Accepté


## Contexte

AURA nécessite une mémoire persistante.


## Décision

Utiliser :

- Markdown pour identité
- SQLite pour mémoire dynamique
- Qdrant pour recherche vectorielle


## Raisons

Markdown:

- humainement lisible
- versionnable avec Git


SQLite:

- portable
- simple
- local


Qdrant:

- recherche sémantique


## Conséquences

Architecture évolutive.