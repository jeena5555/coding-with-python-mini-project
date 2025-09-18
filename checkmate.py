def checkmate(board: str):
    rows = [r.strip() for r in board.strip().splitlines() if r.strip()]
    n = len(rows)
    board = [list(r) for r in rows]

    # Find king
    king_pos = None
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        print("Error: No King found.")
        return

    kx, ky = king_pos

    def in_bounds(x, y):
        return 0 <= x < n and 0 <= y < n

    rook_dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    bishop_dirs = [(1,1), (1,-1), (-1,1), (-1,-1)]
    knight_moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
    pawn_moves = [(1,-1),(1,1)]  # pawns go downwards

    # Rook & Queen
    for dx, dy in rook_dirs:
        x, y = kx+dx, ky+dy
        while in_bounds(x,y):
            if board[x][y] != '.':
                if board[x][y] in ('R','Q'):
                    print("Success")
                    return
                break
            x += dx
            y += dy

    # Bishop & Queen
    for dx, dy in bishop_dirs:
        x, y = kx+dx, ky+dy
        while in_bounds(x,y):
            if board[x][y] != '.':
                if board[x][y] in ('B','Q'):
                    print("Success")
                    return
                break
            x += dx
            y += dy

    # Knights
    for dx, dy in knight_moves:
        x, y = kx+dx, ky+dy
        if in_bounds(x,y) and board[x][y] == 'N':
            print("Success")
            return

    # Pawns
    for dx, dy in pawn_moves:
        x, y = kx+dx, ky+dy
        if in_bounds(x,y) and board[x][y] == 'P':
            print("Success")
            return

    print("Fail")
