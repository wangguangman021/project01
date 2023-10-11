from fastapi import FastAPI
import os
import uvicorn
import subprocess

app = FastAPI()

@app.get("/execute_files/tts_text_process_one")
def execute_tts_text_process_one():
    # 执行tts_text_process_one.py的代码逻辑
    file_path = "/path/to/project/folder/tts_text_process_one.py"
    subprocess.call(["python", file_path])

    return {"message": "tts_text_process_one.py 执行完毕"}

@app.get("/execute_files/tts_process_two_final_trans")
def execute_tts_process_two_final_trans():
    # 执行tts_process_two_final_trans.py的代码逻辑
    file_path = "/path/to/project/folder/tts_process_two_final_trans.py"
    subprocess.call(["python", file_path])

    return {"message": "tts_process_two_final_trans.py 执行完毕"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
