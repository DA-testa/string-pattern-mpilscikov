# python3

def read_input():

    input_type = input().rstrip()

    if 'I' in input_type:
        pattern = input().rstrip()
        text = input().rstrip()

    elif 'F' in input_type:
        file_name = input().rstrip()
        if 'a' in file_name:
            raise Exception('a in filename')

        with open(f'test/{file_name}', 'r', encoding='utf-8') as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()

    else:
        raise Exception('wrong input')

    return (pattern, text)


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

