from bdfutilities.bdf_utils import BDFUtils, readBDF

# Rotate the wing about the z-axis and write out an updated file

bdfInFile = "B717_wingbox.bdf"
bdfOutFile = "B717_wingbox_out.bdf"

axis = [0.0, 0.0, 1.0]

model = readBDF(bdfInFile)
bdfUtil = BDFUtils(model)
bdfUtil.rotate(*axis, 45.0)
bdfUtil.writeBDF(bdfOutFile)
