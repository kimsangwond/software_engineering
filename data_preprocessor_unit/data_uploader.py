from elasticsearch import Elasticsearch, helpers
from pathlib import Path
import json

from file_manager import FileLoader
from config import (
    HOST, 
    PORT, 
    CONGRESS_MEMBER_LIST_INDEX_BODY, 
    PLENARY_SESSION_INDEX_BODY
)

class ElasticsearchAPI:

    ES = Elasticsearch(hosts=HOST, port=PORT)

    @classmethod
    def data_bulk(cls, file_path):
        result = list()
        with file_path.open('r', encoding="utf-8") as f:
            for line in f.readlines():
                result.append(json.loads(line))
        helpers.bulk(cls.ES, result)

    @classmethod
    def create_index(cls, index_name: str, body_name: dict):
        cls.ES.indices.create(
            index=index_name,
            body=body_name
        )

    @classmethod
    def is_index_exist(cls, index_name: str) -> bool:
        return cls.ES.indices.exists(index=index_name)

class Uploader:
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def extract_index(self):
        pass

    def bulk_new_index(self, index_name: str, body_name: dict):
        ElasticsearchAPI.create_index(index_name, body_name)
        ElasticsearchAPI.data_bulk(self.file_path)

    def bulk_existing_index(self):
        ElasticsearchAPI.data_bulk(self.file_path)

    @classmethod
    def run(cls, file_path: Path):
        pass

class PlenarySessionUploader(Uploader):
    def extract_index(self):
        ordinal,_round,time,_,_ = self.file_path.name.split("_")
        return f"{ordinal}th_{_round}round_plenary_session"

    @classmethod
    def run(cls, file_path: Path):
        klass = cls(file_path)
        current_index = klass.extract_index()
        if ElasticsearchAPI.is_index_exist(current_index):
            klass.bulk_existing_index()
        else:
            klass.bulk_new_index(current_index, PLENARY_SESSION_INDEX_BODY)

class CongressMemberListUploader(Uploader):
    def extract_index(self):
        return "congress_member_list"

    @classmethod
    def run(cls, file_path: Path):
        klass = cls(file_path)
        current_index = klass.extract_index()
        if ElasticsearchAPI.is_index_exist(current_index):
            klass.bulk_existing_index()
        else:
            klass.bulk_new_index(current_index, CONGRESS_MEMBER_LIST_INDEX_BODY)

def upload_data(partial_file_name: str, klass):
    pattern = "*" + partial_file_name + "*"
    for file_path in FileLoader(pattern):
        klass.run(file_path)
    print("finish")

if __name__=="__main__":
    uploader_type = input("업로드할 유형의 파일을 선택해주세요:\n")
    if "congress_member_list" == uploader_type:
        upload_data(uploader_type, CongressMemberListUploader)
    elif "plenary_session" == uploader_type:
        upload_data(uploader_type, PlenarySessionUploader)
    else:
        KeyError("업로드할 유형의 파일을 잘못 적었습니다.")