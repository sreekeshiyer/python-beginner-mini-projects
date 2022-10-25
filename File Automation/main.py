import os
import pathlib
import shutil

dir_path = "C:/Users/Downloads/"

file_list = []
executables = []

for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        file_list.append(path)

for file in os.listdir(dir_path):
    file_extension = pathlib.Path(file).suffix
    if (file_extension) == ".exe" or file_extension==".EXE":
        path = f"C:/Users/Downloads/{file}"
        dest_path = f"C:/Users/Downloads/Executables/{file}"
        shutil.move(path, dest_path)
    elif (file_extension) == ".pdf":
        path = f"C:/Users/Downloads/{file}"
        dest_path = f"C:/Users/Downloads/PDFs/"
        shutil.move(path, dest_path)
    elif (
        (file_extension) == ".mp3"
        or file_extension == ".mp4"
        or file_extension == ".mkv"
    ):
        path = f"C:/Users/Downloads/{file}"
        dest_path = f"C:/Users/Downloads/Media/"
        shutil.move(path, dest_path)
    elif (
        (file_extension) == ".ppt"
        or file_extension == ".pptx"
        or file_extension == ".pptm"
    ):
        path = f"C:/Users/Downloads/{file}"
        dest_path = f"C:/Users/Downloads/PPTs/"
        shutil.move(path, dest_path)
    elif (
        (file_extension) == ".png"
        or file_extension == ".jpg"
        or file_extension == ".jpeg"
        or file_extension == ".JPG"
        or file_extension == ".PNG"
        or file_extension == ".JPEG"
    ):
        path = f"C:/Users/Downloads/{file}"
        dest_path = f"C:/Users/Downloads/images/"
        shutil.move(path, dest_path)
    elif file_extension==".xlsx" or file_extension==".xls" or file_extension==".csv":
        path=f"C:/Users/Downloads/{file}"
        dest_path = f"C:/Users/Downloads/Spreadsheets/"
        shutil.move(path,dest_path)
    elif file_extension==".txt" or file_extension==".doc" or file_extension==".docx":
        path=f"C:/Users/Downloads/{file}"
        dest_path = f"C:/Users/Downloads/Text_Documents/"
        shutil.move(path,dest_path)
    elif file_extension==".rar" or file_extension==".zip" or file_extension==".tar" or file_extension==".gz":
        path=f"C:/Users/Downloads/{file}"
        dest_path = f"C:/Users/Downloads/Compressed/"
        shutil.move(path,dest_path)
    else:
        if os.path.isdir(dir_path)!=True:
            path=f"C:/Users/Downloads/{file}"
            dest_path = f"C:/Users/Downloads/Miscellaneous/"
            shutil.move(path,dest_path)