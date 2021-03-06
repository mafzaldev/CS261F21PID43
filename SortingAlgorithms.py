import math
from typing import List
from abc import ABC, abstractmethod

class Sort(ABC):
    @abstractmethod
    def perform_sorting(self, array: List, column):
        pass

class MergeSort(Sort):
    def perform_sorting(self, array: List, column):
        print("MERGE")
        self.merge_sort(array, 0, len(array)-1, column)

    def merge(self, A, start, mid, end, column):
        index1 = mid - start + 1
        index2 = end - mid
        
        left = []
        right= []
        
        for i in range(0,index1):
            left.append(A[start + i])
        for j in range(0,index2):
            right.append(A[mid + j + 1])
        
        left.append(math.inf)
        right.append(math.inf)
        
        i = 0
        j = 0
        
        for k  in range(start, end+1):
            if left[i] != math.inf and right[j] != math.inf and left[i].all_attributes[column] <= right[j].all_attributes[column]:
                A[k] = left[i]
                i += 1
            elif right[j] != math.inf:
                A[k] = right[j]
                j += 1
            elif right[j] == math.inf and left[i] != math.inf:
                A[k] = left[i]
                i += 1

    def merge_sort(self, A, start, end, column):
        if start < end:
            mid = int((start + end)/2)
            self.merge_sort(A, start, mid, column)
            self.merge_sort(A, mid+1, end, column)
            self.merge(A, start, mid, end, column)

class InsertionSort(Sort):
    def perform_sorting(self, array: List, column):
        print("INSERTION")
        for idx in range(1,len(array)):
            key = array[idx]
            i = idx-1
            while i >= 0 and array[i].all_attributes[column] > key.all_attributes[column]:
                array[i+1] = array[i]
                i = i - 1
            array[i+1] = key

class SelectionSort(Sort):
    def perform_sorting(self, array: List, column):
        print("SELECTION")
        for outer in range(0, len(array)):
            min = outer
            for inner in range(outer+1, len(array)):
                if array[inner].all_attributes[column] < array[min].all_attributes[column]:
                        min= inner
            
            temp = array[outer]
            array[outer] = array[min]
            array[min] = temp
        return array

class BubbleSort(Sort):
     def perform_sorting(self, array: List, column):
        print("BUBBLE")
        n = len(array)
        for outer in range(0,n):
            for inner in range(0,n-outer-1):
                if(array[inner].all_attributes[column] > array[inner + 1].all_attributes[column]):
                    temp = array[inner]
                    array[inner] = array[inner+1]
                    array[inner+1] = temp
        return array

class QuickSort(Sort):
    def perform_sorting(self, array: List, column):
        print("QUICK")
        return self.quickSort(array, 0, len(array)-1, column)

    def Partition(self, array, low, high, column):
        pivot = array[high]
        i = low - 1
        for idx in range(low, high):
            if array[idx].all_attributes[column] < pivot.all_attributes[column]:
                i+=1
                temp = array[i]
                array[i] = array[idx]
                array[idx] = temp
        
        temp = array[i+1]
        array[i+1] = array[high]
        array[high] = temp
        return i+1

    def quickSort(self, array, low, high, column):
        if low < high:
            pivot = self.Partition(array, low, high, column)
            self.quickSort(array, low, pivot - 1, column)
            self.quickSort(array, pivot + 1, high, column)

class BucketSort(Sort):
    def perform_sorting(self, array: List):
        bucket = []
        for idx in range(0,10):
            bucket.append([])
        
        for element in array:
            index = math.floor(element*10)
            bucket[index].append(element)
            
        
        for bucketIDX in range(0 , len(bucket)):
            bucket[bucketIDX] = InsertionSort.insertion_sort(bucket[bucketIDX])
        
        original_idx = 0
        for bucketidx in range(0 , len(bucket)):
            for idx in range(0 , len(bucket[bucketidx])):
                array[original_idx] = bucket[bucketidx][idx]
                original_idx += 1
            
        return array

class CountingSort(Sort):
    
    def perform_sorting(self, array: List, column):
        print("COUNTING")
        return self.countingSort(array, column)

    def countingSort(self, array: List, column):
        max_var =  max(array).all_attributes[column]
        min_var =  min(array).all_attributes[column]
        key = (max_var - min_var) + 1
        
        counts = []
        output = []
        
        for idx in range(0 , key):
            counts.append(0)
            
        for i in range(0 ,  len(array)):
            output.append(0)
        
        for j in range(0 , len(array)):
            k = self.find_key(array[j].all_attributes[column] , min_var) 
            counts[k] += 1
        
        for a in range(1 , key):
            counts[a] += counts[a-1]
        
        for i in range(len(array) - 1, -1, -1):
            j = self.find_key(array[i].all_attributes[column] , min_var) 
            counts[j] -= 1
            output[counts[j]] = array[i]
    
    def find_key(self, element, min):
        key = (min * -1) + element
        return key

class GnomeSort(Sort):
    def perform_sorting(self, array: List, column):
        print("GNOME")
        n = len(array)
        idx = 0
        while idx < n:
            if idx == 0:
                idx +=1
            elif array[idx].all_attributes[column] >= array[idx-1].all_attributes[column]:
                idx +=1
            else:
                array[idx] , array[idx - 1] = array[idx- 1] , array[idx]
                idx -=1
        print("GNOME")


class ShellSort(Sort):
    def perform_sorting(self, array: List, column):
        print("SHELL")
        gap = int(len(array)/2)
        while gap > 0:
            i = 0
            inner = gap
            while inner < len(array):
                if array[i].all_attributes[column] > array[inner].all_attributes[column]:
                    array[i], array[inner] = array[inner], array[i]
                
                i += 1
                inner += 1

                idx = i
                while idx - gap  > -1:
                    if array[idx - gap].all_attributes[column] > array[idx].all_attributes[column]:
                        array[idx - gap], array[idx] = array[idx], array[idx-gap]
                    idx -= 1
            gap = int(gap / 2)

        print("SHELL")


class RadixSort(Sort):
    def perform_sorting(self, array: List):
        self.radixSort(array)
        return array

    def countingSort(self, array, place):
        n = len(array)
        counts = []
        output = []
        
        for idx in range(0 , 10):
            counts.append(0)
            
        for i in range(0 ,  len(array)):
            output.append(0)

        for i in range(0, n):
            idx = array[i] // place
            counts[idx % 10] += 1

        for i in range(1, 10):
            counts[i] += counts[i - 1]

        for i in range(len(array) - 1, -1, -1):
            index = array[i] // place
            output[counts[index % 10] - 1] = array[i]
            counts[index % 10] -= 1

        for i in range(0, n):
            array[i] = output[i]

    def radixSort(self, array):
        max_elem = max(array)
        place = 1
        while max_elem // place > 0:
            self.countingSort(array, place)
            place = place * 10


class HeapSort(Sort):
    def perform_sorting(self, array: List):
        self.heapSort(array)
        return array
    
    def heapify(self, array, n, i):
        max_num = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and array[i] < array[left]:
            max_num = left
            if right < n and array[max_num] < array[right]:
                max_num = right
            
            if max_num != i:
                array[i], array[max_num] = array[max_num], array[i]
                self.heapify(array, n, max_num)

    def heapSort(self, array):
        n = len(array)
        for idx in range(n // 2 - 1, -1, -1):
            self.heapify(array, n, idx)
            for i in range(n-1, 0, -1):
                array[i], array[0] = array[0], array[i]
                self.heapify(array, i, 0)