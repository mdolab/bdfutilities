from bdfutilities.bdf_utils import BDFUtils, readBDF

# Scale the wing and write out an updated file

bdfInFile = "B717_wingbox.bdf"
bdfOutFile = "B717_wingbox_out.bdf"

scaleFact = 1.1

model = readBDF(bdfInFile)
bdfUtil = BDFUtils(model)
bdfUtil.scale(scaleFact)
bdfUtil.writeBDF(bdfOutFile)
