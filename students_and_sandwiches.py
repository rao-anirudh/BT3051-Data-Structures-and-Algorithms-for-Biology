# We define a Stack class and a Queue class with their respective standard operations.

class Stack:

    def __init__(self):
        self.elements = []

    def is_empty(self):
        if len(self.elements) == 0:
            return True
        else:
            return False

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if self.is_empty():
            return "pop() not possible"
        last = self.elements[-1]
        self.elements = self.elements[:-1]
        return last

    def top(self):
        return self.elements[-1]

    def __str__(self):
        return " ".join([str(element) for element in self.elements])

    def __len__(self):
        return len(self.elements)


class Queue:

    def __init__(self):
        self.elements = []

    def is_empty(self):
        if len(self.elements) == 0:
            return True
        else:
            return False

    def enqueue(self, elements):
        if type(elements) != list:
            elements = [elements]
        self.elements = self.elements + elements

    def dequeue(self):
        if len(self.elements) == 0:
            return "dequeue() not possible"
        self.elements = self.elements[1:]

    def front(self):
        return self.elements[0]

    def __str__(self):
        return " ".join([str(element) for element in self.elements])

    def __len__(self):
        return len(self.elements)


def numstud(students, sandwiches):

    """
    Returns the number of students who are unable to eat.

    INPUT(S)
        students - list
        sandwiches - list

    OUTPUT(S)
        num_hungry - int

    EXAMPLES(S)
        numstud([1,1,0,0],[0,1,0,1]) = 0
        numstud([1,1,1,0,0,1],[1,0,0,0,1,1] = 3

    """

    # We initialise a student queue and a sandwich stack.

    student_queue = Queue()
    sandwich_stack = Stack()

    # We populate the queue and the stack with the given inputs.

    student_queue.enqueue(students)

    for sandwich in sandwiches[::-1]:
        sandwich_stack.push(sandwich)

    # We initialise the number of rejected sandwiches as 0.

    num_rejections = 0

    # We iterate as long as no student in the queue wants to take the top sandwich.

    while num_rejections != len(student_queue):

        # We define the front-most student and the top-most sandwich.

        student = student_queue.front()
        sandwich = sandwich_stack.top()
        student_queue.dequeue()

        # If it is a match, we pop the sandwich and reset the number of rejections to 0.

        if student == sandwich:

            dummy = sandwich_stack.pop()
            num_rejections = 0

        # If it is a mismatch, the student is moved to the back of the queue.

        else:

            student_queue.enqueue(student)
            num_rejections += 1

    # The number of students unable to eat is the final length of the student queue.

    num_hungry = len(student_queue)

    # We return the number of students unable to eat.

    return num_hungry
