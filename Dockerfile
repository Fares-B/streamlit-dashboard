FROM python:3.7.13

COPY src .

RUN pip3 install streamlit && pip3 install pandas && pip3 install matplotlib

EXPOSE 8501

ENTRYPOINT [ "streamlit", "run" ]
CMD [ "Dashboard.py" ]
