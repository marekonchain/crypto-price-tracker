from solana.rpc.api import Client

# Connect to Solana mainnet RPC
solana_client = Client("https://api.mainnet-beta.solana.com")

# Get recent block details
block = solana_client.get_recent_blockhash()

# Extract fee per signature (lamports)
fee_per_sig = block['result']['value']['feeCalculator']['lamportsPerSignature']

# Convert lamports → SOL
fee_in_sol = fee_per_sig / 1_000_000_000

print("Solana Gas Fee per transaction:")
print(f"{fee_per_sig} lamports (~{fee_in_sol:.9f} SOL)")
