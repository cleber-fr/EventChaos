import queue
import random
import time
import logging

from infra.worker import Worker
from infra.event_bus import EventBus
from infra.metrics import Metrics

from events.email_event import EmailEvent

logger = logging.getLogger("EmailService")

class EmailService:
    def __init__(self, bus: EventBus, metrics: Metrics):
        self._queue = queue.Queue()
        bus.register(EmailEvent, self._queue)

        Worker(
            "EmailWorker", 
            self._queue, 
            self.handle, 
            bus, 
            metrics
        ).start()

    def handle(self, event: EmailEvent):
        logger.info(f"Sending email to {event.email}")

        time.sleep(random.uniform(1, 3))

        if random.random() < 0.3:
            raise Exception("SMTP failure")

        logger.info(f"Email sent to {event.email}")