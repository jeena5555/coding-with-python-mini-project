def checkmate(rawboard):
    """
    rawboard รับ stringมา เปลี่ยนเป็น list of string
    """

    board = rawboard.splitlines()

    king_pos = find_king(board)
    if not king_pos:
        print("Error")
        return

    if (check_straight_lines(board, king_pos) or
        check_diagonal_lines(board, king_pos) or
        check_pawns(board, king_pos)):
        print("Success")
    elif false:
        print("Error")
    else:
        print("Fail")

def find_king(board):
    board_size = len(board)
    
    for x in range(board_size):
        for y in range(board_size):
            if board[x][y] == 'K':
                return (x, y)
    return None

def check_straight_lines(board, king_pos):
    """
    หาแนวตั้งแนวนอน นับจาก king (หา Rook, Queen)
    """

    k_x, k_y = king_pos
    board_size = len(board)
    # ขวา, ซ้าย, ล่าง, บน
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] 

    for dx, dy in directions:
        # ยึดkingเป็นจุดเริ่มต้น
        x, y = k_x + dx, k_y + dy

        while 0 <= x < board_size and 0 <= y < board_size:
            piece = board[x][y]
            if piece in 'RQ':
                return True
            if piece != '.':
                break
            x, y = x + dx, y + dy

    return False

def check_diagonal_lines(board, king_pos):
    """
    หาแนวทแยงมุม นับจาก king (หา Bishop, Queen)
    """
    k_x, k_y = king_pos
    board_size = len(board)
    # ล่างขวา, ล่างซ้าย, บนขวา, บนซ้าย
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)] 

    for dx, dy in directions:
        x, y = k_x + dx, k_y + dy

        while 0 <= x < board_size and 0 <= y < board_size:
            piece = board[x][y]
            if piece in 'BQ':
                return True
            if piece != '.':
                break
            x, y = x + dx, y + dy

    return False

def check_pawns(board, king_pos):
    """
    หาpawn
    """
    board_size = len(board)
    k_x, k_y = king_pos
    to_check = [(-1, -1), (-1, 1)]

    for dx, dy in to_check:
        x, y = x + dx, y + dy
        if 0 <= x < board_size and 0 <= y < board_size:
            if board[x][y] == 'P':
                return True
    return False
