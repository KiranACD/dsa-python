# Problem Solving

## What are the key ingredients to becoming a good problem solver?

Lets explore the required skills by solving a problem. 

Given a number, check if it is prime.

What is a prime number? Any number greater than 1 and has exactly 2 factors.

Approach 1: Count the number of factors.

```
boolean checkPrime(n){
    int c = 0;
    for (i=0; i<=n; i++){
        if (N%i == 0){
            c++;
        }
    }
    if (c == 2){
        return True;
    }
    return False;
}
```

Lets count the number of iterations we are making in this code. We can see, i takes all values in the range [1, n]. Remember, when we count iterations, we always count iterations for the worst case. This means we count the maximum possible number of iterations.

Now, we make some assumptions. The processor we are going to use will make 10^8 iterations per second. If value of n = 10^9, then the iterations will be performed in 10 seconds. Similarly, if value of n = 10^18, then there will be 10^18 iterations. All the iterations will be performed in 10^10 seconds. This innocuous looking figure is actually approximately 317 years. This code will likely run for 6 generations or so.

Why is this the case? Surely, checking if a number is prime shouldn't be taking this long. We have to make a few optimizations to reduce the runtime. Identifying what optimizations to make will require some observations. And here we reach the first key skill required to become a good problem solver. The ability to make observations about the problem at hand and using these observations to optimize our code.

Lets make an observation related to the problem at hand. Given 3 positive numbers a, b and N, where a*b = N. As a is a factor of N, then N/a will also be a factor of N. 

Lets consider a number 24. The factors of this number are


    i    |   N/i

    1        24
    2        12
    3         8
    4         6
    6         4
    8         3
   12         2
   24         1


What observation can you make given the above table. If we were running an iteration from 1 to 24, then we can observe that every factor of 24 is being visited twice. After a value of i, the factors start repeating. Till i<=N/i, we get unique factors. Once i<N/i, the factors start repeating. 

The maximum value of i till we have unique factors = sqrt(N). Hence, iterating in the range [1, floor(sqrt(N))] will still see all the unique factors of a given number.

```
boolean checkPrime(n){
    c = 0;
    for (i=1; i<=sqrt(n); i++){
        if (N%i == 0){
            if (i*i == N){
                c += 1;
            }
            else {
                c += 2;
            }
            
        }
    }
    if (c == 2){
        return True;
    }
    return False;
}
```

The number of iterations required to check if n=10^18 is prime has come down to 10^9. The time to run these iterations is now 10 seconds. We have taken a solution that took 317 years to check if a number is prime to one that takes just 10 seconds for the same output. This is the power of making observations.


Lets move on to the next question.

Given N, how many times do we have to divide by 2 till it becomes 1.

Lets jump straight into making observations in this case.

Value                 Number of times
N = 1  -------------->       0
N = 2  -------------->       1
N = 4  -------------->       2
N = 8  -------------->       3
N = 32 -------------->       5

The number of times is the power of 2 in each case. Which math function when applied as fn(32) = 5? The answer is log(32) with base 2. So, we have to apply log with base 2 to the number to get the number of times we need to divide by 2 till the number becomes 1. 


With that, lets look at the next question and check if we can make some observations.

Given a perfect square, find the sqrt of the number.

Approach: Sqrt(N) lies in the range [1, N]. The intuitive approach here is to iterate over the range and return i when i*i = N. In the worst case, there are going to be sqrt(N) iterations.

```
int sqrt(N){
    for (i = 1; i<=N; i++){
        if (i*i == N){
            return i;
        }
    }
}
```
If N = 2^32, how many iterations will the above code do? Its 2^16. As the number N gets larger, the number of iterations will increase.

To optimize lets make some observations.

Consider N = 100. We know that sqrt(100) will lie in the range[1, 100]. Let us select i = 50 and check if i*i == N. If i*i > N, then no number above 50 will every be the answer. So we update the range to [1, 49].

We continue this till we reach the value that is the answer. In every step, the size of the array is getting halved. Hence, the total number of steps to be taken is logN with base 2.




