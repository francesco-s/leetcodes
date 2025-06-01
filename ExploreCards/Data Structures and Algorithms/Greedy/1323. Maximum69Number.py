class Solution:
    def maximum69Number2(self, num: int) -> int:
        str_num = str(num)
        to_add = 3
        found = False

        for n in str_num:
            if n == '6' and not found:
                found = True
            elif found:
                to_add *= 10
        
        return num + to_add if found else num
    
    def maximum69Number(self, num: int) -> int:
        str_num_list = list(str(num))
        for i, n in enumerate(str_num_list):
            if n == '6':
                str_num_list[i] = '9'
                break
        return int("".join(str_num_list))




# Test cases
solution = Solution()

# Test case 1
n1 = 9669
print(f"Test case 1: {solution.maximum69Number(n1)}")  # Expected: 9969

# Test case 2
n2 = 9996
print(f"Test case 2: {solution.maximum69Number(n2)}")  # Expected: 9999