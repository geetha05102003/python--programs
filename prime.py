def find_primes_in_range(start, end):
    return [num for num in range(start, end + 1) if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]

# Example usage
start = 10
end = 50
print(find_primes_in_range(start, end))
