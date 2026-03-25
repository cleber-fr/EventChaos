import time
import subprocess
import os

def run_dashboard(metrics):
    while True:
        subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

        print("=== SYSTEM DASHBOARD ===\n")

        print(f"Processed: {metrics.processed}")
        print(f"Failed: {metrics.failed}")
        print(f"Retries: {metrics.retries}")

        print("\nPer Worker:")
        for worker, data in metrics.per_worker.items():
            print(
                f"- {worker}: {data["processed"]} processed / {data["failed"]} failed / {data["retry"]} retries"
            )

        time.sleep(2)