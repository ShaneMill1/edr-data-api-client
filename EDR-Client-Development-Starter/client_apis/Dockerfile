FROM debian:latest

RUN apt-get update && apt-get -y install vim curl bzip2 cron libzstd-dev libssl-dev libopenblas-base libopenblas-dev \
    && curl -sSL https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /tmp/miniconda.sh \
    && bash /tmp/miniconda.sh -bfp /usr/local \
    && rm -rf /tmp/miniconda.sh \
    && apt-get -qq -y remove curl bzip2 \
    && apt-get -qq -y autoremove \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* /var/log/dpkg.log \
    && conda clean --all --yes

ENV PATH /opt/conda/bin:$PATH
RUN conda install -c conda-forge flask flask-cors

COPY . /

ENV FLASK_APP=/app.py

CMD flask run --no-debugger --no-reload --host=0.0.0.0 --port=80
