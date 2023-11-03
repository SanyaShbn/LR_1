class Triangle:
    def __init__(self, first_side, second_side, third_side):
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side
    def is_triangle(self):
        if (((self.first_side + self.second_side) < self.third_side) or ((self.first_side + self.third_side) < self.second_side)
        or ((self.third_side + self.second_side) < self.first_side)):
            print("Треугольника с данными сторонами не может существовать!")
            return 0
        else:
            print("Ваш треугольник имеет стороны: " + str(self.first_side) + ", " + str(self.second_side) + ", "
                  + str(self.third_side))
            return 1
    def count_P(self):
       P = self.first_side + self.second_side + self.third_side
       print("P = " + str(P))
    def count_S(self):
        p = (self.first_side + self.second_side + self.third_side)/2
        S = (p*(p-self.first_side)*(p-self.second_side)*(p-self.third_side))**0.5
        print("S = " + str(S))

triangle = Triangle(3,4,5)
if(triangle.is_triangle()):
    triangle.count_P()
    triangle.count_S()
        