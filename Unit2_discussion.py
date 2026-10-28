"""
===========================================================
UNIT 2 DISCUSSION: BOSTON CELTICS STACKS AND QUEUES
===========================================================

OVERVIEW:
This program demonstrates stacks (LIFO) and queues (FIFO)
using Boston Celtics basketball scenarios.

The stack represents Celtics players' most recent game
highlights, while the queue represents fans waiting to
enter the arena.
"""

from collections import deque


class Stack:
    def __init__(self):
        # Store basketball highlights in a list.
        self.items = []

    def push(self, value):
        # LIFO means the last highlight added is removed first.
        self.items.append(value)
        print(f"Added Celtics highlight: {value}")

    def pop(self):
        # Check whether the stack is empty before removing a value.
        if self.is_empty():
            print("No Celtics highlights available to remove.")
            return None

        value = self.items.pop()
        print(f"Removed most recent highlight: {value}")
        return value

    def peek(self):
        # View the latest highlight without removing it.
        if self.is_empty():
            print("No Celtics highlights available to view.")
            return None

        print(f"Most recent Celtics highlight: {self.items[-1]}")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # Store Celtics fans in arrival order.
        self.items = deque()

    def enqueue(self, value):
        # FIFO means the first fan to arrive is served first.
        self.items.append(value)
        print(f"{value} joined the line to enter TD Garden.")

    def dequeue(self):
        # Check whether any fans are waiting before removing one.
        if self.is_empty():
            print("No Celtics fans are waiting in line.")
            return None

        value = self.items.popleft()
        print(f"{value} entered TD Garden.")
        return value

    def front(self):
        # View the first fan in line without removing them.
        if self.is_empty():
            print("There are no fans at the front of the line.")
            return None

        print(f"First fan in line: {self.items[0]}")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0


def main():
    print("=" * 50)
    print("       BOSTON CELTICS DATA STRUCTURES")
    print("=" * 50)

    # ===================================
    # STACK DEMO: CELTICS GAME HIGHLIGHTS
    # ===================================
    print("\n=== CELTICS HIGHLIGHTS: STACK DEMO ===")

    highlights = Stack()

    print("\nRecording Celtics game highlights:")
    highlights.push("Jayson Tatum hits a three-pointer")
    highlights.push("Jaylen Brown makes a dunk")
    highlights.push("Derrick White blocks a shot")
    highlights.push("Payton Pritchard scores at the buzzer")

    print("\nViewing the latest highlight:")
    highlights.peek()

    print("\nRemoving highlights using LIFO:")
    highlights.pop()
    highlights.pop()
    highlights.pop()
    highlights.pop()

    print(f"\nAre all highlights removed? {highlights.is_empty()}")

    print("\nTesting an empty stack:")
    highlights.pop()
    highlights.peek()

    print("\nTesting a single-highlight stack:")
    single_highlight = Stack()
    single_highlight.push("Celtics win the championship!")
    single_highlight.pop()
    print(
        "Is the single-highlight stack empty?",
        single_highlight.is_empty()
    )

    # ===================================
    # QUEUE DEMO: FANS ENTERING TD GARDEN
    # ===================================
    print("\n=== CELTICS FANS: QUEUE DEMO ===")

    fans = Queue()

    print("\nFans arrive at TD Garden:")
    fans.enqueue("Fan 1")
    fans.enqueue("Fan 2")
    fans.enqueue("Fan 3")
    fans.enqueue("Fan 4")

    print("\nChecking who is next to enter:")
    fans.front()

    print("\nAdmitting fans using FIFO:")
    fans.dequeue()
    fans.dequeue()
    fans.dequeue()
    fans.dequeue()

    print(f"\nIs the entrance line empty? {fans.is_empty()}")

    print("\nTesting an empty queue:")
    fans.dequeue()
    fans.front()

    print("\nTesting a single-fan queue:")
    single_fan = Queue()
    single_fan.enqueue("Celtics Superfan")
    single_fan.dequeue()
    print(
        "Is the single-fan queue empty?",
        single_fan.is_empty()
    )

    print("\n" + "=" * 50)
    print("       GO CELTICS! ☘️")
    print("=" * 50)


if __name__ == "__main__":
    main()
