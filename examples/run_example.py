import json
from app.triage import triage_ticket

result = triage_ticket("FREE-0001")
print(json.dumps(result, indent=2))
