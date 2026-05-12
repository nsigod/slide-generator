from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import generate, parse_link

app = FastAPI(title="文字转幻灯片API")

# CORS配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境应限制为具体域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(generate.router, prefix="/api")
app.include_router(parse_link.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "文字转幻灯片API服务正在运行"}
