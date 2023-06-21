

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return self.data

    def __str__(self):
        return str(self.data)

def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)

node1 = Node(1)
head = node1

for i in range(2, 10):
    add(i)

node = head

def serchNode(n):
    print(n.data)
    while n.next:
        n = n.next
        print(n.data)

node3 = Node(1.5)
# serchNode(node)

# 1. 데이터 사이에 데이터 추가
def addNode(originNode, targetData, targetNode):
    search = True
    while search:
        if originNode.data == targetData:
            search = False
        else:
            originNode = originNode.next
    
    node_next = originNode.next
    originNode.next = targetNode
    targetNode.next = node_next

    return originNode

node = addNode(node, 1, node3)
serchNode(node)





