
def longest_non_repeating_chars_1(s): # T: O(n2) S: O(n)
    if not s:
        return ""
    
    substrings = []
    
    for i in range(len(s)): # O(n)
        ch = s[i] # O(1)
        if i == 0:
            substrings.append([ch]) # O(1)
            continue
        if ch in substrings[-1]: # O(n)
            substrings.append([ch]) # O(1)
            continue
        
        substrings[-1].append(ch) # O(1)
        
    return max([len(sub) for sub in substrings]) # O(n) + O(n)


def longest_non_repeating_chars_2(s): # T: O(n2) S: O(n)
    if not s:
        return ""
    if len(s) == 1:
        return s
    
    left = max_length = 0
    char_set = set()
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

def longest_non_repeating_chars_3(s): # T: O(n) S: O(n)
    max_length = 0
    left = 0
    last_seen = {}

    for right in range(len(s)):
        c = s[right]
        if c in last_seen and last_seen[c] >= left:
            left = last_seen[c] + 1
        
        max_length = max(max_length, right - left + 1)
        last_seen[c] = right

    return max_length
    