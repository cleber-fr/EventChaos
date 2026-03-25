import queue
import random
import logging

from infra.worker import Worker
from infra.event_bus import EventBus
from infra.metrics import Metrics

from events.message_event import MessageEvent

logger = logging.getLogger("MessageService")

class MessageService:
    def __init__(self, bus: EventBus, metrics: Metrics):
        self._queue = queue.Queue()

        bus.register(MessageEvent, self._queue)

        Worker(
            "MessageWorker",
            self._queue,
            self.handle,
            bus,
            metrics
        ).start()

    def handle(self, event):
        logger.info(f"Processing: {event.content}")

        if random.random() < .5:
            raise Exception(f"Message cannot be delivered")
        
        logger.info(f"Sent: {event.content}")