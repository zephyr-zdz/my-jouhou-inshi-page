# collect all the .md files -r in the ../content folder and build an index into ./index.md in an Obsidian friendly format
# Example file:
# ---
# title: Welcome to my notes
# ---
# {a blank line}
# - folder1
# {2space} - subfolder1
# {2space}{2space} - [file1](file1.md)
# {2space}{2space} - [file2](file2.md)
# {a blank line}
# - folder2
# ...

import os
import re
def clean_text(text, rules=None):
    file_replace_dict = {
        " ": "-",
        "&": "-and-",
    } if rules is None else rules
    for i, j in file_replace_dict.items():
        text = text.replace(i, j)
    return text

def buildIndexTree():
    # folder: {foldername:"", orig_name: "", subfolders: [subfolders], files: [files]}

    # build the tree and the index
    folders_tree = {"subfolders": {}, "files": []}
    for root, dirs, files in os.walk("../content"):
        if ".git" in root or ".obsidian" in root or "../content" == root:
            continue
        path = root.replace("../content\\", "").split(os.sep)
        current_folder = folders_tree
        for folder in path:
            foldername = clean_text(folder)
            if foldername not in current_folder["subfolders"]:
                current_folder["subfolders"][foldername] = {"orig_name": folder, "subfolders": {}, "files": []}
            current_folder = current_folder["subfolders"][foldername]
        for file in files:
            if file.endswith(".md"):
                current_folder["files"].append({"file": file, "cleaned_file": clean_text(file)})
    return folders_tree

def buildIndexFile():
    # build the index file
    folders_tree = buildIndexTree()
    def buildIndexFileRecursively(folders_tree, depth, current_folder=""):
        # - folder
        #   - subfolder
        #     - [file1](folder/subfolder/file1.md)
        #   - [file](folder/file.md)
        text = ""

        rules = {
            "CBMS-": "",
            "IS_CS-": "",
            "IS_Math-": "",
            ".md": "",
        }

        for file in folders_tree["files"]:
            filename = clean_text(file["file"], rules)
            text += ("  " + "- [" + filename + "](" + current_folder + file["cleaned_file"]+ ")\n")

        text += "\n"

        for folder in folders_tree["subfolders"]:
            text += "#" * (depth+1) + " " + folders_tree["subfolders"][folder]["orig_name"] + "\n\n"
            text += buildIndexFileRecursively(folders_tree["subfolders"][folder], depth + 1, current_folder + folder + "/")

        return text

    index_file = buildIndexFileRecursively(folders_tree, 1, "")

    return index_file

if __name__ == "__main__":
    titles = "---\ntitle: Home\n---\n\n"
    titles += "Welcome to my notes on entrance exams of CS Master program, IST, UTokyo "
    titles += "and CBMS Master program, GSFS, UTokyo\n\n"
    titles += "# Table of Contents\n\n"
    buildIndexFile()
    with open("./index.md", "w", encoding="utf-8") as f:
        f.write(titles + buildIndexFile())
