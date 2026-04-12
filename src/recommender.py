import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool
    likes_danceable: bool = False

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        # 
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and normalize numeric fields."""
    numeric_field_types = {
        "id": int,
        "energy": float,
        "tempo_bpm": float,
        "valence": float,
        "danceability": float,
        "acousticness": float,
    }

    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            normalized_row: Dict = {}
            for key, value in row.items():
                if value is None:
                    normalized_row[key] = value
                    continue

                cleaned_value = value.strip()
                caster = numeric_field_types.get(key)
                if caster is None:
                    normalized_row[key] = cleaned_value
                else:
                    normalized_row[key] = caster(cleaned_value) if cleaned_value != "" else None

            songs.append(normalized_row)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song against user preferences."""
    score = 0.0
    reasons: List[str] = []

    user_genre = str(user_prefs.get("genre", "")).strip().lower()
    user_mood = str(user_prefs.get("mood", "")).strip().lower()
    song_genre = str(song.get("genre", "")).strip().lower()
    song_mood = str(song.get("mood", "")).strip().lower()

    # Phase 2 recipe: reward exact genre and mood matches.
    if user_genre and song_genre == user_genre:
        score += 1.0
        reasons.append("genre matches your preference")

    if user_mood and song_mood == user_mood:
        score += 1.0
        reasons.append("mood matches your preference")

    # Phase 2 recipe: add energy similarity points.
    target_energy = float(user_prefs.get("energy", 0.5))
    song_energy = float(song.get("energy", 0.5))
    energy_similarity = max(0.0, 1.0 - abs(song_energy - target_energy))
    score += 2.0 * energy_similarity
    reasons.append(f"energy similarity: {energy_similarity:.2f}")

    return (score, reasons)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top-k scored songs and their explanations."""
    if k <= 0:
        return []

    scored_songs = [
        (song, *score_song(user_prefs, song))
        for song in songs
    ]

    #original data is not changed
    ranked = sorted(scored_songs, key=lambda item: item[1], reverse=True)

    top_k: List[Tuple[Dict, float, str]] = [
        (song, score, "; ".join(reasons))
        for song, score, reasons in ranked[:k]
    ]
    return top_k
