# lecture 3 - in-class exercise - file handling

import os


def create_directory(directory_name):
    if os.path.exists(directory_name):
        print(f"The directory {directory_name} already exists. Please enter another name.")
    else:
        os.makedirs(directory_name)
        print(f"The directory {directory_name} has been created successfully.")


user_input = input("Please enter a directory name: ")
create_directory(user_input)


def create_txt_file(directory_name, txt_file_name, txt_file_content):
    if not os.path.exists(directory_name):
        print(f"The directory {directory_name} does not exist. Please create it first.")
    else:
        create_directory(user_input)

    if not txt_file_name.endswith(".txt"):
        txt_file_name = txt_file_name + ".txt"

    file_path = os.path.join(directory_name, txt_file_name)

    with open(file_path, "w") as file:
        file.write(txt_file_content)

    print(f"The file {txt_file_name} has been created inside the directory {directory_name}.")

directory_input = input("Enter the directory name where you want to create the .txt file: ")
file_name_input = input("Enter the name of the .txt file (without extension): ")
content_input = input("Enter the content to be written into the file: ")

create_txt_file(directory_input, file_name_input, content_input)