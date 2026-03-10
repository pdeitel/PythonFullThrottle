#!/usr/bin/env bash
set -e

# Start JupyterLab (default token behavior) in the background
nohup jupyter lab --ip=0.0.0.0 --port=8888 --no-browser >/tmp/jupyterlab.log 2>&1 &
