# Risk Management at Tesla

## Project Description
This repository contains a series of presentations focusing on risk management at Tesla. The presentations detail various aspects of Tesla as a company, identify risk factors, measure risk, and analyze potential returns or losses from selected risk variables.

## Presentation 0: Introduction to Tesla 
 `Presentation_0_of_the_Tesla_company.pdf`
  
This presentation provides an overview of Tesla, covering:
- Industry and type of business.
- Company structure.
- Company size.
- Markets in which Tesla operates, including partners, clients, and competitors.
- Required data and potential sources.

## Presentation 1: Risk Identification at Tesla 
 `Presentation_1_risk_identification.pdf`
  
This presentation includes:
1. Identification of risk sources/factors.
2. Creation of a risk register (`Register_Tesla.png`):
   - Risk description.
   - Risk category.
   - Consequences of occurrence.
   - Significance assessment.
   - Frequency assessment.
   - Possible preventive actions.
3. Development of a risk map and risk hierarchy.
4. Development of a risk assessment questionnaire for a selected area.

## Presentation 2: Risk Measurement
`Presentation_2_determining_the_risk_measure_for_selected_risk_variables.pdf`. Associated script: `SCRIPT_presentation_2.ipynb` with data from `USD_EUR.csv` and `USD_CNY.csv`. Written in Python.
  
Measuring risk for two selected variables: USD/EUR and USD/CNY exchange rates.
1. Univariate analysis:
   - Variability measures.
   - Quantiles.
   - Distribution values.
2. Multivariate analysis:
   - Variability measures for a portfolio.
   - Portfolio quantiles.
   - Portfolio and 2-dimensional distribution values.
   - Comparison with univariate results.
3. Extreme risk analysis for USD/CNY exchange rate:
   - Fitting a conditional exceedance distribution.
4. Backtesting for selected risk variables.
   

## Presentation 3: Value at risk calculations
`Presentation_3_Value_at_risk.pdf`. Associated script: `SCRIPT_presentation_3.ipynb` with data from `USD_EUR.csv`.
1. Calculations of VaR95% and VaR99%:

   a) Parametric method with T-student distribution.

   b) Historical method:
     - Standard.
     - Weighted.
     - Using GARCH filtering.
   
   c) Monte Carlo method with T-student distribution
3. Backtesting the selected methods from 1a), 1b), 1c).

## Tools Used
- **Python language**

**Libraries**: pandas, matplotlib.pyplot, numpy, statsmodels, scipy, csv, seaborn, arch
