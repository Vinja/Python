def count(sequence, item): # Long count function
    counter = 0
    for i in sequence:
        if i == item:
            counter+=1
    return counter
    
def purify(numbers): # returns all even numbers in a list
    evens = []
    for i in numbers:
        if i%2 == 0:
            evens.append(i)
    return evens
    
def product(numbers): # returns the product of a list of int's 
    product = 1
    for i in numbers:
        product*=i
    return product
  
def remove_duplicates(num): # passes a list and returns the list sans dupes.  No Dupes!
    dupeless = []
    for i in num:
        if i not in dupLess:
            dupLess.append(i)
    return dupeless
