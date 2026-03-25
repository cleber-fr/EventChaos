from events.base_event import Event

class EmailEvent(Event):
    def __init__(self, email: str, content: str):
        super().__init__()
        self.email = email
        self.content = content