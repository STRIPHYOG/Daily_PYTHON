def isPalindrome(s: str) -> bool:
    # Filter and normalize the string
    filtered_chars = [char.lower() for char in s if char.isalnum()]
    normalized_str = ''.join(filtered_chars)
    
    # Check if the normalized string is a palindrome
    return normalized_str == normalized_str[::-1]

# Test cases
print(isPalindrome("A man, a plan, a canal: Panama"))  # Output: true
print(isPalindrome("race a car"))                      # Output: false
print(isPalindrome(" "))                               # Output: true
