
def parse_input(pos_str):
    files = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    file = pos_str[0].lower()
    rank = int(pos_str[1])
    col = files[file]
    row = 8 - rank
    return (row, col)
