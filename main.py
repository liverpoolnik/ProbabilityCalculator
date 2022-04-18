import copy
import random

random.seed(95)


class Hat:
    def __init__(self, **kwargs):
        self.contents = list()
        for k, v in kwargs.items():
            for _ in range(v):
                self.contents.append(k)

    def draw(self, num_balls_drawn):
        draw_item = list()
        if num_balls_drawn > len(self.contents):
            draw_item = copy.deepcopy(self.contents)
            self.contents.clear()
            return draw_item
        else:
            for _ in range(num_balls_drawn):
                item = random.choice(self.contents)
                self.contents.remove(item)
                draw_item.append(item)
            return draw_item


def experiment(**kwargs):
    m = 0
    n = kwargs['num_experiments']
    hat = kwargs['hat']
    actual_balls = {}
    expected_balls = kwargs['expected_balls']
    num_balls_drawn = kwargs['num_balls_drawn']
    for _ in range(n):
        true_or_false = True
        hat_copy = copy.deepcopy(hat)
        draw_balls = hat_copy.draw(num_balls_drawn)
        # print(draw_balls)
        for item in expected_balls:
            actual_balls[item] = 0
            for i in draw_balls:
                if item == i:
                    actual_balls[item] += 1
        for j in expected_balls:
            if expected_balls[j] > actual_balls[j]:
                true_or_false = False
        # print(actual_balls)
        # print(true_or_false)
        if true_or_false:
            m += 1
    return m / n


# Starter code
hat1 = Hat(blue=3, red=2, green=6)
hat2 = Hat(red=5, blue=2)
# print(hat2.contents)
# print(hat2.draw(8))
# print(hat2.contents)
hat3 = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat1, expected_balls={"blue": 2, "green": 1},
                         num_balls_drawn=4, num_experiments=1000)
print(probability)
