from nodoS import Node

class TaskList:
    def __init__(self):
        self.head = None

    def add_contac(self, task):
        new_node = Node(task)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def delete_task(self, task):
        current = self.head
        previous = None

        while current is not None:
            if current.task == task:
                temp = current.next

                if previous is None:
                    self.head = temp
                else:
                    previous.next = temp

                return True

            previous = current
            current = current.next

        return False

    def update_task(self, old_task, new_task):
        current = self.head

        while current is not None:
            if current.task == old_task:
                current.task = new_task
                return True
            current = current.next

        return False

    def move_task_to_end(self, task):
        current = self.head
        previous = None

        while current is not None:
            if current.task == task:

                if current.next is None:
                    return True

                temp = current.next

                if previous is None:
                    self.head = temp
                else:
                    previous.next = temp

                tail = self.head
                while tail.next is not None:
                    tail = tail.next

                tail.next = current
                current.next = None
                return True

            previous = current
            current = current.next

        return False

    def get_tasks(self):
        tasks = []
        current = self.head

        while current is not None:
            tasks.append(current.task)
            current = current.next

        return tasks