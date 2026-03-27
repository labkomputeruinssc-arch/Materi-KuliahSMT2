# Membuat Set dalam python
# 1. dengan menggunakan kurung Kurawal 
import sys
kataSambung = {"kemudian", "lalu", "setelah"}
print(kataSambung)
print(type(kataSambung))
print("Ukuran memori", sys.getsizeof(kataSambung))

# 2. dengan menggunakan fungsi set()
tokenWord = set(["tidak"])
print(tokenWord)
print(type(tokenWord))
print("Ukuran memori", sys.getsizeof(tokenWord))

# Membuktikan tidak menganut konsep indexing
# print(tokenWord[0])
# Menambah anggota didalam set
# 1. dengan metode add()
tokenWord.add("login")
print(tokenWord)

# 2. Metode Update
tokenWord.update(["sebelum"])
print(tokenWord)
# Menghapus anggota didalam set
#1.  dengan metode Remove
# kataSambung.remove("setelah")
# print(kataSambung)
# # 2. dengan Discard
# kataSambung.discard("lalu")
# print(kataSambung)
# 3. dengan Pop
kataSambung.pop()
print(kataSambung)
print(tokenWord)

# Mengubah anggota didalam set
tokenWord.discard("sebelum")
tokenWord.update(["kemudian"])
print(tokenWord)

# implementasi Operasi pada Set
# 1. Union / Gabungan
set1 = {1,2,3,4}
set2={3,4,5,6}
print(set1|set2)
print(set1.union(set2))

# 2. Intersection / irisan
print(set1&set2)
print(set1.intersection(set2))

# 3. Difference / selisih
print(set1-set2)
print(set2.difference(set1))

# 4. Symmetric Difference / selisih simetri
print(set1^set2)
print(set1.symmetric_difference(set2))
