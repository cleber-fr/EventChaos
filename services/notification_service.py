import queue
import random
import time
import logging

from infra.worker import Worker
from infra.event_bus import EventBus
from infra.metrics import Metrics

from events.notification_event import NotificationEvent

logger = logging.getLogger("NotificationService")

class NotificationService:
    def __init__(self, bus: EventBus, metrics: Metrics):
        self._queue = queue.Queue()
        bus.register(NotificationEvent, self._queue)

        Worker(
            "NotificationWorker",
            self._queue, 
            self.handle, 
            bus, 
            metrics
        ).start()

    def handle(self, event: NotificationEvent):
        logger.info(f"Sending notification to user {event.user_id}")

        time.sleep(0.2)

        if random.random() < 0.05:
            raise Exception("Push service down")

        logger.info(f"Notification sent: {event.message}")