from collections import deque
 
class Graph:
    def __init__(self, graph):
        self.graph = graph
 
    def getNeighbors(self, v):
        return self.graph[v]
 
   
    def AStarAlgorithm(self, startNode, endNode):
        
        openSet = set([startNode])
        closeSet = set([])
 
        distanceFromParent = {}
        distanceFromParent[startNode] = 0
 
        parent = {}
        parent[startNode] = startNode
 
        while len(openSet) > 0:
            n = None
            #duyệt danh sách trong open list để tìm ra node có đường đi tới đích ngắn nhất: 
            for v in openSet:
                if n == None or distanceFromParent[v] + self.h(v) < distanceFromParent[n] + self.h(n):
                    n = v;
 
          
            #nếu  bằng vị trí kết thúc: 
            if n == endNode:
                value = distanceFromParent[n] + self.h(n)
                
                reconst_path = []
                
                while parent[n] != n:
                    reconst_path.append(n) 
                    n = parent[n]

                reconst_path.append(startNode)
                reconst_path.reverse()

                print('Chi phí của đường đi-f(x) là : {}'.format(value))
                print('Đường đi theo giải thuật A*: ',end=' ')
                for index in range(len(reconst_path)): 
                    if(index != len(reconst_path)-1): 
                        print(reconst_path[index]+'->',end=' ')
                    else: 
                        print(reconst_path[index])

                return reconst_path
 
           #cập nhật lại trang thái cho các node liền kề: 
            for (m, cost) in self.getNeighbors(n):
              
                if m not in openSet and m not in closeSet:
                    openSet.add(m)
                    parent[m] = n
                    distanceFromParent[m] = distanceFromParent[n] + cost
 
                
                else:
                    if distanceFromParent[m] > distanceFromParent[n] + cost:
                        distanceFromParent[m] = distanceFromParent[n] + cost
                        parent[m] = n
 
                        if m in closeSet:
                            closeSet.remove(m)
                            openSet.add(m)
 
            
            openSet.remove(n)
            closeSet.add(n)
 
        print('Không tồn tại đường đi từ '+startNode+' đến '+endNode)
        return None
 # Bài toán 1: tìm đường đi từ A đến B: minh họa bằng hình graph1.png
    def h(self, n):
        H = {
            'A': 14,
            'B': 0,
            'C': 15,
            'D': 6,
            'E': 8,
            'F': 7,
            'G': 12,
            'H': 10,
            'K': 2,
            'I': 4
        }
 
        return H[n]

   
graph = {
    'A': [('C', 9), ('D', 7),('E',13),('F',20)],
    'C': [('H', 6)],
    'D': [('E', 4),('H',8)],
    'E': [('I', 3),('K',4)],
    'F': [('G', 4),('I',6)],
    'H': [('K', 5)],
    'I': [('B', 5)],
    'K': [('B', 6)],
    }     


#bài toán 2: tìm đường đi  từ A đến K trên đồ thị vô hướng: minh họa bằng hình graph2.png
#     def h(self, n):
#         H = {
#             'A': 33,
#             'B': 35,
#             'C': 43,
#             'D': 36,
#             'E': 28,
#             'F': 13,
#             'G': 17,
#             'H': 10,
#             'K': 0,
#             'I': 24,
#             'J': 19
#         }
 
#         return H[n]
    
# graph = {
#     'A': [('C', 10), ('D', 16),('E',12),('F',20)],
#     'B': [('C', 12),('D',10),('I',11),('G',18)],
#     'C': [('A', 10),('B',12)],
#     'D': [('A', 16),('B',10),('E',8)],
#     'E': [('A', 12),('I',7),('J',9)],
#     'F': [('A', 20),('J',12),('K',13)],
#     'G': [('B',18),('I',8),('J',6),('H',7)],
#     'H': [('K', 10),('F',16),('J',9),('G',7)],
#     'I': [('B', 11),('E',7),('J',5),('G',8)],
#     'J': [('E', 9),('F',12),('H',9),('G',6),('I',5)],
#     'K': [('F', 12),('H',10)]
#     }     


#bài toán thứ 3: tìm đường đi từ A đến F, kết quả không tìm thấy: minh họa bằng hình graph3.png
#     def h(self, n):
#         H = {
#             'A': 6,
#             'B': 3,
#             'C': 8,
#             'D': 10,
#             'E': 5,
#             'F': 4,
#              'G': 0,
#         }
 
#         return H[n]
    
# graph = {
#     'A': [('C', 17), ('D', 14),('B',15)],
#     'B': [('A', 15)],
#     'C': [('A', 17)],
#     'D': [('A', 14)],
#     'E': [('F', 8)],
#     'F': [('E', 8),('G',7)],
#     'G': [('F', 7)]
#     }  

if __name__ == "__main__":
    graph1 = Graph(graph)

    #bài toán thứ nhất trên đồ thị có hướng: 
    graph1.AStarAlgorithm('A', 'B')


    #bài toán thứ hai trên đồ thị vô hướng: 
    # graph1.AStarAlgorithm('A', 'K')

    #bài toán thứ ba trên đồ thị vô hướng-không tìm thấy: 
    # graph1.AStarAlgorithm('A', 'G')