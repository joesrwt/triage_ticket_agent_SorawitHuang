# triage_ticket_agent_SorawitHuang


## 🧱 Architecture Overview

This support ticket triage agent is built around a **RAG-based (Retrieval-Augmented Generation) architecture**. It retrieves relevant FAQs and documentation using embeddings, taking into account both the customer’s latest message and their support history as context.

Key points:

- **Reliability**: Leveraging historically verified FAQs and useful Docs ensures the guidance provided is accurate and consistent.
- **Self-help for customers**: When an issue is generic or informational, the system can provide immediate guidance, reducing the need for human intervention.
- **Mock Data**: Customer History and Knowledge Base are easy to replace or scale for more data.

## 🚀 What This App Does

This application demonstrates an interactive, RAG-based support ticket triage system. Using a customer ID, it performs the following steps:

1. **Select a Customer**: The user chooses from available customer IDs (e.g., FREE-0001, ENT-0001, PRO-0001).  

2. **View Customer Profile**: Displays structured customer information such as plan, region, tenure, and seat count.

3. **Review Conversation History**: Shows the latest message and previous context messages with timestamps, so the agent or user can understand the conversation flow.

4. **Semantic Search for Relevant Knowledge**: Uses OpenAI embeddings (`text-embedding-3-small`) to find the top relevant FAQ and document that may provide guidance or have solved similar issues before.


5. **Run GPT-based Triage**: The GPT-4o Mini model evaluates the latest customer message and classifies:  
   - **Urgency**: critical / high / medium / low  
   - - **Issue Type**: from 14 most common support ticket types (e.g., Service Request, Outage, Feature Request, etc.) based on [medium.com/kommunicate/what-is-ticket-triage-in-customer-support-processes-and-tools](https://medium.com/kommunicate/what-is-ticket-triage-in-customer-support-processes-and-tools-4b9a1343925d)
   - **Product**: plan/ feature/ system  
   - **Customer Sentiment**: positive / frustrated / angry  
   - **Reasoning**: a concise, 1-sentence explanation of the classification


6. **Determine Next Action**: The system uses a simple, explainable rule-based layer on top of the LLM and embedding retrieval results to decide the appropriate next step:

   - **`auto_respond`**: If the top relevant FAQ or document has a high relevance (≥ 80%) **and** the issue urgency is low or medium, the system provides self-help guidance automatically.  

   - **`escalate_to_human`**: If the urgency is critical **or** the customer has already followed up multiple times (≥ 3), the system flags the ticket for immediate human attention.
     
   - **`route_to_specialist`**: For all other cases, the system routes the ticket to a specialist team. 


7. **Explainable Output**:  Provides a structured summary of the ticket: 
   - urgency, issue type, product, sentiment, next action and reasoning
   - top 1 relevant FAQ and Doc with content and relevance scores



---

## 🚀 How To Run an Example for The Demo

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
   !python -m examples.run_interactive


6. Paste OpenAI API key :
 - (1) for embeddings "text-embedding-3-small"
 - (2) for GPT model "gpt-4o-mini"

7. Select a customer ID from the list (type 1-3)
