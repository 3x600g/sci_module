import os
import shutil

# 원본 파일 경로와 파일 이름을 지정합니다.
original_file_path = 'D:/input/SCI/cases/case.txt'

# 대상 디렉토리 경로를 지정합니다.
target_directory = 'D:/input/SCI/new_cases/no4'

# 대상 디렉토리가 없으면 생성합니다.
os.makedirs(target_directory, exist_ok=True)

# 300부터 452까지의 파일을 생성합니다.
for i in range(3001, 4001):
    # 각 파일의 이름을 생성합니다.
    new_file_name = f"case_{i}.txt"
    new_file_path = os.path.join(target_directory, new_file_name)

    # 원본 파일을 대상 파일로 복사합니다.
    shutil.copy(original_file_path, new_file_path)

print('파일 생성이 완료되었습니다.')