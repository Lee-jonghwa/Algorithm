def simulate_gravity(grid):
    N = len(grid)

    # 하강 시뮬레이션 (열을 기준으로)
    for col in range(N):
        stack = []
        for row in range(N):
            if grid[row][col] == 1:
                stack.append(1)
        # 맨 아래부터 채워 나간다
        for row in range(N - 1, -1, -1):
            if stack:
                grid[row][col] = stack.pop()
            else:
                grid[row][col] = 0

    # 오른쪽 이동 시뮬레이션 (행을 기준으로)
    for row in range(N):
        stack = []
        for col in range(N):
            if grid[row][col] == 1:
                stack.append(1)
        # 맨 오른쪽부터 채워 나간다
        for col in range(N - 1, -1, -1):
            if stack:
                grid[row][col] = stack.pop()
            else:
                grid[row][col] = 0

    return grid


def count_blocks(grid):
    N = len(grid)

    # 맨 아래 행에 있는 블록 수
    bottom_row_count = sum(grid[N - 1][col] for col in range(N))

    # 맨 오른쪽 열에 있는 블록 수
    right_column_count = sum(grid[row][N - 1] for row in range(N))

    return bottom_row_count, right_column_count


def main():
    T = int(input().strip())
    for test_case in range(1, T + 1):
        N = int(input().strip())
        grid = []
        for _ in range(N):
            grid.append(list(map(int, input().split())))

        # 시뮬레이션 진행
        grid = simulate_gravity(grid)

        # 블록 수 세기
        bottom_row_count, right_column_count = count_blocks(grid)

        # 결과 출력
        print(f"#{test_case} {bottom_row_count} {right_column_count}")


if __name__ == "__main__":
    main()
