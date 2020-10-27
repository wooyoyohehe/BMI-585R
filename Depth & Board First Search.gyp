# 图的深度优先遍历
# 1.利用栈实现
# 2.从源节点开始把节点按照深度放入栈，然后弹出
# 3.每弹出一个点，把该节点下一个没有进过栈的邻接点放入栈
# 4.直到栈变空

def DFS(node):
    if not node:
        return 
    stack = []
    nodeSet = set()
    nodeSet.add(node)
    stack.append(node)
    while len(stack) > 0:
        current_node = stack.pop()
        for next in current_node.nexts:
            if next not in nodeSet:
                nodeSet.add(next)
                stack.append(next)
                # Use break to keep DFS
                break

# 图的广度优先遍历
# 1.利用队列实现
# 2.从源节点开始依次按照宽度进队列，然后弹出
# 3.每弹出一个节点，就把该节点所有没有进过队列的邻接点放入队列
# 4.直到队列变空

from queue import Queue
def bfs(node):
    queue = Queue()
    queue.put(node)
    nodeSet = set()
    nodeSet.add(node)
    if node != None:
        while len(queue) != 0:
            for next in queue.get().nexts:
                print next
                if next not in nodeSet:
                    nodeSet.add(next)
                    queue.put(next)



                
