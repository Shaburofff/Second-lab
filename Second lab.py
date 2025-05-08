DIGITS = {
    '0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
    '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'
}

PATTERN = r'\b97\d{2}\b'

def number_to_words(number):
    """Преобразование числа в последовательность русских слов"""
    return ' '.join(DIGITS[digit] for digit in number)

def process_stream(filename):
    with open(filename, 'r') as file:
        content = file.read()
        
    matches = re.findall(PATTERN, content)
    
    odd_numbers = []
    for match in matches:
        num = int(match)
        if num % 2 != 0:
            odd_numbers.append(num)
    
    count = len(odd_numbers)
    min_odd_number = str(min(odd_numbers)) if odd_numbers else None
    
    print("Подходящие числа:")
    for n in sorted(odd_numbers):
        print(n)
    
    print(f"\nКоличество чисел: {count}")
    if min_odd_number:
        print("Минимальное число прописью:", number_to_words(min_odd_number))

process_stream("2lab.txt")