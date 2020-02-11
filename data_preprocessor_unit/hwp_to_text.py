import subprocess
import re
from pathlib import Path

from file_manager import FileConverter

def rename_plenary_session_file(file_name: str) -> str:
    if "개회식" in file_name:
        file_name = file_name.replace("개회식", "0차")
    number_in_string = re.findall(r"\d+", file_name) 
    # number_in_string = [몇 대 국회인지, 몇 번째 회차인지, 몇 번째 차수인지로 구성이 되어있다.]
    return f"{number_in_string[0]}_{number_in_string[1]}_{number_in_string[2]}_plenary_session.txt"

def reassign_output_path(output_path: Path, file_name: str) -> str:
    absolute_path = output_path/Path(file_name)
    return absolute_path.resolve()

def convert_plenary_session():
    pattern = "*국회본회의*"
    for source_file,output_path in FileConverter(pattern):
        new_file_name = rename_plenary_session_file(source_file.name)
        result_path = reassign_output_path(output_path, new_file_name)
        subprocess.run(
            ["hwp5txt", str(source_file.resolve())],
            stdout=result_path.open("w+", encoding="utf-8"),
            encoding="utf-8",
            text=True
        )
    print("finish")

if __name__=="__main__":
    print('주의! 생성하려는 파일과 같은 이름의 파일이 있을 경우에 append합니다.')
    converter_type = input("컨버터의 유형을 선택하세요:\n")
    if converter_type == "plenary_session":
        convert_plenary_session()
    else:
        raise KeyError("잘못된 컨버터 유형을 선택하셨습니다.")
