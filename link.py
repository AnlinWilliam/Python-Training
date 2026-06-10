class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=new_node
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
    def count1(self):
        temp=self.head
        c=0
        while temp:
            c+=1
            temp=temp.next
        print(c)
    def evensum(self):
        temp=self.head
        s=0
        while temp:
            if temp.data%2==0:
                s+=temp.data
            temp=temp.next
        print(s)
    # def prime(self):
    #     temp=self.head
    #     f=1
    #     while temp:
    #         for i in range(2,temp.data):
    #             if temp.data%i==0:
    #                 f=0
    #             temp=temp.next
    #         if f==1:
    #             print(temp.data,end="->")
    #             temp=temp.next
    #     print("None")
l1=LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)
l1.display()
#count of all elements in the list
l1.count1()
#sum of even nos
l1.evensum()
#print prime nos
# l1.prime()


















