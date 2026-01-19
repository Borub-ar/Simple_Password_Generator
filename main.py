from utils import split_integer, generate_random_characters, generate_random_numbers

password_length = int(input('What length?'))
special_char = bool(input('Include special char?'))
uppercase = bool(input('Include upper case?'))
lowercase = bool(input('Include lower case?'))
numbers = bool(input('Include numbers?'))

# przypisać losową ilość znaków do każdego typu ++
# wygenerować znaki
# połączyć wszystkie znaki w jeden string
# pomieszać powstały string

character_types = []

if special_char:
    character_types.append({
        'type': 'special'
    })
if uppercase:
    character_types.append({
        'type': 'uppercase'
    })
if lowercase:
    character_types.append({
        'type': 'lowercase'
    })
if numbers:
    character_types.append({
        'type': 'numbers'
    })

characters_limits = split_integer(password_length, len(character_types))

for i, type in enumerate(character_types):
    type['char_counter'] = characters_limits[i]

for char_type in character_types:
    if char_type['type'] == 'numbers':
        char_type['generated_characters'] = generate_random_numbers(char_type['char_counter'])
    elif char_type['type'] == 'uppercase':
        char_type['generated_characters'] = generate_random_characters(char_type['char_counter'], True)
    elif char_type['type'] == 'lowercase':
        char_type['generated_characters'] = generate_random_characters(char_type['char_counter'])
    elif char_type['type'] == 'special':
        char_type['generated_characters'] = generate_random_characters(char_type['char_counter'])

print(character_types)
