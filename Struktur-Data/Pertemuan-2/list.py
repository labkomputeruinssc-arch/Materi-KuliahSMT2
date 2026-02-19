import sys
# Membuat List
logs = [1]
print (logs)
check_mem = print (sys.getsizeof(logs))

# Menambahkan Element didalam List Logs
logs.append(2)
print (logs)
check_mem = print (sys.getsizeof(logs))

# Menambahkan Element didalam List Logs
logs.append(3)
print (logs)
check_mem = print (sys.getsizeof(logs))

# Menambahkan Element didalam List Logs
logs.append(4)
print (logs)
check_mem = print (sys.getsizeof(logs))

# Menambah Element ke-5 didalam List Logs
logs.append(5)
print (logs)
check_mem = print (sys.getsizeof(logs))

# Menambah Element ke-6 didalam List Logs
logs.append(6)
print (logs)
check_mem = print (sys.getsizeof(logs))

# Menambah Element ke-7 didalam List Logs
logs.append(7)
print (logs)
check_mem = print (sys.getsizeof(logs))

# Menambah Element ke-8 didalam List Logs
logs.append(8)
print (logs)
check_mem = print (sys.getsizeof(logs))

# Menambah Element ke-9 didalam List Logs
logs.insert(-8,9)
print (logs)
check_mem = print (sys.getsizeof(logs))

# Menghapus Element didalam List Logs
logs.pop()
print (logs)
check_mem = print (sys.getsizeof(logs))

# Menghapus Element tertentu didalam List Logs
logs.remove(9)
print (logs)
check_mem = print (sys.getsizeof(logs))

# Sort List Logs
logs.sort(reverse=True)
print (logs)
check_mem = print (sys.getsizeof(logs))

# Reverse List Logs
logs.sort()
print (logs)
check_mem = print (sys.getsizeof(logs))

# Mencari Toal Jumlah Element didalam List Logs
print (sum(logs))
check_mem = print (sys.getsizeof(logs))

# Mencari Jumlah Element didalam List Logs
print (len(logs))
check_mem = print (sys.getsizeof(logs))

logs_backup = logs.copy()
print (logs_backup)
check_mem = print (sys.getsizeof(logs_backup))

MhsInf = ["Abu Shofiyyah", "2026", "Informatika", "3.8"]
print (MhsInf)
check_mem = print (sys.getsizeof(MhsInf))