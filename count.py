import sys


nama = "test"
alphabets = digits = special = 0

for line in sys.stdin:
    nama = line
    for i in range(len(nama)):
        if((nama[i] >= 'a' and nama[i] <= 'z') or (nama[i] >= 'A' and nama[i] <= 'Z')): 
            alphabets = alphabets + 1 
        elif(nama[i] >= '0' and nama[i] <= '9'):
            digits = digits + 1
        else:
            special = special + 1

sys.stdout.write("Total Angka: " + str(digits))
sys.stdout.write('\n')
sys.stdout.write("Total Huruf: " + str(alphabets))
sys.stdout.write('\n')
sys.stdout.write("Total Symbol: " + str(special))
sys.stdout.write('\n')
