from Life import Board

v = Board(30,30)
v.seed([[2,2],[3,3],[3,4],[2,4],[1,4]])
for i in range(0,100):
    Board.Print(v)
    Board.Process(v)
    print('-' * 100)