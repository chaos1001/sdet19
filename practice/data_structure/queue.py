
# 普通队列
class Queue:
    def __init__(self, capacity):
        # 头节点
        self.head = 0
        # 尾节点，代表插入位置，队尾位置其实是tail-1
        self.tail = 0
        self.capacity = capacity
        self.items = [-1] * self.capacity

    def enqueue(self, item):
        # 队列已满
        if self.tail >= self.capacity:
            return False
        # 入队时移动尾节点
        self.items[self.tail] = item
        self.tail += 1
        return True

    def dequeue(self):
        # 队列为空
        if self.head >= self.tail:
            return -1
        # 出队时移动头节点
        item = self.items[self.head]
        self.head += 1
        return item


def test_queue():
    q = Queue(10)
    q.enqueue("10")
    q.enqueue("20")
    deque_item = q.dequeue()
    assert deque_item == "10"
    q.enqueue("30")
    assert q.items[q.head] == "20"
    assert q.items[q.tail - 1] == "30"
    assert q.dequeue() == "20"
    assert q.dequeue() == "30"
    assert q.dequeue() == -1


# 优化队列
class BetterQueue(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = 0
        self.tail = 0
        self.items = [-1] * self.capacity

    def enqueue(self, item):
        # 如果头结点的位置不在初始位，说明需要搬移数据
        if self.head > 0:
            for i in range(self.head, self.tail):
                self.items[i - self.head] = self.items[i]
            self.head -= self.head
            self.tail -= self.head
        if self.tail >= self.capacity:
            return False
        # 搬移数据完毕后再插入
        self.items[self.tail] = item
        self.tail += 1
        return True

    def dequeue(self):
        if self.head >= self.tail:
            return -1
        item = self.items[self.head]
        self.head += 1
        return item


def test_better_queue():
    q = BetterQueue(3)
    q.enqueue("10")
    q.enqueue("20")
    q.enqueue("30")
    assert not q.enqueue("40")
    deque_item = q.dequeue()
    assert deque_item == "10"
    q.enqueue("30")
    assert q.items[0] == "20"
    assert q.items[2] == "30"
    assert q.dequeue() == "20"
    assert q.dequeue() == "30"
    assert q.dequeue() == "30"
    assert q.dequeue() == -1


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkQueue(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        # 给入队的数据建一个new_node
        new_tail = Node(data)
        # 没有head时，head=new_node
        if not self.head:
            self.head = new_tail
        # 有head时，将原tail的next指向新tail
        else:
            self.tail.next = new_tail
        # 在尾部插入new_node
        self.tail = new_tail

    def dequeue(self):
        # 没有head时无法出队
        if not self.head:
            return Node(-1)
        # 取出原head留底
        item = self.head
        # 将head改为的原head的next
        self.head = self.head.next
        return item


def test_link_queue():
    q = LinkQueue()
    q.enqueue("10")
    q.enqueue("20")
    q.enqueue("30")
    deque_item = q.dequeue()
    assert deque_item.data == "10"
    q.enqueue("30")
    assert q.head.data == "20"
    assert q.head.next.data == "30"
    assert q.dequeue().data == "20"
    assert q.dequeue().data == "30"
    assert q.dequeue().data == "30"
    assert q.dequeue().data == -1


class CircleQueue(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [-1]*self.capacity
        self.head = 0
        self.tail = 0

    def enqueue(self, item):
        # 如果队列已满，则无法插入
        if (self.tail + 1) % self.capacity == self.head:
            return False
        # 如果队列未满，则在tail位置插入
        self.items[self.tail] = item
        # 并将tail后移一位，注意循环回头的位置
        self.tail = (self.tail + 1) % self.capacity
        return True

    def dequeue(self):
        # 如果head和tail在同一个位置，说明队列为空
        if self.head == self.tail:
            return -1
        item = self.items[self.head]
        # head后移一位，注意循环回头的位置
        self.head = (self.head + 1) % self.capacity
        return item


def test_circle_queue():
    q = CircleQueue(3)
    q.enqueue("10")
    q.enqueue("20")
    assert not q.enqueue("30")
    assert q.dequeue() == "10"
    q.enqueue("30")
    assert q.items[2] == "30"
    assert not q.enqueue("10")
    assert q.dequeue() == "20"
    assert q.dequeue() == "30"
    assert q.dequeue() == -1


if __name__ == '__main__':
    test_queue()
    test_better_queue()
    test_link_queue()
    test_circle_queue()

