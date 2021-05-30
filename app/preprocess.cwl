#!/usr/bin/env cwltool

cwlVersion: v1.0
class: CommandLineTool


baseCommand: preprocess.py
# hints:
#   DockerRequirement:
#     dockerPull: ratinacnikola/ml-workflow
inputs:  
  data:
    type: File
    inputBinding:
      position: 1
outputs:
  ppc_data: 
    type: File
    outputBinding:
      glob: "*.csv" 
  