'''
Created on Mar 1, 2023

@author: eohay
'''
import pandas as pd
import numpy as np
from sympy import symbols, solve

def standard_deviation_from_index_model(Sigma_m: float, Sigma_E_Alpha: float, beta: float)-> float:
    """
    This method returns the standard deviation of a stock using the index model
    @param Sigma_m: standard deviation of the market
    @param Sigma_E_Alpha: sigma of the stock's unexpected
    @param beta: The beta between stock and market
    @return: The standard deviation of the stocl
    """
    return np.sqrt(((np.square(beta)*np.square(Sigma_m))+np.square(Sigma_E_Alpha)))

def calculate_beta_of_a_stock(alpha: float, return_market_index: float, risk_free_return: float, stock_return_exceeds: float)-> float:
    """
    CAPM formula
    This method uses capm to calculate the beta of a stock
    @param alpha: Alpha 
    @param return_market_index: return of the market index
    @param risk_free_return:
    @param stock_return_exceeds:
    @returns: the beta of the stock with the market  
    """
    b=symbols('Beta')
    eq=alpha+b*(return_market_index-risk_free_return)-stock_return_exceeds
    return solve(eq)

def calculate_covarince_of_two_stock(beta_stock_a: float, beta_stock_b: float, sigma_market: float )-> float:
    """
    This function calculates the covariance between 2 stocks using their betas to the market and market std
    @param beta_stock_a: beta between stock a and market
    @param beta_stock_b: beta between stock b and market
    @param sigma_market: standard deviation of the market
    @return covariance between stock A and and stock B
    """
    return beta_stock_a*beta_stock_b*np.square(sigma_market)


def calculate_covariance_stock_market(beta: float, sigma_market: float )-> float:
    """
    This function calculates the covariance between a stock and the market
    @param beta_stock_a: beta between stock and market
    @param sigma_market: standard deviation of the market
    @return covariance between stock and market
    """
    return sigma_market**2 * beta

def portfolio_with_proportions(weight_stock_a: float, weight_stock_b: float, weight_risk_free: float, standard_deviation_market: float, expectedReturns: list, betas: list, standard_deviation: list) -> tuple:
    """
    This function returns the Expected Return, Standard Deviation, Beta, and nonsystematic std of a portfolio consisting of 3 weights using the market index theory
    @param weight_stock_a: 
    @param weight_stock_b: 
    @param weight_risk_free: 
    @param standard_deviation_market: standard deviation of the market
    @param expectedReturns: a list consisting of the expected returns of each asset where expected[0]= expected return of stock a, expected[1]= expected return of stock b and so forth
    @param betas: a list consiting of the betas of each asset, follows same rules as expectedReturns
    @param standard_deviation: list of the standard deviations, standard deviation of stock a followed by b
    @return: a tuple representing the calculated values
    """
    expected_return_portfolio= expectedReturns[0]*weight_stock_a+ expectedReturns[1]* weight_stock_b+expectedReturns[2]*weight_risk_free
    beta_of_portfolio= betas[0]* weight_stock_a+ betas[1]*weight_stock_b+ betas[2]*weight_risk_free
    
    unsystematic_component=weight_stock_a**2*standard_deviation[0]**2+ weight_stock_b**2 * standard_deviation[1]**2
    standard_deviation_of_portfolio= np.sqrt(np.square(beta_of_portfolio)*np.square(standard_deviation_market)+unsystematic_component)
    return (    ("The portfolio's expected return: ", expected_return_portfolio), ("The standard deviation of the portfolio: ", standard_deviation_of_portfolio), ("The beta of the portfolio is ", beta_of_portfolio), ("Nonsystematic standard devaition: ", np.sqrt(unsystematic_component)) )
#print(f"{portfolio_with_proportions(.25,.5,.25,25,[8,16,9], [1,1.6,0], [28,40]    )}")    
   
def standard_deviation_two_stock_rsquared_and_8_9(Beta_a: float, Beta_b: float, sigma_m: float, r_sqaure_a:float, r_square_b: float)-> tuple: 
    standard_deviation_a=np.sqrt(Beta_a**2* (sigma_m**2/r_sqaure_a))
    standard_deviation_b=np.sqrt(Beta_b**2* (sigma_m**2/r_square_b))
    return (("STD A :" ,standard_deviation_a) ,("STD B: " ,standard_deviation_b))

def held_well_diversified_portfolio(sigma_port:float, sigma_m: float):
    """
    This function calculates the beta of a well diverified portfolio to the market
    @param sigma_port: std port
    @param sigma_m: std marekt
    @return: Beta to market
    """
    return np.sqrt(sigma_port**2/sigma_m**2)


"""
========================================
CHAPTER 9
========================================
"""

def market_price_security_correlationCoefficDoubles(oldPrice: float, expected_return: float, rf: float, marketRiskPremium: float )-> float:
    """
    This function calculates the new stock price when the coreelation coeficient with market doubles but can modify for other
    @param oldPrice: Current stock price
    @param expected_return: expected return of the stock
    @param rf:risk free rate
    @param Market risk premium:This is the market expected return-rf 
    @return: New price of stock   
    
    """
    beta=(expected_return-rf)/(marketRiskPremium)
    divended=oldPrice*expected_return
    new_beta=2*beta
    new_expected_ret=rf+new_beta*marketRiskPremium
    return divended/new_expected_ret

def calculate_beta(rf: float, expected_ret_market: float, expected_return_stock: float)-> float:
    """
    This function calculates the beta of a stock
    @param rf:risk free
    @param expected_ret_market: expected return of market
    @param expected_return_stock:expected return of stock
    @return: beta of stock 
    """
    return (expected_return_stock-rf)/(expected_ret_market-rf)

"""
Put in percent form
"""
def use_capm_to_determine_over_or_under_priced(expected_rate: float, beta: float, rf: float, market_expected_return: float)->str:
    cap_mReturn= beta*(market_expected_return-rf)+rf
    if cap_mReturn<expected_rate:
        return "OverPriced"
    return 'UnderPriced'
def calculate_if_possible(exp_return: list, sd: list)->bool:
    """
    This function calculates if a situation is possible based on capm
    Percentages in decimal form
    @param exp_return: a list of expected returns where exp_ret[0]=A (stock), exp_ret[1]= market, and exp_ret[2]= rf
    @param sd: a list of standard deviations where exp_ret[0]=A (stock), exp_ret[1]= market, and exp_ret[2]= rf
    @return: bool representing whether the situation is valid
    """
    sharpe_a=((exp_return[0]-exp_return[2])/sd[0])
    sharpe_b=((exp_return[1]-exp_return[2])/sd[1])
    
    if sharpe_a<sharpe_b:
        return True
    return False
print(calculate_if_possible([.14,.16,.04], [.25,.27,0]))

def problem_9_21_info_on_portfolio(beta: float, rf: float, expected_return_market: float, current_price:float, sell_price: float, div: float)-> tuple:
    """
    This function calculates the expected return of a stock based on a portfolio and whether it is over/underpriced
    @param beta: Beta of the stock/port to market
    @param rf:risk free rate
    @param expected_return_marekt: expected return of portiflio by market
    @param current_price :current prince of stock
    @param sell_price: selling price of stock
    @param div: dividend on stock  
    @return: a tuple representing the expected rate of return and whether the stock is over/under priced
    """
    rm=expected_return_market
    expected_rate_return= rf+beta*(rm-rf)
    hpr= (sell_price-current_price+div)/current_price
    ans=""
    capm=rf+beta*(rm-rf)
    
    if capm<hpr:
        ans="UnderPriced"
    else:
        ans="OverPriced"
        
    return (("expected rate of return: ", expected_rate_return), ("the stock is ", ans) )

def problem_expected_return_using_hpr_problem_9_17(risk_free: float, market_return: float, price_today: float, div: float, beta: float)-> float:
    """
    This function returns the expected stock price-> what investors expect to sell the stock at in a year
    @param risk_free: risk free rate
    @param market_return: The expected rate of return of the market  
    @param price_today: The price of the stock today
    @param div : Dividend 
    @param beta: Beta of stock to market 
    """
    expected_return=beta*(market_return-risk_free)+risk_free
    
    if(expected_return>1): #ignore this
        expected_return/=100 #ignore this
        
    required_return=expected_return-(div/price_today)
    return price_today*(1+required_return)

def problem_investors_comparing_2_assets_which_is_better(investor_1_returns: float, investor_2_returns: float, beta_investor1: float, beta_investor2: float, return_market: float, rf: float):
    """
    This fuction compares the investments of 2 investors against the capm to determine which one has the better investment through a greater excess return
    @param investor_1_returns: The actual returns of investor 1's portfolio
    @param investor_2_returns: The actual returns of investor 2's portfolio
    @param beta_investor1: The beta of investor 1's portfolio
    @param beta_investor2: The beta of investor 2's portfolio
    @param return_market: The market's return
    @param rf: risk free rate
    @return: Which investor has the better portfolio
    @note: All percentages go in decimal form
    """
    excess_return_investor_1=investor_1_returns-(beta_investor1*(return_market - rf)+rf)
    excess_return_investor_2=investor_2_returns-(beta_investor2*(return_market - rf)+rf)
    if excess_return_investor_1>excess_return_investor_2:
        return "Investor 1 excess is "+ str(excess_return_investor_1) 
    return "Investor 2 excess is " + str(excess_return_investor_2)

#print(problem_investors_comparing_2_assets_which_is_better(21, 18, 1.4, 1, 17, 4))





def problem_accidentialy_overestimate_beta(rf: float, return_market: float, expected_cash_flow: float, predicted_beta: float, actual_beta: float):
    """
    This function is used to determine by how much one over/underpays for an asset when they estimate an incorrect beta
    @param rf: risk free rate
    @param return_market: market return
    @param expected_cash_flow: expected cash flow
    @param predicted_beta: The investors beta
    @param actual_beta: The actual beta of the asset
    @return: THe amount the investor over/under paid for the asset
    """
    required_return_my_beta= (rf+predicted_beta*(return_market-rf))/100
    required_return_actual_beta=(rf+actual_beta*(return_market-rf))/100
    
    pv_my_beta=expected_cash_flow/required_return_my_beta
    pv_actual_beta=expected_cash_flow/required_return_actual_beta
    
    return pv_my_beta-pv_actual_beta

def problem_9_26_portfolio_beta_2_securities(amount_invested_sec_1: float,amount_invested_sec_2: float, beta_security_1: float,beta_security_2: float):
    """
    This function returns the beta of a portfolio made up of 2 assets with diff betas
    @param amount_invested_sec_1: amount invested in security 1
    @param amount_invested_sec_1: amount invested in security 1
    @param beta_security_1: The beta of the first security
    @param beta_security_2: The beta of the second security
    """
    total_amount=amount_invested_sec_1+ amount_invested_sec_2
    return beta_security_1*(amount_invested_sec_1/total_amount)+ beta_security_2*(amount_invested_sec_2/total_amount)

def use_2_index_model_to_cal_missing_risk_premium(stock_expected_return: float, rf: float, beta_first_var: float, beta_second_var:float, risk_premium_first_var: float):
    """
    This function calculates the missing risk premium of a 2 factor model
    @param stock_expected_return: expected return of the stock
    @param rf: risk free rate
    @param beta_first_var:beta of the first factor and also of the one which we know its risk premium
    @param beta_second_var: beta of second variable and of the one we where we need to calculate its risk premium
    @param risk_premium_first_var: The risk premium of the first variable and of the one we have
    @return: The solved risk premium of the second factor
    In percent form
    """
    missing_rp=symbols('rp2')
    eq=-stock_expected_return+rf+beta_first_var*risk_premium_first_var+beta_second_var*missing_rp
    return solve(eq)