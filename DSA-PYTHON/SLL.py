class Node:

    def __init__(self,data):

        self.data = data
        self.next = None

class sll:

    def __init__(self):

        self.head = None

    def create(self):

        n = int(input('Get me number of nodes:\t'))

        for i in range(n):

            data = int(input(f'Get me the Node {i+1} data:\t'))

            new = Node(data)

            if self.head is None:

                self.head = new

            else:

                temp = self.head

                while temp.next:

                    temp = temp.next

                temp.next = new


    def insertBegin(self):

        data = int(input('Get the data to be inserted:\t'))

        new = Node(data)

        new.next = self.head

        self.head = new


    def insertLast(self):

        data = int(input('Get me the element to be inserted at last:\t'))

        new = Node(data)

        if self.head is None:

            self.head = new


        else:

            temp = self.head

            while temp.next:

                temp = temp.next

            temp.next = new


    def count(self):

        c=0

        if self.head is None:

            print('There is no linked list.....')
            return False

        else:

            temp = self.head

            while temp.next:

                c+=1
                temp = temp.next

            print(f'The total number of nodes are {c}')
            return c



    def insertAt(self):

        index=int(input('Get me the area where to get inserted:\t'))

        if index==0:

            return self.insertBegin()

        elif index<0 or index>self.count():

            print('Invalid location to Insert.....')
            return False

        else:

            data = int(input('Get me the value to get inserted:\t'))

            new = Node(data)

            temp = self.head

            for i in range(index-1):

                temp = self.head

                for i in range(index-1):

                    temp = temp.next

                new.next = temp.next

                temp.next = new


    def deleteBegin(self):

        if self.head is None:

            print('No data to get deleted')

        else:

            temp = self.head

            self.head = temp.next

            print(f'The data got deleted is:\t{temp.data}')


    def deleteLast(self):

        if self.head is None:

            print('No Data to get deleted')

        else:

            temp = self.head

            temp1 = temp

            while temp.next:

                temp1= temp
                temp = temp.next

            temp1.next = None


    def deleteAt(self):

        if self.head is None:

            print('No data to get deleted')

        else:

            data = int(input('Get me the Value to Get deleted:\t'))

            temp = self.head

            # If first node contains the value
            if temp.data == data:

                self.head = temp.next

                print('Data got deleted')

                return

        # Search for the node before the node to delete
        while temp.next and temp.next.data != data:

            temp = temp.next

        # Value not found
        if temp.next is None:

            print('Value not detected')

        else:

            temp.next = temp.next.next

            print('Value Got deleted....')

    def display(self):

        if self.head is None:

            print('No data to display')

        else:

            temp = self.head

            while temp:

                print(f'{temp.data}',end='->')
                temp = temp.next

            print('None')



s = sll()

while True:

    print('\n--------- SINGLY LINKED LIST ---------')
    print('1. Create Linked List')
    print('2. Insert at Beginning')
    print('3. Insert at Last')
    print('4. Insert at Index')
    print('5. Delete First Node')
    print('6. Delete Last Node')
    print('7. Delete by Value')
    print('8. Count Number of Nodes')
    print('9. Display / Traverse')
    print('10. Exit')

    ch = int(input('Get me your choice:\t'))

    if ch == 1:

        s.create()

    elif ch == 2:

        s.insertBegin()

    elif ch == 3:

        s.insertLast()

    elif ch == 4:

        s.insertAt()

    elif ch == 5:

        s.deleteBegin()

    elif ch == 6:

        s.deleteLast()

    elif ch == 7:

        s.deleteAt()

    elif ch == 8:

        s.count()

    elif ch == 9:

        s.display()

    elif ch == 10:

        print('Program terminated.....')
        break

    else:

        print('Invalid choice.....')
