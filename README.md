# triage_ticket_agent_SorawitHuang


# 🧠 Support Ticket Triage System (LLM + Embeddings)

This project demonstrates an end-to-end AI-powered support ticket triage system
using OpenAI LLMs and semantic search with embeddings.

It is designed as a **practical AI Engineer assessment** example.

---

## 🚀 What This App Does

Given a `customer_id`, the system:

1. Retrieves customer support history
2. Uses an LLM (GPT-4o Mini) to classify:
   - urgency
   - issue type
   - product
   - customer sentiment
3. Searches FAQs and documentation using embeddings
4. Calculates relevance scores (0–100%)
5. Decides the next action:
   - `auto_respond` (self-help chatbot)
   - `route_to_specialist`
   - `escalate_to_human`

---

## 🧱 Architecture Overview

- **LLM**: GPT-4o Mini (ticket classification)
- **Embeddings**: `text-embedding-3-small` (semantic search)
- **Decision Layer**: deterministic, explainable rules
- **Mock APIs**: customer history + knowledge base (easy to replace)

---


---

## 🚀 How To Run

### 1️⃣ Run on Google Colab

1. Open **Google Colab**
2. Clone the repository:
   ```bash
   !git clone https://github.com/joesrwt/triage_ticket_agent_SorawitHuang.git
%cd triage_ticket_agent_SorawitHuang

4. Install dependencies:
     ```bash
     !pip install -r requirements.txt


5. Run the example:
    ```bash
   !python examples/run_example.py
    python -m examples.run_example


6. When prompted, paste your OpenAI API key


