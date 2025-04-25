import random

print("🎵 Music Recommender🎵")

genres = {
    "rock": ["AC/DC", "Queen", "Led Zeppelin"],
    "pop": ["Michael Jackson", "Ed Sheeran", "Ariana Grande"],
    "hip-hop": ["Drake", "Travis Scott", "J-Cole"]
}

choice = input("What genre do you like (rock, pop, hip-hop): ")

if choice not in genres:
    print("😥 Sorry, I don;t know that genre.")
else:
    print(f"Check out {random.choice(genres[choice])}")
