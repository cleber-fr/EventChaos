import random
import time

from events.message_event import MessageEvent
from events.email_event import EmailEvent
from events.payment_event import PaymentEvent
from events.notification_event import NotificationEvent

def generate_load(bus, duration=10):
    start = time.time()

    while time.time() - start < duration:
        choice = random.choice(["message", "email", "payment", "notification"])
        selected_event = None

        if choice == "message":
            selected_event = MessageEvent("Hello world")

        elif choice == "email":
            selected_event = EmailEvent("placeholder@email.com", "Lorem! lorem. +ipsum##")

        elif choice == "payment":
            selected_event = PaymentEvent(user_id=1, amount=100.0)

        elif choice == "notification":
            selected_event = NotificationEvent(user_id=1, message="Ping!")

        bus.publish(selected_event)

        time.sleep(random.uniform(0.1, 0.5))
        
        if random.random() < 0.2:
            bus.publish(selected_event)
    
    print("Load test finished")