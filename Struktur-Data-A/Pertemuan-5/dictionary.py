# Membuat Struktur Data Dictionary
userLogin = {"name":"Budi", 
             "age":30, 
             "Role":"Admin"}
print(type(userLogin))

# Mengakses Data
print(f"Nama Akun : {userLogin['name']}")
print(f"Umur Akun : {userLogin['age']} Tahun")
print("Role Akun : %s" % userLogin['Role'])

print(userLogin)

# Menambahkan Data
userLogin['email'] = "sample@mail.com"
print(userLogin)

# Update Data
userLogin['age'] = 31
print(userLogin)

# Menghapus Data
del userLogin['email']
print(userLogin)

# Menghapus Semua Data
# userLogin.clear()
# print(userLogin)

# Dictionary Bersarang

tabelLogin = {
    "user1": {
        "name":"Budi",
        "age":30,
        "Role":"Admin"
    },
    "user2": {
        "name":"Ani",
        "age":25,
        "Role":"User"
    }
,
"user3": {
    "name":"Caca",
    "age":22,
    "Role":"Guest"
}
}

print(tabelLogin['user2'])


