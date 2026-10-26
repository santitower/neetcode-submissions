class Solution:

    def encode(self, strs: List[str]) -> str:
        big_str = ""
        for estr in strs:
            big_str += str(len(estr)) + "#" + estr
        return big_str



    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find the delimiter after the length.
            while s[j] != "#":
                j += 1

            # Read the length, which may have multiple digits.
            length = int(s[i:j])

            # Content starts immediately after "#".
            start = j + 1
            word = s[start:start + length]
            result.append(word)

            # Move to the beginning of the next length.
            i = start + length

        return result
