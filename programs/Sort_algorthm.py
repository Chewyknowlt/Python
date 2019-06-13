class Sort:
    def __init__(self, array):
        self.array = array
        None
        
    def selection_sort(self):
        array = self.array
        # 1 by 1 move boundary of unsorted list
        for i in range(0, len(array)):
            min_index = i
            for j in range(i, len(array)):
                if (array[j] < array[min_index]):
                    min_index = j

            #Swap the found min element with the
            #shifted first element
            array[min_index], array[i] = array[i], array[min_index]

        for i in array:
            print(i, end=' ')

    def bubble_sort(self):
        array = self.array
        
        #Traverse through all elements in a list
        for i in range(len(array)):

            #n-i-1 <- in this i shifted from right
            # to left
            for j in range(len(array)-i-1):
                #if the element found greater
                #then the adjescent other swap it 
                if (array[j] > array[j+1]):
                    #swapping it
                    array[j], array[j+1] = array[j+1], array[j]
                    
        #Printing list
        for item in array: print(item, end = ' ')
            

            
lst = [64, 25, 12, 22, 11]
s = Sort(lst)
s.bubble_sort()
