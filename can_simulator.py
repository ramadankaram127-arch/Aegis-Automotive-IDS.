import time
import random

def generate_can_data():
    """Simulates realistic CAN-Bus data packets."""
    can_ids = [0x123, 0x456, 0x789, 0xABC]
    while True:
        can_id = random.choice(can_ids)
        data = [random.randint(0, 255) for _ in range(8)]
        timestamp = time.strftime("%H:%M:%S")
        print(f"[{timestamp}] CAN_ID: {hex(can_id)} | DATA: {data}")
        time.sleep(0.1)

if __name__ == "__main__":
    print("🛡️ AEGIS Engine: Monitoring CAN-Bus Traffic...")
    try:
        generate_can_data()
    except KeyboardInterrupt:
        print("\nStopping Aegis Engine...")
