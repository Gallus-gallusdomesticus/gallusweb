import os, shutil

#print(os.listdir("./static"))  #list file in the directory
#print(os.path.exists("./static/images")) #return True if the path exist
#print(os.path.join("./static","/images")) #join path
#print(os.path.isfile("./static/images/tolkien.png")) #return true if a file
#os.mkdir("./test")
#shutil.rmtree("./public")
#shutil.copy("./static/images/tolkien.png", "./test")


def delete_path(path):
    if os.path.exists(path)==True:
        print(f"Deleting {path} file")
        shutil.rmtree(path)
    os.mkdir(path)

def copy_folder(path, target_path):
    list_dir=os.listdir(path)
    for dir in list_dir:
        combined_path=os.path.join(path, dir)
        combined_target_path=os.path.join(target_path, dir)
        if os.path.isfile(combined_path)==False:
            print(f"Creating {combined_target_path} folder")
            os.mkdir(combined_target_path)
            if os.listdir(combined_path)==[]:
                return
            return copy_folder(combined_path, combined_target_path)
        if os.path.isfile(combined_path)==True:
            print(f"Creating {combined_target_path} file")
            shutil.copy(combined_path,combined_target_path)


def copy_static(path, target_path):
    delete_path(target_path)
    copy_folder(path, target_path)


