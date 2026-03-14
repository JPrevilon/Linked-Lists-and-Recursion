from linked_list import LinkedList

if __name__ == "__main__":

    # Create LinkedList
    ll = LinkedList()

    # Insert sample data
    ll.insert_at_front(10)
    ll.insert_at_front(20)
    ll.insert_at_end(5)

    print("Original List:")
    ll.display()

    # Recursive sum
    total = ll.recursive_sum()
    print("Sum of IDs:", total)

    # Recursive search
    print("Search for 10:", ll.recursive_search(10))
    print("Search for 999:", ll.recursive_search(999))

    # Reverse list
    ll.recursive_reverse()

    print("Reversed List:")
    ll.display()