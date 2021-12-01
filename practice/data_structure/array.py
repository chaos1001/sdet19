class Array(object):
    def __init__(self, capacity):
        # 存放数组数据
        self.data = [-1] * capacity
        # 当前数组容量
        self.count = 0
        # 数组最大容量
        self.capacity = capacity

    def insert(self, index, value):
        # 插入失败的情况，index异常或超过数组最大容量
        if index < 0 or index >= self.capacity or self.count >= self.capacity:
            return False
        # 插入成功的步骤，需要进行数据搬移：从count位开始，给后一位赋予其前一位的值，直到插入位置
        for i in range(self.count, index, -1):
            self.data[i] = self.data[i-1]
        # 修改插入位置的值
        self.data[index] = value
        # 数组长度+1
        self.count += 1
        return True

    def find(self, index):
        if index < 0 or index >= self.count:
            return -1
        return self.data[index]

    def delete(self, index):
        if index < 0 or index >= self.count:
            return False
        # 删除成功的步骤，依然需要数据搬移：从删除位置开始，给当前位赋予后一位的值，直到count-1位=count位
        for i in range(index, self.count-1):
            self.data[i] = self.data[i+1]
        # 最后将多余的count位删除
        self.count -= 1
        return True


def test_demo():
    array = Array(5)
    array.insert(0, 1)
    array.insert(0, 2)
    array.insert(1, 3)
    array.insert(2, 4)
    array.insert(4, 5)

    # 判断插入不成功
    assert not array.insert(0, 100)
    assert array.find(0) == 2
    assert array.find(2) == 4
    assert array.find(4) == 5
    assert array.find(10) == -1
    assert array.count == 5
    removed = array.delete(4)
    assert removed
    assert array.find(4) == -1
    removed = array.delete(10)
    assert not removed
    # 2 3 4 1 5
    assert array.data == [2, 3, 4, 1, 5]


if __name__ == '__main__':
    test_demo()