from events.base_event import Event

class DeadLetterEvent(Event):
    def __init__(self, original_event: Event , reason: str):
        super().__init__()
        self.original_event = original_event
        self.reason = reason

        