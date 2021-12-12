# 2.	Penjumlahan Angka
# Desc:
# Diberikan array angka yang diurutkan dan jumlah target, temukan pasangan dalam array yang jumlahnya sama dengan target yang diberikan.

# Tulis fungsi untuk mengembalikan indeks dari dua angka (yaitu pasangan) sedemikian rupa sehingga mereka menambahkan hingga target yang diberikan.

# Test Case:
# Input: [1, 2, 3, 4, 6], target=6
# Output: [1, 3]

# Penjelasan:Angkanya ada di index 1 and 3 yang mana jika dijumlahkan sesuai dengan target => 2 + 4 = 6

# Input: [2, 5, 9, 11], target=11
# Output: [0, 2]

# Penjelasan: Angkanya ada di index 0 and 2 yang mana jika dijumlahkan sesuai dengan target => 2 + 9 = 11


#==================================================

def fungsi2():
    for i in range(len(input_list)):
        for j in range(len(input_list)):
            if input_list[i] + input_list[j] == penjumlahan and i != j:
                if i not in index_hasil or j not in index_hasil:
                    index_hasil.append(i)
                    index_hasil.append(j)
    return index_hasil

input_list = list(map(int,input().split()))
penjumlahan = int(input())
index_hasil = []

print(fungsi2())

#==================================================

# input_list = list(map(int,input().split()))
# penjumlahan = int(input())
# index_hasil = []

# for i in range(len(input_list)):
#     if penjumlahan - input_list[i] in input_list:
#         index_hasil.append(i)

# print(index_hasil)

#==================================================