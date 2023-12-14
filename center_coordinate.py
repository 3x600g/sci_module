import os

# 대상 디렉토리 경로를 지정합니다.
directory_path = 'D:/input/SCI/cases'

# coordinate.txt 파일 경로를 지정합니다.
coordinate_file_path = 'D:/input/SCI/result/coordinate.txt'

# coordinate.txt 파일이 이미 존재하면 삭제합니다.
if os.path.exists(coordinate_file_path):
    os.remove(coordinate_file_path)

# 파일 이름의 템플릿을 정의합니다.
file_template = "case_{}.txt"

# 원본 파일에서 수정할 원본 파일 개수를 지정합니다.
for i in range(1, 5001):
    # 각 파일의 이름을 생성합니다.
    file_name = file_template.format(i)
    file_path = os.path.join(directory_path, file_name)

    # 파일을 읽어서 수정합니다.
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 수정할 input 파일 내의 index 범위를 설정합니다.
    line_start = 220
    line_end = 222

    # 511이 포함된 줄에서 숫자 추출
    for j in range(line_start - 1, line_end):
        if "511    3" in lines[j]:
            try:
                # 괄호 안의 공백으로 구분된 두 숫자를 추출
                numbers = lines[j].split('(')[1].split(')')[0].split()
                x, y = map(float, numbers)

                # 결과를 coordinate.txt 파일에 추가
                with open(coordinate_file_path, 'a') as coordinate_file:
                    coordinate_file.write(f"{x} {y}\n")
            except (ValueError, IndexError):
                print(f"Skipping line {j + 1}: {lines[j]}")

print('추출이 완료되었습니다.')
