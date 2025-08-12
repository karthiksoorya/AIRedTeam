import subprocess
import threading
import webbrowser
import time

def run_fastapi():
    subprocess.run(["uvicorn", "main:app", "--reload"])

def run_streamlit():
    subprocess.run(["streamlit", "run", "streamlit_app/app.py"])

if __name__ == "__main__":
    # Start both servers in parallel threads
    t1 = threading.Thread(target=run_fastapi)
    t2 = threading.Thread(target=run_streamlit)

    t1.start()
    t2.start()

    # Wait a moment for servers to start
    time.sleep(30)

    # Open Swagger and Streamlit in browser tabs
    webbrowser.open_new_tab("http://localhost:8000/docs")
    webbrowser.open_new_tab("http://localhost:8501")

    t1.join()
    t2.join()
