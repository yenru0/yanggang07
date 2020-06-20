print("="*40)
print("그래프: (유향)인접 행렬")
print("="*40)

def show():
    for i in Cs:
        for j in i:
            print(j, end=" ")
        print()
    print()

Cs = [[0 for i in range(5)] for i in range(5)]

show()

Cs[0][1] = 1
Cs[1][4] = 1
Cs[1][3] = 1
show()
print("위 그림은 노드(버텍스): (0,1), (1,4), (1,3)이 연결된 모습 (유향)")
