from importlib.resources import path
import os
import shutil
import time

def main():

    path = "F:/Coding/HW/Python/C99"
    days = 30
    sec = time.time()-(days*24*60*60)
    deleted_folders_count = 0
    deleted_files_count = 0

    if os.path.exists(path):
        #Iterating over each and every folder and file in the path
        for root_folder, folders, files in os.walk(path):
            #comparing the days
            if sec >= get_file_or_folder_age(root_folder):
                #removing the folder
                remove_folder(root_folder)
                deleted_folders_count += 1
                #breaking after removing the root folder
                break
            
            else:
                #checking folder from the root folder
                for folder in folders: 
                    folder_path = os.path.join(root_folder, folder)

                    if sec >= get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        deleted_folders_count += 1

                for file in files: 
                    file_path = os.path.join(root_folder, file)

                    if sec >= get_file_or_folder_age(file_path):
                        remove_file(file_path)
                        deleted_files_count += 1
        else:
            if sec >= get_file_or_folder_age(path):
                remove_file(path)
                deleted_files_count += 1

    else:
        print(f'"{path}" is not found')
        deleted_files_count += 1

    print(f"Total folders deleted: {deleted_folders_count}")
    print(f"Total files deleted: {deleted_files_count}")


def remove_folder(path):
    #removing the folder
    if not shutil.rmtree(path):
        #success message
        print(f"{path} is removed successfully")

    else:
        print(f"{path} is unable to be deleted")

def remove_file(path):
    #removing the file
    if not os.remove(path):
        #success message
        print(f"{path} is removed successfully")

    else:
        print(f"{path} is unable to be deleted")

def get_file_or_folder_age(path):
    ctime = os.stat(path).st_ctime

    return ctime

if __name__ == '__main__':
    main()