
'''

No theory,,






'''









def accum(s):
    # your code
    ans = ''
    for i in range(len(s)):
        ans = ans + s[i].upper() + s[i].lower()*i  + "-"
    return ans[:-1]
