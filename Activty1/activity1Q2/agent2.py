from collections import deque

def jugSearch(a,b,c,d):
    
    if d > max(a,b,c):
        return -1
    
    queue = deque([(0,0,0,0)]) # the 3 jugs with steps taken
    
    visitState = [[[False] * (c+1) for _ in range(b+1) ] for _ in range(a+1)]
    visitState[0][0][0] = True
    
    while queue:
        #actions 
        jug1,jug2,jug3,steps = queue.popleft()
        assert 0<=jug1<=a and 0<=jug2<=b and 0<=jug3<=c, (jug1,jug2,jug3)
        #count steps of each jug path
        if jug1 == d or jug2 == d or jug3 == d:
            return steps
        
        #fill jug1,2,3
        
        if not visitState[a][jug2][jug3]:
            visitState[a][jug2][jug3] = True
            queue.append((a,jug2,jug3,steps+1))

        if not visitState[jug1][b][jug3]:
            visitState[jug1][b][jug3] = True
            queue.append((jug1,b,jug3,steps+1))
        
        if not visitState[jug1][jug2][c]:
            visitState[jug1][jug2][c] = True
            queue.append((jug1,jug2,c,steps+1))

        #Empty jug1,2,3

        if not visitState[0][jug2][jug3]:
            visitState[0][jug2][jug3]=True
            queue.append((0,jug2,jug3,steps+1))
            
        if not visitState[jug1][0][jug3]:
            visitState[jug1][0][jug3]=True
            queue.append((jug1,0,jug3,steps+1))
            
        if not visitState[jug2][jug3][0]:
            visitState[jug2][jug3][0]=True
            queue.append((jug1,jug2,0,steps+1))

        #Pourinto jug1,2, or 3
        
        pourJ1J2 = min(jug1,b-jug2)
        pourJ1J3 = min(jug1,c-jug3)
        pourJ2J1 = min(jug2,a-jug1)
        pourJ2J3 = min(jug2,c-jug3)
        pourJ3J1 = min(jug3,a-jug1)
        pourJ3J2 = min(jug3,b-jug2)
        
        if not visitState[jug1 - pourJ1J2][jug2+pourJ1J2][jug3]:
            visitState[jug1 - pourJ1J2][jug2+pourJ1J2][jug3] = True
            queue.append((jug1 - pourJ1J2,jug2+pourJ1J2,jug3, steps + 1))
        
        if not visitState[jug1 - pourJ1J3][jug2][jug3+pourJ1J3]:
            visitState[jug1 - pourJ1J3][jug2][jug3+pourJ1J3] = True
            queue.append((jug1 - pourJ1J3,jug2,jug3+pourJ1J3,steps + 1))
        
        if not visitState[jug1+pourJ2J1][jug2 - pourJ2J1][jug3]:
            visitState[jug1+pourJ2J1][jug2 - pourJ2J1][jug3] = True
            queue.append((jug1 + pourJ2J1,jug2-pourJ2J1,jug3,steps + 1))
        
        if not visitState[jug1][jug2 - pourJ2J3][jug3+pourJ2J3]:
            visitState[jug1][jug2 - pourJ2J3][jug3+pourJ2J3] = True
            queue.append((jug1,jug2 - pourJ2J3,jug3+pourJ2J3,steps + 1))
        
        if not visitState[jug1+pourJ3J1][jug2][jug3 - pourJ3J1]:
            visitState[jug1+pourJ3J1][jug2][jug3 - pourJ3J1] = True
            queue.append((jug1+pourJ3J1,jug2,jug3 - pourJ3J1,steps + 1))
        
        if not visitState[jug1][jug2+pourJ3J2][jug3 - pourJ3J2]:
            visitState[jug1][jug2+pourJ3J2][jug3 - pourJ3J2] = True
            queue.append((jug1,jug2+pourJ3J2,jug3 - pourJ3J2,steps + 1)) 

    return -1


j1 = 13
j2 = 8
j3 = 3
target = 1

print(jugSearch(j1,j2,j3,target))

