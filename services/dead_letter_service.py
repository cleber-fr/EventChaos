import queue
import logging

from infra.worker import Worker
from infra.event_bus import EventBus
from infra.metrics import Metrics

from events.dead_letter_event import DeadLetterEvent

logger = logging.getLogger("DeadLetterService")

class DeadLetterService:
    def __init__(self, bus: EventBus, metrics: Metrics):
        self._queue = queue.Queue()
        bus.register(DeadLetterEvent, self._queue)

        Worker(
            "DeadLetterWorker",
            self._queue,
            self.handle,
            bus,
            metrics
        ).start()

    def handle(self, event: DeadLetterEvent):
        logger.error(
            f"[FAILURE] Event [{event.original_event.id}] reason: {event.reason}"
        )