###########################################
# Tuple
###########################################

empty_tuple = ()
print(type(empty_tuple))

empty_tuple2 = tuple()
print(type(empty_tuple))


lst = [10, 11, 12]
lst_tuple = tuple(lst)
print(type(lst_tuple))


filled_tuple = (10, 12, 15, 'Hello', 'Hi', [100, 101, 102])
print(filled_tuple[1])
print(filled_tuple[-1])
print(filled_tuple[:5])
print(filled_tuple[1:])

lst = [10, 11, 12]
lst[1] = 200
print(lst)

filled_tuple[1] = 1500
print(filled_tuple)

filled_tuple[-1].append("Hello")
print(filled_tuple)


one_element_tuple = (10,)
print(one_element_tuple)


number1, number2 = 10, 15
print(number1)
print(number2)

*first, second, third = ('first_element', 'second_element', 'third_element', 'fourth_element', 'fifth_element', 'sixth_element')

print(first)
print(second)
print(third)

tuple1 = (1, 2, 3, 4, 5, 5, 5, 5)
tuple2 = (6, 7, 8, 9, 10)

print(tuple1 + tuple2)
print(tuple1)
print(tuple2)
print(tuple1 * 3)
print(tuple1.count(5))
print(tuple1.index(5))


###########################################
# Set
###########################################

empty_set = {}
print(type(empty_set))

empty_set = set(tuple1)
print(empty_set)


filled_set = {10, 11, 5, 2, 'Hello', 10, 15, 'Hi', 0, False, True, 1}
print(filled_set)

filled_set.add('Python')
print(filled_set)

for data in filled_set:
    filled_set.remove(data)
print(filled_set)

print(filled_set.pop())
print(filled_set.pop())
print(filled_set.pop())
print(filled_set.pop())
print(filled_set.pop())
print(filled_set)


# (1, 2, 3, 4, 5) (3, 4, 5, 6, 7, 8)

# (1, 2, 3, 4, 5) - (3, 4, 5, 6, 7, 8) = (1, 2)
# (1, 2, 3, 4, 5) ი (3, 4, 5, 6, 7, 8) = (3, 4, 5)
# (1, 2, 3, 4, 5) u (3, 4, 5, 6, 7, 8) = (1, 2, 3, 4, 5, 3, 4, 5, 6, 7, 8)


filled_set1 = {10, 11, 5, 2, 'Hello', 'Hi', False, True}
filled_set2 = {100, 200, 300, 400, 'Hello', 'Hi', False, True}

difference = filled_set1.difference(filled_set2)
print(difference)
print(filled_set1)

filled_set1.difference_update(filled_set2)
print(filled_set1)


intersection = filled_set1.intersection(filled_set2)
print(intersection)

filled_set1.intersection_update(filled_set2)
print(filled_set1)

union = filled_set1.union(filled_set2)
print(union)

print(filled_set1.symmetric_difference(filled_set2))
filled_set1.symmetric_difference_update(filled_set2)
print(filled_set1)

###########################################
# Frozen Set
###########################################

filled_set1 = {10, 11, 5, 2, 'Hello', 'Hi', False, True}
filled_set2 = {100, 200, 300, 400, 'Hello', 'Hi', False, True}


frozen1 = frozenset(filled_set1)
frozen2 = frozenset(filled_set2)

print(frozen1.difference(frozen2))



frozen_set = frozenset({1, 2, 3, 4, 5})
dct = {frozen_set: 'Frozen Value'}

print(dct[frozen_set])
