import matrix

while True:
    i = input()
    if i == "p":
        target = (int(input()), int(input()), int(input()))
        print(matrix.post_coords(target))
    elif i == "g":
        target = str(input())
        print(matrix.get_coords(target))