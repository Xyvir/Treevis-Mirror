import chess
import chess.polyglot
import json
import os

BOOK_PATH = 'Blitz.bin'
OUTPUT_PATH = 'explorer_db.json'
MAX_PLY = 24  # Limit depth to keep JSON size reasonable

def normalize_fen(fen):
    """Normalize FEN to ignore move clocks for indexing."""
    parts = fen.split(' ')
    return ' '.join(parts[:3])

def convert():
    if not os.path.exists(BOOK_PATH):
        print(f"Error: {BOOK_PATH} not found.")
        return

    db = {}
    queue = [(chess.Board(), 0)]
    visited_fens = set()
    
    print(f"Converting {BOOK_PATH} to JSON (Max Ply: {MAX_PLY})...")

    with chess.polyglot.open_reader(BOOK_PATH) as reader:
        while queue:
            board, ply = queue.pop(0)
            if ply > MAX_PLY:
                continue
                
            fen = normalize_fen(board.fen())
            if fen in visited_fens:
                continue
            visited_fens.add(fen)

            entries = list(reader.find_all(board))
            if not entries:
                continue

            # Calculate total weight for normalization
            total_weight = sum(e.weight for e in entries)
            
            db[fen] = {}
            for entry in entries:
                move_san = board.san(entry.move)
                # We don't have real win/loss/draw in Polyglot, 
                # so we use weight as a proxy for frequency.
                # To mimic Lichess UI, we'll store a percentage.
                percentage = (entry.weight / total_weight) * 100 if total_weight > 0 else 0
                db[fen][move_san] = {
                    "count": entry.weight,
                    "white": round(percentage * 0.5), # Dummy distribution
                    "draw": round(percentage * 0.1),
                    "black": round(percentage * 0.4)
                }
                
                # Add next position to queue
                new_board = board.copy()
                new_board.push(entry.move)
                queue.append((new_board, ply + 1))

            if len(visited_fens) % 1000 == 0:
                print(f"Indexed {len(visited_fens)} positions...")

    print(f"Finished. Total positions: {len(visited_fens)}")
    print("Saving JSON...")
    with open(OUTPUT_PATH, 'w') as f:
        json.dump(db, f)
    
    size_mb = os.path.getsize(OUTPUT_PATH) / (1024 * 1024)
    print(f"Success! {OUTPUT_PATH} created ({size_mb:.2f} MB).")

if __name__ == "__main__":
    convert()
