class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bank = defaultdict(list)
        for s in strs:
            sortedstr = "".join(sorted(s))
            sortedstr = sortedstr
            bank[sortedstr].append(s)
        return list(bank.values())
        