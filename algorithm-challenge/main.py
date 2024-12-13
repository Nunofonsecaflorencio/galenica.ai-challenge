from solutions import *
import time

if __name__ == "__main__":
    test_case = "abcabcbb"
    print("Test String: ", test_case)
    
    t0 = time.time()
    print("Solution 1")
    print(longest_non_repeating_chars_1("abcabcbb"))
    print("Time:", time.time() - t0)
    
    t0 = time.time()
    print("\nSolution 2")
    print(longest_non_repeating_chars_2("abcabcbb"))
    print("Time:", time.time() - t0)
    
    t0 = time.time()
    print("\nSolution 3")
    print(longest_non_repeating_chars_3("abcabcbb"))
    print("Time:", time.time() - t0)