def longest_unique_substring(s):
    char_index = {}
    max_length = 0
    start = 0

    for end in range(len(s)):
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1
        char_index[s[end]] = end
        max_length = max(max_length, end - start + 1)

    return max_length


# Test cases
print(longest_unique_substring("abcabcbb"))  # Output: 3 ("abc")
print(longest_unique_substring("bbbbb"))  # Output: 1 ("b")
print(longest_unique_substring("pwwkew"))  # Output: 3 ("wke")




# Project Structure

# /AgrichainAutomation
# │── /tests
# │   ├── test_longest_substring.py
# │── /pages
# │   ├── home_page.py
# │   ├── result_page.py
# │── /utils
# │   ├── browser_setup.py
# │── pytest.ini
# │── requirements.txt

