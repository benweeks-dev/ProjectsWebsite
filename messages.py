"""View all contact messages. Run: python messages.py"""
from app import create_app
from app.models import ContactMessage

app = create_app()

with app.app_context():
    messages = ContactMessage.query.order_by(ContactMessage.date_sent.desc()).all()

    if not messages:
        print("No messages yet.")
    else:
        print(f"=== {len(messages)} Message(s) ===\n")
        for m in messages:
            status = "" if m.is_read else "[NEW] "
            print(f"{status}From: {m.name} ({m.email})")
            print(f"Subject: {m.subject or '(no subject)'}")
            print(f"Date: {m.date_sent.strftime('%Y-%m-%d %H:%M')}")
            print(f"Message: {m.message}")
            print("-" * 40)
    