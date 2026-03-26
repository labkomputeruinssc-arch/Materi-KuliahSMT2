import sys
import streamlit as st
# Membuat Struktur Tuple
logApps = ("User1 Login")
print (logApps)
st.write ("Memiliki ukuran Tuple", sys.getsizeof(logApps)) 
# Membuktikan Tuple lebih efisien dari List
st.title("Membuktikan Memory Tuple lebih efisien dari List")
logAppsList = ["User1 Login"]
st.write(logAppsList)
st.write ("Memiliki ukuran List", sys.getsizeof(logAppsList))

# Pembuktian Tuple tidak bisa diubah
# 1. Tambah
# logApps.append("User4 Login")
# 2. Ubah
# logApps[0] = "User1 Logout"

# 3. Hapus
# del logApps[1]

# Pembuktian Tuple bisa diakses dengan index
print (logApps[0])
print (logApps[1])
print (logApps[-2])

# Menduplikat Tuple
logAppsBackup = logApps
print ("ini isi logAppsBackup", logAppsBackup)
print("ini isi logApps", logApps)
