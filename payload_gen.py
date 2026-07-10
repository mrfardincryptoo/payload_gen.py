import time

# Structure a mock raw transaction object for secure cold-storage signing
def create_raw_transaction_payload(nonce, to_address, value_eth, chain_id=8453):
    return {
        "chainId": chain_id,
        "nonce": nonce,
        "to": to_address,
        "value": int(value_eth * 10**18),
        "timestamp": int(time.time())
    }

raw_tx = create_raw_transaction_payload(nonce=4, to_address="0x742d35Cc6634C0532925a3b844Bc454e4438f44e", value_eth=0.05)
print("Structured Transaction Payload:")
for key, val in raw_tx.items():
    print(f"  {key}: {val}")
