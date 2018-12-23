#../CSP/bin/cd spython3
import board

def main():
    try:
        sq = board.board(load = True, name = "test_2.csv")
    except:
        sq = board.board(load = True, name = "src/test_2.csv")
    sq.print()
    sq.toCSP()
    sq.nodeConsistency()
    sq.GeneralArchConsistency()
    print("ehiehi")

if __name__ == "__main__":
    main()