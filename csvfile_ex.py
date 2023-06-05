import csv

# CSV 파일에 저장할 데이터
data = [
    ["main2.main2.py"]
]

# CSV 파일 열기
with open("premier.csv", mode="w", newline="") as file:
    # CSV writer 생성
    writer = csv.writer(file)

    # 데이터 쓰기
    for row in data:
        writer.writerow(row)

print("CSV 파일 쓰기 완료")