from queue_ai import Queue

if __name__ == "__main__":
    # Initialize a queue with some elements
    q = Queue(1, 2, 3, 4)

    # Test if the queue initializes correctly
    print("Initial queue ", q)

    # Test enqueue operation
    q.enqueue(5)
    print("After enqueue 5 ", q)

    # Test dequeue operation
    dequeued = q.dequeue()
    print("Dequeued element ", dequeued)
    print("After dequeue ", q)

    # Test peek operation
    peeked = q.peek()
    print("Peeked element", peeked)
    print("Queue after peek (should remain unchanged)", q)

    # Test is_empty operation
    is_empty = q.is_empty()
    print("Is queue empty? ", is_empty)

    # Test reverse operation
    q.reverse()
    print("After reverse ", q)

    # Test dequeue after reverse
    dequeued = q.dequeue()
    print("Dequeued element after reverse ", dequeued)
    print("After dequeue post-reverse ", q)

    # Test peek after reverse
    peeked = q.peek()
    print("Peeked element after reverse ", peeked)
    print("Queue after peek post-reverse (should remain unchanged)", q)

    # Test dequeue until empty
    q.dequeue()
    q.dequeue()
    q.dequeue()  # Queue should now be empty
    print("After dequeuing all elements ", q)

    # Test is_empty on an empty queue
    is_empty = q.is_empty()
    print("Is queue empty now? ", is_empty)

    # Test dequeue on an empty queue (should handle gracefully)
    try:
        q.dequeue()
    except Exception as e:
        print("Dequeue on empty queue error ", e)

    # Test peek on an empty queue (should handle gracefully)
    try:
        q.peek()
    except Exception as e:
        print("Peek on empty queue error ", e)

    # Test reverse on an empty queue
    try:
        q.reverse()
        print("Reverse on empty queue ", q)
    except Exception as e:
        print("Reverse on empty queue error ", e)
