## Task 1
# TODO: add task description
def congruent_mod(b: int, n: int, lower: int, upper: int) -> list[int]:
    if n == 0:
        raise ValueError("Divison by zero is undefined!")
    if lower > upper:
        raise ValueError("Lower cannot be greater than upper!")
    
    congruent_list = []
    for a in range(lower, upper + 1):
        if a % n == b % n:
            congruent_list.append(a)
            
    return congruent_list

## Task 2
# TODO: add task description
def divisors(x: int) -> list[int]:
    factors = []
    for i in range(1, abs(x) + 1):
        if not x % i:
            factors.append(i)
    if x < 0:
        inverse_factors = [factor * -1 for factor in factors]
        factors.extend(inverse_factors)
    return factors

## Task 3
# TODO: add task description
def greatest_common_divisor(a: int, b: int) -> int:
    if a == b:
        return a
    elif a == 0:
        return max(divisors(b))
    elif b == 0:
        return max(divisors(a))
    else:
        set_a = set(divisors(a))
        set_b = set(divisors(b))
        common = set_a.intersection(set_b)

        return max(common)
    
## Task 4
# TODO: add task description
def multiplicative_inverse(a: int, b: int, n: int) -> bool:
    if (a * b) % n == 1:
        return True
    else:
        return False

## Task 5
# TODO: add task description
def relatively_prime(a: int, b: int) -> bool:
    return greatest_common_divisor(a, b) == 1

## Task 6
# TODO: add task description
def january_first(n: int) -> str:
    calendar = {
        0 : "Sunday",
        1 : "Monday",
        2 : "Tuesday",
        3 : "Wednesday",
        4 : "Thursday",
        5 : "Friday",
        6 : "Saturday",
    }
    
    day = (n + ((n - 1) // 4) - ((n - 1) // 100) + ((n - 1) // 400)) % 7
    return calendar[day]

## Task 7
# TODO: add task description
def relatively_prime_euclid(a: int, b: int) -> bool:
    if a < 0 or b < 0:
        raise ValueError("Integer values must be greater than or equal to zero!")
    
    def gcd(a: int, b: int) -> int:
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    
    return gcd(a, b) == 1