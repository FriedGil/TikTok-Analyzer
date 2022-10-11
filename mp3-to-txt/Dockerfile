FROM cschranz/gpu-jupyter
USER root
RUN apt update && sudo apt install ffmpeg
RUN pip install git+https://github.com/openai/whisper.git 
USER jovyan
# docker run --gpus all -it -p 8888:8888 gilfried/whisper_notebook