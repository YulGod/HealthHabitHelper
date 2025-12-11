# app.py (임시 테스트용 최소 코드)
from flask import Flask

# Flask 인스턴스만 생성합니다. 이 코드는 최소한의 임포트만 실행합니다.
app = Flask(__name__)

# 테스트용 더미 함수 (API 문서에 필요할 경우)
def health_status():
    """Returns the current application health status."""
    return "OK"