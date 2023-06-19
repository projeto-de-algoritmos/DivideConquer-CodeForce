import sys

def calculate_max_strength(n, q, pokemon_strengths, swaps):
    max_strengths = []
    current_strength = 0
    max_difference = lambda a, b: a - b if a - b > 0 else 0

    for i in range(n + 1):
        if pokemon_strengths[i] > pokemon_strengths[i - 1]:
            current_strength += pokemon_strengths[i] - pokemon_strengths[i - 1]

    max_strengths.append(current_strength)

    for i in range(q):
        left_index, right_index = swaps[i]
        if left_index == right_index:
            max_strengths.append(current_strength)
            continue

        left_strength, right_strength = pokemon_strengths[left_index], pokemon_strengths[right_index]
        left_prev_strength = pokemon_strengths[left_index - 1]
        right_smaller_than_n = right_index < n

        if right_smaller_than_n:
            right_next_strength = pokemon_strengths[right_index + 1]

        pokemon_strengths[left_index], pokemon_strengths[right_index] = right_strength, left_strength
        loss_value = next_value = 0

        if right_index - left_index < 2:
            if right_strength > left_strength:
                loss_value += right_strength - left_strength
            if left_strength > left_prev_strength:
                loss_value += left_strength - left_prev_strength
            if right_smaller_than_n and right_next_strength > right_strength:
                loss_value += right_next_strength - right_strength
            if left_strength > right_strength:
                next_value += left_strength - right_strength
            if right_strength > left_prev_strength:
                next_value += right_strength - left_prev_strength
            if right_smaller_than_n and right_next_strength > left_strength:
                next_value += right_next_strength - left_strength
        else:
            left_next_strength, right_prev_strength = pokemon_strengths[left_index + 1], pokemon_strengths[right_index - 1]

            if left_next_strength > left_strength:
                loss_value += left_next_strength - left_strength
            if left_strength > left_prev_strength:
                loss_value += left_strength - left_prev_strength
            if right_strength > right_prev_strength:
                loss_value += right_strength - right_prev_strength
            if right_smaller_than_n and right_next_strength > right_strength:
                loss_value += right_next_strength - right_strength
            if left_next_strength > right_strength:
                next_value += left_next_strength - right_strength
            if right_strength > left_prev_strength:
                next_value += right_strength - left_prev_strength
            if left_strength > right_prev_strength:
                next_value += left_strength - right_prev_strength
            if right_smaller_than_n and right_next_strength > left_strength:
                next_value += right_next_strength - left_strength

        current_strength += next_value - loss_value
        max_strengths.append(current_strength)

    return max_strengths


num_test_cases = int(sys.stdin.readline())
results = []

for _ in range(num_test_cases):
    num_pokemon, num_operations = map(int, sys.stdin.readline().split())
    pokemon_strengths = [0] + list(map(int, sys.stdin.readline().split()))
    swaps = [list(map(int, sys.stdin.readline().split())) for _ in range(num_operations)]
    max_strengths = calculate_max_strength(num_pokemon, num_operations, pokemon_strengths, swaps)
    results.extend(max_strengths)

print('\n'.join(map(str, results)))

