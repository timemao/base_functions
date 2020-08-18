#import torch
import onnx
import numpy as np

onnxfile=".data\\checkpoints\\regression\\save_ckpt\\checkpoint.onnx"
new_onnxfile=".data\\checkpoints\\regression\\save_ckpt\\ckpt.onnx"
onnx_model = onnx.load(onnxfile)
graph = onnx_model.graph

idx=0
for id in range(len(graph.node)):
    if(graph.node[id].op_type=="Pad"):
        node1=graph.node[id]
        node2=graph.node[id+1]

        node2.input[0]=node1.input[0]
    else:
        idx=idx+1

print("idx=",idx)

for id in range(idx):

    if(graph.node[id].op_type=="Pad"):

        node1=graph.node[id]

        graph.node.remove(node1)

onnx.checker.check_model(onnx_model)
onnx.save(onnx_model, new_onnxfile)
