from typing import List
from collections import defaultdict


class Folder:
    def __init__(self, value: str) -> None:
        self.value = value
        self.subfolders = {}
        self.deleted = False


class FileSystem:
    def __init__(self) -> None:
        self.root = Folder("/")
        self.hash_to_folder = defaultdict(list[Folder])

    def insert(self, path: list[str]) -> None:
        cur_folder = self.root
        for folder in path:
            if folder not in cur_folder.subfolders:
                cur_folder.subfolders[folder] = Folder(folder)
            cur_folder = cur_folder.subfolders[folder]

    def hash_folder(self, folder: Folder) -> int:
        hashes = []
        for subfolder in sorted(folder.subfolders):
            hashes.append(str(self.hash_folder(folder.subfolders[subfolder])))
        merged_hash = "".join(hashes)
        if len(folder.subfolders):
            self.hash_to_folder[merged_hash].append(folder)
        return hash(str(merged_hash) + str(hash(folder.value)))

    def get_undeleted(
        self, undeleted_folders: list[list[str]], folder: Folder, path: list[str]
    ) -> None:
        if folder.deleted:
            return
        if len(path):
            undeleted_folders.append(path[:])
        for subfolder in folder.subfolders:
            path.append(subfolder)
            self.get_undeleted(undeleted_folders, folder.subfolders[subfolder], path)
            path.pop()


class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        # Trie + Hash Function: O(plog(p)) time, O(p) space, where p is the size
        # of paths

        file_system = FileSystem()
        for path in paths:
            file_system.insert(path)
        file_system.hash_folder(file_system.root)
        for hash_value in file_system.hash_to_folder:
            if len(file_system.hash_to_folder[hash_value]) > 1:
                for folder in file_system.hash_to_folder[hash_value]:
                    folder.deleted = True
        remaining_folders = []
        file_system.get_undeleted(remaining_folders, file_system.root, [])
        return remaining_folders
