import os
def rename_files():
    # get file names from a folder
    file_list = os.listdir(r"C:\Users\Jasdeep\Downloads\alphabet")
    print(file_list)
    current_path = os.getcwd()
    os.chdir(r"C:\Users\Jasdeep\Downloads\alphabet")
    print("The current path is " + current_path)

    # for each file, rename file
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))
        os.chdir(r"C:\Users\Jasdeep\Downloads\alphabet")
        
rename_files()

