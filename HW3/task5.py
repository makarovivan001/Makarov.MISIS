def count_digits_and_letters(sequence):
    digit_count = 0
    letter_count = 0
    for char in sequence:
        if char.isdigit(): 
            digit_count += 1
        elif char.isalpha() and char.isascii(): 
            letter_count += 1

    return digit_count, letter_count


input_sequence = input("Введите последовательность символов, заканчивающуюся точкой: ")
digits, letters = count_digits_and_letters(input_sequence)
print(digits, letters)