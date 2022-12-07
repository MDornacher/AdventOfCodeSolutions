"""
Example terminal output:
cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

from aocd.models import Puzzle
from treelib import Tree


DAY = 7
YEAR = 2022

TOTOL_DISK_SPACE = 70_000_000
UPDATE_SIZE = 30_000_000


def main():
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle.answer_a = solve_a(puzzle.input_data)
    puzzle.answer_b = solve_b(puzzle.input_data)


def parse_file_structure_tree(terminal_output: str) -> Tree:
    """
    Example terminal output:
    $ cd /
    $ ls
    dir a
    14848514 b.txt
    8504156 c.dat
    dir d
    $ cd a
    $ ls
    dir e
    29116 f
    2557 g
    62596 h.lst
    $ cd e
    $ ls
    584 i
    $ cd ..
    $ cd ..
    $ cd d
    $ ls
    4060174 j
    8033020 d.log
    5626152 d.ext
    7214296 k
    Return a tree of the file structure
    """
    tree = Tree()
    root = "/"
    full_current_dir = [root]
    tree.create_node(root, root)
    for line in terminal_output.splitlines()[1:]:
        # skip ls command
        if line.startswith("$ ls"):
            continue
        # if command is cd, change directory
        if line.startswith("$ cd"):
            new_dir = line.split()[-1]
            full_current_dir = change_directory(new_dir, full_current_dir)
            continue
        # skip if directory/file name is already in tree
        if line.split()[-1] in tree.all_nodes():
            continue
        # if line is not a command and starts with dir,
        # add directory node to current directory current_dir_name
        # however, directory names are not unique, so add the full path
        if line.startswith("dir") and line.split()[-1] not in tree.all_nodes():
            dir_name = line.split()[-1]
            full_dir_name = "/".join(full_current_dir + [dir_name])
            tree.create_node(dir_name, full_dir_name, parent="/".join(full_current_dir))
        # if line is not a command and does not start with dir,
        # add file node to current directory current_dir_name
        # and add file size to node as data
        # however, directory names are not unique, so add the full path
        else:
            file_name = line.split()[-1]
            full_file_name = "/".join(full_current_dir + [file_name])
            tree.create_node(
                file_name,
                full_file_name,
                parent="/".join(full_current_dir),
                data=int(line.split()[0]),
            )
    return tree


def change_directory(new_dir: str, full_current_dir: list):
    if new_dir == "..":
        full_current_dir.pop()
    else:
        full_current_dir.append(new_dir)
    return full_current_dir


def sum_file_sizes(tree: Tree, directory: str) -> int:
    """
    Sum the file sizes of all files in directory and all subdirectories
    """
    file_sizes = []
    for node in tree.children(directory):
        if node.data is not None:
            file_sizes.append(node.data)
        else:
            file_sizes.append(sum_file_sizes(tree, node.identifier))
    return sum(file_sizes)


def solve_a(puzzle_input):
    file_structure = parse_file_structure_tree(puzzle_input)
    print(file_structure.show())
    # sum up file sizes in each directory and add to total_file_size if directory size is at most 100000
    total_file_size_of_small_directories = 0
    for directory in file_structure.all_nodes():
        # skip root node
        if directory.identifier == "/":
            continue
        if directory.data is None:
            directory_size = sum_file_sizes(file_structure, directory.identifier)
            print(f"{directory.identifier} size: {directory_size}")
            if directory_size <= 100000:
                total_file_size_of_small_directories += directory_size
    return total_file_size_of_small_directories


def solve_b(puzzle_input):
    file_structure = parse_file_structure_tree(puzzle_input)
    print(file_structure.show())
    # sum up file sizes of root directory
    root_dir_size = sum_file_sizes(file_structure, "/")
    # print nicely formated used, free and total disk space
    print(f"Used: {root_dir_size}")
    print(f"Free: {TOTOL_DISK_SPACE - root_dir_size}")
    print(f"Total: {TOTOL_DISK_SPACE}")
    minimal_disk_space_to_be_deleted = UPDATE_SIZE - (TOTOL_DISK_SPACE - root_dir_size)
    print(f"Minimal disk space to be deleted: {minimal_disk_space_to_be_deleted}")
    # find smallest directory that can be deleted to satisfy minimal_disk_space_to_be_deleted
    smallest_directory_to_be_deleted_size = root_dir_size
    # for each directory, check if it is bigger then minimal_disk_space_to_be_deleted
    # and if it is smaller than the current smallest_directory_to_be_deleted_size
    for directory in file_structure.all_nodes():
        # skip root node
        if directory.identifier == "/":
            continue
        if directory.data is None:
            directory_size = sum_file_sizes(file_structure, directory.identifier)
            if directory_size >= minimal_disk_space_to_be_deleted:
                if directory_size < smallest_directory_to_be_deleted_size:
                    smallest_directory_to_be_deleted_size = directory_size
                    print(
                        f"New smallest directory to be deleted: {directory.identifier}"
                    )
    return smallest_directory_to_be_deleted_size


if __name__ == "__main__":
    main()
