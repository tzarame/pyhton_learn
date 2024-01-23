tree_height = int(input("Введите высоту дерева: "))

for i in range(tree_height):
    symbol = "*"
    spaces = " " * (tree_height - i - 1)
    stars = symbol * (2 * i + 1)
    print(spaces + stars)