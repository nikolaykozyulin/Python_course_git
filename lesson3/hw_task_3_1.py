class rectangle:
    def __init__(self, width, hight):
        self.width = width
        self.hight = hight

    def square(self):
        return self.width*self.hight


    def perimeter(self):
        return 2*self.width+2*self.hight



rectangle1= rectangle(10, 20)
print(rectangle1.square())
print(rectangle1.perimeter())
