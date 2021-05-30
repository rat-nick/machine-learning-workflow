#!/usr/bin/env cwltool

cwlVersion: v1.0
class: CommandLineTool



baseCommand: split-k-fold.py
hints:
  DockerRequirement:
    dockerPull: ratinacnikola/ml-workflow

inputs:
  data: 
    type: File
    inputBinding:
      position: 1
  k:
    type: int
    inputBinding:
      position: 2

outputs:
  train_data: 
    type:
      type: array
      items: File  
    outputBinding:
      glob: "*train.csv" 
  test_data: 
    type:
      type: array
      items: File  
    outputBinding:
      glob: "*test.csv" 