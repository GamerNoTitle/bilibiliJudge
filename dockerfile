FROM python:3.7.10-alpine3.13
WORKDIR /bilibiliJudge
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
# ENV SESSDATA "***"
# ENV csrf "***"
# ENV GiveUpEnable "True"
# ENV delay "300"
# ENV JudgeProportion "0.7"
RUN python Main.py "${SESSDATA}" "${csrf}}" "${GiveUpEnable}" "${delay}" "${JudgeProportion}"