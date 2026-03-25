from collections import defaultdict
import threading

class Metrics:
    def __init__(self):
        self._lock = threading.Lock()

        self.processed = 0
        self.failed = 0
        self.retries = 0

        self.per_worker = defaultdict(lambda: {
            "processed": 0,
            "failed": 0,
            "retry": 0
        })

    def inc_processed(self, workerName: str):
        with self._lock:
            self.processed += 1
            self.per_worker[workerName]["processed"] += 1

    def inc_failed(self, workerName: str):
        with self._lock:
            self.failed += 1
            self.per_worker[workerName]["failed"] += 1

    def inc_retry(self, workerName: str):
        with self._lock:
            self.retries += 1
            self.per_worker[workerName]["retry"] += 1