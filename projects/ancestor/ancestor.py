
def earliest_ancestor(ancestors, starting_node, parent=None):
    if starting_node in [x[1] for x in ancestors]:
        for i in ancestors:
            if i[1] == starting_node:
                return earliest_ancestor(ancestors, i[0], parent=True)
    elif parent == True:
        return starting_node
    else:
        return -1

        