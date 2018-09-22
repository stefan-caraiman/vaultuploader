FROM python:2.7-onbuild
ADD . /usr/src/app/
EXPOSE 6969
RUN python setup.py install