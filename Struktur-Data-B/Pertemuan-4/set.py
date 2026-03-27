# cara iniasiasi Set
# 1 (kurung kurawal)
import sys 
tokenWord = {"tidak","bisa"}
print(tokenWord)
print(type(tokenWord))
print("Ukuran memori", sys.getsizeof(tokenWord))

# 2 (set())
kataSambung = set(["kemudian", "lalu", "setelah"])
print(kataSambung)
print(type(kataSambung))
print("Ukuran memori", sys.getsizeof(kataSambung))

# Pembuktian terkait tidak memiliki sistem indexing
# print(kataSambung[-1])

# Menghapus elemen pada set
kataSambung.remove("kemudian")
print(kataSambung)
tokenWord.discard("tidak")
print(tokenWord)

# Menambahkan elemen pada set
tokenWord.add("mungkin")
print(tokenWord)
tokenWord.update(["pasti","mungkin"])
print(tokenWord)

# Mengubah elemen set
tokenWord.remove("mungkin")
tokenWord.add("nanti")
print(tokenWord)

# Operasi pada set
setA = {1,2,3,4}
setB = {3,4,5,6}

# Union
print(setA|setB)
# Intersection
print(setA&setB)
# Difference
print(setA-setB)
# Symmetric Difference
print(setA^setB) 

setUnion = setA.union(setB)
print(setUnion)


