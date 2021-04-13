FROM continuumio/miniconda3
LABEL maintainer="François Valadier <francois.valadier@openvalue.fr>"
WORKDIR /src
COPY . .
RUN conda env create -f environment.yml -p .conda \
&& conda clean --all -f -y

EXPOSE 80

ENTRYPOINT ["./entrypoint.sh"]