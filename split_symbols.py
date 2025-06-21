import os

INPUT_FILE = 'all_symbols.txt'
OUTPUT_DIR = 'symbols'
SYMBOLS_PER_FILE = 500

with open(INPUT_FILE, 'r') as f:
    all_symbols = [line.strip() for line in f.readlines() if line.strip() != '']

os.makedirs(OUTPUT_DIR, exist_ok=True)

for i in range(0, len(all_symbols), SYMBOLS_PER_FILE):
    part = all_symbols[i:i + SYMBOLS_PER_FILE]
    file_index = (i // SYMBOLS_PER_FILE) + 1
    filename = os.path.join(OUTPUT_DIR, f'symbols_{file_index}.txt')

    with open(filename, 'w') as f:
        for symbol in part:
            f.write(symbol + '\n')

    print(f'✅ كتبنا {filename} وفيه {len(part)} سهم')