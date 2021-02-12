# 추상 데이터 타입 
# 스택(Stack)

# 예제1
# 리스트의 append()와 pop() 메서드로 스택 구현
class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not bool(self.items)

    def push(self, value):
        self.items.append(value)

    def pop(self):
        value = self.items.pop()
        if value is not None:
            return value
        else:
            print('Stack is empty.')

    def size(self):
        return len(self.items)

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print('Stack is empty.')

    def __repr__(self):
        return repr(self.items)

if __name__ == '__main__':
    stack = Stack()
    print('스택이 비었나요? {0}'.format(stack.isEmpty()))
    print('스택에 숫자 0~9를 추가합니다.')
    for i in range(10):
        stack.push(i)
    print('스택 크기: {0}'.format(stack.size()))
    print('peek: {0}'.format(stack.peek()))
    print('pop: {0}'.format(stack.pop()))
    print('peek: {0}'.format(stack.peek()))
    print('스택이 비었나요? {0}'.format(stack.isEmpty()))
    print(stack)

# 예제2
# 노드(객체)의 컨테이너로 스택 구현
class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer

class Stack(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def isEmpty(self):
        return not bool(self.head)

    def push(self, item):
        self.head = Node(item, self.head)
        self.count += 1

        

     