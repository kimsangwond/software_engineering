from dataclasses import *
from pathlib import Path
from multiprocessing.pool import Pool
from typing import List
import copy
import json

from data_manager import FileConverter

SOURCE_FILE_EXTENSION = "*.txt"
RESULT_FILE_EXTENSION = ".json"

@dataclass
class MeetingLog:
    meeting_log: dict  

    def __init__(self):
        self.meeting_log = {
            "_index": str,
            "_type": "_doc",
            "_id": int,
            "_source": {
                "agenda": List[str],
                "discussion": List[str] 
            }
        }

def parse_agenda_list(agendas: str) -> list:
    return [agenda for agenda in agendas.split("\n") if agenda]

def parse_data(raw_data: str) -> tuple:
    data = raw_data.replace("\n\n","").split("<그림>")
    for agenda_discussion_paragraph in data:
        if "◯" in agenda_discussion_paragraph:
            paragraph_contents = agenda_discussion_paragraph.split("◯")
            agenda_list = parse_agenda_list(paragraph_contents[0])
            discussion_paragraph = paragraph_contents[1:]
            yield (agenda_list, discussion_paragraph)

def extract_data(raw_data: str) -> tuple:
    temporary_discussion_paragraph = list()## 발언 초과로 인해 잘리는 경우를 위해서
    temporary_agenda_index = int()
    temporary_agenda_list = list()
    for agenda_index,agenda_discussion_paragraph in enumerate(parse_data(raw_data)):
        agenda_list,discussion = agenda_discussion_paragraph
        if agenda_list:
            temporary_agenda_index = agenda_index
            temporary_agenda_list = agenda_list # 안건들이 들어있다.
            temporary_discussion_paragraph = discussion # 안건에 대한 토론 내용이 담겨있다.
            yield (temporary_agenda_index, temporary_agenda_list, temporary_discussion_paragraph)
        else:
            temporary_discussion_paragraph.extend(discussion) #토론만 들어있다.

def construct_data(raw_data:str, log_data: MeetingLog) -> MeetingLog:
    for paragraph_index, agenda_list, discussion_paragraph in extract_data(raw_data):
        new_log_data = copy.deepcopy(log_data)
        new_log_data.meeting_log["_id"] = paragraph_index
        new_log_data.meeting_log["_source"]["agenda"] = agenda_list
        new_log_data.meeting_log["_source"]["discussion"] = discussion_paragraph
        yield new_log_data

def name_index(file_name: str) -> str:
    return file_name.replace(".txt","")

def export_json(result: list, file_name: str, output_path: Path):
    export_path = output_path/Path(file_name + RESULT_FILE_EXTENSION)
    with export_path.open(mode="a+", encoding="utf-8") as f: 
        for document in result:
            document = asdict(document)
            index = json.dump(document["meeting_log"], fp=f, ensure_ascii=False)
            f.write("\n")

def construct_result_format(file_path: Path) -> MeetingLog:
    log = MeetingLog()
    _index = name_index(file_path.name)
    log.meeting_log["_index"] = _index
    return (log, _index)

def job(file_path: Path, output_path: Path):
    log, export_file_name = construct_result_format(file_path)
    result = [meeting_log for meeting_log in construct_data(file_path.read_text(), log)]
    export_json(result, export_file_name, output_path)

if __name__=="__main__":
    with Pool() as mp:
        mp.starmap(job, FileConverter(SOURCE_FILE_EXTENSION))