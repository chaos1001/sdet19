class ArrayStack:
    def __init__(self, n):
        self.data = [-1] * n
        # 栈的最大容量
        self.n = n
        # 栈的当前容量，同时也是当前入栈的位置
        self.count = 0

    def push(self, value):
        if self.n == self.count:
            return False

        self.data[self.count] = value
        self.count += 1
        return True

    def pop(self):
        if self.count == 0:
            return None

        self.count -= 1
        return self.data[self.count]


def test_array_stack():
    array_stack = ArrayStack(5)
    data = ["a", "b", "c", "d", "e"]
    for i in data:
        array_stack.push(i)

    result = array_stack.push("a")
    assert not result
    data.reverse()
    for i in data:
        assert i == array_stack.pop()

    assert array_stack.pop() is None


class LinkedStack:
    def __init__(self):
        # 栈顶位置
        self.top = None

    def push(self, value):
        new_node = self.Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top.next
            self.top = new_node

    def pop(self):
        if self.top is None:
            return -1

        # 先拿到当前栈顶node的值
        result = self.top.data
        # 把当前栈顶node出栈
        self.top = self.top.next
        return result

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None


if __name__ == '__main__':
    test_array_stack()
