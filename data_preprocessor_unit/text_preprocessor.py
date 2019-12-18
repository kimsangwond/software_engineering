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
                "agenda": list(),
                "discussion": list()
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
        for agenda, discussion in extract_data(file_path):
            result.contents["_source"]["agenda"].extend(agenda)
            result.contents["_source"]["discussion"].extend(discussion)
        export_json(result, file_path, output_path)

def is_stop_by_timeover(speaking: str) -> bool:
    if '마이크 중단' in speaking:
        return False
    else:
        return True

def parse_data(file_path: Path) -> tuple:
    raw_data = file_path.read_text(encoding="utf-8")
    #전자투표 또는 참석자 명단 뒷 부분 제거
    if "산회" in raw_data:
        #개회식이 아닌 경우
        splited_data = raw_data.split("산회)")
        raw_data = splited_data[0]
    elif "폐식" in raw_data:
        #개회식인 경우
        splited_data = raw_data.split("폐식)")
        raw_data = splited_data[0]
    #안건 및 토의 단락별로 나누기
    return raw_data.replace("\n\n","").split("<그림>")

def extract_data(file_path: Path) -> tuple:
    temporary_agenda_discussion_paragraph = list()
    for agenda_discussion_paragraph in parse_data(file_path):
        #발화자가 말하는 단락 별로 나누기
        paragraph_contents = agenda_discussion_paragraph.split("◯")
        ## 마이크 중단으로 인해 잘리는 경우를 방지
        if paragraph_contents and all(map(is_stop_by_timeover, paragraph_contents)):
            agenda_list = list()
            discussion_paragraph_list = list()
            agendas = ''.join(paragraph_contents[0])
            discussion_paragraph = '\n'.join(paragraph_contents[1:])
            # 마이크 중단으로 누적된 단락이 있을 경우
            if temporary_agenda_discussion_paragraph:
                agenda_list.append(''.join(temporary_agenda_discussion_paragraph[0]))
                discussion_paragraph_list.append('\n'.join(temporary_agenda_discussion_paragraph[1:]))
                temporary_agenda_discussion_paragraph.clear()
            # 단락 내 안건이나 토론 내용이 없으면 버립니다.
            if agendas and discussion_paragraph:
                agenda_list.append(agendas)
                discussion_paragraph_list.append(discussion_paragraph)
            # 누적된 발언이나 새로운 하나의 단락이 있을 경우 return
            if agenda_list and discussion_paragraph_list:
                yield (agenda_list, discussion_paragraph_list)
        else:
            temporary_agenda_discussion_paragraph.extend(paragraph_contents)

def name_json_file(file_path: Path):
    file_name = file_path.name
    return file_name.replace(".txt",".json")    

def export_json(result: PlenarySessionLog, source_path: Path, output_path: Path):
    file_name = name_json_file(source_path)
    export_path = output_path/Path(file_name)
    with export_path.open(mode="a+", encoding="utf-8") as f: 
        document = asdict(result)
        index = json.dump(document["contents"], fp=f, ensure_ascii=False)

def run_preprocessor(partial_file_name: str, klass):
    pattern = "*" + partial_file_name + "*.txt"
    with Pool() as mp:
        mp.starmap(
            klass.process_plenary_session, 
            FileConverter(pattern)
        )
    print("finish")

if __name__=="__main__":
    print('주의! 생성하려는 파일과 같은 이름의 파일이 있을 경우에 append합니다.')
    preprocessor_type = input("전처리기의 유형을 선택하세요:\n")
    if preprocessor_type == "plenary_session":
        run_preprocessor(preprocessor_type, PlenarySessionPreProcessor)
    else:
        raise KeyError("잘못된 전처리기 유형을 선택하셨습니다.")