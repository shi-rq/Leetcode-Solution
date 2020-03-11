# coding=utf-8
'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''


# 1 o(n^2), Brute force
class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        for i in range(2, n):
            is_prime = True
            for j in range(2, i):
                if i % j == 0: is_prime = False
            if is_prime: count += 1
        return count


# 2 Check former primes
class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        prime = []
        for i in range(2, n):
            is_prime = True
            for j in prime:
                if i % j == 0: is_prime = False
            if is_prime:
                count += 1
                prime.append(i)
        return count


# 3 o(nloglogn), Sieve of Eratosthenes, 埃拉托斯特尼筛法
class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        is_prime = [True for i in range(n)]
        for i in range(2, n):
            if is_prime[i]:
                for j in range(2, i):
                    if i % j == 0: is_prime[i] = False
                multiple = 2
                while i * multiple < n:
                    is_prime[i * multiple] = False
                    multiple += 1
        count = 0
        for i in is_prime[2:]:  # 0, 1 aren't primes
            if i: count += 1
        return count


# 4 o(n), Sieve of Ruler, 欧拉筛法
class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        prime = []
        is_prime = [True for i in range(n)]
        for i in range(2, n):
            if is_prime[i]:
                for j in prime:
                    if i % j == 0: is_prime[i] = False
                # check if i is a prime
                for j in prime:
                    if i * j < n:
                        is_prime[i * j] = False
                        if i % j == 0: break
                        # if i is a multiple of j, i * j+1 can be determined by other primes, not need for a repeated check
                    else: break
                # multiples of a prime isn't a prime
            if is_prime[i]:
                count += 1
                prime.append(i)
        return count