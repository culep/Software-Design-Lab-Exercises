def recursiveMin(data):
        if len(data) == 0:
            return None
        if len(data) == 1:
            return data[0]
        return min(data[0], recursiveMin(data[1:]))
        
def recursiveMax(data):
    if len(data) == 0:
        return None
    if len(data) == 1:
            return data[0]
    return max(data[0], recursiveMax(data[1:]))

print ("min", recursiveMin([1, 2, 3, 4, 5, 6]))
print ("max", recursiveMax([1, 2, 3, 4, 5, 6]))
