#вариант 1
def func1
    def sum_of_prime_divisors(number):
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
    
        prime_divisors = []
        for i in range(2, number + 1):
            if number % i == 0 and is_prime(i):
                prime_divisors.append(i)
        return sum(prime_divisors)

    number = int(input("Введите число: "))
    result = sum_of_prime_divisors(number)
    print(number, ":", result)
