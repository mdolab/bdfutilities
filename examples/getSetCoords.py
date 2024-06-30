from bdfutilities.bdf_utils import BDFUtils, readBDF

# Get GRID coordinates, modify them externally, and set them back

bdfInFile = "B717_wingbox.bdf"
bdfOutFile = "B717_wingbox_out.bdf"

model = readBDF(bdfInFile)
bdfUtil = BDFUtils(model)
coords = bdfUtil.getGridCoords()
coords[:, 2] += 1.0
bdfUtil.setGridCoords(coords)
bdfUtil.writeBDF(bdfOutFile)
