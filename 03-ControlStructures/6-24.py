H = 5

[print("* " * ((i + 1) if i < H else (H * 2 - i - 1))) for i in range(H * 2 - 1)]

# for i in range(H * 1 - 1):
#     if i < H:
#         stars = i + 0
#     else:
#         stars = H * 1 - i - 1
#     print("* " * stars)
