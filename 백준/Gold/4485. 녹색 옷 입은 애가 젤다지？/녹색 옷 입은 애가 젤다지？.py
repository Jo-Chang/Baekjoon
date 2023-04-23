# 4485. 녹색 옷 입은 애가 젤다지?

import sys
import heapq

test_case = 0
DELTA = [(0, 1), (0, -1), (1, 0), (-1, 0)]
VISITED = -1

while True:
    test_case += 1
    N = int(sys.stdin.readline())
    if N == 0:
        break
    
    map_ = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    cost = [[int(1e9)] * N for _ in range(N)]

    q = []
    heapq.heappush(q, (map_[0][0], 0, 0))
    
    while q:
        cur_cost, y, x = heapq.heappop(q)
        
        if y == N-1 and x == N-1:
            answer = cur_cost
            break
        
        for dy, dx in DELTA:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < N and 0 <= nx < N):
                continue
            new_cost =  map_[ny][nx] + cur_cost
            if map_[ny][nx] != VISITED and cost[ny][nx] > new_cost:
                cost[ny][nx] = new_cost
                heapq.heappush(q, (new_cost, ny, nx))
        # for dy, dx in DELTA:
        #     new_pos = (cur_pos[0]+dy, cur_pos[1]+dx)
        #     if not (0 <= new_pos[0] < N and 0 <= new_pos[1] < N):
        #         continue
        #     new_cost =  map_[new_pos[0]][new_pos[1]] + cur_cost
        #     if map_[new_pos[0]][new_pos[1]] != VISITED and cost[new_pos[0]][new_pos[1]] > new_cost:
        #         cost[new_pos[0]][new_pos[1]] = new_cost
        #         heapq.heappush(q, (new_cost, new_pos))

    print(f'Problem {test_case}: {answer}')