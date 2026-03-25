from events.base_event import Event

class PaymentEvent(Event):
    def __init__(self, user_id: int, amount: float):
        super().__init__()
        self.user_id = user_id
        self.amount = amount