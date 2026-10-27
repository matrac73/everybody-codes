"""Quest 02 template."""

import math as m

######## PART 1 ########

data = """1<2 4<2 5<1 3<2 1>3 3>4 4<1 5>4 5<2 5>3
4>2 2<5 4>1 2<3 4>3 3>1 3<5 5>1 2>1 4<5
5>1 4<2 3<2 4>3 4<5 1>3 3<5 2<1 1>4 2<5
2>5 1>4 1>3 2>3 5>4 2>1 3<4 2>4 5>1 3<5
3>5 5<1 3<1 4<1 3>4 5<2 5<4 4<2 3<2 1>2
5>1 2>4 2>5 1<3 2>1 5<3 1<4 3>2 4<5 4<3
3>4 1<5 5<3 2>4 4<5 4<1 1>2 1<3 5>2 2<3
5<1 2<3 4<5 4<1 4<3 1>3 2<4 2<5 3<5 1>2
2>5 2>4 4<1 1>3 1>2 5<1 4<3 4>5 2>3 5<3
4<5 4<1 2<1 4<2 2<5 5>1 5>3 3<1 2>3 3>4"""

data_split = [line.split('\n') for line in data.splitlines()]

def order(line):
    useful_elements = [comp for comp in line[0].split() if abs(int(comp[0])-int(comp[2])) == 1]
    for useful_comp in useful_elements:
        
    sol = 0
    return(sol)

def sum_order(lines):
    return sum([order(line) for line in lines])

data_test = """4<3 2<5 3>1 1>2 1<5 4<1 3>2 4<2 3>5 4<5
4>1 2>1 3>2 1<5 4>5 2<5 3>1 4>3 2<4 5<3
5>1 5>2 4>1 2<4 3>2 3<4 1>2 3>5 1<3 4>5"""

data_split_test = [line.split('\n') for line in data.splitlines()]

assert sum_order(data_split_test) == 122157