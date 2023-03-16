# django_yolov5
- yolov5 deployment via django web service

- easy deployment and extend thanks to Django framework

- v5 folder is a copy of yolov5 version 7.0 @ Mar 2023

### 02 Mar 2023

#### Modification

- v5/stream.py

modified from detect.py for save frames from stream as image files

- v5/webDetect.py

modified from detect.py for save frames from stream as image files, + auto stop after stream ended 

- v5/utils/plots_r.py

modified from plots.py for better CHN charactors support

### 16 Mar 2023

#### Modification

- AIDevOps/settings.py

Added settings for redis connection

- objectDetection/urls.py

comment urls

- objectDetection/views.py

redis operations added

- v5/detect_folder.py

infer all images under folder, save results and empty file as finishing mark in the same dir
