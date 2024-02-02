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

def func2
    def count_odd_digits(num):
        count = 0
        num = abs(num)  

        while num > 0:
            digit = num % 10 
            if digit > 3 and digit % 2 != 0:
                count += 1
            num //= 10

        return count
    number = int(input("Введите число: "))
    result = count_odd_digits(number)
    print(number, ":", result)
