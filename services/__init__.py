from services.message_service import MessageService
from services.email_service import EmailService
from services.payment_service import PaymentService
from services.notification_service import NotificationService
from services.dead_letter_service import DeadLetterService


def load_services(bus, metrics):
    MessageService(bus, metrics)
    EmailService(bus, metrics)
    PaymentService(bus, metrics)
    NotificationService(bus, metrics)
    DeadLetterService(bus, metrics)