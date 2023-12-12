import os
import numpy as np
import subprocess

# 디렉토리 경로를 지정합니다.
directory_path = 'D:/input/SCI/new_cases/no4'

# 파일 이름의 템플릿을 정의합니다.
file_template = "case_{}.txt"

# 숫자 범위를 설정합니다.
for i in range(3001, 4001):
    # 각 파일의 이름을 생성합니다.
    file_name = file_template.format(i)
    file_path = os.path.join(directory_path, file_name)

    # 파일을 읽어서 수정합니다.
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 수정할 input 파일 내의 index 범위를 설정합니다(trcl 들어가는 index).
    line_start = 58
    line_end = 394

    # 핵연료 집합체
    for j in range(line_start-1, line_end):
        if "406    3" in lines[j]:
            x = round(np.random.uniform(-0.8184, 0.8184), 4)
            x = '{:.4f}'.format(x)
            y = round(np.random.uniform(-0.8184, 0.8184), 4)
            y = '{:.4f}'.format(y)
            modified_line = lines[j].replace("(0 0)", f"({x} {y})")
            lines[j] = modified_line

        if "421    3" in lines[j]:
            x = round(np.random.uniform(-0.8184, 0.8184), 4)
            x = '{:.4f}'.format(x)
            y = round(np.random.uniform(-0.8184, 0.8184), 4)
            y = '{:.4f}'.format(y)
            modified_line = lines[j].replace("(0 0)", f"({x} {y})")
            lines[j] = modified_line

        if "431    3" in lines[j]:
            x = round(np.random.uniform(-0.8184, 0.8184), 4)
            x = '{:.4f}'.format(x)
            y = round(np.random.uniform(-0.8184, 0.8184), 4)
            y = '{:.4f}'.format(y)
            modified_line = lines[j].replace("(0 0)", f"({x} {y})")
            lines[j] = modified_line

        if "441    3" in lines[j]:
            x = round(np.random.uniform(-0.8184, 0.8184), 4)
            x = '{:.4f}'.format(x)
            y = round(np.random.uniform(-0.8184, 0.8184), 4)
            y = '{:.4f}'.format(y)
            modified_line = lines[j].replace("(0 0)", f"({x} {y})")
            lines[j] = modified_line

        if "451    3" in lines[j]:
            x = round(np.random.uniform(-0.8184, 0.8184), 4)
            x = '{:.4f}'.format(x)
            y = round(np.random.uniform(-0.8184, 0.8184), 4)
            y = '{:.4f}'.format(y)
            modified_line = lines[j].replace("(0 0)", f"({x} {y})")
            lines[j] = modified_line

        if "461    3" in lines[j]:
            x = round(np.random.uniform(-0.8184, 0.8184), 4)
            x = '{:.4f}'.format(x)
            y = round(np.random.uniform(-0.8184, 0.8184), 4)
            y = '{:.4f}'.format(y)
            modified_line = lines[j].replace("(0 0)", f"({x} {y})")
            lines[j] = modified_line

        if "471    3" in lines[j]:
            x = round(np.random.uniform(-0.8184, 0.8184), 4)
            x = '{:.4f}'.format(x)
            y = round(np.random.uniform(-0.8184, 0.8184), 4)
            y = '{:.4f}'.format(y)
            modified_line = lines[j].replace("(0 0)", f"({x} {y})")
            lines[j] = modified_line

        if "481    3" in lines[j]:
            x = round(np.random.uniform(-0.8184, 0.8184), 4)
            x = '{:.4f}'.format(x)
            y = round(np.random.uniform(-0.8184, 0.8184), 4)
            y = '{:.4f}'.format(y)
            modified_line = lines[j].replace("(0 0)", f"({x} {y})")
            lines[j] = modified_line

        if "491    3" in lines[j]:
            x = round(np.random.uniform(-0.8184, 0.8184), 4)
            x = '{:.4f}'.format(x)
            y = round(np.random.uniform(-0.8184, 0.8184), 4)
            y = '{:.4f}'.format(y)
            modified_line = lines[j].replace("(0 0)", f"({x} {y})")
            lines[j] = modified_line

        if "501    3" in lines[j]:
            x = round(np.random.uniform(-0.8184, 0.8184), 4)
            x = '{:.4f}'.format(x)
            y = round(np.random.uniform(-0.8184, 0.8184), 4)
            y = '{:.4f}'.format(y)
            modified_line = lines[j].replace("(0 0)", f"({x} {y})")
            lines[j] = modified_line

        if "511    3" in lines[j]:
            x = round(np.random.uniform(-0.8184, 0.8184), 4)
            x = '{:.4f}'.format(x)
            y = round(np.random.uniform(-0.8184, 0.8184), 4)
            y = '{:.4f}'.format(y)
            modified_line = lines[j].replace("(0 0)", f"({x} {y})")
            lines[j] = modified_line

        if "521    3" in lines[j]:
            x = round(np.random.uniform(-0.8184, 0.8184), 4)
            x = '{:.4f}'.format(x)
            y = round(np.random.uniform(-0.8184, 0.8184), 4)
            y = '{:.4f}'.format(y)
            modified_line = lines[j].replace("(0 0)", f"({x} {y})")
            lines[j] = modified_line

        if "531    3" in lines[j]:
            x = round(np.random.uniform(-0.8184, 0.8184), 4)
            x = '{:.4f}'.format(x)
            y = round(np.random.uniform(-0.8184, 0.8184), 4)
            y = '{:.4f}'.format(y)
            modified_line = lines[j].replace("(0 0)", f"({x} {y})")
            lines[j] = modified_line

        if "541    3" in lines[j]:
            x = round(np.random.uniform(-0.8184, 0.8184), 4)
            x = '{:.4f}'.format(x)
            y = round(np.random.uniform(-0.8184, 0.8184), 4)
            y = '{:.4f}'.format(y)
            modified_line = lines[j].replace("(0 0)", f"({x} {y})")
            lines[j] = modified_line

        if "551    3" in lines[j]:
            x = round(np.random.uniform(-0.8184, 0.8184), 4)
            x = '{:.4f}'.format(x)
            y = round(np.random.uniform(-0.8184, 0.8184), 4)
            y = '{:.4f}'.format(y)
            modified_line = lines[j].replace("(0 0)", f"({x} {y})")
            lines[j] = modified_line

        if "561    3" in lines[j]:
            x = round(np.random.uniform(-0.8184, 0.8184), 4)
            x = '{:.4f}'.format(x)
            y = round(np.random.uniform(-0.8184, 0.8184), 4)
            y = '{:.4f}'.format(y)
            modified_line = lines[j].replace("(0 0)", f"({x} {y})")
            lines[j] = modified_line

        if "571    3" in lines[j]:
            x = round(np.random.uniform(-0.8184, 0.8184), 4)
            x = '{:.4f}'.format(x)
            y = round(np.random.uniform(-0.8184, 0.8184), 4)
            y = '{:.4f}'.format(y)
            modified_line = lines[j].replace("(0 0)", f"({x} {y})")
            lines[j] = modified_line

        if "581    3" in lines[j]:
            x = round(np.random.uniform(-0.8184, 0.8184), 4)
            x = '{:.4f}'.format(x)
            y = round(np.random.uniform(-0.8184, 0.8184), 4)
            y = '{:.4f}'.format(y)
            modified_line = lines[j].replace("(0 0)", f"({x} {y})")
            lines[j] = modified_line

        if "591    3" in lines[j]:
            x = round(np.random.uniform(-0.8184, 0.8184), 4)
            x = '{:.4f}'.format(x)
            y = round(np.random.uniform(-0.8184, 0.8184), 4)
            y = '{:.4f}'.format(y)
            modified_line = lines[j].replace("(0 0)", f"({x} {y})")
            lines[j] = modified_line

        if "901    3" in lines[j]:
            x = round(np.random.uniform(-0.8184, 0.8184), 4)
            x = '{:.4f}'.format(x)
            y = round(np.random.uniform(-0.8184, 0.8184), 4)
            y = '{:.4f}'.format(y)
            modified_line = lines[j].replace("(0 0)", f"({x} {y})")
            lines[j] = modified_line

        if "921    3" in lines[j]:
            x = round(np.random.uniform(-0.8184, 0.8184), 4)
            x = '{:.4f}'.format(x)
            y = round(np.random.uniform(-0.8184, 0.8184), 4)
            y = '{:.4f}'.format(y)
            modified_line = lines[j].replace("(0 0)", f"({x} {y})")
            lines[j] = modified_line

        # 다른 라인에 대한 추가 조건을 필요에 따라 추가하세요.

    # 수정된 내용을 파일에 쓰기 모드로 저장합니다.
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

    print(f'{file_name} 파일이 수정되었습니다.')

print('수정이 완료되었습니다.')
