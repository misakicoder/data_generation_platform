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

    def upload(self, prefix , data_name , local_file, befix = ".csv"):
        file_name = f"{data_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}"

        if not os.path.exists(local_dir + prefix):
            os.makedirs(local_dir + prefix)

        with open(local_dir + prefix + file_name + befix, "wb") as f:
            f.write(local_file.read())
        self.bucket.put_object_from_file(prefix + file_name + befix, local_dir + prefix + file_name + befix)
        os.remove(local_dir + prefix + file_name + befix)
        return f"{prefix}{file_name}{befix}"
    
    def download(self, abs_file_name):
        self.bucket.get_object_to_file(abs_file_name, local_dir + abs_file_name)
        return local_dir + abs_file_name


ossUtil = OssUtil()