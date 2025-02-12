import requests
import schedule
import time
from datetime import datetime

# Daftar address yang akan diklaim
addresses = [
    "0x2Ae8985D9c26F0117994A0f1451FeBAc6B8F7C51",
    "0xdCBE27b400061aA390bAE364D5D7Eb405F515aE5",
    "0x1D0ea7ece412880FE94C8B3BCd7342054C79a033",
    "0x8538BBAF6d262AC520AF853236cBaD496233E48B",
    "0xD6b10b7B50be88d053cb0b9Dad58B5Ab6B9F636C",
    "0x2F9b3803423e3a6c38Bc94F5Ea12Ac75D3eC9266",
    "0xdB6b1A9c14D05947Ff6F6be6958AdE8C19061A5c",
]

FAUCET_URL = "https://faucet.haust.app/api/claim"

HEADERS = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,en;q=0.5",
    "Cache-Control": "no-cache",
    "Content-Type": "application/json",
    "Origin": "https://faucet.haust.app",
    "Pragma": "no-cache",
    "Referer": "https://faucet.haust.app/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
}

def claim_faucet(address):
    """Mengklaim faucet untuk satu address"""
    payload = {"address": address}
    try:
        response = requests.post(FAUCET_URL, json=payload, headers=HEADERS)
        if response.status_code == 200:
            print(f"[{datetime.now()}] [SUCCESS] {address} claimed successfully!", response.json())
        elif response.status_code == 429:
            print(f"[{datetime.now()}] [WARNING] {address} Rate limit exceeded. Try again later.")
        else:
            print(f"[{datetime.now()}] [ERROR] {address} Unexpected response: {response.status_code}", response.text)
    except Exception as e:
        print(f"[{datetime.now()}] [ERROR] {address} An error occurred: {e}")

def claim_all_addresses():
    """Loop semua address dan klaim faucet"""
    print(f"\n[{datetime.now()}] [INFO] Running faucet claim process...")
    for address in addresses:
        claim_faucet(address)
        time.sleep(5)  # Delay antar request untuk menghindari limit API
    print(f"[{datetime.now()}] [INFO] Faucet claim process completed.")

# Jalankan setiap 15 menit
schedule.every(15).minutes.do(claim_all_addresses)

print("Scheduler started. Running every 15 minutes...")
while True:
    try:
        schedule.run_pending()
    except Exception as e:
        print(f"[{datetime.now()}] [ERROR] Scheduler encountered an error: {e}")
    time.sleep(60)  # Mengecek setiap 1 menit
