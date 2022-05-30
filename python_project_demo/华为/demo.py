"""
@Author :       yangleiw
@File   :       .py
@Time   :       2022年05月22日 21:01
@Desc   :
"""
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkocr.v1 import *
# 导入指定云服务的库 huaweicloudsdk{service}
from huaweicloudsdkocr.v1.region.ocr_region import OcrRegion

config = HttpConfig.get_default_config()
ak = 'EFVTUAI8EKLCRUMDNJY1'
sk = 'nN2yoqwcSh6NmJXNgXwEPgQJbxeu0qY9efC4QLuN'

credentials = BasicCredentials(ak, sk)

client = OcrClient.new_builder() \
    .with_http_config(config) \
    .with_credentials(credentials) \
    .with_region(OcrRegion.value_of("cn-north-4")) \
    .build()

# request = RecognizeGeneralTableRequest()
# request.body = GeneralTableRequestBody(
#             url="1.png"
#         )
# response = client.recognize_general_table(request)
# print(response)

try:
    request = RecognizeGeneralTableRequest()
    request.body = GeneralTableRequestBody(
        url="1.png"
    )
    response = client.recognize_general_table(request)
    print(response)
except exceptions.ClientRequestException as e:
    print(e.status_code)
    print(e.request_id)
    print(e.error_code)
    print(e.error_msg)

# if __name__ == "__main__":
#    pass
