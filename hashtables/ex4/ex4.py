def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    d = {}
    arr = []
    for i in a:
        d[i] = i
    for i in d:
        if i + (i * -2) in d:
            arr.append(i)
    arr.sort()
    arr = arr[int(round(len(arr)/2)):] # slice to cut arr in half to only have positive values and round up to exclude 0
    return arr


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 0, 3, 4, -4, -3, 5, -5, 9]))
