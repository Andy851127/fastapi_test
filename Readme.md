# 切換至虛擬環境
到 D:\poetry-demo 路徑下
執行 poetry shell 進入虛擬環境

# 啟動 FastAPI Server
uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload 

# 進入 Swagger UI
http://localhost:8001/docs