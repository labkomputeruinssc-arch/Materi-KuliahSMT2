import sys
# Membuat Tuple
logsApps = ("User1 Login", "User2 Login")
print(logsApps)
print("Memiliki ukuran Tuple", sys.getsizeof(logsApps))

logsApps = ["User1 Login", "User2 Login"]
print(logsApps)
print("Memiliki ukuran List", sys.getsizeof(logsApps))

# buktikan bahwa tuple bersifat immutable  / tidak dapat diubah
# Menambahkan elemen ke dalam tuple
# logsApps.append("User3 Login")
# update elemen tuple
# logsApps[0] = "User4 Login"
# menghapus elemen tuple
# logsApps.remove("User2 Login")

# Pembuktian bahwa tuple bisa diakses dengan index
print(logsApps[0])#akses index ke-0
print(logsApps[-1])#akses index ke-1

# Slice dan copy
print(logsApps[0:1])
backup_logsApps = logsApps[:]
print(backup_logsApps)

usr1, usr2 = logsApps
print(usr1)
print(usr2)