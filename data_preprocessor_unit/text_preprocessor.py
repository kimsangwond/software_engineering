from dataclasses import *
from pathlib import Path
from multiprocessing.pool import Pool
import json

from file_manager import FileConverter

@dataclass
class PlenarySessionLog:
    contents: dict  

    def __init__(self):
        self.contents = {
            "_index": str, #대수th_회수round_plenary_session
            "_type": "_doc",
            "_id": int, #차수
            "_source": {
                "dialogue": list()
            }
        }

class PlenarySessionPreProcessor:
    @classmethod
    def construct_plenary_session_format(cls, file_path: Path) -> PlenarySessionLog:
        log = PlenarySessionLog()
        ordianl,_round,time,_,_ = file_path.name.split('_')
        log.contents["_index"] = f"{ordianl}th_{_round}round_plenary_session"
        log.contents["_id"] = time
        return log

    @classmethod
    def process_plenary_session(cls, file_path: Path, output_path: Path):
        result = cls.construct_plenary_session_format(file_path)
        for plenary_session_log in construct_data(file_path):
            result.contents["_source"]["dialogue"].append(plenary_session_log)
        export_json(result, file_path, output_path)

def parse_agenda_list(agendas: str) -> list:
    return [agenda for agenda in agendas.split("\n") if agenda]

def parse_data(raw_data: str) -> tuple:
    #전자투표 또는 참석자 명단 뒷 부분 제거
    if "산회" in raw_data:
        #개회식이 아닌 경우
        splited_data = raw_data.split("산회)")
        raw_data = splited_data[0]
    elif "폐식" in raw_data:
        #개회식인 경식
        splited_data = raw_data.split("폐식)")
        raw_data = splited_data[0]
    #안건 및 토의 단락별로 나누기
    data = raw_data.replace("\n\n","").split("<그림>")
    for agenda_discussion_paragraph in data:
        #발화자가 말하는 단락 별로 나누기
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

def construct_data(file_path: Path) -> dict:
    for agenda_list, discussion_paragraph in extract_data(file_path.read_text(encoding="utf-8")):
        meeting_log = {
            "agenda": agenda_list,
            "discussion": discussion_paragraph
        }
        yield meeting_log

def name_json_file(file_path: Path):
    file_name = file_path.name
    return file_name.replace(".txt",".json")    

def export_json(result: list, source_path: Path, output_path: Path):
    file_name = name_json_file(source_path)
    export_path = output_path/Path(file_name)
    with export_path.open(mode="a+", encoding="utf-8") as f: 
        document = asdict(result)
        index = json.dump(document["contents"], fp=f, ensure_ascii=False)

def run_preprocessor(partial_file_name: str, klass):
    pattern = "*" + partial_file_name + "*"
    with Pool() as mp:
        mp.starmap(
            klass.process_plenary_session, 
            FileConverter(pattern)
        )
    print("finish")

if __name__=="__main__":
    preprocessor_type = input("전처리기의 유형을 선택하세요:\n")
    if preprocessor_type == "plenary_session":
        run_preprocessor(preprocessor_type, PlenarySessionPreProcessor)
    else:
        raise KeyError("잘못된 전처리기 유형을 선택하셨습니다.")