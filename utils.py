import random
import string


def split_integer(n, types_count):
    cuts = sorted(random.sample(range(1, n), types_count - 1))

    result = [cuts[0]]
    for i in range(len(cuts) - 1):
        result.append(cuts[i + 1] - cuts[i])
    result.append(n - cuts[-1])

    if len(set(result)) != types_count:
        return split_integer(n, types_count)

    return result


def generate_random_numbers(count):
    return [random.randint(1, 9) for _ in range(count)]


def generate_random_characters(count, uppercase=False):
    if uppercase:
        return [random.choice(string.ascii_uppercase) for _ in range(count)]
    else:
        return [random.choice(string.ascii_lowercase) for _ in range(count)]
