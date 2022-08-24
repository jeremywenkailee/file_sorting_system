from genericpath import isfile
import os
from dotenv import load_dotenv
import json
import pathlib
import shutil

def scan_json(json_path):
    try:
        with open(json_path,'r') as f:
            filter_object = json.load(f)
    except FileNotFoundError:
        print("filters.json could not be found. Please add a filters.json to the root directory(where this program is being executed)")

    return filter_object

def build_directories(destination_path, filter_object):
    filter_folders = ["Others"]
    [filter_folders.append(filter_name["name"]) for filter_name in filter_object["filters"]]
    current_list_of_directories = os.listdir(destination_path)

    check_current_directories = set(filter_folders).issubset(set(current_list_of_directories))

    if(not check_current_directories):
        for filter in filter_folders:
            if(filter not in current_list_of_directories):
                os.mkdir(f'{destination_path}\\{filter}')
    

def scan_source(source_path):
    file_list = os.listdir(source_path)
    for file in file_list:
        if os.path.isdir(f'{source_path}\\{file}'):
            file_list.remove(file)
    return file_list

def sort(single_item_path_raw,source_path,destination_path, filter_object):
    prepath, single_item_path = os.path.split(single_item_path_raw)
    file_extension = pathlib.Path(single_item_path_raw).suffix
    src = f'{source_path}\\{single_item_path}'
    dst = f'{destination_path}\\Others\\{single_item_path}'
    print(f"File Name: {single_item_path}\n")

    for filter_item in filter_object["filters"]:
        if file_extension in filter_item["type"]:
            dst = f'{destination_path}\\{filter_item["name"]}\\{single_item_path}'
            break
    
    shutil.move(src,dst)
    print(f'--Sorting to: {dst}\n')
    return 0

def main(source_path,destination_path):
    filter_object = scan_json('filters.json')
    build_directories(destination_path, filter_object)
    file_list = scan_source(source_path)
    for file in file_list:
        sort(file,source_path,destination_path, filter_object)


if __name__ == "__main__":
    load_dotenv()
    SOURCE_FOLDER = os.getenv('SOURCE_FOLDER')
    DEST_FOLDER = os.getenv('DESTINATION_FOLDER')
    main(SOURCE_FOLDER,DEST_FOLDER)

