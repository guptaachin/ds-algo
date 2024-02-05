class Solution:
    def simplifyPath(self, path: str) -> str:
        if len(path) == 0: return path
        split_path_stack = path.split("/")
        canonical_stk = []
        # create canonical stk
        for d in split_path_stack:
            if d == "..":
                if len(canonical_stk) > 0:
                    canonical_stk.pop(-1)
            elif d == "" or d == ".":
                continue
            else:
                canonical_stk.append(d)
        # create canonical path from canonical_stk
        canonical_path = ""
        for c in canonical_stk:
            canonical_path += "/" + c
        if canonical_path == "": return "/"
        return canonical_path