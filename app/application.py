from infra.event_bus import EventBus
from infra.metrics import Metrics
from services import load_services

def create_application() -> tuple[EventBus, Metrics]:
    bus = EventBus()
    metrics = Metrics()

    load_services(bus, metrics)

    return bus, metrics