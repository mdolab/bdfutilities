#!/bin/bash

set -e

BDF_INFILE="B717_wingbox.bdf"
BDF_OUTFILE="B717_wingbox_out.bdf"

# Test rotate
bdf_utils rotate $BDF_INFILE 0.0 0.0 1.0 45.0 $BDF_OUTFILE
