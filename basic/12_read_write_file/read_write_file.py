path='players.txt'

# read file
f=open(path,"r")
for line in f:
    print(line)
f.close()

# readlines()
f=open(path,"r")
lines = f.readlines()
print(lines)

# write file
f=open(path,"w")
f.write("1 Alisson Becker")
f.close()

# same file when you write something the previous line goes away
f=open(path,"w")
f.write('1 Alisson Becker\n4 Vergil Van Dijk\n')
f.close()

# You can use append mode to stop having previous lines overwritten
f=open(path,"a")
f.write('11 Mohamed Salah\n26 Andy Robertson\n66 Trent Alexander-Arnold')
f.close()

# writelines
f=open(path,"w")
f.writelines(['1 Alisson Becker\n',
              '4 Vergil Van Dijk\n',
              '11 Mohamed Salah\n',
              '26 Andy Robertson\n',
              '66 Trent Alexander-Arnold'])
f.close()

# with statement
with open(path,"r") as f:
    for line in f:
        print(line)