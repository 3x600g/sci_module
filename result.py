import os
import re

# 아웃풋 파일이 있는 디렉토리 경로
output_directory = 'D:/input/SCI/cases'

# 결과를 저장할 파일
result_file_path = 'D:/input/SCI/result/result.txt'

# 결과 파일이 이미 존재하면 삭제
if os.path.exists(result_file_path):
    os.remove(result_file_path)

# 아웃풋 파일을 하나씩 처리
for i in range(1, 5001):
    output_file_path = os.path.join(output_directory, f'case_{i}.o')

    # 아웃풋 파일이 존재하는지 확인
    if os.path.exists(output_file_path):
        with open(output_file_path, 'r') as output_file:
            # 파일의 각 줄을 읽어오기
            for line in output_file:
                # "final result"를 포함하는 줄 찾기
                if "final result" in line:
                    # 숫자 추출하기
                    result_value = re.search(r'\b\d+\.\d+\b', line)
                    if result_value:
                        result_value = result_value.group()
                        # 결과를 파일에 쓰기
                        with open(result_file_path, 'a') as result_file:
                            result_file.write(f"{result_value}\n")
                    break

print(f'Results are saved in {result_file_path}')
