#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    ticketDict = {}
    route = [None] * length
    for ticket in tickets:
        ticketDict[ticket.source] = ticket.destination
    route[0] = ticketDict["NONE"]
    for i in range(1, length):
        route[i] = ticketDict[route[i-1]]
    return route