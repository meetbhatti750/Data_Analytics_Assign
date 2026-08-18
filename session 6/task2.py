playlist_prices = {
    "Chill Vibes": 99,
    "Workout Hits": 149,
    "Party Mix": 199,
    "Romantic Songs": 129,
    "Bollywood Hits": 179
}

def update_playlist_price(playlist, new_price):
    playlist_prices[playlist] = new_price

update_playlist_price("Party Mix", 249)

print(playlist_prices)