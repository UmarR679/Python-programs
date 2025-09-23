class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def Insert_at_begin(self, data):
        print()
        new = Node(data)
        new.next = self.head
        self.head = new

    def Insert_at_end(self, data):
        print()
        new = Node(data)
        if self.head is None:
            self.head = new
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new

    def Insert_at_specific(self, data, pos):
        print()
        new2 = Node(data)
        temp = self.head
        for i in range(1, pos-1):
            temp = temp.next
        new2.next = temp.next
        temp.next = new2

    def deletion_at_begin(self):
        print()
        temp=self.head
        self.head=temp.next
        temp.next=None

    def deletion_at_end(self):
        print()
        prev=self.head
        temp=self.head.next
        while temp.next!=None:
            temp=temp.next
            prev=prev.next
        prev.next=None

    def deletion_at_particular(self,pos):
        print()
        prev=self.head
        temp=self.head.next
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None

    def traversal(self):
        if self.head is None:
            print("Linked Lis is empty")
        else:
            temp = self.head
            while temp != None:
                print(temp.data, end="->")
                temp = temp.next

    def sum_all(self):
        s=0
        temp=self.head
        while temp!=None:
            s=s+temp.data
            temp=temp.next
        print(s)

    def count_all(self):
        c=0
        temp=self.head
        while temp!=None:
            c=c+1

    def sum_even_nodes(self):
        t=self.head
        s=0
        pos=1
        while(t!=None):
            if(pos%2==0):
                s=s+t.data
            t=t.next
            pos=pos+1
        print(s)


n1 = Node(5)
sll = SLL()
sll.head = n1
n2 = Node(10)
n1.next = n2
n3 = Node(15)
n2.next = n3

sll.traversal()
sll.Insert_at_begin(2)
sll.traversal()
sll.Insert_at_end(20)
sll.traversal()
sll.Insert_at_specific(8,3)
sll.traversal()