"""
OPC UA Client Data Logger

- Connects to an OPC UA server
- Reads 10 dummy tags at a configurable interval
- Logs data into hourly CSV files
- CSV includes timestamp (24hr), epoch UTC, Tag1–Tag10

Author: Nagapriya N
"""

from opcua import Client
from datetime import datetime
import time
import csv
import os
import argparse

# CLI CONFIG 
parser = argparse.ArgumentParser(description="OPC UA Client Logger")
parser.add_argument(
    "--interval",
    type=int,
    default=60,
    help="Read interval in seconds (default: 60)"
)
args = parser.parse_args()

READ_INTERVAL = args.interval


# STATIC CONFIG 
SERVER_URL = "opc.tcp://localhost:4840"

TAG_NODE_IDS = [
    "ns=2;i=2",
    "ns=2;i=3",
    "ns=2;i=4",
    "ns=2;i=5",
    "ns=2;i=6",
    "ns=2;i=7",
    "ns=2;i=8",
    "ns=2;i=9",
    "ns=2;i=10",
    "ns=2;i=11"
]

OUTPUT_DIR = "sample_output"


os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_csv_filename(current_time):
    return os.path.join(
        OUTPUT_DIR,
        f"OPC_Log_{current_time.strftime('%Y-%m-%d_%H')}.csv"
    )

def write_header_if_new(file_path):
    if not os.path.exists(file_path):
        with open(file_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "Timestamp",
                "Epoch_UTC",
                "Tag1", "Tag2", "Tag3", "Tag4", "Tag5",
                "Tag6", "Tag7", "Tag8", "Tag9", "Tag10"
            ])

client = Client(SERVER_URL)

try:
    client.connect()
    print("Connected to OPC UA Server")

    while True:
        now = datetime.now()
        epoch_time = int(now.timestamp())

        csv_file = get_csv_filename(now)
        write_header_if_new(csv_file)

        values = []
        for node_id in TAG_NODE_IDS:
            node = client.get_node(node_id)
            values.append(node.get_value())

        row = [
            now.strftime("%Y-%m-%d %H:%M:%S"),
            epoch_time
        ] + values

        with open(csv_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(row)

        print(
            f"Logged data at {now.strftime('%Y-%m-%d %H:%M:%S')} "
            f"(interval={READ_INTERVAL}s)"
        )

        time.sleep(READ_INTERVAL)

except KeyboardInterrupt:
    print("\nStopping client...")

finally:
    client.disconnect()
    print("Disconnected from OPC UA Server")
