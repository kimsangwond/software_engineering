import openpyxl as xl
from pathlib import Path
import re
import json
from dataclasses import *

from data_manager import FileConverter

FILE_EXTENSION = "*.xlsx"

@dataclass
class CongressMemberList:
    contents: dict  

    def __init__(self):
        self.contents = {
            "_index": "congress_member_list",
            "_type": "_doc",
            "_id": int, #대수
            "_source": {
                "member_info_list": list()
            }
        }

class ExcelAPI:
    def __init__(self, excel_file_path: str):
        self.file = xl.load_workbook(excel_file_path)

    def choose_sheet(self, sheet_name: str):
        self.sheet = self.file[sheet_name]

    def read_row_by_column_name(self, cell_name: str) -> list:
        for column in self.sheet[cell_name]:
            yield column.value
        
def read_member_list(api: ExcelAPI, party_cell_name: str, congress_member_name: str) -> list:
    result = list()
    for party, congress_member_name in zip(
            api.read_row_by_column_name(party_cell_name),
            api.read_row_by_column_name(congress_member_name)
        ):
        result.append(party + " " + congress_member_name)
    return result

def get_member_list_from_data(excel_file_path: Path, result: CongressMemberList) -> CongressMemberList:
    file_path = str(excel_file_path.resolve())
    api = ExcelAPI(file_path)
    api.choose_sheet("지역구")
    result.contents["_source"]["member_info_list"].extend(read_member_list(api,"C","E")) #지역구는 여기에 있어요!
    api.choose_sheet("비례대표")
    result.contents["_source"]["member_info_list"].extend(read_member_list(api,"A","C")) #비례대표는 여기에 있어요!
    return result

def name_json_file(source_file_path: Path) -> str:
    congress_ordinal = re.findall(r"\d+", source_file_path.name)
    return f"{congress_ordinal[0]}th_congress_member_list.json" 

def export_to_json_file(source_file_path: Path, output_file_path: Path, data: CongressMemberList):
    json_file_name = name_json_file(source_file_path)
    export_path = output_file_path/Path(json_file_name)
    with export_path.open("a+", encoding="utf-8") as f:
        data = asdict(data)
        json.dump(data["contents"], fp=f, ensure_ascii=False)

def make_json_format(source_file_path: Path) -> CongressMemberList:
    congress_ordinal = re.findall(r"\d+", source_file_path.name) 
    member_list = CongressMemberList()
    member_list.contents["_id"] = int(congress_ordinal[0])
    return member_list

def main(source_file_path: Path, output_file_path: Path):
    result_format = make_json_format(source_file_path)
    congress_member_list = get_member_list_from_data(source_file_path, result_format)
    export_to_json_file(source_file_path, output_file_path, congress_member_list)    

if __name__=="__main__":
    for file_path,output_path in FileConverter(FILE_EXTENSION):
        main(file_path, output_path)         
    print('finish')

