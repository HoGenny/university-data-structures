import sys
sys.stdin = open('input.txt', 'r')

def solve():
    # 입력: N은 수의 개수, K는 추적할 이동 횟수
    N, K = map(int, input().split())
    data = list(map(int, input().split()))
    count = 0  # 이동 횟수 카운트

    # 삽입 정렬 수행
    for i in range(1, N):
        key = data[i]
        j = i - 1

        # 왼쪽으로 밀어내는 동안 count 증가
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            count += 1
            if count == K:
                print(data[j])  # K번째 이동된 값 출력
                return
            j -= 1

        # key를 제자리에 넣을 때도 이동으로 간주
        if j + 1 != i:
            data[j + 1] = key
            count += 1
            if count == K:
                print(key)  # K번째 이동된 값 출력
                return

    # K번 이동이 일어나지 않으면 -1 출력
    print(-1)

solve()

### 백준 24051. 알고리즘 수업 - 삽입 정렬 1