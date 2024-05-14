import logging
from time import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

# 配置日志
logging.basicConfig(level=logging.INFO, filename='api_logs.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # 记录请求信息
        start_time = time()
        logging.info(f"Request: {request.method} {request.url} Headers: {request.headers}")

        response = await call_next(request)

        # 记录响应信息
        process_time = time() - start_time
        logging.info(f"Response: Status Code: {response.status_code} Process Time: {process_time}s")

        return response
