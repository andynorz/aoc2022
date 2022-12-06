import string

def main(inputs: list):
    
    sum = 0
    char_values = dict(zip(string.ascii_lowercase + string.ascii_uppercase, range(1,53)))

    for input in inputs:
        input_len_half = len(input) // 2
        first, second = set(input[0:input_len_half]), set(input[input_len_half:])

        intersect = first.intersection(second)
        for k in intersect:
            sum += char_values[k]
        
    return sum

inputs = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg", "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]
print(main(inputs))