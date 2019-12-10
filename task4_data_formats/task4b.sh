#!/bin/bash


# awk -F',' '{gsub(/([a-z0-9]{6,7})/, "xxxxx", $NF); gsub(/([a-z0-9]{6,7})$/, "xxxxx", $4);}1' generatedData2.csv > replaced_4b.csv

awk '{gsub(/^([a-z0-9]{6,7})/, "xxxxx", $NF);}1' generatedData2.csv > replaced_4b.csv
awk -F, '{gsub(/^([a-z0-9]{6,7})/, "xxxxx", $4);}1' replaced_4b.csv > replaced.csv



