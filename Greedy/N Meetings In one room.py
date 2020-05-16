class Activity:
    def __init__(self, start, finish, index):
        self.start = start
        self.finish = finish
        self.index = index
def meeting(start, finish, n):
    lst = []
    for i in range(n):
        lst.append(Activity(start[i], finish[i], i))

    lst.sort(key=lambda i: i.finish)
    i = 0
    print(lst[i].index + 1, end=" ")
    for j in range(1, n):
        if lst[j].start >= lst[i].finish:
            print(lst[j].index + 1, end=" ")
            i = j
        # print(lst[j].index,lst[j].start,lst[j].finish)
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = int(input())
        start = list(map(int, input().split()))
        finish = list(map(int, input().split()))
        meeting(start, finish, s)
