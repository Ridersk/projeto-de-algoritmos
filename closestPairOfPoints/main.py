from random import randint
from copy import deepcopy
import math

from closestPairOfPoints import ClosestPairOfPointAlg, ListClosestPoints, ClosestPoint


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class MergeSort:
    def __init__(self, list=[]):
        self.__list: list = list

    def add_elem(self, elem):
        self.__list.append(elem)

    def remove_elem(self, elem):
        self.__list.remove(elem)

    def sort_in_x(self) -> list:
        sortList = deepcopy(self.__list)

        return self.__merge_sort_in_x(0, len(sortList) - 1, sortList)

    def __merge_list_in_x(self, list1: list, list2: list) -> list:
        count1 = 0
        count2 = 0

        resultList = []

        while(count1 < len(list1) or count2 < len(list2)):
            if count1 >= len(list1):
                resultList.extend(list2[count2:])
                break
            elif count2 >= len(list2):
                resultList.extend(list1[count1:])
                break
            elif (list2[count2].x < list1[count1].x):
                resultList.append(list2[count2])
                if count2 < len(list2):
                    count2 += 1
            else:
                resultList.append(list1[count1])
                if count1 < len(list1):
                    count1 += 1
        return resultList

    def __merge_sort_in_x(self, begin, end, sortList: list) -> list:
        part1 = []
        part2 = []

        if (begin < end):
            part1 = self.__merge_sort_in_x(
                begin, int((begin + end) / 2), sortList)
            part2 = self.__merge_sort_in_x(
                int((begin + end) / 2) + 1, end, sortList)
            return self.__merge_list_in_x(part1, part2)

        return sortList[begin: begin+1]


def create_point(qtt=0, points=[]):

    while(True):
        x = randint(0, qtt)
        y = randint(0, qtt)
        invalid = False
        for point in points:
            if x == point.x:
                invalid = True
                break
            if y == point.y:
                invalid = True
                break

        if invalid is False:
            return Point(x, y)


def euclideanDistance(point1, point2): return math.sqrt(
    abs(point1.x - point2.x)**2 + abs(point1.y - point2.y)**2)


def bruteForce(sortedList):
    print("------------------------ Prova Bruta ---------------------")
    closestPairBruteForce = ClosestPoint(None, None, math.inf)
    for i in range(0, len(sortedList)):
        for j in range(1, len(sortedList)):
            if (i != j):
                distance = euclideanDistance(sortedList[i], sortedList[j])
                if distance < closestPairBruteForce.distance:
                    closestPairBruteForce.point1 = sortedList[i]
                    closestPairBruteForce.point2 = sortedList[j]
                    closestPairBruteForce.distance = distance

    closest = closestPairBruteForce
    point1 = closest.point1
    point2 = closest.point2
    ditance = closest.distance
    print("{", point1.x, ", ", point1.y, "} , {", point2.x,
          ", ", point2.y, "} = ", closest.distance)

    return closest


def test(loops):
    for i in range(loops):
        points = []

        qtt = 1000
        for i in range(100):
            points.append(create_point(qtt, points))

        sortedList = []
        sort = MergeSort(points)

        sortedList = sort.sort_in_x()

        print("------------------------ Pontos Gerados ---------------------")
        for point in sortedList:
            print("{", point.x, ", ", point.y, "}, ", end="")
        print()

        closest = ClosestPairOfPointAlg(sortedList)

        result_orderedY = closest.search()

        print("------------------------ Ordenacao Y ---------------------")
        for point in result_orderedY.list:
            print("{", point.x, ", ", point.y, "}, ", end="")
        print()

        print("------------------------ Par de Pontos Mais Próximos ---------------------")
        closest = result_orderedY.closestPoints
        point1 = closest.point1
        point2 = closest.point2
        ditance = closest.distance
        print("{", point1.x, ", ", point1.y, "} , {", point2.x,
              ", ", point2.y, "} = ", closest.distance)

        closestBrute = bruteForce(sortedList)

        if closest.distance != closestBrute.distance:
            print("Diferentes")
            print("Test: ", i)
            return

    print("\n\n-------------------------- Test OK -----------------------------")


def main():
    test(50000)


main()
