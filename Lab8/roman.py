class DecimalToRoman:
    def __init__(self, number):
        if not isinstance(number, int) or number <= 0 or number >= 4000:
            raise ValueError("Число: 1-3999")
        self.number = number

    def convert(self):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        num, roman = self.number, ''
        for i, v in enumerate(values):
            count = num // v
            roman += symbols[i] * count
            num -= v * count
        return roman


class RomanToDecimal:
    def __init__(self, roman):
        if not isinstance(roman, str) or not roman.strip():
            raise ValueError("Римське число: непорожній рядок")
        self.roman = roman.upper().strip()

    def convert(self):
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num, prev_value = 0, 0
        for char in reversed(self.roman):
            if char not in roman_dict:
                raise ValueError(f"Невірний символ: {char}")
            value = roman_dict[char]
            if value < prev_value:
                num -= value
            else:
                num += value
                prev_value = value

        if DecimalToRoman(num).convert() != self.roman:
            raise ValueError(f"Некоректний формат: {self.roman}")
        return num
