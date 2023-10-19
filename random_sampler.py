import os
import random
lp=[]
random.seed(42)
def take_random_file_and_create_new_folder(folder_path, new_folder_name):

  # Get a list of all the files in the current folder.
  files = os.listdir(folder_path)
  

  # Generate a random number between 0 and the length of the list of files.
  t=True
  while(t):
   try:
    random_index = random.randint(0, len(files) - 1)
    p=lp.index(random_index)
    t=True
   except ValueError:
    t=False
  lp.append(random_index)
  

  # Get the file at the random index.
  file = files[random_index]

  # Move the file to a new folder with the given name.
  new_folder_path = os.path.join(folder_path, new_folder_name)
  if not os.path.exists(new_folder_path):
    os.makedirs(new_folder_path)

  os.rename(os.path.join(folder_path, file), os.path.join(new_folder_path, file))



# Example usage:
lis=['A', 'B', 'C', 'D', 'del', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'nothing', 'O', 'P', 'Q', 'R', 'S', 'space', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for j in lis:
 data_dir = './asl_alphabet_train/asl_alphabet_train/{}'.format(j)
 data_new = "C:\\Users\\LENOVO\\OneDrive\\Desktop\\Sign_Language\\asl_alphabet\\"+j+"_val"
 lp=[]
 for i in range(0,500):
  take_random_file_and_create_new_folder(data_dir, data_new)
