from pycoingecko import CoinGeckoAPI

# Initialize API
cg = CoinGeckoAPI()

# Choose coins to track
coins = ["bitcoin", "ethereum", "solana"]

# Fetch prices in USD
prices = cg.get_price(ids=coins, vs_currencies="usd")

# Print results
for coin in coins:
    print(f"{coin.capitalize()}: ${prices[coin]['usd']}")
