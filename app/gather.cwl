#!/usr/bin/env cwltool

cwlVersion: v1.0
class: CommandLineTool
requirements:
  InlineJavascriptRequirement: {}

baseCommand: cat
# arguments: 
#   - $(inputs.content)
#   - ">"
#   - rezultati.txt

inputs:
  content:
    type:
      type: array
      items: File
    inputBinding:
      position: 1
  
outputs: 
  rezultati:
    type: File
    streamable: true
    outputBinding:
      glob: "rezultati.txt"
stdout: "rezultati.txt"
