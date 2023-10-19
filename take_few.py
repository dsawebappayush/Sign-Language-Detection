import os

def take(data_dir):
      # Get a list of all the files in the current folder.
  files = os.listdir(data_dir)
  count =0
  for i in files:
      os.remove(data_dir+"/"+i)
      count+=1
      if count == 400: 
          break
  file=os.listdir(data_dir)
  print(len(file))
lis=['A', 'B', 'C', 'D', 'del', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'nothing', 'O', 'P', 'Q', 'R', 'S', 'space', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for j in lis:
 data_dir = './asl_alphabet/{}'.format(j+'_val')
 data_new = "C:\\Users\\LENOVO\\OneDrive\\Desktop\\Sign_Language\\asl_alphabet\\"+j+"_val"
 take(data_dir)
 