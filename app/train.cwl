#!/usr/bin/env cwltool

cwlVersion: v1.0
class: CommandLineTool
baseCommand: train.py

# hints:
#   DockerRequirement:
#     dockerPull: ratinacnikola/ml-workflow

inputs:
  train_data:
    type: File
    inputBinding:
      position: 1
  test_data:
    type: File
    inputBinding:
      position: 2
outputs:
  results:
    type: stdout


