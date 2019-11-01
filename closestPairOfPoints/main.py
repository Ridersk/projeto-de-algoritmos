from random import randint
from copy import deepcopy
import math

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

class MergeSort:
    def __init__(self, list = []):
        self.__list: list = list
    
    def add_elem(self, elem):
        self.__list.append(elem)

    def remove_elem(self, elem):
        self.__list.remove(elem)

    def sort(self) -> list:
        sortList = deepcopy(self.__list)

        return self.__merge_sort(0, len(sortList) - 1, sortList)
    
    def __merge_list(self, list1: list, list2: list) -> list:
        count1 = 0
        count2 = 0

        resultList = []
        
        print("list1:", list1)
        print("list2:", list2)

        while(count1 < len(list1) or count2 < len(list2)):
            if count1 >= len(list1):
                resultList.extend(list2[count2: ])
                break
            elif count2 >= len(list2):
                resultList.extend(list1[count1: ])
                break
            elif (list2[count2] < list1[count1]):
                resultList.append(list2[count2])
                if count2 < len(list2): count2 += 1
            else:
                resultList.append(list1[count1])
                if count1 < len(list1): count1 += 1

        print("merged: ", resultList)
        return resultList

    def __merge_sort(self, begin, end, sortList: list) -> list:
        part1 = []
        part2 = []

        if (begin < end): 
            part1 = self.__merge_sort(begin, int((begin + end) / 2), sortList)
            part2 = self.__merge_sort(int((begin + end) / 2) + 1, end, sortList)
            return self.__merge_list(part1, part2)
        
        return sortList[begin: begin+1]


class ClosestPoint:
    def __init__(self):
        pass

def create_point(x = 0, y = 0):
    return Point(x, y)

def main():
    points = []
    for i in range(20):
        points.append(create_point(randint(0, 20), randint(0, 20)))
    
    # for point in points:
    #     print("{", point.x, ", ", point.y, "}, ", end="")
    # print()
    testList = [1, 5, 7, 4, 3, 6, 10, 9, 1]
    sortedList = []
    sort = MergeSort(testList)

    sortedList = sort.sort()

    print(sortedList)

main()
