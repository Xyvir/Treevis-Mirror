import chess.polyglot
import os

BOOK_PATH = 'Blitz.bin'

def check_book():
    if not os.path.exists(BOOK_PATH):
        print(f"Error: {BOOK_PATH} not found.")
        return

    print(f"Checking {BOOK_PATH} (Size: {os.path.getsize(BOOK_PATH) / (1024*1024):.2f} MB)...")
    
    try:
        with chess.polyglot.open_reader(BOOK_PATH) as reader:
            # Check starting position
            board = chess.Board()
            entries = list(reader.find_all(board))
            
            if entries:
                print("Success! This is a valid Polyglot opening book.")
                print(f"Found {len(entries)} moves for the starting position:")
                for entry in entries:
                    print(f" - {board.san(entry.move)} (Weight: {entry.weight})")
                return True
            else:
                print("Warning: Polyglot reader opened the file, but found no moves for the starting position.")
                print("This might be a different format or a very specialized book.")
                return False
    except Exception as e:
        print(f"Error: Failed to read as Polyglot book. {e}")
        return False

if __name__ == "__main__":
    check_book()
