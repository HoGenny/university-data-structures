import sys
sys.stdin = open('input.txt', 'r')

# n: 저장할 사이트 수, howmany: 검색할 횟수
n, howmany = map(int, input().split())

# URL과 비밀번호를 저장할 딕셔너리
findPassword = {}

# n개의 사이트 정보를 입력받아 저장
for _ in range(n):
    url, pw = input().split()
    findPassword[url] = pw  # key: URL, value: password

# howmany개의 URL을 입력받아 비밀번호 출력
for _ in range(howmany):
    url = input()
    print(findPassword[url])

    ### 이 코드는 사이트 주소를 기준으로 비밀번호를 빠르게 찾는 딕셔너리 기반 예제입니다.