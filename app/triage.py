from app.tools.customer_history import get_customer_history
from app.tools.knowledge_base import FAQ_KB, DOC_KB
from app.embeddings import embed, retrieve_best_kb_item
from app.llm_classifier import classify_with_llm

def triage_ticket(customer_id: str):
    history = get_customer_history(customer_id)

    messages = history["conversation_history"]["messages"]
    support_ctx = history["support_context"]

    latest_msg = messages[-1]["message"]
    context_msgs = " ".join(m["message"] for m in messages[:-1])

    classification = classify_with_llm(history, latest_msg)

    query = f"""
    PRIMARY ISSUE:
    {latest_msg}

    CONTEXT:
    {context_msgs}
    """

    query_embedding = embed(query)

    faq, faq_score = retrieve_best_kb_item(query_embedding, FAQ_KB)
    doc, doc_score = retrieve_best_kb_item(query_embedding, DOC_KB)

    max_relevance = max(faq_score, doc_score)

    if max_relevance >= 80 and classification["urgency"] in ["low", "medium"]:
        next_action = "auto_respond"
    elif classification["urgency"] == "critical":
        next_action = "escalate_to_human"
    else:
        next_action = "route_to_specialist"

    return {
        "urgency": classification["urgency"],
        "product": classification["product"],
        "issue_type": classification["issue_type"],
        "customer_sentiment": classification["customer_sentiment"],
        "knowledge_base": {
            "faq": {**faq, "relevance_score_percent": faq_score},
            "doc": {**doc, "relevance_score_percent": doc_score}
        },
        "next_action": next_action,
        "reasoning": classification["reasoning"]
    }
