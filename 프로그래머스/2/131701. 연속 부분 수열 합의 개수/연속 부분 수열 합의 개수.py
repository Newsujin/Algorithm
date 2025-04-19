def solution(elements):
    two_elements = elements[:] + elements[:]
    sequence = set()

    for i in range(1, len(elements) + 1):
        for j in range(len(elements)):
            sequence.add(sum(two_elements[j:j + i]))

    return len(sequence)