import subprocess
import re
from pathlib import Path

from data_manager import FileConverter

FILE_EXTENSION = "*.hwp"

def rename_file(file_name: str) -> str:
    if "개회식" in file_name:
        file_name = file_name.replace("개회식", "0차")
    number_in_string = re.findall(r"\d+", file_name) 
    # number_in_string = [몇 대 국회인지, 몇 번째 회차인지, 몇 번째 차수인지로 구성이 되어있다.]
    return f"{number_in_string[0]}th_{number_in_string[1]}round_{number_in_string[2]}time_meeting_log.txt"

def reassign_output_path(output_path: Path, file_name: str) -> str:
    absolute_path = output_path/Path(file_name)
    return absolute_path.resolve()

if __name__=="__main__":
    for source_file,output_path in FileConverter(FILE_EXTENSION):
        new_file_name = rename_file(source_file.name)
        result_path = reassign_output_path(output_path, new_file_name)
        subprocess.run(
            ["hwp5txt", str(source_file.resolve())],
            stdout=result_path.open("w+", encoding="utf-8"),
            encoding="utf-8",
            text=True
        )
