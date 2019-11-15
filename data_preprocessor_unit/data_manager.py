import sys
from pathlib import Path

class DataManager:
    def __init__(self, file_extension):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        pass

    def check_argv(self):
        pass

    def init_file(self, dir_path):
        file_list = dir_path.glob(self.file_extension)
        if not file_list:
            raise IndexError("No file in Directory")
        self.files = (file for file in file_list if file.is_file())

class FileLoader(DataManager):
    def __init__(self, file_extension):
        self.file_extension = file_extension #찾고자 하는 파일의 regex
        source_path = self.check_argv()
        self.init_file(source_path)

    def __next__(self):
        file_path = next(self.files)
        return file_path

    def check_argv(self):
        if not len(sys.argv) == 2:
            raise TypeError(
                f"Usage: python {sys.argv[0]} '파일이 있는 디렉토리 경로'"
            )
        else:
            _,source_path = sys.argv
            source_path = Path(source_path)
            if not source_path.exists():
                raise OSError("해당 디렉토리는 존재하지 않습니다.")
            if not source_path.is_dir():
                raise OSError("해당 디렉토리 경로는 디렉토리가 아닙니다.")
            return source_path

class FileConverter(DataManager):

    def __init__(self, file_extension):
        self.file_extension = file_extension #찾고자하는 파일의 regex
        source_path,self.output_path = self.check_argv()
        self.init_file(source_path)

    def __next__(self):
        file_name = next(self.files)
        return (file_name, self.output_path)

    def check_argv(self):
        if not len(sys.argv) == 3:
            raise TypeError(
                f"Usage: python {sys.argv[0]} '파일이 있는 디렉토리 경로' '결과가 저장될 디렉토리 경로'"
            )
        else:
            _,source_path,output_path = sys.argv
            source_path = Path(source_path)
            output_path = Path(output_path)
            if not source_path.exists() or not output_path.exists():
                raise OSError("해당 디렉토리는 존재하지 않습니다.")
            if not source_path.is_dir() or not output_path.is_dir():
                raise OSError("해당 디렉토리 경로는 디렉토리가 아닙니다.")
            return (source_path, output_path)

class FileUploader(DataManager):

    def __init__(self, file_extension):
        self.file_extension = file_extension #찾고자하는 파일의 regex
        source_path,self.file_name_type = self.check_argv()
        self.init_file(source_path)

    def __next__(self):
        file_name = next(self.files)
        return (file_name, self.file_name_type)

    def check_argv(self):
        if not len(sys.argv) == 3:
            raise TypeError(
                f"Usage: python {sys.argv[0]} '파일이 있는 디렉토리 경로' '업로드할 파일의 타입'"
            )
        else:
            _,source_path,file_name_type = sys.argv
            source_path = Path(source_path)
            if not source_path.exists():
                raise OSError("해당 디렉토리는 존재하지 않습니다.")
            if not source_path.is_dir():
                raise OSError("해당 디렉토리 경로는 디렉토리가 아닙니다.")
            return (source_path, file_name_type)    
