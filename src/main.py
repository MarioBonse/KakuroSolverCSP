#../CSP/bin/cd spython3
import board

def main():
    sq = board.board(6,10)
    sq.print()
    sq.fill()
    #sq.print()
    sq.save()

if __name__ == "__main__":
    main()