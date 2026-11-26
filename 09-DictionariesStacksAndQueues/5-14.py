import queue


ticket_queue = queue.Queue()
next_ticket = 1

while True:
    print("1. New customer (take ticket)")
    print("2. Serve next customer")
    print("0. Quit")

    choice = input("Select an option: ").strip()

    if choice == "1":
        ticket_queue.put(next_ticket)
        print(f"Ticket #{next_ticket} assigned. Added to queue.")
        next_ticket += 1

    elif choice == "2":
        if not ticket_queue.empty():
            served_ticket = ticket_queue.get()
            print(f"Serving customer with ticket #{served_ticket}.")
        else:
            print("No customers waiting in the queue.")

    elif choice == "0":
        break

    else:
        print("Invalid option. Please choose 1, 2, or 0.")