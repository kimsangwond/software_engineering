from dataclasses import *
from pathlib import Path
from multiprocessing.pool import Pool
import json

from data_manager import FileConverter

SOURCE_FILE_EXTENSION = "*.txt"
RESULT_FILE_EXTENSION = ".json"

@dataclass
class MeetingLog:
    contents: dict  

    def __init__(self):
        self.contents = {
            "_index": str, #대수th_회수round 
            "_type": "_doc",
            "_id": int, #차수
            "_source": {
                "meeting_log": list()
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
    temporary_agenda_list = list()
    for agenda_discussion_paragraph in parse_data(raw_data):
        agenda_list,discussion = agenda_discussion_paragraph
        if agenda_list:
            temporary_agenda_list = agenda_list # 안건들이 들어있다.
            temporary_discussion_paragraph = discussion # 안건에 대한 토론 내용이 담겨있다.
            yield (temporary_agenda_list, temporary_discussion_paragraph)
        else:
            temporary_discussion_paragraph.extend(discussion) #토론만 들어있다.

def construct_data(raw_data:str, log_data: MeetingLog) -> MeetingLog:
    for agenda_list, discussion_paragraph in extract_data(raw_data):
        meeting_log = {
            "agenda": agenda_list,
            "discussion": discussion_paragraph
        }
        log_data.contents["_source"]["meeting_log"].append(meeting_log)
        yield log_data

def name_json_file(file_path: Path):
    file_name = file_path.name
    return file_name.replace(".txt","")    

def export_json(result: list, source_path: Path, output_path: Path):
    file_name = name_json_file(source_path)
    export_path = output_path/Path(file_name + RESULT_FILE_EXTENSION)
    with export_path.open(mode="a+", encoding="utf-8") as f: 
        for document in result:
            document = asdict(document)
            index = json.dump(document["contents"], fp=f, ensure_ascii=False)
            f.write("\n")

def construct_result_format(file_path: Path) -> MeetingLog:
    log = MeetingLog()
    file_name = file_path.name.replace(".txt","")
    ordianl,_round,time,_ = file_name.split('_')
    log.contents["_index"] = f"{ordianl}th_{_round}round"
    log.contents["_id"] = time
    return log

def job(file_path: Path, output_path: Path):
    log = construct_result_format(file_path)
    result = [meeting_log for meeting_log in construct_data(file_path.read_text(), log)]
    export_json(result, file_path, output_path)

if __name__=="__main__":
    with Pool() as mp:
        mp.starmap(job, FileConverter(SOURCE_FILE_EXTENSION))
    print("finish")