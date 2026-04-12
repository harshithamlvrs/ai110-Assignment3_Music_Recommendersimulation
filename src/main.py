"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print("loaded songs:", len(songs))

    # 3 distinct user preference dictionaries (e.g., "High-Energy Pop," "Chill Lofi," "Deep Intense Rock").
    user_pref1 = {"genre": "pop", "mood": "happy", "energy": 0.8}
    user_pref2 = {"genre": "lofi", "mood": "chill", "energy": 0.3}
    user_pref3 = {"genre": "rock", "mood": "intense", "energy": 0.9}
    user_prefs = [user_pref1, user_pref2, user_pref3]
    edge_case_profiles = [
        {"name": "Conflicting preferences", "prefs": {"genre": "rock", "mood": "chill", "energy": 0.95}},
        {"name": "Unknown labels", "prefs": {"genre": "screamo", "mood": "melancholy", "energy": 0.5}},
        {"name": "Boundary energy low", "prefs": {"genre": "pop", "mood": "happy", "energy": 0.0}},
        {"name": "Boundary energy high", "prefs": {"genre": "pop", "mood": "happy", "energy": 1.0}},
        {"name": "Missing preferences", "prefs": {"genre": "", "mood": "", "energy": 0.5}},
        {"name": "Overly broad taste", "prefs": {"genre": "", "mood": "", "energy": 0.98}},
        {"name": "Opposite vibe", "prefs": {"genre": "metal", "mood": "peaceful", "energy": 0.2}},
    ]

    print("\n" + "=" * 70)
    print("TOP RECOMMENDATIONS")
    print("=" * 70 + "\n")

    for index, user_prefs in enumerate(user_prefs, 1):
        print(f"Profile {index}: {user_prefs}")
        recommendations = recommend_songs(user_prefs, songs, k=5)

        for i, rec in enumerate(recommendations, 1):
            song, score, explanation = rec
            print(f"  {i}. {song['title']}")
            print(f"     Score: {score:.2f}")
            print(f"     Reasons: {explanation}")

        print()

    print("\n" + "=" * 70)
    print("EDGE CASE RECOMMENDATION CHECKS")
    print("=" * 70 + "\n")

    for profile in edge_case_profiles:
        print(f"Profile: {profile['name']}")
        print(f"Preferences: {profile['prefs']}")
        recommendations = recommend_songs(profile["prefs"], songs, k=3)

        for i, rec in enumerate(recommendations, 1):
            song, score, explanation = rec
            print(f"  {i}. {song['title']}")
            print(f"     Score: {score:.2f}")
            print(f"     Reasons: {explanation}")

        print()


if __name__ == "__main__":
    main()
