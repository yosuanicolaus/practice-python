class Solution:
    def countDigits(self, num: int) -> int:
        digits = str(num)
        count = 0

        for digit in digits:
            digit_val = int(digit)
            if num % digit_val == 0:
                count += 1

        return count
