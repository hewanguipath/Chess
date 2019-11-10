import chess
import chess.engine
import time

start=time.time()
engine = chess.engine.SimpleEngine.popen_uci(r"C:\Program Files (x86)\LucasChess\Engines\Windows\stockfish\Windows\stockfish_10_x64_bmi2.exe")
gap1 = time.time()-start
def move(fen_str):
    global engine
    board = chess.Board(fen_str)
    result = engine.play(board, chess.engine.Limit(time=0.100))
    gap2 = time.time()-start
    print(result.move)
    return str(result.move) +" "+ str(gap1) +" " + str(gap2)

if __name__ == "__main__":
    print(move ("5k2/R7/2p2Pp1/1prp2Kp/p7/7P/6P1/8 w KQkq - 0 1"))