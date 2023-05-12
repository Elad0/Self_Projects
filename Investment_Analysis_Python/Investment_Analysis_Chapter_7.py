'''
Created on Feb 8, 2023
Notes on all functions and some examples provided with the more complicated ones
@author: eohay
'''
import pandas as pd
import numpy as np
from sympy import symbols, solve

#=======================================================CHAPTER 7 STUFF=========================================== 

#====================================================================================================================



#    ===================================
#    Relationship Between 2 Things (Vague I know)
#    ===================================

def CovarianceCalculator(returnsofStockA: list, returnsofStockB: list) -> float:
    '''
    This Method calculates the covariance between 2 stocks and their returns
    @param returnsofStockA: #list representing the returns of stock A
    @param returnsofStockB: list representing the returns of stock b
    @return: the covariance between the two lists
    Throws exception if the 2 methods of calculation dont equal eachother (shouldn't happen)
    '''
    df = pd.DataFrame({
        'Stock A':returnsofStockA, 
        'Stock B':returnsofStockB,
        })

    stockReturns1=pd.Series(returnsofStockA)
    stockReturns2=pd.Series(returnsofStockB)

    value_from_DataFrame=df.cov().iloc[0]['Stock B']
    value_from_Series= stockReturns1.cov(stockReturns2)
    
    #print(df.cov()) #Visualization
    if value_from_DataFrame != value_from_Series:
        raise Exception("Conflict between 2 methods of calculation", value_from_Series, " preferred")
    
    return value_from_Series
    
def coefficient_Of_Correlation(returnsofStockA: list, returnsofStockB: list)-> float:
    '''
    This method calculates the Pearson coefficent of correlation
    @param returnsofStockA: The first list representing the returns of stock A
    @param returnsofStockB: The first list representing the returns of stock B
    @throws Exception if the 2 methods of calculation vary
    @return: the Pearson coefficent of correlation between the 2 lists
    '''
    df = pd.DataFrame({
        'Stock A':returnsofStockA, 
        'Stock B':returnsofStockB,
        })
    
    stockReturns1=pd.Series(returnsofStockA)
    stockReturns2=pd.Series(returnsofStockB)
    
    value_from_DataFrame=df.corr().iloc[0]['Stock B']
    correlation_from_Series=stockReturns1.corr(stockReturns2, method='pearson')
    if value_from_DataFrame != correlation_from_Series:
        raise Exception("Conflict between 2 methods of calculation", correlation_from_Series, " preferred")
    
    #print(df.corr())
    return(value_from_DataFrame)

def Regular_SD_and_Variance(numbers: list) ->tuple:
    '''
    Returns the standard deviation of the inputted list
    @param numbers: Just some numbers
    @returns: A tuple of the standard deviation and variance in this order
    '''
    SD=pd.Series(numbers).std()
    return(SD, np.square(SD))

def Discrete_SD_and_Variance(probabilities: list, returns: list) ->tuple:
    '''
    This method calculates and returns the mean, standard deviation and variance (in this order) of returns when they have a probability associated with them
    @param probabilities: the probability of each outome happeneing. probailities[0] corresponds to returns[0] and so forth
    @param returns: the returns of the being associated with this calculation 
    @returns: A tuple of the Mean, standard deviation and variance in this order
    '''
    if len(probabilities) != len(returns):
        raise Exception("why are you even doing this")
    
    
    weighted_expected_return=0
    weighted_variance=0
      
    for p,r in zip(probabilities,returns):
        weighted_expected_return+=p*r
    
    
    for p,r in zip(probabilities,returns):
        weighted_variance+=p*(r-weighted_expected_return)**2
        
    
    return weighted_expected_return, weighted_variance**.5, weighted_variance  
print(Discrete_SD_and_Variance([.1,.2,.2,.3,.2], [8,7,6,9,8]))
def coefficient_Of_Correlation_Probabilities_associated(probabilities: list, returnsofStockA: list, returnsofStockB: list) -> float:
    """
    This function calculates the correlation coeffiecnt between 2 stocks when there are probabilities associated with them
    @requires: This function calls Discrete_SD_and_Variance
    @param probabilities: The probabilities assocated with the 2 stocks
    @param returnsofStockA: #list representing the returns of stock A
    @param returnsofStockB: list representing the returns of stock b
    @return: The correlation coefficent between the 2 stocks
    
    """
    Expected_Stock_A=Discrete_SD_and_Variance(probabilities, returnsofStockA)[0]
    Expected_Stock_B=Discrete_SD_and_Variance(probabilities, returnsofStockB)[0]
    Standard_Deviation_Stock_A=Discrete_SD_and_Variance(probabilities, returnsofStockA)[1]
    Standard_Deviation_Stock_B=Discrete_SD_and_Variance(probabilities, returnsofStockB)[1]
    
    Cov_A_B=0
    for prob,return_A,return_B in zip(probabilities,returnsofStockA, returnsofStockB):
        Cov_A_B+=prob*(return_A-Expected_Stock_A)*(return_B-Expected_Stock_B)

    return Cov_A_B/(Standard_Deviation_Stock_A* Standard_Deviation_Stock_B)

def blended_standard_deviation_of_2_assets(weight_stock_a: float, weight_stock_b: float, probabilities: list, returnsofStockA: list, returnsofStockB: list )-> float:
    """
    @requires: uses the function {Discrete_SD_and_Variance} and {coefficient_Of_Correlation_Probabilities_associated} 
    This function calculates the Standard Deviation of a Portfolio Consisting of a blend of 2 stocks
    @param weight_stock_a: Weight of stock a in the portfolio
    @param weight_stock_b: Stock B's weight in the portfolio
    @param probabilities: The probabilities assocated with the 2 stocks
    @param returnsofStockA: #list representing the returns of stock A
    @param returnsofStockB: list representing the returns of stock b
    @return: The standard deviation of the optimal blended portfolio
    
    @attention: example: blended_standard_deviation_of_2_assets(.25, .75, [.3,.5,.2], [7,11,-16], [-9,14,26])
    Where weight_stock_a= .25, weight_stock_b=.75, probabilities=[30%, 50%, 20%], returnsofStockA are= [7%, 11%, -16%], returnsofStockB are= [-9%, 14%, 26%]
    """
    Data_Stock_A= Discrete_SD_and_Variance(probabilities, returnsofStockA)
    Data_Stock_B= Discrete_SD_and_Variance(probabilities, returnsofStockB)
    corr_a_b= coefficient_Of_Correlation_Probabilities_associated(probabilities, returnsofStockA, returnsofStockB)
    Variance_A=Data_Stock_A[2]
    Variance_B=Data_Stock_B[2]

    return(np.sqrt( (weight_stock_a**2 * Variance_A) + (weight_stock_b**2 * Variance_B) + (2*weight_stock_a*weight_stock_b*Variance_A**.5 * Variance_B**.5 * corr_a_b)))

def calculate_optimal_differnce_between_2stocks_risky_portfolio_along_with_RiskyPortfolio_Expected_Return_and_Standard_Deviation(expectedReturn: list, sd: list, corr_a_b: float)-> tuple:
    '''
    This method calcuclates the optimal risky portfolio made up of 2 risky assets PUT ZERO WHEN RISK FREE NOT GIVEN
    @param expectedReturn: The expected return of stock A followed by stock B, followed by risk free rate IN PERCENT FORM. This risk free rates can equal zero
    @param sd: The standard deviation of stock A followed by stock B IN PERCENT FORM
    @param corr_a_b: The correlation between A and B IN PERCENT FORM
    @return: a tuple representing the amount of money in A (y), the percentage in B (1-y), portfolio expected return, portfolio SD and IN PERCENT FORM
    '''
    expectedReturn_StockA=expectedReturn[0]
    expectedReturn_StockB=expectedReturn[1]
    risk_free_rate=expectedReturn[2]
    var_StockA=np.square(sd[0])
    var_StockB=np.square(sd[1])
    cov_a_b= sd[0] * sd[1] * corr_a_b
    numerator= ((expectedReturn_StockA-risk_free_rate)*var_StockB)-(expectedReturn_StockB-risk_free_rate)*cov_a_b 
    denominator= ((expectedReturn_StockA-risk_free_rate)*var_StockB+ (expectedReturn_StockB-risk_free_rate)*var_StockA) - ((expectedReturn_StockA-risk_free_rate+expectedReturn_StockB-risk_free_rate)*cov_a_b)
    wA=numerator/denominator
    wB=1-wA
    sd_risky_portfolio=np.sqrt(np.square(wA)*var_StockA+ np.square(wB)*var_StockB+(2*wA*wB*cov_a_b))
    return ("Weight of stock A", wA), ("Weight of stock B", wB), ("Expected Return of Risky Portfolio is ", wA*expectedReturn_StockA+wB*expectedReturn_StockB), ("SD of Risky Portfolio is ", sd_risky_portfolio)

print(calculate_optimal_differnce_between_2stocks_risky_portfolio_along_with_RiskyPortfolio_Expected_Return_and_Standard_Deviation([.14,.18,.3], [.6,.1],-1))

def calculate_SD_MoneyMarketFund_Stocks_Bonds(expectedReturn: list, sd: list, corr_a_b: float, required_complete_return: float)-> tuple:
    """
    @requires: This function relies on calculate_optimal_differnce_between_2stocks_risky_portfolio_along_with_RiskyPortfolio_Expected_Return_and_Standard_Deviation and extracts data from it 
    This method makes the same calulations as the above but of the complete portfolio when expecting a return of x and proportion invested in money market fund, Stocks, and Bonds
    @param expectedReturn: The expected return of stock A followed by stock B, followed by risk free rate IN PERCENT FORM. This risk free rate can equal zero
    @param sd: The standard deviation of stock A followed by stock B IN PERCENT FORM
    @param corr_a_b: The correlation between A and B IN PERCENT FORM
    @param required_complete_return: The required return of the complete portfolio
    
    @return A tuple representing the Weight of the Money Market Fund, Standard Deviation of the Complete Portfolio, Weight of the Stock Fund (Fund A), and Weight of the Bond Fund (Fund B)
    
    @attention: example: 
    """
    extractedData=[x[1] for x in calculate_optimal_differnce_between_2stocks_risky_portfolio_along_with_RiskyPortfolio_Expected_Return_and_Standard_Deviation(expectedReturn,sd, corr_a_b)]
    moneyA=extractedData[0]
    moneyB= extractedData[1]
    expectedRetRisky=extractedData[2]
    riskySD=extractedData[3]

    
    w=symbols('w')
    eq=(1-w)*expectedRetRisky+w*expectedReturn[2]-required_complete_return
    weight_tbill=float(solve(eq)[0])
    weight_optimal_portfilio=1-weight_tbill
    SDRC= np.sqrt(((weight_optimal_portfilio*riskySD)**2 + (weight_tbill*0)**2+ 2*weight_optimal_portfilio*weight_tbill*riskySD*0*0))
    W_fund_A= moneyA*weight_optimal_portfilio
    W_fund_B= moneyB*weight_optimal_portfilio
    
    return (("weight of t-bill is (Money market Fund):", weight_tbill), ("Standard Deviation Complete Portfolio", SDRC), ("Weight Stock Fund (FUND A)", W_fund_A),("Weight Bond Fund (FUND B)", W_fund_B) ) 


"""
Need a comment here due to IDE -> ignore
"""

#   =====================================
#    Dealing with Risk Aversion and Y
#  ======================================

def calculate_proportionY_RiskyEquities_and_Bonds(expected_return: float, risk_free_rate: float, risk_aversion_coefficient: float, isStandardDevation: bool, sigma: float )-> tuple:
    '''
    This function uses the equation y=E[r]-rf/(A*Variance) to calculate the proportion a portfolio should be in risky equity and bonds
    @param expected_return: The expected return of equity in decimal form
    @param risk_free_rate: the risk free rate in decimal form
    @param risk_aversion_coefficient: Measures how risk averse someone is. The higher the more risk averse the person is
    @param isStandardDevation: bool to check if the sigma is variance or SD
    @param sigma: the sigma, in decimal form
    
    @return: a tuple representing y (what goes in risky assets) and 1-y what goes in bonds
    '''
    if not isStandardDevation: #If we are given variance we need to squareroot it
        sigma=np.sqrt(sigma)
        
    y=(expected_return-risk_free_rate)/(risk_aversion_coefficient * np.square(sigma))
    
    return ("(Percent in Risky Assests) y=", y), ("(Percent in T-Bills) 1-y=",1-y)


def calculate_propotionY_riskyPort_Risk_port(required_expectedReturn: float, expected_return_risky: float, expected_return_risk_free: float, SDP: float)-> tuple:
    """
    This method calculates the SD of the Complete Port, and Y of risky port and 1-y not risky. Rearrange to solve for other things
    It uses the Equation E[rc] = E[rf]-y(E[rp]-E[rf] 
    @param required_expectedReturn: The required Expected Return for the complete Portfolio (E[RC])
    @param expected_return_risky: The expected return of the risky portfolio
    @param expected_return_risk_free: The expected Return of the risk free portfolio
    @param SDP: The standard deviation of the risky portoflio
    
    @reqturn a tuple of y*, 1-y*, and the standard deviation of the complete porfolio
    y represents the weight of the risky porfolio in the complete portfolio 
    1-y represents the weight of the risk free assets in the risk free portoflio
    
    @attention: example: calculate_propotionY_riskyPort_Risk_port(.08, .12, .03, .17)) Where our required expected return of the complete portfolio= 8%, 
    the expected return of the risky portfolio= 12%, the expected return of the risk-free portfolio= 3%, and the standard deviation of the risky portfolio=17
    """
    y=symbols('y')
    eq=expected_return_risk_free-required_expectedReturn+y*(expected_return_risky-expected_return_risk_free)
    ans=solve(eq)[0]
    
    return(("Percentage in Risky asset", ans), ("Percentage in non risky ", 1-ans), ("SD Complete is ", SDP*ans))

#    ======================================================CHAPTER 7 ENDS=========================================== 



#====================================================================================================================