class LuhnValidator:
    def __init__(self):
        self.stack = []
    def push_digit(self, digit):
        """Push a digit onto the stack."""
        self.stack.append(digit)
    def pop_digit(self):
        """Pop a digit from the stack."""
        if self.stack:
            return self.stack.pop()
        return None
    def validate(self, card_number):
        """Validate the card number using the Luhn algorithm."""
        card_number = ''.join(filter(str.isdigit, card_number))
        if len(card_number) < 2:
            return False
        for index, digit in enumerate(reversed(card_number)):
            digit = int(digit)
            if index % 2 == 1:
                digit *= 2
                if digit > 9:
                    digit -= 9
            self.push_digit(digit)
        total_sum = 0
        while self.stack:
            total_sum += self.pop_digit()
        return total_sum % 10 == 0
if __name__ == "__main__":
    validator = LuhnValidator()
    
    test_card_numbers = [
        "4539 1488 0343 6467",  
        "6011 1111 1111 1117",  
        "3782 8224 6310 005",    
        "1234 5678 9012 3456", 
        "4532 1488 0343 6467",  
        "1234 5678 9012 345"    
    ]

    for card_number in test_card_numbers:
        is_valid = validator.validate(card_number)
        print(f"Card Number: {card_number} - Valid: {is_valid}")
