class Solution:
    def interpret(self, command: str) -> str:
        str = command.replace("()","o")
        str = str.replace("(al)","al")
        return str