import oss2
from oss2.credentials import EnvironmentVariableCredentialsProvider
import os
from datetime import datetime
# 使用环境变量中获取的RAM用户的访问密钥配置访问凭证。

local_dir = "static/"

class OssUtil:
    def __init__(self):
        self.accessKeyId = 'LTAI5tQdXzhbQLLNwjxEUakj'
        self.accessKeySecret = 'cd11bdJWPv8FFqA6iyBp0cuWndo8mC'
        self.auth = oss2.Auth(self.accessKeyId, self.accessKeySecret)
        self.endpoint = 'https://oss-cn-beijing.aliyuncs.com'
        self.bucket = oss2.Bucket(self.auth, self.endpoint, 'data-generation') 

    def upload(self, prefix , file_name , local_file, befix = ".csv"):
        self.bucket.put_object_from_file(prefix + file_name + befix, local_file)
        return f"{prefix}{file_name}{befix}"
    
    def download(self, abs_file_name):
        if not os.path.exists(os.path.dirname(abs_file_name)):
            os.makedirs(os.path.dirname(abs_file_name))
        self.bucket.get_object_to_file(abs_file_name, local_dir + abs_file_name)
        return local_dir + abs_file_name

    def search_by_prefix(self,dir,prefix):
        return [obj.key for obj in oss2.ObjectIterator(self.bucket, prefix=dir+prefix)]

ossUtil = OssUtil()