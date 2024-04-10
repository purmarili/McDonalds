def nth_fibonacci(n: int):
    x_1 = 0
    x_2 = 1
    for _ in range(n - 2):
        new = x_1 + x_2
        x_1 = x_2
        x_2 = new
    return x_2


def nth_fibonacci_recursion(n: int):  # 3
    if n in (0, 1):
        return n

    return nth_fibonacci_recursion(n - 1) + nth_fibonacci_recursion(n - 2)


# 5! = 5 * 4 * 3 * 2 * 1
def factorial(n: int):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def factorial_generator(n: int):
    for number in range(1, n):
        yield number


gen = factorial_generator(5)

# 1 - (n = 5)  - 5 * 24
# 2 - (n = 4)  - 4 * 6
# 3 - (n = 3)  - 3 * 2
# 4 - (n = 2)  - 2 * 1
# 5 - (n = 1)  - 1

print(factorial(5))


# print(nth_fibonacci_recursion(6))


# 1 Lari
#
def coins_recursion_problem(price: int, coins_: list, amount_: int):
    all_variations = []

    def get_min_coins(amount: int, coins: list, coins_given: list):
        if amount == 0:
            all_variations.append(coins_given)
            return
        if len(coins) == 0:
            return
        if amount < 0:
            return

        for coin in coins:
            new_coins = coins.copy()
            new_coins.remove(coin)
            new_coins_given = coins_given.copy()
            new_coins_given.append(coin)
            get_min_coins(amount=amount - coin, coins=new_coins, coins_given=new_coins_given)

    get_min_coins(amount=amount_ - price, coins=coins_, coins_given=[])

    all_variations = sorted(all_variations, key=len)
    return all_variations[0]


print(coins_recursion_problem(price=117, coins_=[50, 50, 50, 60, 120, 20, 11, 11, 2, 4, 6, 1, 1], amount_=200))
