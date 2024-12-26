FROM python:3.11.9-slim-bookworm AS build
WORKDIR /src

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv  \
    && pipenv requirements > requirements.txt

FROM python:3.11.9-slim-bookworm as final
WORKDIR /src

COPY --from=build /src/requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY /src .
COPY /src/static /src/static
COPY /entrypoints /entrypoints

RUN chmod -R 755 /entrypoints
