# Standard Python modules
import argparse
import os
import shutil
import tempfile

# External modules
import numpy as np
from pyNastran.bdf.bdf import BDF

# Local modules
from .utils import rotationMatrix


def get_parser():
    # List out all of the possible options here.
    parser = argparse.ArgumentParser(prog="bdf_utils")

    subparsers = parser.add_subparsers(help="Choose one of the listed operations to perform", dest="mode")

    p_rot = subparsers.add_parser("rotate", help="Rotate a grid around a given direction.")
    p_rot.add_argument("bdfFile", help="Name of input BDF file")
    p_rot.add_argument("vx", help="x-component of the rotation axis", type=float)
    p_rot.add_argument("vy", help="y-component of the rotation axis", type=float)
    p_rot.add_argument("vz", help="z-component of the rotation axis", type=float)
    p_rot.add_argument("theta", help="rotation angle [deg]", type=float)
    p_rot.add_argument("outFile", nargs="?", default=None, help="Optional output file")

    p_t = subparsers.add_parser("translate", help="Translate a grid.")
    p_t.add_argument("bdfFile", help="Name of input BDF file")
    p_t.add_argument("dx", help="x-displacement", type=float)
    p_t.add_argument("dy", help="y-displacement", type=float)
    p_t.add_argument("dz", help="z-displacement", type=float)
    p_t.add_argument("outFile", nargs="?", default=None, help="Optional output file")

    return parser


class BDFUtils(object):
    """This class wraps common"""

    def __init__(self, model):

        self.model = model

    def rotate(self, vx, vy, vz, theta):

        """
        Rotate the grid around an axis that passes through the origin.

        parameters
        ----------
        vx, vy, vz : float
            components of the rotation vector
        theta : float
            rotation angle, in degrees
        """
        # Get rotation matrix
        rotMat = rotationMatrix(vx, vy, vz, theta)

        # Perform the rotation
        for node in self.model.nodes.values():
            node.xyz = np.dot(node.xyz, rotMat)

    def translate(self, dx, dy, dz):
        """
        Translates the geometry

        parameters
        ----------
        dx, dy, dz : float
            components of the translation vector
        """

        # Perform the rotation
        for node in self.model.nodes.values():
            node.xyz += np.array([dx, dy, dz])

    def writeBDF(self, bdfFile):
        self.model.write_bdf(bdfFile)


def readBDF(bdfFile, validate=False, xref=False):
    # Disable cross-referencing unless we actually need it,
    # Read the BDF object and return for usage
    model = BDF(debug=True)
    model.read_bdf(bdfFile, validate=validate, xref=xref)

    return model


def main():
    parser = get_parser()
    args = parser.parse_args()

    model = readBDF(args.bdfFile)
    bdfUtil = BDFUtils(model)

    if args.mode == "rotate":
        bdfUtil.rotate(args.vx, args.vy, args.vz, args.theta)

    elif args.mode == "translate":
        bdfUtil.translate(args.dx, args.dy, args.dz)

    # Check if we have an outFile argument, if not this option does not write out anything
    try:
        if args.outFile is None:
            # Determine where to put a file:
            dirpath = tempfile.mkdtemp()

            # Define a temp output file
            outFileName = os.path.join(dirpath, "tmp.bdf")
        else:
            outFileName = args.outFile
    except Exception:
        outFile = None

    # Write the final grid
    bdfUtil.writeBDF(outFileName)

    # Possibly copy back to the original:
    if args.outFile is None:
        shutil.copyfile(outFileName, args.gridFile)
        shutil.rmtree(dirpath)
