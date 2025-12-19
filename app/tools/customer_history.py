# tools/customer_history.py

from datetime import datetime, timedelta

# Mock current time
NOW = datetime(2025, 12, 17, 15, 0, 0)  # 17 Dec 2025, 15:00


CUSTOMER_HISTORY_DB = {

    "FREE-0001": {
        "customer_id": "FREE-0001",
        "customer_profile": {
            "plan": "Free",
            "region": None,
            "tenure_months": 4,
            "seat_count": None
        },
        "support_context": {
            "ticket_id": "T-FREE-0001",
            "ticket_status": "open",
            "first_time_contact": True,
            "first_contact_at": NOW - timedelta(hours=3),
            "total_unresolved_hours": 3,
            "customer_follow_up_count": 3
        },
        "conversation_history": {
            "total_messages": 4,
            "messages": [
                {
                    "timestamp": NOW - timedelta(hours=3),
                    "message": "My payment failed when I tried to upgrade to Pro. Can you check what's wrong?"
                },
                {
                    "timestamp": NOW - timedelta(hours=2),
                    "message": "I tried again with a different card. Now I see TWO pending charges but my account still shows Free plan??"
                },
                {
                    "timestamp": NOW - timedelta(hours=1),
                    "message": "Okay this is getting ridiculous. Just checked my bank app - I have THREE charges of $29.99 now. None of them refunded. And I STILL don't have Pro access."
                },
                {
                    "timestamp": NOW,
                    "message": "HELLO?? Is anyone there??? I need this fixed NOW. I have a presentation in 2 hours and I need the Pro export features. If these charges aren't reversed by end of day I'm disputing all of them with my bank."
                }
            ]
        }
    },

    "ENT-0001": {
        "customer_id": "ENT-0001",
        "customer_profile": {
            "plan": "Enterprise",
            "region": "Asia / Thailand",
            "tenure_months": 8,
            "seat_count": 45
        },
        "support_context": {
            "ticket_id": "T-ENT-0001",
            "ticket_status": "open",
            "first_time_contact": True,
            "first_contact_at": NOW - timedelta(hours=2),
            "total_unresolved_hours": 2,
            "customer_follow_up_count": 3
        },
        "conversation_history": {
            "total_messages": 4,
            "messages": [
                {
                    "timestamp": NOW - timedelta(hours=2),
                    "message": "ระบบเข้าไม่ได้ครับ ขึ้น error 500"
                },
                {
                    "timestamp": NOW - timedelta(hours=1, minutes=30),
                    "message": "ลองหลายเครื่องแล้ว ทั้ง Chrome, Safari, Firefox ผลเหมือนกันหมด เพื่อนร่วมงานก็เข้าไม่ได้เหมือนกัน"
                },
                {
                    "timestamp": NOW - timedelta(minutes=45),
                    "message": "ตอนนี้ลูกค้าโวยเข้ามาเยอะมาก เรามี demo กับลูกค้ารายใหญ่บ่ายนี้ ถ้าระบบไม่กลับมา deal นี้อาจจะหลุด"
                },
                {
                    "timestamp": NOW,
                    "message": "เช็ค status.company.com แล้ว บอกว่า all systems operational แต่เราใช้งานไม่ได้จริงๆ ช่วยเช็คให้หน่อยได้ไหมครับ region Asia มีปัญหาหรือเปล่า?"
                }
            ]
        }
    },

    "PRO-0001": {
        "customer_id": "PRO-0001",
        "customer_profile": {
            "plan": "Pro",
            "region": None,
            "tenure_months": 5,
            "seat_count": None
        },
        "support_context": {
            "ticket_id": "T-PRO-0001",
            "ticket_status": "open",
            "first_time_contact": True,
            "first_contact_at": NOW - timedelta(days=2),
            "total_unresolved_hours": 48,
            "customer_follow_up_count": 3
        },
        "conversation_history": {
            "total_messages": 4,
            "messages": [
                {
                    "timestamp": NOW - timedelta(days=2),
                    "message": "Hey, just wondering if you support dark mode? No rush 😊"
                },
                {
                    "timestamp": NOW - timedelta(days=1),
                    "message": "Thanks for the reply! Oh nice, so it's in Settings > Appearance. Found it! But hmm I'm on Pro plan and I only see 'Light' and 'System Default' options. No dark mode toggle?"
                },
                {
                    "timestamp": NOW - timedelta(hours=21),
                    "message": "Okay so I switched to 'System Default' and my Mac is set to dark mode, but your app still shows light theme. Is this a bug or am I missing something?"
                },
                {
                    "timestamp": NOW,
                    "message": "Also random question while I have you - is there a way to schedule dark mode? Like auto-switch at 6pm? Some apps have that. Would be cool if you guys added it 👀"
                }
            ]
        }
    }
}


def get_customer_history(customer_id: str) -> dict:
    """
    Mocked tool: fetch customer history from in-memory database.
    All timestamps are datetime objects.
    """
    return CUSTOMER_HISTORY_DB.get(customer_id, {})
