# Prime Numbers

Any positive number N such that it has only 2 factors, [1, N].

## Find number of factors of N

Brute Force approach: Check if i, where 1<=i<=N, is a factor of N.
```
ans = 0
for i in range(1, N+1):
    if N%i == 0:
        ans += 1
return ans
```
TC: O(N)
SC: O(1)

Approach 2: Iterate till N/2
```
ans = 0
for i in range(1, N//2):
    if N%i == 0:
        ans += 1
return ans+1
```
TC: O(N)
SC: O(1)

Approach 3:

N = a*b s.t. a<=b
b = N/a
a <= N/a
a^2 <= N
a <= sqrt(N)
```
ans = 0
for i in range(1, sqrt(N)+1):
    if i == N//i:
        ans += 1
    elif N%i == 0:
        ans += 2
return ans
```
TC: O(sqrt(N))
SC: O(1)

## Check if given number N is prime

Prime number N = 1 * N. 
```
def check_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
```
TC: O(sqrt(N))
SC: O(1)

## Find all prime numbers from 1 to N

Brute Force Approach: For all i s.t. 1<=i<=N, check if i is prime num
```
def get_primes(n):
    ans = []
    for i in range(2, n+1):
        if check_prime(i):
            ans.append(i)
    return ans
```
TC: O(N*sqrt(N))
SC: O(1)

Approach 2: Sieve of Eratosthenes
```
def get_primes(n):
    
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5)+1):
        if is_prime[i] is False:
            continue
        for j in range(i*i, n, i):
            is_prime[j] = False
    return [i for i, bool in enumerate(is_prime) if bool is True]
```
TC < (N/2 + N/3 + N/5 + N/7 + ... + 1) < Nlog(N)
(1/2 + 1/3 + 1/4 + 1/5 + 1/6 + ... + 1/N) = log(N) - log(2)

TC: O(Nlog(log(N)))
SC: O(N) 

Consider N doors numbered from 1 to N. Initially all doors are closed. A person is standing in front of every door. 
- The first person toggles the state of every single door starting from the first door till the Nth door. The sequence is 1, 2, 3, 4, 5,...., N
- The second person toggles the state of every second door starting from the second door. 2, 4, 6, 8, 10,....
- The third person toggles the state of every third door starting from the third door. 3, 6, 9, 12,......
- This goes on till the person standing in front of the Nth door.

Return the number of doors that will remain open after all the passes.

When you change the state of the door even number of times - the doors retain their original state. When you change the state of the door odd number of times, the doors will be in the opposite state.

The number of times a door's state is toggled is the number of factors of the prticular door number. As 2 has 2 factors, the door number 2's state will be toggled 2 times.

Now, the question becomes, how many numbers from 1 to N have odd factors? The answer is the number of perfect squares between 1 and N. This is because only perfect squares have odd number of factors. 
```
def count_perfect_squares(n):
    return int(n**0.5)
```
