# https://leetcode.com/problems/design-file-system/
class FileSystem:

    def __init__(self):
        self.filesystem = {}


    def createPath(self, path: str, value: int) -> bool:
        if path in ['', '/']:
            return False

        if path in self.filesystem:
            return False

        paths = path.split('/')
        if len(paths) > 2:
            index = len(paths) - 1
            while index > 1:
                if '/'.join(paths[:index]) not in self.filesystem:
                    return False
                index -= 1

        self.filesystem[path] = value
        return True


    def get(self, path: str) -> int:
        return self.filesystem[path] if path in self.filesystem else -1


