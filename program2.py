class Solution(object):
    def romanToInt(self, roman_numeral):
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
        converted_value = 0
        for i in range(len(roman_numeral)):
            current_value = roman_map[roman_numeral[i]]
            if i + 1 < len(roman_numeral) and current_value < roman_map[roman_numeral[i + 1]]:
                converted_value -= current_value
            else:
                converted_value += current_value
        return converted_value
