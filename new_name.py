import os
lp=['A','B', 'C', 'D', 'del', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'nothing', 'O', 'P', 'Q', 'R', 'S', 'space', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# Get the path to the folder that you want to move.
for i in lp:
 old_folder_path = "C:\\Users\\LENOVO\\OneDrive\\Desktop\\Sign_Language\\asl_alphabet_train\\asl_alphabet_train\\"+i+"\\asl_alphabet_val"

# Get the path to the new location for the folder.
 new_folder_path = "C:\\Users\\LENOVO\\OneDrive\\Desktop\\Sign_Language\\asl_alphabet\\"+i+"_val"


# Rename the folder to the new location.
 os.rename(old_folder_path, new_folder_path)