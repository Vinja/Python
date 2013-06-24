def count(sequence, item):
    counter = 0
    for i in sequence:
        if i == item:
            counter+=1
    return counter
    
def purify(numbers):
    evens = []
    for i in numbers:
        if i%2 == 0:
            evens.append(i)
    return evens
  
