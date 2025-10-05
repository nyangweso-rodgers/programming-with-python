# Codility Assessment

# Description
* There are N empty glasses with a capacity of 1, 2, .... N litres (there is exactly one glass of each unique capacity). You want to pour exactly K litres of water into glasses. Each glass may be either full or empty ( a glass cannot be partially filled). What is the minimum number of glasses that you need to contain K litres of water?

* Write a function:
    ```py
        def solution(N, K):
            pass
    ```

* that, given two integers N and K, return the minimum number of glasses that are needed to contain exactly K litres of water.If it is not possible to pour exactly K litres of water into glasses then the function should return -1.

# Examples
1. Given N = 5 and K = 8, the function should return 2. There are 5 glasses of capacity 1,2,3,4, and 5. You can use 2 glasses with capacity 3 and 5 to hold 8 litres of water.

2. Given N = 4 and K = 10, the function should return 4. You must use all the glasses to contain 10 litres of water.

3. Given N = 1 and K = 2, the function should return -1. There is only one glass with capacity 1, so you cannot pour 2 litres of water.

4. Given N = 10 and K = 5,  the function should return 1. You can use the glass with capacity 5.

# Remark
* Write an efficient algorithm with the following assumptions:
    - N is an integer within the range [1, ...., 1,000,000]
    - K is an integer within the range [1, ---, 1,000,000,000]