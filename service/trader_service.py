import smtplib
from abc import ABCMeta, abstractmethod
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from custom_logging import CustomLogger
from provider.env_provider import EnvProvider


class TraderService(metaclass=ABCMeta):

    def __init__(self, env_provider: EnvProvider):
        self.envs = env_provider.get_data()
        self.logger = CustomLogger().get_logger(__class__.__name__)

    @abstractmethod
    def create_buy(self, inputs):
        """ 매수 """

    @abstractmethod
    def create_sell(self, inputs):
        """ 매도 """

    def send_mail(self, inputs: dict[str, str]) -> None:
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = f"[{inputs['ticker']}] {inputs['content']}"
            msg['From'] = self.envs["smtpFrom"]
            msg['To'] = self.envs["smtpTo"]
            part = MIMEText(f"<h4>{inputs['content']}</h4>", 'html')
            msg.attach(part)
            # with open(f"{self.__data_path}/{inputs['filename']}", 'rb') as handler:
            #     file = MIMEBase("application", "octet-stream")
            #     file.set_payload(handler.read())
            #     encoders.encode_base64(file)
            #     file.add_header("Content-Disposition", f"attachment; filename={inputs['filename']}")
            #     msg.attach(file)
            s = smtplib.SMTP('smtp.naver.com', 587)
            s.starttls()
            s.login(self.envs["naverId"], self.envs["naverPw"])
            s.sendmail(self.envs["smtpFrom"], self.envs["smtpTo"], msg.as_string())
            s.close()
        except Exception as error:
            self.logger.error(f"메일 보내다가 에러났음 {str(error)}")
            raise UserWarning("SEND MAIL ERROR") from error