from elasticsearch import Elasticsearch, helpers
import json

from data_manager import FileLoader
from config import (HOST,PORT, INDEX_BODY)

SOURCE_FILE_EXTENSION = "*.json"

class ElasticsearchUploader:

    def __init__(self, file):
        self.es = Elasticsearch(hosts=HOST, port=PORT)
        self.file = file

    @classmethod
    def run(cls, file):
        klass = cls(file)
        klass.create_index()        
        klass.data_bulk()

    def data_bulk(self):
        data = self.read_data()
        helpers.bulk(self.es, data)

    def read_data(self):
        result = list()
        with self.file.open('r', encoding="utf-8") as f:
            for line in f.readlines():
                result.append(json.loads(line))
        return result

    def name_index(self):
        return self.file.name.replace(".json","")

    def create_index(self):
        index_name = self.name_index()
        self.es.indices.create(
            index=index_name,
            body=INDEX_BODY
        )

if __name__=="__main__":
    for file in FileLoader(SOURCE_FILE_EXTENSION):
        ElasticsearchUploader.run(file)        




