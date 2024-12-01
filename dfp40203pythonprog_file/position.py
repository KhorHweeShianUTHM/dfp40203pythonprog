f = open('Balik_Kampung.txt', "r+")
str=f.read(14) # 20 character
print("Read string is:", str)

#tells() tell the current position within the file
position=f.tell()
print("tell() show Current file position:", position)
print("----------")

#method changes the current file position.
position=f.seek(0,0) # seek(offset,from) from = mula dr mana
str=f.read(7) # 10 character
print("Read again string is:", str)

f.close()