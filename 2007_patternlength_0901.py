T = int(input())
for tc in range(1, T+1):
    words = input()
    pattern = ""
    for i in range(1,30): #다 순회하는 동안
        pattern = words[:i] # 일단 지금까지 있는 걸 패턴으로 둠
        if words[i:i + len(pattern)] == pattern: # 같은 길이의 뒤가 같을 때
            print(f"#{tc} {len(pattern)}")
            break # 가장 먼저 나오는 것에서 멈춤