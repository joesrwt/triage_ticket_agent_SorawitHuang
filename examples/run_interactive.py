import json
from app.triage import triage_ticket
from app.tools.customer_history import CUSTOMER_HISTORY_DB

def main():
    # Step 1: Let user pick a customer
    print("Select a customer ID from the list below:")
    customer_ids = list(CUSTOMER_HISTORY_DB.keys())
    for i, cid in enumerate(customer_ids, start=1):
        print(f"{i}. {cid}")

    choice = int(input("Enter the number of the customer: "))
    selected_customer_id = customer_ids[choice - 1]

    # Step 2: Fetch customer history
    history = CUSTOMER_HISTORY_DB[selected_customer_id]
    profile = history["customer_profile"]
    messages = history["conversation_history"]["messages"]
    latest_msg = messages[-1]["message"]
    context_msgs = [m["message"] for m in messages[:-1]]

    # Step 3: Print structured info
    print("\n--- Customer Profile ---")
    for k, v in profile.items():
        print(f"{k}: {v}")

    print("\n--- Latest Message ---")
    print(latest_msg)

    print("\n--- Context Messages ---")
    if context_msgs:
        for i, m in enumerate(context_msgs, start=1):
            print(f"{i}. {m}")
    else:
        print("No previous messages.")

    # Step 4: Run triage
    result = triage_ticket(selected_customer_id)

    # Step 5: Print explainable, structured output
    print("\n--- Triage Result ---")
    print(f"Urgency: {result['urgency']}")
    print(f"Issue Type: {result['issue_type']}")
    print(f"Product: {result['product']}")
    print(f"Customer Sentiment: {result['customer_sentiment']}")
    print(f"Next Action: {result['next_action']}")
    print(f"Reasoning: {result['reasoning']}")

    print("\n--- Recommended FAQ ---")
    faq = result["knowledge_base"]["faq"]
    print(f"ID: {faq['id']}")
    print(f"Title: {faq['title']}")
    print(f"Content: {faq['content']}")
    print(f"Relevance: {faq['relevance_score_percent']}%")

    print("\n--- Recommended Document ---")
    doc = result["knowledge_base"]["doc"]
    print(f"ID: {doc['id']}")
    print(f"Title: {doc['title']}")
    print(f"Content: {doc['content']}")
    print(f"Relevance: {doc['relevance_score_percent']}%")

if __name__ == "__main__":
    main()
