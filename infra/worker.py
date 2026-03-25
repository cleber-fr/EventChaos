import threading
import time
import logging

from typing import Any
from queue import Queue

from infra.event_bus import EventBus
from infra.metrics import Metrics

from events.dead_letter_event import DeadLetterEvent

class Worker:
    def __init__(self, name: str, queue: Queue[Any], handler, bus: EventBus, metrics: Metrics, max_retries=3):
        self._name = name
        self._queue = queue
        self._handler = handler
        self._max_retries = max_retries
        self._bus = bus
        self._metrics = metrics
        self._logger = logging.getLogger(name)
        self._processed_events = set()

        self._thread = threading.Thread(target=self.run, daemon=True)

    def start(self):
        self._thread.start()

    def run(self):
        
        while True:
            event = self._queue.get()

            if event.id in self._processed_events:
                self._logger.warning(f"[{event.id}] Duplicate event, skipping")
                self._queue.task_done()
                continue

            attempt = 0

            self._logger.info(f"[{event.id}] Processing {type(event).__name__}")
            
            while attempt < self._max_retries:
                try:
                    self._handler(event)
                    self._metrics.inc_processed(self._name)
                    self._logger.info(f"[{event.id}] Processed successfully")
                    break

                except Exception as e:
                    attempt += 1
                    self._logger.error(f"[{event.id}] Error processing event")

                    if attempt < self._max_retries:
                        backoff = 2 ** attempt
                        self._logger.info(f"[{event.id}] Retrying in {backoff}s")
                        time.sleep(backoff)
                        self._metrics.inc_retry(self._name)

                    else:
                        self._logger.error(f"[{event.id}] Max retries reached, sending to DLQ")
                        self._metrics.inc_failed(self._name)
                        self._bus.publish(DeadLetterEvent(
                            original_event=event,
                            reason=str(e)
                        ))

            self._queue.task_done()