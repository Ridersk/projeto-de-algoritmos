import math

'''
    example, minimum classroms to lectures
'''


class Lecture:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end

    def start_min(self):
        return self.__calculate_minutes(self.start)

    def end_min(self):
        return self.__calculate_minutes(self.end)

    def __calculate_minutes(self, original_time):
        hour = math.floor(original_time)
        minutes = ((original_time - hour) * 100) + (hour * 60)
        return int(minutes)


class ClassRoom:
    def __init__(self, name):
        self.name = name
        self.lectures = []

    def add_lecture(self, lecture):
        self.lectures.append(lecture)

    def check_hour_free(self, unallocated_lecture):
        start_min = unallocated_lecture.start_min()
        end_min = unallocated_lecture.end_min()
        for lecture in self.lectures:
            if ((lecture.start_min() <= start_min and
                    lecture.end_min() >= end_min) or
                    (lecture.start_min() <= start_min and
                        lecture.end_min() > start_min) or
                    (lecture.start_min() < end_min) and
                    lecture.end_min() >= end_min):
                return False
        return True

    def show_lectures(self):
        for lecture in self.lectures:
            print(lecture.name, end=", ")
        print("\n")


# representando horas como float
lectures = [
    Lecture('a', 9, 10.30),
    Lecture('b', 9, 12.30),
    Lecture('c', 9, 10.30),
    Lecture('d', 11, 12.30),
    Lecture('e', 11, 14),
    Lecture('f', 13, 14.30),
    Lecture('g', 13, 14.30),
    Lecture('h', 14, 16.30),
    Lecture('i', 15, 16.30),
    Lecture('j', 15, 16.30),
]

# classroom working shedule 8:0 - 18:0
classrooms = []


def is_compatible(lecture):
    for room in classrooms:
        if room.check_hour_free(lecture):
            return room
    return False


def interval_partitioning():
    number_classrooms = 0

    for lecture in lectures:
        compatibleClass = is_compatible(lecture)
        if (compatibleClass):
            compatibleClass.add_lecture(lecture)
        else:
            print('new class to the lecture %s' % (lecture.name))
            new_classRoom = ClassRoom('new room')
            new_classRoom.add_lecture(lecture)
            classrooms.append(new_classRoom)
            number_classrooms += 1
    return number_classrooms


def main():
    print([lecture.name for lecture in lectures])

    print(interval_partitioning())

    print("Turmas: \n")
    for classroom in classrooms:
        classroom.show_lectures()


main()
