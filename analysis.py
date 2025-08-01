import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER lexicon if not already downloaded
nltk.download('vader_lexicon')

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Sample reviews about BottleBack product
reviews = [
    "So sweet❤️",
    "It's so gud 😊",
    "So sweet and unique perfume bottles❤️",
    "Love this picture ❤️",
    "Can make it more affordable it will be useful 😢",
    "Perfume is so nice and good 💗",
    "omg 😍😍😍😍",
    "Amazing 😍"
]

# Analyze sentiments
for review in reviews:
    score = sia.polarity_scores(review)
    sentiment = "Positive" if score['compound'] > 0.05 else "Negative" if score['compound'] < -0.05 else "Neutral"
    
    print(f"Review: {review}")
    print(f"Sentiment: {sentiment} | Score: {score}")
    print("-" * 50)
