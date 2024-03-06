tuple1 = tuple(x for x in input('Enter the Elements: ').split(','))
tuple2 = tuple(x for x in input('Enter the Elements: ').split(','))
if len(tuple1) == len(tuple2):
    resultDictionary = dict(zip(tuple1,tuple2))
print('The result Dict: ',resultDictionary)