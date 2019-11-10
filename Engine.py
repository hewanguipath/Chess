import chess
import chess.engine
import time

start=time.time()
engine = chess.engine.SimpleEngine.popen_uci(r"C:\Users\He.Wang\rnd\stockfish-10-win\Windows\stockfish_10_x64_bmi2.exe")
gap1 = time.time()-start
def move(fen_str):
    global engine
    board = chess.Board(fen_str)
    result = engine.play(board, chess.engine.Limit(depth=15))
    gap2 = time.time()-start
    print(result.move)
    return str(result.move) +" "+ str(round(gap1,3)) +" " + str(round(gap2,3))

if __name__ == "__main__":
    print(move ("r1b1k3/pppp3p/8/8/2P5/8/PP5P/RNBQK2R w KQkq - 0 1"))