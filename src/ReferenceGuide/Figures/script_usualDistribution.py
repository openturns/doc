from openturns import *
from math import *



# ARCSIN

derivativeArcsine = Arcsine(2.0, 4.0)
pdf_derivativeArcsine =  derivativeArcsine.drawPDF()
pdf_derivativeArcsine.setTitle("PDF - Arcsine(a, b)")
draw = pdf_derivativeArcsine.getDrawable(0)
draw.setLegend("Arcsine(2.0, 4.0)")
pdf_derivativeArcsine.setDrawable(draw,0)
pdf_derivativeArcsine.draw("pdf_Arcsine", 640, 480, GraphImplementation.PNG)
Show(pdf_derivativeArcsine)

# BERNOULLI
bernoulli = Bernoulli(0.3)
pdf_bernoulli =  bernoulli.drawPDF()
pdf_bernoulli.setTitle("PDF - Bernoulli(p)")
draw = pdf_bernoulli.getDrawable(0)
draw.setLegend("Bernoulli(0.3)")
pdf_bernoulli.setDrawable(draw,0)
pdf_bernoulli.setXTitle("values")
pdf_bernoulli.draw("pdf_Bernoulli", 640, 480, GraphImplementation.PNG)
Show(pdf_bernoulli)


cdf_bernoulli =  bernoulli.drawCDF(-1.0, 1.5)
cdf_bernoulli.setTitle("CDF - Bernoulli(p)")
draw = cdf_bernoulli.getDrawable(0)
draw.setLegend("Bernoulli(0.3)")
cdf_bernoulli.setDrawable(draw,0)
cdf_bernoulli.setXTitle("values")
cdf_bernoulli.draw("cdf_Bernoulli", 640, 480, GraphImplementation.PNG)
Show(cdf_bernoulli)

# BINOMIAL
binomial = Binomial(5,0.7)
pdf_binomial=  binomial.drawPDF()
pdf_binomial.setTitle("PDF - Binomial(n,p)")
draw = pdf_binomial.getDrawable(0)
draw.setLegend("Binomial(5,0.7)")
pdf_binomial.setXTitle("values")
pdf_binomial.setDrawable(draw,0)
pdf_binomial.draw("pdf_Binomial", 640, 480, GraphImplementation.PNG)
Show(pdf_binomial)


cdf_binomial=  binomial.drawCDF(-1.0, 6.0)
cdf_binomial.setTitle("CDF - Binomial(n,p)")
draw = cdf_binomial.getDrawable(0)
draw.setLegend("Binomial(5,0.7)")
cdf_binomial.setDrawable(draw, 0)
cdf_binomial.setXTitle("values")
cdf_binomial.setXTitle("values")
cdf_binomial.draw("cdf_Binomial", 640, 480, GraphImplementation.PNG)
Show(cdf_binomial)




# BETA 1
beta_1 = Beta(2.0, 3.0, 0.0, 2.0)
pdf_beta_1 =  beta_1.drawPDF()
pdf_beta_1.setTitle("PDF - Beta(r,t,a,b)")
draw = pdf_beta_1.getDrawable(0)
draw.setLegend("Beta(2.0, 3.0, 0.0, 2.0)")
pdf_beta_1.setDrawable(draw,0)
pdf_beta_1.setXTitle("values")
pdf_beta_1.setLegendPosition("topleft")
pdf_beta_1.draw("pdf_Beta_1", 640, 480, GraphImplementation.PNG)
Show(pdf_beta_1)


# BETA 2
beta_2 = Beta(1.0, 2.0, 0.0, 2.0)
pdf_beta_2 =  beta_2.drawPDF(-3.0, 4.0)
pdf_beta_2.setTitle("PDF - Beta(r,t,a,b)")
draw = pdf_beta_2.getDrawable(0)
draw.setLegend("Beta(1.0, 2.0, 0.0, 2.0)")
pdf_beta_2.setDrawable(draw,0)
pdf_beta_2.setXTitle("values")
pdf_beta_2.setLegendPosition("topleft")
pdf_beta_2.draw("pdf_Beta_2", 640, 480, GraphImplementation.PNG)
Show(pdf_beta_2)



# BETA 3
beta_3 = Beta(2.0, 4.0, 0.0, 2.0)
pdf_beta_3 =  beta_3.drawPDF()
pdf_beta_3.setTitle("PDF - Beta(r,t,a,b)")
draw = pdf_beta_3.getDrawable(0)
draw.setLegend("Beta(2.0, 4.0, 0.0, 2.0)")
pdf_beta_3.setDrawable(draw,0)
pdf_beta_3.setXTitle("values")
pdf_beta_3.draw("pdf_Beta_3", 640, 480, GraphImplementation.PNG)
Show(pdf_beta_3)


# BETA 4
beta_4 = Beta(2.0, 2.5, 0.0, 2.0)
pdf_beta_4 =  beta_4.drawPDF()
pdf_beta_4.setTitle("PDF - Beta(r,t,a,b)")
draw = pdf_beta_4.getDrawable(0)
draw.setLegend("Beta(2.0, 2.5, 0.0, 2.0)")
pdf_beta_4.setDrawable(draw,0)
pdf_beta_4.setXTitle("values")
pdf_beta_4.setLegendPosition("topleft")
pdf_beta_4.draw("pdf_Beta_4", 640, 480, GraphImplementation.PNG)
Show(pdf_beta_4)

# BETA 5
beta_5 = Beta(0.5, 1.0, 0.0, 2.0)
pdf_beta_5 =  beta_5.drawPDF(-1.0, 4.0)
pdf_beta_5.setTitle("PDF - Beta(r,t,a,b)")
draw = pdf_beta_5.getDrawable(0)
draw.setLegend("Beta(0.5, 1.0, 0.0, 2.0)")
pdf_beta_5.setDrawable(draw,0)
pdf_beta_5.setXTitle("values")
pdf_beta_5.draw("pdf_Beta_5", 640, 480, GraphImplementation.PNG)
Show(pdf_beta_5)

# BETA 6
beta_6 = Beta(0.5, 2.0, 0.0, 2.0)
pdf_beta_6 =  beta_6.drawPDF()
pdf_beta_6.setTitle("PDF - Beta(r,t,a,b)")
draw = pdf_beta_6.getDrawable(0)
draw.setLegend("Beta(0.5, 2.0, 0.0, 2.0)")
collDraw= DrawableCollection(1)
collDraw[0] = draw
pdf_beta_6.setDrawable(draw,0)
pdf_beta_6.setXTitle("values")
pdf_beta_6.draw("pdf_Beta_6", 640, 480, GraphImplementation.PNG)
Show(pdf_beta_6)

# BETA 7
beta_7 = Beta(6, 12.0, 0.0, 2.0)
pdf_beta_7 =  beta_7.drawPDF()
pdf_beta_7.setTitle("PDF - Beta(r,t,a,b)")
draw = pdf_beta_7.getDrawable(0)
draw.setLegend("Beta(6.0, 12.0, 0.0, 2.0)")
pdf_beta_7.setDrawable(draw,0)
pdf_beta_7.setXTitle("values")
pdf_beta_7.draw("pdf_Beta_7", 640, 480, GraphImplementation.PNG)
Show(pdf_beta_7)


# BURR 1
burr_1 = Burr(1.0, 2.0)
pdf_burr_1 =  burr_1.drawPDF()
pdf_burr_1.setTitle("PDF - Burr(c,k)")
draw = pdf_burr_1.getDrawable(0)
draw.setLegend("Burr(1.0, 2.0)")
pdf_burr_1.setDrawable(draw,0)
pdf_burr_1.setXTitle("values")
pdf_burr_1.setLegendPosition("topleft")
pdf_burr_1.draw("pdf_Burr_1", 640, 480, GraphImplementation.PNG)
Show(pdf_burr_1)


# BURR 2
burr_2 = Burr(3.0, 2.0)
pdf_burr_2 =  burr_2.drawPDF()
pdf_burr_2.setTitle("PDF - Burr(c,k)")
draw = pdf_burr_2.getDrawable(0)
draw.setLegend("Burr(3.0, 2.0)")
pdf_burr_2.setDrawable(draw,0)
pdf_burr_2.setXTitle("values")
pdf_burr_2.setLegendPosition("topleft")
pdf_burr_2.draw("pdf_Burr_2", 640, 480, GraphImplementation.PNG)
Show(pdf_burr_2)

# BURR 3
burr_3 = Burr(0.1, 2.0)
pdf_burr_3 =  burr_3.drawPDF()
pdf_burr_3.setTitle("PDF - Burr(c,k)")
draw = pdf_burr_3.getDrawable(0)
draw.setLegend("Burr(0.1, 2.0)")
pdf_burr_3.setDrawable(draw,0)
pdf_burr_3.setXTitle("values")
pdf_burr_3.setLegendPosition("topleft")
pdf_burr_3.draw("pdf_Burr_3", 640, 480, GraphImplementation.PNG)
Show(pdf_burr_3)



# Chi 1

chi = Chi(2.3)
pdf_chi =  chi.drawPDF()
pdf_chi.setTitle("PDF - Chi(nu)")
draw = pdf_chi.getDrawable(0)
draw.setLegend("Chi(2.3)")
pdf_chi.setDrawable(draw,0)
pdf_chi.setXTitle("values")
pdf_chi.draw("pdf_Chi_1", 640, 480, GraphImplementation.PNG)
Show(pdf_chi)


# ChiSquare 1

chiSquare = ChiSquare()
pdf_chiSquare =  chiSquare.drawPDF()
pdf_chiSquare.setTitle("PDF - ChiSquare(nu)")
draw = pdf_chiSquare.getDrawable(0)
draw.setLegend("ChiSquare(1.0)")
pdf_chiSquare.setDrawable(draw,0)
pdf_chiSquare.setXTitle("values")
pdf_chiSquare.draw("pdf_ChiSquare_1", 640, 480, GraphImplementation.PNG)
Show(pdf_chiSquare)


# ChiSquare 2

chiSquare = ChiSquare(2.0)
pdf_chiSquare =  chiSquare.drawPDF()
pdf_chiSquare.setTitle("PDF - ChiSquare(nu)")
draw = pdf_chiSquare.getDrawable(0)
draw.setLegend("ChiSquare(2.0)")
pdf_chiSquare.setDrawable(draw,0)
pdf_chiSquare.setXTitle("values")
pdf_chiSquare.draw("pdf_ChiSquare_2", 640, 480, GraphImplementation.PNG)
Show(pdf_chiSquare)


# ChiSquare 3

chiSquare = ChiSquare(3.0)
pdf_chiSquare =  chiSquare.drawPDF()
pdf_chiSquare.setTitle("PDF - ChiSquare(nu)")
draw = pdf_chiSquare.getDrawable(0)
draw.setLegend("ChiSquare(3.0)")
pdf_chiSquare.setDrawable(draw,0)
pdf_chiSquare.setXTitle("values")
pdf_chiSquare.draw("pdf_ChiSquare_3", 640, 480, GraphImplementation.PNG)
Show(pdf_chiSquare)


# DIRAC
dirac = Dirac([1.3])
pdf_dirac =  dirac.drawPDF()
pdf_dirac.setTitle("PDF - Dirac(p)")
draw = pdf_dirac.getDrawable(0)
draw.setLegend("Dirac(1.3)")
pdf_dirac.setDrawable(draw,0)
pdf_dirac.setXTitle("values")
pdf_dirac.draw("pdf_Dirac", 640, 480, GraphImplementation.PNG)
Show(pdf_dirac)


cdf_dirac =  dirac.drawCDF()
cdf_dirac.setTitle("CDF - Dirac(p)")
draw = cdf_dirac.getDrawable(0)
draw.setLegend("Dirac(1.3)")
cdf_dirac.setDrawable(draw,0)
cdf_dirac.setXTitle("values")
cdf_dirac.draw("cdf_Dirac", 640, 480, GraphImplementation.PNG)
Show(cdf_dirac)

# Epanechnikov

epanechnikov = Epanechnikov()
pdf_epanechnikov =  epanechnikov.drawPDF()
pdf_epanechnikov.setTitle("PDF - Epanechnikov()")
draw = pdf_epanechnikov.getDrawable(0)
draw.setLegend("Epanechnikov()")
pdf_epanechnikov.setDrawable(draw,0)
pdf_epanechnikov.setXTitle("values")
pdf_epanechnikov.draw("pdf_Epanechnikov", 640, 480, GraphImplementation.PNG)
Show(pdf_epanechnikov)



# Exponential

exponential = Exponential()
pdf_exponential =  exponential.drawPDF()
pdf_exponential.setTitle("PDF - Exponential(lambda, gamma)")
draw = pdf_exponential.getDrawable(0)
draw.setLegend("Exponential(1.0, 0.0)")
pdf_exponential.setDrawable(draw,0)
pdf_exponential.setXTitle("values")
pdf_exponential.draw("pdf_Exponential", 640, 480, GraphImplementation.PNG)
Show(pdf_exponential)



# FisherSnedecor 1

fisherSnedecor_1 = FisherSnedecor(100, 100)
pdf_fisherSnedecor_1 =  fisherSnedecor_1.drawPDF()
pdf_fisherSnedecor_1.setTitle("PDF - Fisher-Snedecor(d1, d2)")
draw = pdf_fisherSnedecor_1.getDrawable(0)
draw.setLegend("FisherSnedecor(100, 100)")
pdf_fisherSnedecor_1.setDrawable(draw,0)
pdf_fisherSnedecor_1.setXTitle("values")
pdf_fisherSnedecor_1.draw("pdf_FisherSnedecor_1", 640, 480, GraphImplementation.PNG)
Show(pdf_fisherSnedecor_1)

# FisherSnedecor 2

fisherSnedecor_2 = FisherSnedecor(1, 1)
pdf_fisherSnedecor_2 =  fisherSnedecor_2.drawPDF()
pdf_fisherSnedecor_2.setTitle("PDF - Fisher-Snedecor(d1, d2)")
draw = pdf_fisherSnedecor_2.getDrawable(0)
draw.setLegend("FisherSnedecor(1, 1)")
pdf_fisherSnedecor_2.setDrawable(draw,0)
pdf_fisherSnedecor_2.setXTitle("values")
pdf_fisherSnedecor_2.draw("pdf_FisherSnedecor_2", 640, 480, GraphImplementation.PNG)
Show(pdf_fisherSnedecor_2)

# Gamma

gamma_1 = Gamma()
pdf_gamma_1 =  gamma_1.drawPDF()
pdf_gamma_1.setTitle("PDF - Gamma(k, lambda, gamma)")
draw_1 = pdf_gamma_1.getDrawable(0)
draw_1.setLegend("Gamma(1.0, 1.0, 0.0)")
pdf_gamma_1.setDrawable(draw_1,0)
pdf_gamma_1.setXTitle("values")
pdf_gamma_1.draw("pdf_Gamma_1", 640, 480, GraphImplementation.PNG)
Show(pdf_gamma_1)


gamma_2 = Gamma(2.5, 1.0, 0.0)
pdf_gamma_2 =  gamma_2.drawPDF()
pdf_gamma_2.setTitle("PDF - Gamma(k, lambda, gamma)")
draw_2 = pdf_gamma_2.getDrawable(0)
draw_2.setLegend("Gamma(2.5, 1.0, 0.0)")
pdf_gamma_2.setDrawable(draw_2,0)
pdf_gamma_2.setXTitle("values")
pdf_gamma_2.draw("pdf_Gamma_2", 640, 480, GraphImplementation.PNG)
Show(pdf_gamma_2)



gamma_3 = Gamma(0.5, 1.0, 0.0)
pdf_gamma_3 =  gamma_3.drawPDF()
pdf_gamma_3.setTitle("PDF - Gamma(k, lambda, gamma)")
draw_3 = pdf_gamma_3.getDrawable(0)
draw_3.setLegend("Gamma(0.5, 1.0, 0.0)")
collDraw_3 = DrawableCollection(1)
collDraw_3[0] = draw_3
pdf_gamma_3.setDrawables(collDraw_3)
pdf_gamma_3.setXTitle("values")
pdf_gamma_3.draw("pdf_Gamma_3", 640, 480, GraphImplementation.PNG)
Show(pdf_gamma_3)



# Generalized Pareto

gpd = GeneralizedPareto(1.0, 2.0)
pdf_gpd =  gpd.drawPDF()
pdf_gpd.setTitle("PDF - Gpd(sigma, xi)")
draw = pdf_gpd.getDrawable(0)
draw.setLegend("Gpd(1.0, 2.0)")
pdf_gpd.setDrawable(draw,0)
pdf_gpd.setXTitle("values")
pdf_gpd.draw("pdf_GPD_1", 640, 480, GraphImplementation.PNG)
Show(pdf_gpd)

gpd2 = GeneralizedPareto(1.0, 0.0)
pdf_gpd2 =  gpd2.drawPDF()
pdf_gpd2.setTitle("PDF - Gpd(sigma, xi)")
draw2 = pdf_gpd2.getDrawable(0)
draw2.setLegend("Gpd(1.0, 0.0)")
pdf_gpd2.setDrawable(draw2,0)
pdf_gpd2.setXTitle("values")
pdf_gpd2.draw("pdf_GPD_2", 640, 480, GraphImplementation.PNG)
Show(pdf_gpd2)



# Geometric

geometric = Geometric(0.1)
pdf_geometric =  geometric.drawPDF(0.0,70 )
pdf_geometric.setTitle("PDF - Geometric(p)")
draw = pdf_geometric.getDrawable(0)
draw.setLegend("Geometric(0.1)")
pdf_geometric.setDrawable(draw,0)
pdf_geometric.setXTitle("values")
pdf_geometric.draw("pdf_Geometric", 640, 480, GraphImplementation.PNG)
Show(pdf_geometric)


geometric = Geometric(0.1)
cdf_geometric =  geometric.drawCDF(0.0,70 )
cdf_geometric.setTitle("CDF - Geometric(p)")
draw = cdf_geometric.getDrawable(0)
draw.setLegend("Geometric(0.1)")
cdf_geometric.setDrawable(draw,0)
cdf_geometric.setXTitle("values")
cdf_geometric.draw("cdf_Geometric", 640, 480, GraphImplementation.PNG)
Show(cdf_geometric)




# Gumbel

gumbel = Gumbel(1.0, 1.0)
pdf_gumbel =  gumbel.drawPDF()
pdf_gumbel.setTitle("PDF - Gumbel(alpha, beta)")
draw = pdf_gumbel.getDrawable(0)
draw.setLegend("Gumbel(1.0, 1.0)")
pdf_gumbel.setDrawable(draw,0)
pdf_gumbel.setXTitle("values")
pdf_gumbel.draw("pdf_Gumbel", 640, 480, GraphImplementation.PNG)
Show(pdf_gumbel)



# Histogram
collection = HistogramPairCollection(4)
collection[0] = HistogramPair(1.0, 0.5)
collection[1] = HistogramPair(0.7, 1.5)
collection[2] = HistogramPair(1.2, 3.5)
collection[3] = HistogramPair(0.9, 2.5)
collectionSize = len( collection )
histogram = Histogram(-1.5, collection)
pdf_histogram =  histogram.drawPDF()
pdf_histogram.setTitle("PDF - Histogram")
draw = pdf_histogram.getDrawable(0)
draw.setLegend("Histogram")
pdf_histogram.setDrawable(draw,0)
pdf_histogram.setXTitle("values")
pdf_histogram.draw("pdf_Histogram", 640, 480, GraphImplementation.PNG)
Show(pdf_histogram)

cdf_histogram =  histogram.drawCDF()
cdf_histogram.setTitle("CDF - Histogram")
draw = cdf_histogram.getDrawable(0)
draw.setLegend("Histogram")
cdf_histogram.setDrawable(draw,0)
cdf_histogram.setXTitle("values")
cdf_histogram.draw("cdf_Histogram", 640, 480, GraphImplementation.PNG)
Show(cdf_histogram)

# Inverse ChiSquare

invChiSquare = InverseChiSquare()
pdf_invChiSquare =  invChiSquare.drawPDF()
pdf_invChiSquare.setTitle("PDF - Inverse ChiSquare(nu)")
draw = pdf_invChiSquare.getDrawable(0)
draw.setLegend("Inverse ChiSquare(1.0)")
pdf_invChiSquare.setDrawable(draw,0)
pdf_invChiSquare.setXTitle("values")
pdf_invChiSquare.draw("pdf_InverseChiSquare", 640, 480, GraphImplementation.PNG)
Show(pdf_invChiSquare)

# Inverse Gamma

invGamma = InverseGamma()
pdf_invGamma =  invGamma.drawPDF()
pdf_invGamma.setTitle("PDF - Inverse Gamma(k, lambda)")
draw = pdf_invGamma.getDrawable(0)
draw.setLegend("Inverse Gamma(1.0, 1.0)")
pdf_invGamma.setDrawable(draw,0)
pdf_invGamma.setXTitle("values")
pdf_invGamma.draw("pdf_InverseGamma", 640, 480, GraphImplementation.PNG)
Show(pdf_invGamma)


# InverseNormal 1

inverseNormal_1 = InverseNormal(0.2,1)
pdf_inverseNormal_1 =  inverseNormal_1.drawPDF()
pdf_inverseNormal_1.setTitle("PDF - Inverse Normal(lambda, mu)")
draw = pdf_inverseNormal_1.getDrawable(0)
draw.setLegend("Inverse Normal(0.2,1)")
pdf_inverseNormal_1.setDrawable(draw,0)
pdf_inverseNormal_1.setXTitle("values")
pdf_inverseNormal_1.draw("pdf_InverseNormal_1", 640, 480, GraphImplementation.PNG)
Show(pdf_inverseNormal_1)


# InverseNormal 2

inverseNormal_2 = InverseNormal(1,2)
pdf_inverseNormal_2 =  inverseNormal_2.drawPDF()
pdf_inverseNormal_2.setTitle("PDF - Inverse Normal(lambda, mu)")
draw = pdf_inverseNormal_2.getDrawable(0)
draw.setLegend("Inverse Normal(1,2)")
pdf_inverseNormal_2.setDrawable(draw,0)
pdf_inverseNormal_2.setXTitle("values")
pdf_inverseNormal_2.draw("pdf_InverseNormal_2", 640, 480, GraphImplementation.PNG)
Show(pdf_inverseNormal_2)

# laplace

laplace = Laplace()
pdf_laplace =  laplace.drawPDF()
pdf_laplace.setTitle("PDF - Laplace(lambda, mu)")
draw = pdf_laplace.getDrawable(0)
draw.setLegend("Laplace(1.0, 0.0)")
pdf_laplace.setDrawable(draw,0)
pdf_laplace.setXTitle("values")
pdf_laplace.draw("pdf_Laplace", 640, 480, GraphImplementation.PNG)
Show(pdf_laplace)


# logistic

logistic = Logistic(0.0, 1.0)
pdf_logistic =  logistic.drawPDF()
pdf_logistic.setTitle("PDF - Logistic(alpha, beta)")
draw = pdf_logistic.getDrawable(0)
draw.setLegend("Logistic(0.0, 1.0)")
pdf_logistic.setDrawable(draw,0)
pdf_logistic.setXTitle("values")
pdf_logistic.draw("pdf_Logistic", 640, 480, GraphImplementation.PNG)
Show(pdf_logistic)


# LogNormal

logNormal = LogNormal(1.0, 0.5, 0.0)
pdf_logNormal =  logNormal.drawPDF()
pdf_logNormal.setTitle("PDF - LogNormal(mu_l, sigma_l, gamma)")
draw = pdf_logNormal.getDrawable(0)
draw.setLegend("LogNormal(1.0, 0.5, 0.0)")
pdf_logNormal.setDrawable(draw,0)
pdf_logNormal.setXTitle("values")
pdf_logNormal.draw("pdf_LogNormal", 640, 480, GraphImplementation.PNG)
Show(pdf_logNormal)

# LogUniform

logUniform = LogUniform(-0.5, 0.5)
pdf_logUniform =  logUniform.drawPDF()
pdf_logUniform.setTitle("PDF - LogUniform(a_l, b_l)")
draw = pdf_logUniform.getDrawable(0)
draw.setLegend("LogUniform(-0.5, 0.5)")
pdf_logUniform.setDrawable(draw,0)
pdf_logUniform.setXTitle("values")
pdf_logUniform.draw("pdf_LogUniform", 640, 480, GraphImplementation.PNG)
Show(pdf_logUniform)


# MeixnerDistribution

meixnerDistribution = MeixnerDistribution(1., 2.5, 3.0, -2.)
pdf_meixnerDistribution =  meixnerDistribution.drawPDF()
pdf_meixnerDistribution.setTitle("PDF - MeixnerDistribution(a, b, d, m)")
draw = pdf_meixnerDistribution.getDrawable(0)
draw.setLegend("MeixnerDistribution(1., 2.5, 3.0, -2.)")
pdf_meixnerDistribution.setDrawable(draw,0)
pdf_meixnerDistribution.setXTitle("values")
pdf_meixnerDistribution.draw("pdf_MeixnerDistribution", 640, 480, GraphImplementation.PNG)
Show(pdf_meixnerDistribution)

# NEGATIVE BINOMIAL
negativeBinomial = NegativeBinomial(5,0.7)
pdf_negativeBinomial=  negativeBinomial.drawPDF(0, 50)
pdf_negativeBinomial.setTitle("PDF - NegativeBinomial(n,p)")
draw = pdf_negativeBinomial.getDrawable(0)
draw.setLegend("NegativeBinomial(5,0.7)")
pdf_negativeBinomial.setXTitle("values")
pdf_negativeBinomial.setDrawable(draw,0)
pdf_negativeBinomial.draw("pdf_NegativeBinomial", 640, 480, GraphImplementation.PNG)
Show(pdf_negativeBinomial)


cdf_negativeBinomial=  negativeBinomial.drawCDF(0, 50)
cdf_negativeBinomial.setTitle("CDF - NegativeBinomial(n,p)")
draw = cdf_negativeBinomial.getDrawable(0)
draw.setLegend("NegativeBinomial(5,0.7)")
cdf_negativeBinomial.setDrawable(draw, 0)
cdf_negativeBinomial.setXTitle("values")
cdf_negativeBinomial.setXTitle("values")
cdf_negativeBinomial.draw("cdf_NegativeBinomial", 640, 480, GraphImplementation.PNG)
Show(cdf_negativeBinomial)


# NonCentralChiSquare_1

nonCentralChiSquare_1 = NonCentralChiSquare(4.0, 2.0)
pdf_nonCentralChiSquare_1 =  nonCentralChiSquare_1.drawPDF()
pdf_nonCentralChiSquare_1.setTitle("PDF - NonCentralChiSquare_1(nu, lambda)")
draw = pdf_nonCentralChiSquare_1.getDrawable(0)
draw.setLegend("NonCentralChiSquare(4,2)")
pdf_nonCentralChiSquare_1.setDrawable(draw,0)
pdf_nonCentralChiSquare_1.setXTitle("values")
pdf_nonCentralChiSquare_1.draw("pdf_NonCentralChiSquare_1", 640, 480, GraphImplementation.PNG)
Show(pdf_nonCentralChiSquare_1)



# NonCentralChiSquare_2

nonCentralChiSquare_2 = NonCentralChiSquare(0.5, 0.1)
pdf_nonCentralChiSquare_2 =  nonCentralChiSquare_2.drawPDF()
pdf_nonCentralChiSquare_2.setTitle("PDF - NonCentralChiSquare_2(nu, lambda)")
draw = pdf_nonCentralChiSquare_2.getDrawable(0)
draw.setLegend("NonCentralChiSquare(0.5,0.1)")
pdf_nonCentralChiSquare_2.setDrawable(draw,0)
pdf_nonCentralChiSquare_2.setXTitle("values")
pdf_nonCentralChiSquare_2.draw("pdf_NonCentralChiSquare_2", 640, 480, GraphImplementation.PNG)
Show(pdf_nonCentralChiSquare_2)




# NonCentralStudent

nonCentralStudent = NonCentralStudent(4.5, 0.0, 0.0)
pdf_nonCentralStudent =  nonCentralStudent.drawPDF(-4.5, 6.0)
pdf_nonCentralStudent.setTitle("PDF - NonCentralStudent(nu, delta, gamma)")
draw = pdf_nonCentralStudent.getDrawable(0)
draw.setLegend("NonCentralStudent(4.5, 0.0, 0.0)")
pdf_nonCentralStudent.setDrawable(draw,0)
pdf_nonCentralStudent.setXTitle("values")
pdf_nonCentralStudent.draw("pdf_NonCentralStudent", 640, 480, GraphImplementation.PNG)
Show(pdf_nonCentralStudent)


# Normal

normal = Normal(2.0, 1.0)
pdf_normal =  normal.drawPDF()
pdf_normal.setTitle("PDF - Normal(mu, sigma)")
draw = pdf_normal.getDrawable(0)
draw.setLegend("Normal(2.0, 1.0)")
pdf_normal.setDrawable(draw,0)
pdf_normal.setXTitle("values")
pdf_normal.draw("pdf_Normal", 640, 480, GraphImplementation.PNG)
Show(pdf_normal)


# Poisson

poisson = Poisson(50)
pdf_poisson =  poisson.drawPDF(20, 90)
pdf_poisson.setTitle("PDF - Poisson(lambda)")
draw = pdf_poisson.getDrawable(0)
draw.setLegend("Poisson(50)")
pdf_poisson.setDrawable(draw,0)
pdf_poisson.setXTitle("values")
pdf_poisson.draw("pdf_Poisson", 640, 480, GraphImplementation.PNG)
Show(pdf_poisson)


poisson = Poisson(50)
cdf_poisson =  poisson.drawCDF(20, 90)
cdf_poisson.setTitle("CDF - Poisson(lambda)")
draw = cdf_poisson.getDrawable(0)
draw.setLegend("Poisson(50)")
cdf_poisson.setDrawable(draw,0)
cdf_poisson.setXTitle("values")
cdf_poisson.setLegendPosition("bottomright")
cdf_poisson.draw("cdf_Poisson", 640, 480, GraphImplementation.PNG)
Show(cdf_poisson)



# Rayleigh

rayleigh = Rayleigh(1.0, 0.0)
pdf_rayleigh =  rayleigh.drawPDF()
pdf_rayleigh.setTitle("PDF - Rayleigh(sigma, gamma)")
draw = pdf_rayleigh.getDrawable(0)
draw.setLegend("Rayleigh(1.0, 0.0)")
pdf_rayleigh.setDrawable(draw,0)
pdf_rayleigh.setXTitle("values")
pdf_rayleigh.draw("pdf_Rayleigh", 640, 480, GraphImplementation.PNG)
Show(pdf_rayleigh)



# Rice_1

rice_1 = Rice(1,5)
pdf_rice_1 =  rice_1.drawPDF(0,10)
pdf_rice_1.setTitle("PDF - Rice(sigma,nu)")
draw = pdf_rice_1.getDrawable(0)
draw.setLegend("Rice(1,5)")
pdf_rice_1.setDrawable(draw,0)
pdf_rice_1.setXTitle("values")
pdf_rice_1.draw("pdf_Rice_1", 640, 480, GraphImplementation.PNG)
Show(pdf_rice_1)

# Rice_2

rice_2 = Rice(2, 0.1)
pdf_rice_2 =  rice_2.drawPDF(0,10)
pdf_rice_2.setTitle("PDF - Rice(sigma,nu)")
draw = pdf_rice_2.getDrawable(0)
draw.setLegend("Rice(2,0.1)")
pdf_rice_2.setDrawable(draw,0)
pdf_rice_2.setXTitle("values")
pdf_rice_2.draw("pdf_Rice_2", 640, 480, GraphImplementation.PNG)
Show(pdf_rice_2)


# Student

student = Student(3.0, 1.0)
pdf_student =  student.drawPDF()
pdf_student.setTitle("PDF - Student(mu, sigma)")
draw = pdf_student.getDrawable(0)
draw.setLegend("Student(3.0, 1.0)")
pdf_student.setDrawable(draw,0)
pdf_student.setXTitle("values")
pdf_student.draw("pdf_Student", 640, 480, GraphImplementation.PNG)
Show(pdf_student)

# Skellam

skellam = Skellam(1.,7.)
pdf_skellam =  skellam.drawPDF(-20, 8)
pdf_skellam.setTitle("PDF - Skellam(l1,l2)")
draw = pdf_skellam.getDrawable(0)
draw.setLegend("Skellam(1,7)")
pdf_skellam.setDrawable(draw,0)
pdf_skellam.setXTitle("values")
pdf_skellam.draw("pdf_Skellam", 640, 480, GraphImplementation.PNG)
Show(pdf_skellam)

cdf_skellam =  skellam.drawCDF(-20, 8)
cdf_skellam.setTitle("CDF - Skellam(l1,l2)")
draw = cdf_skellam.getDrawable(0)
draw.setLegend("Skellam(1,7)")
cdf_skellam.setDrawable(draw,0)
cdf_skellam.setXTitle("values")
cdf_skellam.draw("cdf_Skellam", 640, 480, GraphImplementation.PNG)
Show(cdf_skellam)

# Trapezoidal

trapezoidal = Trapezoidal(1.0, 2.0, 3.0, 5.0)
pdf_trapezoidal =  trapezoidal.drawPDF()
pdf_trapezoidal.setTitle("PDF - Trapezoidal(a, b, c, d)")
draw = pdf_trapezoidal.getDrawable(0)
draw.setLegend("Trapezoidal(1.0, 2.0, 3.0, 5.0)")
pdf_trapezoidal.setDrawable(draw,0)
pdf_trapezoidal.draw("pdf_Trapezoidal", 640, 480, GraphImplementation.PNG)
Show(pdf_trapezoidal)


# Triangular

triangular = Triangular(1.0, 3.0, 4.0)
pdf_triangular =  triangular.drawPDF()
pdf_triangular.setTitle("PDF - Triangular(a, m, b)")
draw = pdf_triangular.getDrawable(0)
draw.setLegend("Triangular(1.0, 3.0, 4.0)")
pdf_triangular.setDrawable(draw,0)
pdf_triangular.setXTitle("values")
pdf_triangular.draw("pdf_Triangular", 640, 480, GraphImplementation.PNG)
Show(pdf_triangular)


# TruncatedNormal

truncatedNormal_1 = TruncatedNormal(2.0, 1.0, 1.5, 2.5)
pdf_truncatedNormal_1 =  truncatedNormal_1.drawPDF(1, 4.5)
pdf_truncatedNormal_1.setTitle("PDF - TruncatedNormal(mu_n, sigma_n, a, b)")
draw = pdf_truncatedNormal_1.getDrawable(0)
draw.setLegend("TruncatedNormal(2.0, 1.0, 1.5, 2.5)")
pdf_truncatedNormal_1.setDrawable(draw,0)
pdf_truncatedNormal_1.setXTitle("values")
pdf_truncatedNormal_1.draw("pdf_TruncatedNormal_1", 640, 480, GraphImplementation.PNG)
Show(pdf_truncatedNormal_1)



truncatedNormal_2 = TruncatedNormal(2.0, 1.0, -1.0, 5.0)
pdf_truncatedNormal_2 =  truncatedNormal_2.drawPDF(-2.0, 8.0)
pdf_truncatedNormal_2.setTitle("PDF - TruncatedNormal(mu_n, sigma_n, a, b)")
draw = pdf_truncatedNormal_2.getDrawable(0)
draw.setLegend("TruncatedNormal(2.0, 1.0, -1.0, 5.0)")
pdf_truncatedNormal_2.setDrawable(draw,0)
pdf_truncatedNormal_2.setXTitle("values")
pdf_truncatedNormal_2.draw("pdf_TruncatedNormal_2", 640, 480, GraphImplementation.PNG)
Show(pdf_truncatedNormal_2)


truncatedNormal_3 = TruncatedNormal(2.0, 1.0, 2.0, 5.0)
pdf_truncatedNormal_3 =  truncatedNormal_3.drawPDF()
pdf_truncatedNormal_3.setTitle("PDF - TruncatedNormal(mu_n, sigma_n, a, b)")
draw = pdf_truncatedNormal_3.getDrawable(0)
draw.setLegend("TruncatedNormal(2.0, 1.0, 2.0, 5.0)")
pdf_truncatedNormal_3.setDrawable(draw,0)
pdf_truncatedNormal_3.setXTitle("values")
pdf_truncatedNormal_3.draw("pdf_TruncatedNormal_3", 640, 480, GraphImplementation.PNG)
Show(pdf_truncatedNormal_3)


truncatedNormal_4 = TruncatedNormal(2.0, 1.0, 5.0, 8.0)
pdf_truncatedNormal_4 =  truncatedNormal_4.drawPDF()
pdf_truncatedNormal_4.setTitle("PDF - TruncatedNormal(mu_n, sigma_n, a, b)")
draw = pdf_truncatedNormal_4.getDrawable(0)
draw.setLegend("TruncatedNormal(2.0, 1.0, 5.0, 8.0)")
pdf_truncatedNormal_4.setDrawable(draw,0)
pdf_truncatedNormal_4.setXTitle("values")
pdf_truncatedNormal_4.draw("pdf_TruncatedNormal_4", 640, 480, GraphImplementation.PNG)
Show(pdf_truncatedNormal_4)


# Uniform

uniform = Uniform(0.0, 1.0)
pdf_uniform =  uniform.drawPDF()
pdf_uniform.setTitle("PDF - Uniform(a, b)")
draw = pdf_uniform.getDrawable(0)
draw.setLegend("Uniform(0.0, 1.0)")
pdf_uniform.setDrawable(draw,0)
pdf_uniform.setXTitle("values")
pdf_uniform.draw("pdf_Uniform", 640, 480, GraphImplementation.PNG)
Show(pdf_uniform)



# UserDefined
collection = UserDefinedPairCollection(3,UserDefinedPair(NumericalPoint(1), 0.0))
point1 = NumericalPoint(1, 0.5)
collection[0] = UserDefinedPair(point1, 0.2)
point2 = NumericalPoint(1, 1.)
collection[1] = UserDefinedPair(point2, 0.5)
point3 = NumericalPoint(1, 1.5)
collection[2] = UserDefinedPair(point3, 0.3)

userDefined = UserDefined(collection)
pdf_userDefined =  userDefined.drawPDF(0.0, 2.0)
pdf_userDefined.setTitle("PDF - UserDefined(points, weights)")
draw = pdf_userDefined.getDrawable(0)
draw.setLegend("UserDefined")
pdf_userDefined.setDrawable(draw,0)
pdf_userDefined.setXTitle("values")
pdf_userDefined.draw("pdf_UserDefined", 640, 480, GraphImplementation.PNG)
Show(pdf_userDefined)



userDefined = UserDefined(collection)
cdf_userDefined =  userDefined.drawCDF(0.0, 2.0)
cdf_userDefined.setTitle("CDF - UserDefined(points, weights)")
draw = cdf_userDefined.getDrawable(0)
draw.setLegend("UserDefined")
cdf_userDefined.setDrawable(draw,0)
cdf_userDefined.setXTitle("values")
cdf_userDefined.draw("cdf_UserDefined", 640, 480, GraphImplementation.PNG)
Show(cdf_userDefined)


# Weibull

weibull_1 = Weibull(1.0, 1.0, 0.0)
pdf_weibull_1 =  weibull_1.drawPDF()
pdf_weibull_1.setTitle("PDF - Weibull(e, beta, gamma)")
draw_1 = pdf_weibull_1.getDrawable(0)
draw_1.setLegend("Weibull(1.0, 1.0, 0.0)")
pdf_weibull_1.setDrawable(draw_1,0)
pdf_weibull_1.setXTitle("values")
pdf_weibull_1.draw("pdf_Weibull_1", 640, 480, GraphImplementation.PNG)
Show(pdf_weibull_1)


weibull_2 = Weibull(2.0, 1.0, 0.0, Weibull.MUSIGMA)
pdf_weibull_2 =  weibull_2.drawPDF()
pdf_weibull_2.setTitle("PDF - Weibull(mu, sigma, gamma)")
draw_2 = pdf_weibull_2.getDrawable(0)
draw_2.setLegend("Weibull(2.0, 1.0, 0.0)")
pdf_weibull_2.setDrawable(draw_2,0)
pdf_weibull_1.setXTitle("values")
pdf_weibull_2.draw("pdf_Weibull_2", 640, 480, GraphImplementation.PNG)
Show(pdf_weibull_2)

# ZipfMandelbrot

zipfMandelbrot_1 = ZipfMandelbrot(20, 1.0, 1.0)
pdf_zipfMandelbrot_1 =  zipfMandelbrot_1.drawPDF(0,21)
pdf_zipfMandelbrot_1.setTitle("PDF - Zipf-Mandelbrot(N,q,s)")
draw_1 = pdf_zipfMandelbrot_1.getDrawable(0)
draw_1.setLegend("Zipf-Mandelbrot((20, 1.0, 1.0)")
pdf_zipfMandelbrot_1.setDrawable(draw_1,0)
pdf_zipfMandelbrot_1.setXTitle("values")
pdf_zipfMandelbrot_1.draw("pdf_ZipfMandelbrot_1", 640, 480, GraphImplementation.PNG)
Show(pdf_zipfMandelbrot_1)

zipfMandelbrot_1 = ZipfMandelbrot(20, 1.0, 1.0)
cdf_zipfMandelbrot_1 =  zipfMandelbrot_1.drawCDF(0,21)
cdf_zipfMandelbrot_1.setTitle("CDF - Zipf-Mandelbrot(N,q,s)")
draw_1 = cdf_zipfMandelbrot_1.getDrawable(0)
draw_1.setLegend("Zipf-Mandelbrot(20, 1.0, 1.0)")
cdf_zipfMandelbrot_1.setDrawable(draw_1,0)
cdf_zipfMandelbrot_1.setXTitle("values")
cdf_zipfMandelbrot_1.draw("cdf_ZipfMandelbrot_1", 640, 480, GraphImplementation.PNG)
Show(cdf_zipfMandelbrot_1)
