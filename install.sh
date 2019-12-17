#!/usr/bin/env bash
rm -Rf .conda
rm -Rf .ipynb_checkpoints

conda env create -f environment.yml -p .conda