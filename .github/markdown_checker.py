#!/usr/bin/env python3
"""
Module providing automatic checks functionality to markdown files 
following the some Guidelines
"""
import os
import argparse
import re


def main() -> None:
    """Main program get inputs and run checks"""

    # get input arguments directory, function to run
    in_arg = get_input_args()

    lessons = get_lessons_paths(in_arg.dir)

    # iterate over the files to validate the content
    for lesson_folder_name, lessons_array in lessons.items():
        for lesson_file_name in lessons_array:
            file_path = os.path.join(
                in_arg.dir,
                lesson_folder_name,
                lesson_file_name )
            if "check_broken_paths" in in_arg.func:
                formatted_output = check_broken_links(file_path, "path" , "broken")
                if formatted_output:
                    print(formatted_output)
            if "check_paths_tracking" in in_arg.func:
                formatted_output = check_broken_links(file_path, "path" , "tracking")
                if formatted_output:
                    print(formatted_output)
            if "check_urls_tracking" in in_arg.func:
                formatted_output = check_broken_links(file_path, "url" , "tracking")
                if formatted_output:
                    print(formatted_output)
            if "check_urls_locale" in in_arg.func:
                formatted_output = check_broken_links(file_path, "url" , "locale")
                if formatted_output:
                    print(formatted_output)

# Helper Functions

def get_lessons_paths(root_path: str) -> dict:
    """function to compile a dictionary of directories
    
    Keyword arguments:
    root_path -- directory to go through looking for md files
    Return: formatted dictionary with directories as key and an array of files as values
    """
    lessons = {}

    # get lessons folders
    for item in os.listdir(root_path):
        if os.path.isdir(os.path.join(root_path, item)):
            lessons[item] = []

    # get lesson exercises (md, ipynb files)
    for lesson, _ in lessons.items():
        for item in os.listdir(os.path.join(root_path, lesson)):
            # check for translations directories
            if os.path.isdir(os.path.join(root_path, lesson, item)):
                for sub_item in os.listdir(os.path.join(root_path, lesson, item)):
                    # check for .md and .ipynb files and store them
                    if sub_item.lower().endswith(('.md', '.ipynb')):
                        lessons[lesson].append(os.path.join(item, sub_item))
            # check for .md and .ipynb files and store them
            elif item.lower().endswith(('.md', '.ipynb')):
                lessons[lesson].append(item)

    # check to remove folders that don't have .md files in them
    lessons = {key: values for key, values in lessons.items() if len(values) > 0}

    return lessons

def check_broken_links(file_path : str, link_type : str , check_type: str) -> str:
    """function that checks if urls and hyperlinks are broken
    
    Keyword arguments:
    file_path -- a path to text file to check
    link_type -- path or url
    check_type -- broken or tracking or locale
    Return: broken links and associated file path
    """
    all_links = get_links_from_file(file_path)

    # check if file has links
    if len(all_links) > 0:
        formatted_output = f"> FILE '{file_path}'\n"
        if link_type == "path":
            paths = get_paths_from_links(all_links)
            if check_type == "broken":
                broken_path = check_paths_exists(file_path, paths)
                if len (broken_path) > 0:
                    formatted_output += f'> has the following broken relative paths {broken_path}\n'
                    return formatted_output
            elif check_type == "tracking":
                tracking_id_paths = check_url_tracking(paths)
                if len(tracking_id_paths) > 0:
                    formatted_output += f'> has the following paths with no tracking id {tracking_id_paths}\n'
                    return formatted_output
        elif link_type == "url":
            urls = get_urls_from_links(all_links)
            if check_type == "tracking":
                tracking_id_urls = check_url_tracking(urls)
                if len(tracking_id_urls) > 0:
                    formatted_output += f'> has the following links with no tracking id {tracking_id_urls}\n'
                    return formatted_output
            elif check_type == "locale":
                country_locale_urls = check_url_locale(urls)
                if len(country_locale_urls) > 0:
                    formatted_output += f'> has the following links with country locale {country_locale_urls}\n'
                    return formatted_output

def get_links_from_file(file_path: str) -> list:
    """function to get an array of markdown links from a file
    flags markdown links captures the part inside () that comes right after []
    """
    all_links = []
    with open(file_path, 'r',  encoding="utf-8") as file:
        data = file.read()
        link_pattern = re.compile(r'\[.*\]\((.*?)\)')
        matches = re.finditer(link_pattern, data)
        for matched_group in matches:
            all_links.append(matched_group.group(1))
    return all_links

def get_urls_from_links(all_links: list) -> list:
    """function to get an array of urls from a list"""
    urls = []
    url_pattern = re.compile(r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9]{1,6}\b([-a-zA-Z0-9@:%_\+.~#?&\/\/=]*)')

    for link in all_links:
        matches = re.findall(url_pattern, link)
        if matches:
            urls.append(link)
    return urls

def get_paths_from_links(all_links: list) -> list:
    """function to get relative paths from a list
    flags paths that start with ./ or ../
    """
    paths = []
    path_pattern = re.compile(r'(\.{1,2}\/)+([A-Za-z0-9-]+\/)*(.+\.[A-Za-z]+)')

    for link in all_links:
        matches = re.findall(path_pattern, link)
        if matches:
            paths.append(link)
    return paths

def check_paths_exists(file_path : str, paths : list) -> list:
    """function checks if a path exist if not return non existent paths
    flags any relative path that can't be accessed
    """
    broken_path = []
    for path in paths:
        path = re.sub(r'(\?|\&)(WT|wt)\.mc_id=.*', '', path)
        if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(file_path), path))):
            broken_path.append(path)
    return broken_path

def check_url_locale(urls : list) -> list:
    """function checks if a url has country locale
    flags urls that have ==> /en-us/
    """
    country_locale = []
    for url in urls:
        locale_pattern = re.compile(r'\/[a-z]{2}-[a-z]{2}\/')
        matches = re.findall(locale_pattern, url)
        if matches:
            country_locale.append(url)
    return country_locale

def check_url_tracking(urls : list) -> list:
    """function checks if a url has tracking id
    flags urls missing ==> (? or &) plus WT.mc_id= or wt.mc_id=
    """
    tracking_id = []
    for url in urls:
        tracking_pattern = re.compile(r'(\?|\&)(WT|wt)\.mc_id=')
        matches = re.findall(tracking_pattern, url)
        if not matches:
            tracking_id.append(url)
    return tracking_id

def get_input_args() -> None:
    """
    Retrieves and parses the 2 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to created and defined these 2 command line arguments. If 
    the user fails to provide some or all of the 2 arguments, then the default 
    values are used for the missing arguments. 
    Command Line Arguments:
      1. Tutorials Path as --dir
      2. Function to be executed as --func
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object  
    """
    # Parse using ArgumentParser
    parser = argparse.ArgumentParser()

    parser.add_argument('-d', '--dir', type = str, default = './',
                    help = 'path to the root directory', required=True)

    parser.add_argument('-f', '--func', type = str, required = True,
                        help = 'function to be executed',
                        choices=['check_broken_paths',
                                 'check_paths_tracking',
                                 'check_urls_tracking',
                                 'check_urls_locale'])

    return parser.parse_args()


# Call to main function to run the program
if __name__ == "__main__":
    main()

# DEPRECATED
def get_urls_from_file(file_path: str) -> list:
    """function to get an array of urls from a file"""
    urls = []
    with open(file_path, 'r',  encoding="utf-8") as file:
        data = file.read()
        url_pattern = re.compile(r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9]{1,6}\b([-a-zA-Z0-9@:%_\+.~#?&\/\/=]*)')
        matches = re.finditer(url_pattern, data)
        for matched_group in matches:
            urls.append(matched_group.group())
    return urls

def get_paths_from_file(file_path: str) -> list:
    """function to get relative paths from a file"""
    paths = []
    with open(file_path, 'r',  encoding="utf-8") as file:
        data = file.read()
        path_pattern = re.compile(r'(\.{1,2}\/)+([A-Za-z0-9-]+\/)*([A-Za-z0-9]+\.[A-Za-z]+)')
        matches = re.finditer(path_pattern, data)
        for matched_group in matches:
            paths.append(matched_group.group())
    return paths
