def countOnCollectionWithVal(collection, value = "max"):
    if isinstance(value, str):
        if value == "max" or value == "high":
            value = max(collection)
        elif value == "min" or value == "low":
            value = min(collection)

    return collection.count(value)

print("7: ", countOnCollectionWithVal((7,7,7,7,2,5,3), 7))
print("8: ", countOnCollectionWithVal([7,7,7,7,2,5,3], 8))
print("leer: ", countOnCollectionWithVal([7,7,7,7,2,5,3]))
print("min: ", countOnCollectionWithVal([7,7,7,7,2,5,3], 'min'))
print("low: ", countOnCollectionWithVal([7,7,7,7,2,5,3], 'low'))
print("high: ", countOnCollectionWithVal([7,7,7,7,2,5,3], 'high'))

# set script
set1 = {'test1', 'test2'}
print('Set-Output: ', set1, ', ', len(set1))

