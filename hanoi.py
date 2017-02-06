class Hanoi():
    def __init__(self):
        self.count = 0

    def hanoi(self, n, source, helper, target):
        print("hanoi( ", n, source, helper, target, " called")
        self.count += 1
        if n > 0:
            # move tower of size n - 1 to helper:
            self.hanoi(n - 1, source, target, helper)
            # move disk from source peg to target peg
            if source:
                target.append(source.pop())
            # move tower of size n-1 from helper to target
            self.hanoi(n - 1, helper, source, target)


if __name__ == '__main__':
    source = [5, 4, 3, 2, 1]
    target = []
    helper = []

    hanoi = Hanoi()
    hanoi.hanoi(len(source), source, helper, target)
    print(source, helper, target, hanoi.count)
