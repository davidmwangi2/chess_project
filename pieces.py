
# pieces.py
import os, pygame

SYMBOL_TO_FILENAME = {
    'P': 'wp.png', 'N': 'wn.png', 'B': 'wb.png',
    'R': 'wr.png', 'Q': 'wq.png', 'K': 'wk.png',
    'p': 'bp.png', 'n': 'bn.png', 'b': 'bb.png',
    'r': 'br.png', 'q': 'bq.png', 'k': 'bk.png',
}

def load_piece_images(square_size: int, base_path="pieces"):
    images = {}
    for sym, fname in SYMBOL_TO_FILENAME.items():
        path = os.path.join(base_path, fname)
        if not os.path.exists(path):
            continue
        img = pygame.image.load(path).convert_alpha()
        img = pygame.transform.smoothscale(img, (square_size, square_size))
        images[sym] = img
    return images

