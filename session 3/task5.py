ratings = ['4.5','3.0','5','4.2']

float_ratings = [float(rating) for rating in ratings]

highest_rating = max(float_ratings)
print("Highest ratng:",highest_rating)