#!/usr/bin/env cwltool

class: Workflow
cwlVersion: v1.0
requirements:
  ScatterFeatureRequirement: {}

hints:
  DockerRequirement:
    dockerPull: ratinacnikola/ml-workflow
inputs:
  data: File
  k: int
 
outputs:
  rezultati: 
      type: File
      outputSource: gather/rezultati
      
steps:
  preprocess:
    run: preprocess.cwl
    in: 
      data: data
    out: [ppc_data]
  
  split:
    run: split.cwl
    in:
      data: preprocess/ppc_data
      k: k
    out: [train_data, test_data] 
  
  train:
    run: train.cwl
    scatter: [train_data, test_data]
    scatterMethod: dotproduct
    in:
      train_data: split/train_data
      test_data: split/test_data
    out: [results]

  gather:
    run: gather.cwl
    in:
      content: train/results
    out: [rezultati]