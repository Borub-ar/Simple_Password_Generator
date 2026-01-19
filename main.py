import random

from utils import split_characters_number, generate_random_characters, generate_random_numbers, \
    generate_random_special_characters

password_length = int(input('What length?'))
has_special_char = bool(input('Include special char?'))
has_uppercase = bool(input('Include upper case?'))
has_lowercase = bool(input('Include lower case?'))
has_numbers = bool(input('Include numbers?'))

character_types = []

if has_special_char:
    character_types.append({
        'type': 'special'
    })
if has_uppercase:
    character_types.append({
        'type': 'uppercase'
    })
if has_lowercase:
    character_types.append({
        'type': 'lowercase'
    })
if has_numbers:
    character_types.append({
        'type': 'numbers'
    })

characters_limits = split_characters_number(password_length, len(character_types))

for i, char_type in enumerate(character_types):
    char_type['char_counter'] = characters_limits[i]

for char_type in character_types:
    if char_type['type'] == 'numbers':
        char_type['generated_characters'] = generate_random_numbers(char_type['char_counter'])
    elif char_type['type'] == 'uppercase':
        char_type['generated_characters'] = generate_random_characters(char_type['char_counter'], True)
    elif char_type['type'] == 'lowercase':
        char_type['generated_characters'] = generate_random_characters(char_type['char_counter'])
    elif char_type['type'] == 'special':
        char_type['generated_characters'] = generate_random_special_characters(char_type['char_counter'])

merged_password_characters = []

for char_type in character_types:
    merged_password_characters.extend(char_type['generated_characters'])

random.shuffle(merged_password_characters)
final_password = ''.join(map(str, merged_password_characters))

print(f'Here is your password: {final_password}')
