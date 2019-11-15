import chess
import chess.engine
import time


engine = chess.engine.SimpleEngine.popen_uci(r"C:\Users\He.Wang\rnd\stockfish-10-win\Windows\stockfish_10_x64_bmi2.exe")

def move(fen_str,move_steps=20):
    global engine
    MAXSTEPS = 20
    start=time.time()
    if move_steps+5 >= MAXSTEPS:
        depth = MAXSTEPS
    else:
        depth = move_steps+5
    board = chess.Board(fen_str)
    result = engine.play(board, chess.engine.Limit(depth=depth))
    duration = time.time() - start
    print(result.move)
    return str(result.move) +" "+ str(round(duration,3))

if __name__ == "__main__":
    print(move ("r1b1k3/pppp3p/8/8/2P5/8/PP5P/RNBQK2R w KQkq - 0 1", 15))