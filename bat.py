with open('D:/input/SCI/new_cases/no4/run4.txt', 'w') as file:
    for i in range(3001, 4001):
        line = f"mcnp6 i=case_{i}.txt n=case_{i}. tasks 7\n"
        file.write(line)

print('D:/input/SCI/run.txt 파일이 생성되었습니다.')