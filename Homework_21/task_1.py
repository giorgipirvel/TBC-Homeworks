def norm_sequence(n):
    sequence = [n]

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        sequence.append(n)

    return sequence

def cached_sequence(n, cache={}):
    if n in cache:
        return cache[n]
    
    sequence = [n]
    
    if n == 1:
        return sequence
    
    if n % 2 ==0:
        next = cached_sequence(n // 2, cache)
    else:
        next = cached_sequence(n *3 + 1, cache)

    sequence = sequence + next
    cache[n] = sequence
    return sequence

n = int(input("Enter number: "))

print("sequence - normal:")
print(norm_sequence(n))

print("\nsequence - caching:")
print(cached_sequence(n))
