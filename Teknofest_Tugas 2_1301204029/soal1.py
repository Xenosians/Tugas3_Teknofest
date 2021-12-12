# 1.	Angka Muncul Sekali
# Desc:
# Buat program sesuai dengan deskripsi di bawah. Input merupakan variable string berisi kumpulan angka.
#  Output merupakan list / array berisi angka yang hanya muncul 1 kali pada input.

# Tulis fungsi untuk mengembalikan sebuah array berisi angka angka yang hanya muncul 
# sekali dalam sebuah string yang ada pada parameter fungsi tersebut.

# Test Case:
# Input: “76523752”
# Output: [6, 3] 

# Input: “1122”
# Output: []

# Input: “1234123”
# Output: [4]

#==================================================

def fungsi1():
    for item in input_list:
        if item not in hasil and item not in blacklist:
            hasil.append(item)
        elif item in hasil :
            hasil.remove(item)
            blacklist.append(item)
    return hasil

input_list = list(map(int,input().split()))
hasil = []
blacklist = []

print(fungsi1())

#==================================================