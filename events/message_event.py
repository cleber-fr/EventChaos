from events.base_event import Event

class MessageEvent(Event):
    def __init__(self, content: str):
        super().__init__()
        self.content = content