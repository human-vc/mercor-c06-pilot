#!/bin/sh
set -eu
cd "$(dirname "$0")"
T=data/apex-agents-v1.1/tasks
MODEL=${MODEL:-gemini-3.8-flash}
REPEATS=${REPEATS:-2}
OUT=${OUT:-runs/pilot}
exec ./.venv/bin/python -m c06.run --model "$MODEL" --repeats "$REPEATS" --out "$OUT" ${ASK:+--ask-prompt} --harbor \
  $T/128-jr-1-f7f95d92 \
  $T/world-129-cy-task-3-2bcdc3db \
  $T/world-134-rg-04-4498da8f \
  $T/lawworld433-anb-01-5d12cf8d \
  $T/lawworld417-ne-06-7d454c39 \
  $T/world223-smn-05-b00d08c1 \
  $T/world-225-je-01-70449b2d \
  $T/world-221-hy-05-fa5120b0
