## ipymd the converter

Convenient script for transforming .ipynb files to .md but with the images retained as base64 embedded. Since its execution depends on pandoc and jupyter nbconvert it is meant to be dockerized by using
```console
docker build -t ipymd .
```
and then subsequently run with (an example mount and ipymd cmd arg which shows the path to a folder with .ipynb files)
```docker
docker run --rm \
    -it \
    --mount type=bind,source=/home,target=/home \
    ipymd ./path to .ipynb files referenced by target mount/
```
