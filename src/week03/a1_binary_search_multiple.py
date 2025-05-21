import sys
sys.stdin = open("input.txt", 'r')

# A 배열의 크기 입력
N = int(input())

# A 배열 입력 및 정렬
A = list(map(int, input().split()))
A.sort()

# 검색할 숫자 개수
c = int(input())

# M 배열 입력 (찾고자 하는 숫자들)
M = list(map(int, input().split()))

# M의 각 값에 대해 이진 탐색 수행
for now in M:
    start = 0
    end = len(A) - 1
    found = False

    while start <= end:
        mid = (start + end) // 2

        if A[mid] == now:
            print("1")  # 찾았을 경우 1 출력
            found = True
            break
        elif A[mid] > now:
            end = mid - 1  # 왼쪽 구간 탐색
        else:
            start = mid + 1  # 오른쪽 구간 탐색

    if not found:
        print("0")  # 찾지 못한 경우 0 출력

### 백준 1920. 수찾기