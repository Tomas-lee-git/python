"""文件的写入和读取"""
from pathlib import Path

import json

def write(file_path, content):
    """根据文件路径和内容进行写入"""
    path = Path(file_path)
    contents = json.dumps(content)
    path.write_text(contents)
    
def read(file_path):
    """根据文件路径进行内容读取"""
    path = Path(file_path)
    contents = path.read_text()
    return json.loads(contents)
    
