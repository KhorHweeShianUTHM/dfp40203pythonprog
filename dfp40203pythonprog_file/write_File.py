# write a file
write_file = open("Jom raya.txt", "w") # w mode utk write
write_file.write("Selamat Hari Raya Semua")
write_file = open("Jom raya.txt", "r") # r = read
print(write_file.readline())

# append a file
# append = open("Jom raya.txt", "a")
# append.write("\nMadd Zahir dan Batin") # tambah tulisan
# write_file.close()