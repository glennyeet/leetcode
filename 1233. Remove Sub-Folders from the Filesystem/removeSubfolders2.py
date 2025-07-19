from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Greedy: O(fnlog(n)) time, O(fn) space, where f is the
        # longest path in folder, and n is the size of folder

        sorted_folders = sorted(folder)
        valid_folders = []
        for path in sorted_folders:
            if not valid_folders or not path.startswith(valid_folders[-1] + "/"):
                valid_folders.append(path)
        return valid_folders
