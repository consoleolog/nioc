import os
from dotenv import load_dotenv

from provider.data_provider import DataProvider


class EnvProvider(DataProvider):

    def __init__(self, env_path):
        self.env_path = env_path

    def get_data(self):
        load_dotenv(self.env_path)

        return {
            "naverId": os.getenv("NAVER_ID"),
            "naverPw": os.getenv("NAVER_PASSWORD"),
            "smtpTo": os.getenv("SMTP_TO"),
            "smtpFrom": os.getenv("SMTP_FROM"),
            "upbitAccessKey": os.getenv("UPBIT_ACCESS_KEY"),
            "upbitSecretKey": os.getenv("UPBIT_SECRET_KEY"),
        }
