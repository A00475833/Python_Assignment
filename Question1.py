def stack(our_list, operation, new_element=None):
    if operation == 'add':
        our_list.insert(0, new_element)
    elif operation == 'remove':
        if our_list:
            our_list.pop(0)
    return our_list

def queue(our_list, operation, new_element=None):
    if operation == 'add':
        our_list.append(new_element)
    elif operation == 'remove':
        if our_list:
            our_list.pop(0)
    return our_list

if __name__ == '__main__':
    our_list = [1, 2, 3, 4]

    print("Adding an element to the stack")
    our_list = stack(our_list, 'add', 0)
    print(our_list)

    print("Removing an element from the stack")
    our_list = stack(our_list, 'remove')
    print(our_list)

    print("Adding an element to the queue")
    our_list = queue(our_list, 'add', 5)
    print(our_list)

    print("Removing an element from the queue")
    our_list = queue(our_list, 'remove')
    print(our_list)
