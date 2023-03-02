from django.shortcuts import render
from django.http import HttpResponse
import sys
sys.path.append("..")
from v5 import webDetect
import os

def index(request):
    return HttpResponse("Object Detection platform by Zit!")

def detect(request):
    taskid = request.GET.get('taskid')
    streamurl = request.GET.get('streamurl')
    # -------------------------------------- detect here ----------------------------------------
    # IP:Port/objectDetection/detect?taskid=1&streamurl=https://abc.yeah
    #
    #
    #
    cmd = r'python3 /data/ai/RyAI/AIDevOps/v5/webDetect.py --source ' + streamurl + ' --exist-ok --name TaskID_' + taskid 
    # cmd = r'python3 /data/ai/RyAI/AIDevOps/v5/detect.py --weights /data/ai/RyAI/AIDevOps/v5/ODN_2.pt --source ' + streamurl + ' --vid-stride 30 --device 0 --exist-ok'
    os.system(cmd)
    # 
    return HttpResponse(f"Task {taskid}: infer {streamurl} Success! Result saved at: '/data/ai/RyAI/AIDevOps/v5/runs/detect/TaskID_{taskid}'")