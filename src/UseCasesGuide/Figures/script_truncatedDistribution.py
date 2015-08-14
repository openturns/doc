from openturns import *

from math import *


# logistic

logistic = Logistic(1.0, 2.0)

# PDF
pdf_logistic =  logistic.drawPDF()
draw = pdf_logistic.getDrawable(0)
draw.setColor("black")
draw.setLegendName("Initial Logistic")
pdf_logistic.setDrawable(draw,0)

# truncated to [-2,5]
logisticTruncated_1 = TruncatedDistribution(Distribution(logistic), -2.0, 5.0)
logisticTruncated_1_pdf = logisticTruncated_1.drawPDF()
logisticTruncated_1_pdf_draw = logisticTruncated_1_pdf.getDrawable(0)
logisticTruncated_1_pdf_draw.setColor("blue")
logisticTruncated_1_pdf_draw.setLegendName("Truncated whithin [-2.0, 5.0]")
pdf_logistic.add(logisticTruncated_1_pdf_draw)

# truncated under 3
logisticTruncated_2 = TruncatedDistribution(Distribution(logistic), 3.0, TruncatedDistribution.UPPER)
logisticTruncated_2_pdf = logisticTruncated_2.drawPDF()
logisticTruncated_2_pdf_draw = logisticTruncated_2_pdf.getDrawable(0)
logisticTruncated_2_pdf_draw.setColor("red")
logisticTruncated_2_pdf_draw.setLegendName("Truncated under 3.0")
pdf_logistic.add(logisticTruncated_2_pdf_draw)

# truncated upper 4
logisticTruncated_3 = TruncatedDistribution(Distribution(logistic), 4.0, TruncatedDistribution.LOWER)
logisticTruncated_3_pdf = logisticTruncated_3.drawPDF()
logisticTruncated_3_pdf_draw = logisticTruncated_3_pdf.getDrawable(0)
logisticTruncated_3_pdf_draw.setColor("green")
logisticTruncated_3_pdf_draw.setLegendName("Truncated upper 4.0")
pdf_logistic.add(logisticTruncated_3_pdf_draw)

# Show the graph
pdf_logistic.setTitle("Truncated logistic(alpha=1.0, beta=2.0) - PDF")
pdf_logistic.draw("truncatedDistribution_pdf")



# CDF
cdf_logistic =  logistic.drawCDF()
draw = cdf_logistic.getDrawable(0)
draw.setColor("black")
draw.setLegendName("Initial Logistic")
cdf_logistic.setDrawable(draw,0)

# truncated to [2,5]
logisticTruncated_1 = TruncatedDistribution(Distribution(logistic), -2.0, 5.0)
logisticTruncated_1_cdf = logisticTruncated_1.drawCDF()
logisticTruncated_1_cdf_draw = logisticTruncated_1_cdf.getDrawable(0)
logisticTruncated_1_cdf_draw.setColor("blue")
logisticTruncated_1_cdf_draw.setLegendName("Truncated whithin [-2.0, 5.0]")
cdf_logistic.add(logisticTruncated_1_cdf_draw)

# truncated under 3
logisticTruncated_2 = TruncatedDistribution(Distribution(logistic), 3.0, TruncatedDistribution.UPPER)
logisticTruncated_2_cdf = logisticTruncated_2.drawCDF()
logisticTruncated_2_cdf_draw = logisticTruncated_2_cdf.getDrawable(0)
logisticTruncated_2_cdf_draw.setColor("red")
logisticTruncated_2_cdf_draw.setLegendName("Truncated under 3.0")
cdf_logistic.add(logisticTruncated_2_cdf_draw)

# truncated upper 4
logisticTruncated_3 = TruncatedDistribution(Distribution(logistic), 4.0, TruncatedDistribution.LOWER)
logisticTruncated_3_cdf = logisticTruncated_3.drawCDF()
logisticTruncated_3_cdf_draw = logisticTruncated_3_cdf.getDrawable(0)
logisticTruncated_3_cdf_draw.setColor("green")
logisticTruncated_3_cdf_draw.setLegendName("Truncated upper 4.0")
cdf_logistic.add(logisticTruncated_3_cdf_draw)

# Show the graph
cdf_logistic.setTitle("Truncated logistic(alpha=1.0, beta=2.0)  - CDF")
cdf_logistic.setLegendPosition("bottomright")
cdf_logistic.draw("truncatedDistribution_cdf")
