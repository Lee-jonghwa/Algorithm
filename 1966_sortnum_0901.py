T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 길이
    nums = list(map(int, input().split()))

    # bubble sort
    for i in range(N-1):
        for j in range(N-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    print(f'#{tc}',*nums)
