class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        orders = sorted(s)
        ordert = sorted(t)

        return orders == ordert