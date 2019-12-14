from collections import Counter

def valid(part, number):
    prev = []
    double = False

    for n in number:
        if len(prev) > 0:
            if n < prev[-1]:
                return False
            elif prev.count(n) > 0:
                double = True

        prev.append(n)
                
    if part == 1:
        return double
    elif part == 2:
        return double and 2 in Counter(prev).values()

if __name__ == "__main__":
    total1 = 0
    total2 = 0

    for number in range(153517, 630395):
       if valid(1, str(number)):
            total1 += 1 
       if valid(2, str(number)):
            total2 += 1 
         
    print(total1)
    print(total2)
