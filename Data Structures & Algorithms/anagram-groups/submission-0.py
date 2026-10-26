class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #first check the length of all strings and group all of the ones that are together
        #sort the ones of same length, and if they are the same, they are anagrams
        #for every anagram thats true, append to the final output list
        groups = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())

        
        