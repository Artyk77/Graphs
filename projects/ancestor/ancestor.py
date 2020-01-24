
from graph import Graph
from util import Queue

def earliest_ancestor(ancestors, starting_node):

    # instantiate a graph and a queue
    gr = Graph()
    q = Queue()

    # instantiate the starting node as the first vertex and first item in graph + queue
    gr.add_vertex(starting_node)
    q.enqueue(starting_node)

    # loop through the queue
    while q.size() > 0:
        # grab the item off the front of the queue
        node = q.dequeue()
        # loop through the relationships
        for relationship in ancestors:
            # if the child in the relationship is the current node
            if relationship[1] == node:
                # grab the parent, enqueue the parent, add the parent as a vertex,
                # and add an edge between the node and parent (so it's in reverse order with the youngest first)
                parent = relationship[0]
                q.enqueue(parent)
                gr.add_vertex(parent)
                gr.add_edge(node, parent)

    # get the tree (returns a tuple of relatives + index in family tree as a signature)
    raw_tree = list(gr.dft(starting_node))
    # filter out the start node
    tree = list(filter(lambda x: x[0] != starting_node, raw_tree))
    # if the node has no ancestors, return -1
    if len(tree) == 0:
        return -1
    # otherwise mark the largest/oldest index, filter our for oldest ancestors,
    # and return the smallest id from the list of oldest ancestors
    else:
        oldest = 0
        for item in tree:
            if item[1] > oldest:
                oldest = item[1]
        ancestors = []
        for family_member in tree:
            if family_member[1] == oldest:
                ancestors.append(family_member[0])
        return sorted(ancestors)[0]