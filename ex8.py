#{} means dictionaires that are indexed by keys, which can be any immutable type
#such as strings and numbers can always be keys
#{} a pair of braces creates an empty dictionary, and the requirement is that
#the key value is unique
#columnNames = {} defines an empty dict
#columnNames = [] defines an empty list
#list type is a container that holds a number of other objects, in a given order.
# The list type implements the sequence protocol,
#and also allows you to add and remove objects from the sequence.



formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
