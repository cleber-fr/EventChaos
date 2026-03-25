from events.base_event import Event

class NotificationEvent(Event):
    def __init__(self, user_id: int, message: str):
        super().__init__()
        self.user_id = user_id
        self.message = message