# s = "banana"
# print(s[::2])

not_on_board = input().split()
on_board_bus = input().split()

print(f"Passengers waiting at a bus stop: {not_on_board}")
print(f"Passengers on board: {on_board_bus}")

""" Your code goes here """
left_passenger = not_on_board.pop()
print(f"Passenger left bus stop:{left_passenger}")
on_board_bus.extend(not_on_board)


print(f"Updated passengers on board: {on_board_bus}")
