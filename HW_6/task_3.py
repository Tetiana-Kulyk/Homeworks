def is_prime(num):
    """Check if the number is prime or not
    """
    if num == 1:
        return "The number should be grater than 1!"
    counter = 0
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            counter += 1
    if counter <= 0:
        return True
    else:
        return False
