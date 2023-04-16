def read_input():
    input_type = input().rstrip()

    if 'I' in input_type:
        return (input().rstrip(), input().rstrip())

    elif 'F' in input_type:
        file_name = '06'

        with open(f'test/{file_name}', 'r', encoding='utf-8') as file:
            return (file.readline().rstrip(), file.readline().rstrip())

    else:
        raise Exception('wrong input')


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    p_len, t_len = map(len, (pattern, text))
    p_hash, t_hash = map(hash, (pattern, text))

    occurences = []

    t_hash = hash(text[:p_len])

    for i in range(t_len - p_len + 1):
        
        if p_hash == t_hash and pattern == text[i:i+p_len]:
            occurences.append(i)

        if i < t_len - p_len:
            t_hash = hash(text[i+1:i+p_len+1])

    return occurences


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

