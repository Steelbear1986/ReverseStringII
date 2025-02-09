class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        h=k
        ans=''
        count=0
        for i in range(0, len(s),k):
            if count%2==0:
                ans+=s[i:h][::-1]
            else: ans += s[i:h]
            h+=k
            count+=1
        return ans