import sys, os

try:
   from credentials import *
except:
   print("making credentials.py")

def parse_creds(filein, fileout = 'credentials.py'):
   creds = []
   with open(filein) as fin:
      lines = fin.readlines()

      for line in lines:
         if line[0] == '#' :
            continue
         info = line.strip().split(' ')
         creds.append(info)

   with open(fileout, "a+") as fout:
      credname = filein.split('.')[0].replace(' ','_')

      if credname not in globals():
         fout.write(("{} = {}\n".format(credname,creds)))

if __name__ == "__main__":

   if "SENDER_EMAIL" not in globals():
      with open('credentials.py', "a+") as fout:
         fout.write("SENDER_EMAIL = \'{}\'\n".format(input("Sender E-mail: ")))

   if "PASSWORD" not in globals():
      with open('credentials.py', "a+") as fout:
         fout.write("PASSWORD = \'{}\'\n".format(input("Password: ")))

   if len(sys.argv) == 2:
      parse_creds(sys.argv[1])
   elif len(sys.argv) == 1:
      for file in [f for f in os.listdir(r"./") if f.endswith(".txt")]:
         parse_creds(file)

