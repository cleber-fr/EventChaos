from typing import Type, Dict, List
from queue import Queue
from events.base_event import Event
import logging

logger = logging.getLogger("EventBus")

class EventBus:
    def __init__(self):
        self._queues: Dict[Type[Event], List[Queue]] = {}

    def register(self, event_t: Type[Event], q):
        self._queues.setdefault(event_t, []).append(q)

    def publish(self, event: Event):
        event_type = type(event)
        queues = self._queues.get(event_type)

        if not queues:
            logger.error(f"Queue not found for event {type(event).__name__}")
            return
        
        for q in queues:
            q.put(event)