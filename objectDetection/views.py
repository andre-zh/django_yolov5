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
    cmd = r'python3 /data/ai/RyAI/AIDevOps/v5/webDetect.py --weights ./weights/RY_OD_YV5_640.pt --imgsz 640 --vid-stride 30 --conf-thres 0.25 --iou-thres 0.45 --project runs/od --hide-conf --source ' + streamurl + ' --exist-ok --name TaskID_' + taskid 
    os.system(cmd)
    # 
    return HttpResponse(f"Task {taskid}: infer {streamurl} Success! Result saved at: '/data/ai/RyAI/AIDevOps/v5/runs/od/TaskID_{taskid}'")

def poppy(request):
    taskid = request.GET.get('taskid')
    streamurl = request.GET.get('streamurl')
    # -------------------------------------- detect here ----------------------------------------
    # IP:Port/objectDetection/poppy?taskid=1&streamurl=https://abc.yeah
    #
    cmd = r'python3 /data/ai/RyAI/AIDevOps/v5/webDetect.py --weights ./weights/RY_POPPY_YV5_2048.pt --imgsz 2048 --vid-stride 30 --conf-thres 0.25 --iou-thres 0.45 --project runs/poppy --hide-conf --source ' + streamurl + ' --exist-ok --name TaskID_' + taskid 
    os.system(cmd)
    # 
    return HttpResponse(f"Task {taskid}: infer {streamurl} Success! Result saved at: '/data/ai/RyAI/AIDevOps/v5/runs/poppy/TaskID_{taskid}'")

def helmet(request):
    taskid = request.GET.get('taskid')
    streamurl = request.GET.get('streamurl')
    # -------------------------------------- detect here ----------------------------------------
    # IP:Port/objectDetection/helmet?taskid=1&streamurl=https://abc.yeah
    #
    cmd = r'python3 /data/ai/RyAI/AIDevOps/v5/webDetect.py --weights ./weights/RY_HELM_YV5_1024.pt --imgsz 1024 --vid-stride 30 --conf-thres 0.25 --iou-thres 0.45 --project runs/helmet --hide-conf --source ' + streamurl + ' --exist-ok --name TaskID_' + taskid 
    os.system(cmd)
    # 
    return HttpResponse(f"Task {taskid}: infer {streamurl} Success! Result saved at: '/data/ai/RyAI/AIDevOps/v5/runs/helmet/TaskID_{taskid}'")