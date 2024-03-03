from django.shortcuts import render
import os

from apns2.client import APNsClient
from apns2.payload import Payload

def send_push_notification(token):
    # 현재 파일의 디렉토리 경로를 얻습니다.
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # APNs 인증서의 절대 경로를 설정합니다.
    cert_path = os.path.join(current_dir, 'apns.pem')
    
    # APNs 클라이언트 초기화 (비밀번호 인자 없음)
    client = APNsClient(cert_path, use_sandbox=True, use_alternative_port=False)
    
    # 푸시 알림 내용
    payload = Payload(alert="안녕", sound="default", badge=1)
    
    # 푸시 알림 보내기
    client.send_notification(token, payload, topic='com.flickerFix.screenWeather')

# 사용 예시
device_token = '1607f1769f625433791069453fdc8686a45a4953936233fc6764ab852cc17e01'
send_push_notification(device_token)
