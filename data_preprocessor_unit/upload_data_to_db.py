from elasticsearch import Elasticsearch, helpers
from pathlib import Path
import json

from data_manager import FileLoader
from config import (HOST,PORT, INDEX_BODY)

SOURCE_FILE_EXTENSION = "*.json"

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
    def create_index(cls, index_name):
        cls.ES.indices.create(
            index=index_name,
            body=INDEX_BODY
        )

    @classmethod
    def is_index_exist(cls, index_name: str) -> bool:
        return cls.ES.indices.exists(index=index_name)

def extract_index(file_name: str) -> str:
    ordinal,_round,time,_ = file_name.split("_")
    return f"{ordinal}th_{_round}round"

def bulk_new_index(index_name: str, file_path: Path):
    ElasticsearchAPI.create_index(index_name)
    ElasticsearchAPI.data_bulk(file_path)

def bulk_existing_index(file_path: Path):
    ElasticsearchAPI.data_bulk(file_path)

if __name__=="__main__":
    for file_path in FileLoader(SOURCE_FILE_EXTENSION):
        current_index = extract_index(file_path.name)
        if ElasticsearchAPI.is_index_exist(current_index):
            bulk_existing_index(file_path)
        else:
            bulk_new_index(current_index, file_path)
    print("finish")