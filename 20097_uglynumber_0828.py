import heapq

def ugly_numbers(k_values):
    heap = []
    heapq.heappush(heap, 1) # 가장 첫 ugly number 1을 push
    visited = set() # ugly number 중 중복 제거
    visited.add(1) # visited에 1 추가

    # ugly number를 저장하는 리스트
    ugly_numbers_list = []

    # ugly number 오름차순 생성
    while len(ugly_numbers_list) < max(k_values): # 주어진 값 까지만 생성
        current_ugly = heapq.heappop(heap) # 현재 ugly 팝
        ugly_numbers_list.append(current_ugly) # 현재 ugly 리스트에 저장

        for factor in [2, 3, 5]: # 2, 3, 5를 번갈아가변서
            new_ugly = current_ugly * factor # 일단 곱해보기
            if new_ugly not in visited: # visited가 없으면
                visited.add(new_ugly) # 방문추가
                heapq.heappush(heap, new_ugly) # 힙 추가

    # 각 K 번째에 해당하는 ugly number 를 반환합니다.
    result = [ugly_numbers_list[k - 1] for k in k_values]
    return result


# 입력
Q = int(input())  # 찾는 숫자 개수
k_values = list(map(int, input().split())) # k 번째 값

# 출력
result = ugly_numbers(k_values)
print(*result)

"""
# Function to get the nth ugly number


def getNthUglyNo(n):
    ugly = [0] * n  # To store ugly numbers

    # 1 is the first ugly number
    ugly[0] = 1

    # i2, i3, i5 will indicate indices for
    # 2,3,5 respectively
    i2 = i3 = i5 = 0

    # Set initial multiple value
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5

    # Start loop to find value from
    # ugly[1] to ugly[n]
    for l in range(1, n):

        # Choose the min value of all
        # available multiples
        ugly[l] = min(next_multiple_of_2,
                      next_multiple_of_3,
                      next_multiple_of_5)

        # Increment the value of index accordingly
        if ugly[l] == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = ugly[i2] * 2

        if ugly[l] == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = ugly[i3] * 3

        if ugly[l] == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = ugly[i5] * 5

    # Return ugly[n] value
    return ugly[-1]


# Driver Code
def main():
    n = 150

    print
    getNthUglyNo(n)


if __name__ == '__main__':
    main()

    # ugly number count
    count = 1

    # Check for all integers until
    # ugly count becomes n
    while n > count:
        i += 1
        if isUgly(i):
            count += 1
    return i


# Driver code
no = getNthUglyNo(150)
print("150th ugly no. is ", no)

# This code is contributed by "Sharad_Bhardwaj".
"""
"""

# Function to get the nth ugly number


def getNthUglyNo(n):
    ugly = [0] * n  # To store ugly numbers

    # 1 is the first ugly number
    ugly[0] = 1

    # i2, i3, i5 will indicate indices for
    # 2,3,5 respectively
    i2 = i3 = i5 = 0

    # Set initial multiple value
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5

    # Start loop to find value from
    # ugly[1] to ugly[n]
    for l in range(1, n):

        # Choose the min value of all
        # available multiples
        ugly[l] = min(next_multiple_of_2,
                      next_multiple_of_3,
                      next_multiple_of_5)

        # Increment the value of index accordingly
        if ugly[l] == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = ugly[i2] * 2

        if ugly[l] == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = ugly[i3] * 3

        if ugly[l] == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = ugly[i5] * 5

    # Return ugly[n] value
    return ugly[-1]


# Driver Code
def main():
    n = 150

    print
    getNthUglyNo(n)


if __name__ == '__main__':
    main()
"""
"""
# Python Implementation of the above approach
def uglynumber(n):
    # Base cases...
    if (n == 1 or n == 2 or n == 3 or n == 4 or n == 5):
        return n
    s = [1]
    n -= 1

    while (n):
        it = s[0]

        # Get the beginning element of the set
        x = it

        # Deleting the ith element
        s = s[1:]
        s = set(s)

        # Inserting all the other options
        s.add(x * 2)
        s.add(x * 3)
        s.add(x * 5)
        s = list(s)
        s.sort()
        n -= 1
    # The top of the set represents the nth ugly number
    return s[0]

Q = int(input())

a, b, c = map(int, input().split())

# Function call
print(uglynumber(a),uglynumber(b),uglynumber(c),)

# This code is contributed by Shubham Singh

"""
"""
# Python Program to implement
# the above approach

def upper_bound(a, low, high, element):
    while (low < high):
        middle = low + (high - low) // 2
        if (a[middle] > element):
            high = middle
        else:
            low = middle + 1

    return low


# Print nth Ugly number
def uglynumber(n):
    pow = [1] * 40

    # stored powers of 2 from
    # pow(2,0) to pow(2,30)
    for i in range(1, 31):
        pow[i] = pow[i - 1] * 2

    # Initialized low and high
    l = 1
    r = 2147483647

    ans = -1

    # Applying Binary Search
    while (l <= r):

        # Found mid
        mid = l + ((r - l) // 2)

        # cnt stores total numbers of ugly
        # number less than mid
        cnt = 0

        # Iterate from 1 to mid
        i = 1
        while (i <= mid):

            # Possible powers of i less than mid is i
            j = 1
            while (j * i <= mid):
                # possible powers of 3 and 5 such that
                # their product is less than mid

                # using the power array of 2 (pow) we are
                # trying to find the max power of 2 such
                # that i*J*power of 2 is less than mid

                cnt += upper_bound(pow, 0, 31, mid // (i * j))
                j *= 3

            i *= 5

        # If total numbers of ugly number
        # less than equal
        # to mid is less than n we update l
        if (cnt < n):
            l = mid + 1

        # If total numbers of ugly number
        # less than equal to
        # mid is greater than n we update
        # r and ans simultaneously.
        else:
            r = mid - 1
            ans = mid
    return ans

Q = int(input())

a, b, c = map(int, input().split())

# Function Call
print(uglynumber(a),uglynumber(b),uglynumber(c))

# This code is contributed by code_hunt.
"""