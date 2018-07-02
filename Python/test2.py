

class Test:
    def __init__(self, *x):
        self.nums = x # Tuple

    def __repr__(self):
        return f"Test{self.nums}"

    def __str__(self):
        return f"{self.nums}"


    def __add__(self, other):
        # Ex. (1, 2) + (3, 4) -- ((1 + 2), (2 + 4))
        return Test(*(x+y for x,y in zip(self.nums, other.nums)))

    def __len__(self):
        return len(self.nums)

    def __call__(self, *args, **kwargs):
        print("UHHHH?? idk what to do...")

x1 = Test(1, 2, 3)
x2 = Test(4, 5, 6)

print("str(x1):", x1)
print("repr(x1):", repr(x1))
print("x1 + x2:", x1 + x2)
print("len(x1):", len(x1))

x1()




