FROM python:3

ADD src /src

CMD [ "python", "./src/Calculator_Tests_.py" ]
