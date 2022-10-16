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
