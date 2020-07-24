"""
A way of finding common elements between two python lists
I nthis way we use another object type: sets. They are *different* from lists,
and they already come with a method (yes, a python method) which allows us
to easilly find the common elements.

One could, of course, use another way to solve this. Can you do it? :)
"""

# Just a random way to create two lists
#list_1 = []
#list_2 = []
#for i in range(100):
#    if i % 2 == 0:
#        list_1.append(i)
#    if i % 3 == 0:
#        list_2.append(i)

# creating the lists to be compared
list_1 = [1,2,3,4,5,6,7,8]
list_2 = [2,4,6,8,10]

# HERE's the little trick: we do not actually use lists when we're
# doing things like this, but we use another value type: >>>sets<<< instead.
# So be aware that "sets" are a different thing than "lists"!
set_1 = set(list_1)
set_2 = set(list_2)

# So here we can use the intersection method,
# which is available for sets, but not for lists
answer = set_1.intersection(set_2)

# displaying the answer
print(list_inter)