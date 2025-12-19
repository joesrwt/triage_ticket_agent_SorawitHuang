# examples/run_interactive.py

from app.triage import triage_ticket
from app.tools.customer_history import CUSTOMER_HISTORY_DB
import time

def main():
    # Step 1: Let user pick a customer
    customer_ids = list(CUSTOMER_HISTORY_DB.keys())
    print("Select a customer ID from the list below (type 1-3):")
    for i, cid in enumerate(customer_ids, start=1):
        print(f"{i}. {cid}")

    while True:
        choice = input("Enter the number of the customer: ").strip()
        if choice in ["1", "2", "3"]:
            selected_customer_id = customer_ids[int(choice) - 1]
            break
        print("Please enter a number between 1 and 3.")

    # Step 2: Fetch customer history
    history = CUSTOMER_HISTORY_DB[selected_customer_id]
    profile = history["customer_profile"]
    messages = history["conversation_history"]["messages"]
    latest_msg_obj = messages[-1]
    latest_msg = latest_msg_obj["message"]
    context_msgs = messages[:-1]

    # Step 3: Print structured info
    print("\n===============================")
    print("Customer Profile")
    print("===============================")
    for k, v in profile.items():
        print(f"{k}: {v}")

    print("\n===============================")
    print("Latest Message")
    print("===============================")
    timestamp = latest_msg_obj.get("timestamp", None)
    ts_str = timestamp.strftime("%Y-%m-%d %H:%M") if timestamp else ""
    print(f"{ts_str} {latest_msg}")

    print("\n===============================")
    print("Context Messages")
    print("===============================")
    if context_msgs:
        for idx, m in enumerate(context_msgs, 1):
            ts = m.get("timestamp", None)
            ts_s = ts.strftime("%Y-%m-%d %H:%M") if ts else ""
            print(f"{idx}. [{ts_s}] {m['message']}")
    else:
        print("No previous messages.")

    # Step 4: Wait message before running triage
    print("\nSearching for relevant Docs and FAQs that may have solved similar issues...")
    time.sleep(2)  # simulate wait

    # Step 5: Run triage
    result = triage_ticket(selected_customer_id)

    # Step 6: Print explainable, structured output
    print("\n===============================")
    print("Triage Result")
    print("===============================")
    print(f"Urgency: {result['urgency']}")
    print(f"Issue Type: {result['issue_type']}")
    print(f"Product: {result['product']}")
    print(f"Customer Sentiment: {result['customer_sentiment']}")
    print(f"Next Action: {result['next_action']}")
    print(f"Reasoning: {result['reasoning']}")

    print("\n===============================")
    print("Recommended FAQ")
    print("===============================")
    faq = result["knowledge_base"]["faq"]
    print(f"ID: {faq['id']}")
    print(f"Title: {faq['title']}")
    print(f"Content: {faq['content']}")
    print(f"Relevance: {faq['relevance_score_percent']}%")

    print("\n===============================")
    print("Recommended Document")
    print("===============================")
    doc = result["knowledge_base"]["doc"]
    print(f"ID: {doc['id']}")
    print(f"Title: {doc['title']}")
    print(f"Content: {doc['content']}")
    print(f"Relevance: {doc['relevance_score_percent']}%")

if __name__ == "__main__":
    main()
