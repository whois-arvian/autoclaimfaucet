import requests
import schedule
import time

# Daftar address yang akan diklaim
addresses = [
    "0x2Ae8985D9c26F0117994A0f1451FeBAc6B8F7C51",
    "0xdCBE27b400061aA390bAE364D5D7Eb405F515aE5",
    "0x1D0ea7ece412880FE94C8B3BCd7342054C79a033",
    "0x8538BBAF6d262AC520AF853236cBaD496233E48B",
]

FAUCET_URL = "https://faucet-test.haust.network/api/claim"

def claim_faucet(address):
    """Mengklaim faucet untuk satu address"""
    payload = {"address": address}
    try:
        response = requests.post(FAUCET_URL, json=payload)
        if response.status_code == 200:
            print(f"[SUCCESS] {address} claimed successfully!", response.json())
        elif response.status_code == 429:
            print(f"[WARNING] {address} Rate limit exceeded. Try again later.")
        else:
            print(f"[ERROR] {address} Unexpected response: {response.status_code}", response.text)
    except Exception as e:
        print(f"[ERROR] {address} An error occurred: {e}")

def claim_all_addresses():
    """Loop semua address dan klaim faucet"""
    print("\n[INFO] Running faucet claim process...")
    for address in addresses:
        claim_faucet(address)
        time.sleep(5)  # Delay antar request untuk menghindari limit API
    print("[INFO] Faucet claim process completed.")

# Jalankan setiap 2 jam
schedule.every(2).hours.do(claim_all_addresses)

print("Scheduler started. Running every 2 hours...")
while True:
    schedule.run_pending()
    time.sleep(60)  # Mengecek setiap 1 menit
