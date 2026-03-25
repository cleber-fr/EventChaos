import queue
import random
import time
import logging

from infra.worker import Worker
from infra.event_bus import EventBus
from infra.metrics import Metrics

from events.payment_event import PaymentEvent

logger = logging.getLogger("PaymentService")

class PaymentService:
    def __init__(self, bus: EventBus, metrics: Metrics):
        self._queue = queue.Queue()
        bus.register(PaymentEvent, self._queue)

        Worker(
            "PaymentWorker", 
            self._queue, 
            self.handle,
            bus, 
            metrics
        ).start()

    def handle(self, event: PaymentEvent):
        logger.info(f"Processing payment for user {event.user_id}")

        time.sleep(1)

        if random.random() < 0.1:
            raise Exception("Payment gateway error")

        logger.info(f"Payment of ${event.amount} processed")