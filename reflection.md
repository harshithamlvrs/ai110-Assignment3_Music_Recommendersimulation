# Reflection: Pairwise Profile Comparison

## Profiles Used
- Profile 1: {"genre": "pop", "mood": "happy", "energy": 0.8}
- Profile 2: {"genre": "lofi", "mood": "chill", "energy": 0.3}
- Profile 3: {"genre": "rock", "mood": "intense", "energy": 0.9}

## Pair 1: Profile 1 vs Profile 2
The top songs shifted from upbeat/high-energy songs (for example, "Sunrise City") to calm/low-energy tracks (for example, "Library Rain" and "Midnight Coding"). This makes sense because Profile 2 asks for both a lower energy target (0.3 instead of 0.8) and different categorical preferences (lofi + chill instead of pop + happy), so both the match bonuses and energy similarity favor different songs.

## Pair 2: Profile 1 vs Profile 3
Both profiles keep relatively high-energy songs near the top, but Profile 3 pushes intense tracks higher (for example, "Storm Runner" and "Gym Hero") while Profile 1 favors happy/pop tracks ("Sunrise City"). This makes sense because the energy targets are close (0.8 vs 0.9), so the main difference comes from genre and mood bonuses.

## Pair 3: Profile 2 vs Profile 3
The ranking flips from low-energy chill songs to high-energy intense songs. Profile 2 prioritizes lofi/chill songs near energy 0.3, while Profile 3 prioritizes rock/intense songs near energy 0.9. This makes sense because these profiles differ on all three scoring dimensions at once (genre, mood, and energy), so they produce the most different recommendation lists.
