import sys, os

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

      fout.write(("{} = {}".format(credname,creds)))

if __name__ == "__main__":
   if len(sys.argv) == 3:
      parse_creds(sys.argv[1],sys.argv[2])
   elif len(sys.argv) == 2:
      parse_creds(sys.argv[1])
   elif len(sys.argv) == 1:
      for file in [f for f in os.listdir(r"./") if f.endswith(".txt")]:
         parse_creds(file)

