import requests
import time
import sys

def claim_faucet(url, payload, headers):
    try:
        response = requests.post(url, json=payload, headers=headers)
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
    # API endpoint
    faucet_url = "https://faucet.testnet.mangonetwork.io/gas"

    # Payload
    payload = {
        "FixedAmountRequest": {
            "recipient": "0x9c032312ff372378feed54d41f899aebb37460ff539e418965d3a997bf2a7c9e"
        }
    }

    # Headers
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8,id;q=0.7",
        "cache-control": "no-cache",
        "connection": "keep-alive",
        "content-type": "application/json",
        "host": "faucet.testnet.mangonetwork.io",
        "origin": "chrome-extension://jiiigigdinhhgjflhljdkcelcjfmplnd",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }

    # Time interval in seconds (e.g., 10 seconds)
    interval = 10

    while True:
        print("\nAttempting to claim faucet...")
        claim_faucet(faucet_url, payload, headers)
        countdown(interval)
