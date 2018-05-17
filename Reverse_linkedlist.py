#Reverse a Linked List recursively

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def reverseLL(ls):
    if ls == None:
        return None
    if ls.next == None:
        return ls
    rest = reverseLL(ls.next)
    ls.next.next = ls
    ls.next = None
    return rest


arr = [int(n) for n in input("Enter the elements of the Linked List\n").split(",")]
ls = Node(arr[0])
head  = ls
ls = Node(arr[1])
head.next = ls
for i in range(2,len(arr)):
    ls.next = Node(arr[i])
    ls = ls.next
ls = head
while ls:
    print(ls.data,end="->")
    ls = ls.next
print()


ls = reverseLL(head)

while ls:
    print(ls.data,end="->")
    ls = ls.next
