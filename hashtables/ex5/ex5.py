# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    results = []
    fileDict = {}
    for path in files:
        split = path.split("/")
        fileN = split[-1]
        if fileN in fileDict:
            fileDict[fileN] += [path]
        else:
            fileDict[fileN] = [path]
    for query in queries:
        if query in fileDict:
            results += fileDict[query]
    return results


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz',
        '/usr/bar',
    ]
    queries = [
        "foo",
        "bar",
        "baz"
    ]
    print(finder(files, queries))
