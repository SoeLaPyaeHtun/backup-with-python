import subprocess as sb
import os


#creat tarfilename with date 
sb.run("tar -cjf backupfilename.tar.bz2 --absolute-names sourcefilename", shell=True)

#list file count
file_num = sb.check_output("ls -l backupfoldername | wc -l",shell=True).decode()
intfile = int(file_num)
print("file number is : ",int(file_num) - 1 )
#conditin for how many file ?
if intfile > 21:
    a = sb.check_output("ls -1t backupfoldername | tail -n 1", shell=True)
    os.chdir('backupfoldername')
    file_name = str(a.decode()).rstrip("\n")

    os.remove(file_name)
    print(file_name ," was deleted bcoz file number is over twenty")
    file_num = sb.check_output("ls -l backupfoldername | wc -l",shell=True).decode()
    print(int(file_num) - 1)
