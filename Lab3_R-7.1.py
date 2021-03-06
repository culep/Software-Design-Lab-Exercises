import math

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def secondlastnode(head):
    temp = head

    if (temp == None or temp.next == None):
        return -1

# Traverse the linked list
    while (temp != None):

        if (temp.next.next == None):
            return temp.data

        temp = temp.next


def push(head, new_data):
    new_node = Node(new_data)
    new_node.next = head
    head = new_node
    return head



if __name__ == '__main__':
    head = None

    head = push(head, 272)
    head = push(head, 65)
    head = push(head, 99)
    head = push(head, 21)
    head = push(head, 54)

    print(secondlastnode(head))