def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weightDict = {}
    for index, weight in enumerate(weights):
        if weight in weightDict:
            weightDict[weight] += [index]
        else:
            weightDict[weight] = [index]
    for weight in weights:
        if limit - weight in weightDict:
            if limit/2 == weight:
                return (weightDict[weight][1], weightDict[weight][0])
            else:
                return (weightDict[limit - weight][0], weightDict[weight][0])
    return None

print(get_indices_of_item_weights([4, 6, 9, 4], 4, 13))