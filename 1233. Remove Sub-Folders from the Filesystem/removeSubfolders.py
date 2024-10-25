class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folders = set(folder)
        valid_folders = []
        for f in folder:
            is_subfolder = False
            for i in range(1, len(f)):
                if f[i] == "/":
                    if f[:i] in folders:
                        is_subfolder = True
                        break
            if not is_subfolder:
                valid_folders.append(f)
        return valid_folders
