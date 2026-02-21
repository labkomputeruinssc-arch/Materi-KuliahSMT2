# List adalah kumpulan data yang bisa menyimpan banyak nilai
import sys
colors = ["red"]
print(colors)
print(sys.getsizeof(colors))

# Menambahkan elemen ke dalam list
colors.append("blue")
print(colors)
print(sys.getsizeof(colors))

colors.insert(0, "white")
print(colors)
print(sys.getsizeof(colors))

colors.append("green")
print(colors)
print(sys.getsizeof(colors))

colors.append("yellow")
print(colors)
print(sys.getsizeof(colors))

colors.append("purple")
print(colors)
print(sys.getsizeof(colors))

colors.append("orange")
print(colors)
print(sys.getsizeof(colors))

colors.append("pink")
print(colors)
print(sys.getsizeof(colors))

colors.append("black")
print(colors)
print(sys.getsizeof(colors))

colors.append("brown")
print(colors)
print(sys.getsizeof(colors))

# Menghapus elemen dari list
colors.pop()
print(colors)
print(sys.getsizeof(colors))

colors.remove("blue")
print(colors)
print(sys.getsizeof(colors))

colors.reverse()
print(colors)
print(sys.getsizeof(colors))

numbers = [3.60, 3.80, 3.70, 3.90, 3.50, 3.40, 3.30, 3.20]
print(sum(numbers[0:3])/len(numbers[0:3]))
print(len(numbers))
print(sys.getsizeof(numbers))
print(numbers)

backup_numbers = numbers.copy()
print(backup_numbers)
print(sys.getsizeof(backup_numbers))