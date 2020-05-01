#!/bin/bash -e

DEBUG=0

if [ $# -ne 2 ]
 then
 echo "Usage: $0 config-file stack-height"
 exit 1
 fi

STACK_HEIGHT=$2

if [ $STACK_HEIGHT -lt 1 ]
 then
 echo "Invalid stack height" >&2
 exit 1
 fi

. $1
# Variables from the config
#
#VASE_NORAFT_FILE=stacked-btm.gcode
#INFILL_NORAFT_FILE=bottom-infill.gcode
#VASE_RAFT_FILE=stacked-top.gcode
#INFILL_RAFT_FILE=top-infill.gcode
#BOTTOM_SOLID_LAYER=19.75
#TOP_SOLID_LAYER=21.25
#TOP_RAFT_LAYER=1.75
#TOP_BRIDGE_LAYER=2.35

#BOTTOM model
#save ending g-code for later
awk -f extract-end.awk < $VASE_NORAFT_FILE > end.gcode
# extract preamble and vase-mode layers up to solid infill level
awk -f extract-layers.awk -vLAYER_START=0 \
  -vLAYER_STOP=$BOTTOM_SOLID_LAYER < $VASE_NORAFT_FILE > bottom.gcode
# extract solid infill layers, but omit job-end commands
awk -f truncate-end.awk < $INFILL_NORAFT_FILE |\
 awk -f extract-layers.awk -vLAYER_START=$BOTTOM_SOLID_LAYER \
  -vLAYER_STOP=999 >> bottom.gcode

# TOP model
# re-set coordinate system by using G92 command and raise head
# to ensure unobstructed machine movement
cat > top.gcode << EOF
G92 Z$TOP_RAFT_LAYER
G1 Z$TOP_BRIDGE_LAYER
EOF
# strip off raft and extract vase-mode layers up to solid infill
awk -f extract-layers.awk -vLAYER_START=$TOP_BRIDGE_LAYER \
  -vLAYER_STOP=$TOP_SOLID_LAYER < $VASE_RAFT_FILE >> top.gcode
# extract solid infill layers, but omit job-end commands
awk -f truncate-end.awk < $INFILL_RAFT_FILE |\
 awk -f extract-layers.awk -vLAYER_START=$TOP_SOLID_LAYER \
  -vLAYER_STOP=999 >> top.gcode

cat bottom.gcode
MODEL_COUNT=1
while [ $STACK_HEIGHT -gt $MODEL_COUNT ]
 do
 MODEL_COUNT=$(( $MODEL_COUNT + 1 ))
 echo "; Here starts model N$MODEL_COUNT"
 cat top.gcode
 done
cat end.gcode

if [ $DEBUG -eq 0 ]
 then
 rm end.gcode top.gcode bottom.gcode
 fi