import threading

from app.application import create_application
from app.producer import generate_load

from infra.dashboard import run_dashboard
from infra.logger import setup_logging

if __name__ == "__main__":
    setup_logging()

    bus, metrics = create_application()

    threading.Thread(
        target=run_dashboard,
        args=(metrics,),
        daemon=True
    ).start()

    generate_load(bus, duration=20)