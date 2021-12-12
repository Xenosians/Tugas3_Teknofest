# 3.	Total Kemunculan
# Desc:
# Buatlah sebuah program Most Appear Item yang dapat mengurutkan barang berdasarkan jumlah kemunculannya. Jika ada barang yang duplicate kamu hanya perlu memunculkan sekali, namun kamu perlu menampilkan total kemunculan barang tersebut

# Tulis fungsi untuk mengembalikan tiap item dengan jumlah item tersebut yang ada di dalam sebuah list yang diberikan sebagai parameternya.

# Test Case:
# Input: [“js”, “js”, “golang”, “ruby”, “ruby”, “js”, “js”]
# Output: 
# golang: 1 
# ruby: 2 
# js: 4

# Input: [“danu”, “danu”, “alif”, “indra”, “indra”, “kurniadi”, “indra”]
# Output: 
# alif: 1
# kurniadi: 1
# danu: 2
# indra: 3

#==================================================

def fungsi3():
    for i in input_list:
        if i not in index_hasil:
            index_hasil[i] = 1
        elif i in index_hasil:
            index_hasil[i] += 1
    return index_hasil
    
input_list = list(map(str,input().split()))
index_hasil = {}

fungsi3()

for i in index_hasil:
    k = index_hasil[i]
    print(f'{i} : {k}')


#==================================================