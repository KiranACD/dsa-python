# Time Complexity and Space Complexity

## Maths Concepts

1. How many times do we need to divide by 2 to reduce N to 1?

logN with base 2.

2. [a, b] means all numbers between a and b inclusive of a and b. (a, b) means all numbers between a and b exclusive of a and b. So in the range [3, 10], there are 8 numbers. Generalizing this, in [a, b] we have b-a+1 numbers. In (a, b) we have b-a-1 numbers.

3. Arithmetic progression is a series of numbers where every 2 consecutive numbers have the same difference. 
Sum of first N terms of an aithmetic progression = N/2 * [2a + (N-1) * d] where d is the difference between consecutive terms and a is the first term of the series.

4. Geometric Progression is a series of numbers where every 2 consecutive numbers have the same ratio.
Sum of the first N terms of GP = (a * ((r^N) - 1)) / (r-1) when r > 1. Here a is the first term of the progression, r is the common ratio.

5. log(x) with base a. The number of times we have to divide x by a till x becomes 1. Given this definition, log(a^x) with base a = x. We have to divide a^x by a, x number of times to get 1.

## Counting Iterations

Count the number of iterations in the following bits of code

```
int fn(N){
    s = 0;
    for (i = 1; i <= N; i++){
        s += i;
    }
    return s;
}
```
Iterations run along the range [1, N] and hence hence the number of iterations = N - 1 + 1 = N.

------------------------------------------------------
```
void fn(int N, int M){
    for (i = 1; i <= N; i++){
        if (i%2 == 0){
            print(i);
        }
    }
    for (j = 1; j <= M, j++){
        if (j%2 == 1){
            print(j);
        }
    }
}
```
This is the same concept as above. The code inside the for loop does not, in this case, affect the number of iterations this code runs. However there are two consecutive set of for loops. So, the code will first loop N times and then M times.

So the answer = (N - 1 + 1) + (M - 1 + 1) = N + M. .

------------------------------------------------------
```
int fn(int N){
    s = 0;
    for (i = 1; i <= N; i = i + 2){
        s = s + i;
    }
    return s;
}
```

Here i starts from 1 and we increment it by 2 each time. So i takes only odd numbers. So number of iterations = number of odd numbers in the range [1, N]. If the value of N is even, the count of odd numbers = N/2. If the value of N is odd, the count of odd numbers = int(N/2) + 1. So the number of odd numbers if N = 3 is 2 and if N = 4 is 2. How can we get a generic formula to account for both odd and even case? If N = 3 and we do (N+1)/2, then it gives us 2. If N = 4 and we do (N+1)/2, then too it given us 2 (interger division). So thats the answer for the number of iterations for this piece of code.

------------------------------------------------------
```
int fn(int N){
    s = 0;
    for (i = 0; i <= 100, i++){
        s = s + i + i^2;
    }
    return s;
}
```
Number of iterations will be the number of values in range [0, 100]. As per the formula we saw earlier, number of iterations = 100 - 0 + 1 = 101.

------------------------------------------------------
```
int fn(int N){
    s = 0;
    for (i = 1; i*i <= N; i++){
        s = s + i^2;
    }
    return s
}
```
The breaking condition in the for loop is that i * i <= N. Which means i <= sqrt(N). Hence the number of iterations in the range [1, sqrt(N)] = sqrt(N).

------------------------------------------------------
```
void fn(int N){
    i = N;
    while (i>1){
        i = i/2;
    }
}
```
Lets look at the values i will take in each loop in the above code.

i(before)   |   Iteration    |  i(after)

    N               1              N/2
    N/2             2              N/4
    N/4             3              N/8
    N/8             4              N/16

Here, we are dividing N by 2 at every iteration. When i becomes 1 we stop the iteration. As we have already seen, the number of times we need to divide N by 2 to reduce it to 1 is log(N) with base 2.

Looking at it mathematically, lets assume it takes k iteration of dividing by to reduce N to 1. Hence we get,

N/(2^k) = 1
2^k = N
Taking log to the base 2 on both sides,
log(2^k) = log(N)
k = log(N)

------------------------------------------------------
```
void fn(int N){
    for (i = 1; i <= 10; i++){
        for (j= 1; j <= N; j++){
            print(i*j);
        }
    }
}
```
Count the number of iterations happenning here instead of directly doing 10 * N. We have to count the number of times the inner loop runs, lets say x, and count the number of times the outer loop runs lets say y, then the total number of iterations will be x*y. Lets look at the values i and j take in each iteration.

    i   |   j   |   Inner Loop Iterations
    1     [1, N]            N
    2     [1, N]            N
    3     [1, N]            N
    4     [1, N]            N
    5     [1, N]            N
    6     [1, N]            N
    7     [1, N]            N
    8     [1, N]            N
    9     [1, N]            N
    10    [1, N]            N

Now add up the inner loop iteration and we get the total number of iterations. Directly multiplying x and y will not always give us the right answer.

------------------------------------------------------
```
void fn(int N){
    for (i = 0; i < N; i++){
        for (j= 0; j < N; j++){
            print(i*j);
        }
    }
}
```
In this case, if we make a table as above and add up all the inner loop iterations, then we will get N^2 number of iterations. The inner loop will run N outer loop number of times.

------------------------------------------------------
```
void fn(int N){
    for (i = 1; i <= N; i++){
        for (j = 1; j <= N; j = j*2){
            print(i*j);
        }
    }
}
```
The number of inner loop iterations are logN with base 2. The inner loop iterations will run N times. So the number of iterations = N * logN.

------------------------------------------------------
```
void fn(int N){
    for (i = 1; i <= 2^N; i++){
        print(i);
    }
}
```
The number of iterations = number of values in range [1, 2^N] = 2^N - 1 + 1 = 2^N.

------------------------------------------------------
```
void fn(N){
    for (i = 1; i <= N; i++){
        for (j = 1; j <= 2^i; j++){
            print(i*j);
        }
    }
}
```
Lets build the table for this one.

    i   |   j   |   Inner Loop Iterations
    1     [1, 2]            2
    2     [1, 4]            4
    3     [1, 8]            8
    4     [1, 16]           16
    .       .               .
    .       .               .
    .       .               .
    N     [1, 2^N]          2^N

The inner loop iterations form a geometric progression and we have to find the sum of N terms of these values.

Sum(Inner Loop Iterations) = (a * (r^N - 1)) / (r-) = 2*(2^N - 1).

## How to calculate Big O notation from number of iterations.

1) Neglect all lower order terms relative to the term with the highest power. 
2) Neglect all the coeficients of the highest order term.

eg. number of iterations = 4N^2 + 3N + 1. 
O(N) = N^2

eg. number of iterations = 3N*sqrt(N) + 4logN + 31NlogN.
Which is the term with the highest power here? In such cases, we substitute N with a large number, eg 2^32. Then we get, N * sqrt(N) = 2^32 * 2^16. NlogN = 2^32 * 32. In this case, undoubtedly, Nsqrt(N) is the biggest power term.
O(N) = Nsqrt(N)

When the highest order term in your number of iterations has a power of 0, then that is known as constant time complexity.
If, number of iterations = 100, then O(N) = 1.




