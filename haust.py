import requests
import time
import sys

def claim_faucet(url, payload):
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("[SUCCESS] Faucet claimed successfully!", response.json())
        elif response.status_code == 429:
            print("[WARNING] Too many requests. Please wait.")
        else:
            print(f"[ERROR] Unexpected response: {response.status_code}", response.text)
    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")

def countdown(seconds):
    for remaining in range(seconds, 0, -1):
        sys.stdout.write(f"\rWaiting {remaining} seconds...")
        sys.stdout.flush()
        time.sleep(1)
    print("\rStarting next claim...                ")

if __name__ == "__main__":
    # API endpoint and payload
    faucet_url = "https://faucet-test.haust.network/api/claim"
    payload = {"address": "0x2Ae8985D9c26F0117994A0f1451FeBAc6B8F7C51"}

    # Time interval in seconds (1 minute 5 seconds = 70 seconds)
    interval = 70

    while True:
        print("\nAttempting to claim faucet...")
        claim_faucet(faucet_url, payload)
        countdown(interval)