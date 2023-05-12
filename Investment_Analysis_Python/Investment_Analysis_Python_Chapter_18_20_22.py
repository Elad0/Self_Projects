'''
Created on May 7, 2023
EVERY PERCENT IN DECIMAL FORM
@author: eohay
'''
#TB MC Qu. 22-39 You sold one wheat future contract...
"""
@parameter sellprice: price you sold futures at
@param buyPrice: also known as spot price: where you bought the future
@param contractSize: how much of the comodity the contract represents
"""
def solfBushelPandL(sellPrice, buyPrice, contractSize):
    return (sellPrice-buyPrice)*contractSize

"""
An investor purchases a stock for $38 and a put for $.50 with a strike price of $35. 
The investor sells a call for $.50 with a strike price of $40. 
What is the maximum profit for this position?

This function returns the maximum profit and maximum loss on an options strategery when a call is sold, a put is bought and a stock is bought
@param price_stock_bought: price of a share
@param price_put: price of the long put
@param strike_put: strike of the put
@param: price_call_sold: price the call was sold at (premium collected on short call
@param strike_call: strike of the short call
@return: tuple representing max profit and max loss

"""
def problem_20_10(price_stock_bought, price_put, strike_put, price_call_sold, strike_call):
    max_profit=strike_call-price_stock_bought-price_put+price_call_sold
    max_loss= strike_put-price_stock_bought- price_put + price_call_sold
    
    return (("Max profit", max_profit), ("Max loss", max_loss))

"""
Computer stocks currently provide an expected rate of return of 26%. MBI, 
a large computer company, will pay a year-end dividend of $3.90 per share.

@param expected_rate_return: expected rate of return on stock 
@param year_end_dividend: dividend being paid at the end of the year
@param current_price: The current price of the stock
@return: the growth rate of the stock

If dividend growth forecast decrease, then so does price of stock
so will p/e ratio in extension

example: print(problem_18_18(.26, 3.9, 69))
"""
# expectected rate of return in decimal form
def problem_18_18(expected_rate_return, year_end_dividend, current_price):
    return expected_rate_return-(year_end_dividend/current_price)

"""
Calculate the amount of money and percent returned from buying N number of option contracts
Example: price of stock is 160, Strike of contract is 150, 15 contracts, and 15,000$ invested
print(problem_20_6_option_return_calculator(170,150,15,15000))
@param price_stock: price of the stock
@param strike_option: strike price of the option
@param number_contracts: number of contracts (each represents 100)
@param money invested: the amount of money invested  
"""
def problem_20_6_option_return_calculator(price_stock, strike_option, number_contracts, money_invested):
    if price_stock<strike_option:
        return 0,-100
    
    money_return=(price_stock- strike_option)* (number_contracts * 100)
    
    percent_return=((money_return-money_invested)/money_invested) *100
    return (money_return, percent_return)

"""
 Buy 100 options (one contract) for $1,000, 
 and invest the remaining $14,000 in a money market fund paying 5% in interest over 6 months (10% per year).
@param price_stock: price of the stock
@param strike_option: strike price of the option
@param number_contracts: number of contracts (each represents 100)
@param money_invested_options: the amount of money invested into options
@param money_invested_tbill:  money invested into tbill
@param interest_rate_tbill:  rate of return on tbill
@param num_periods_tbill_return: number of periods tbill is being held

Example:  
print(problem_20_6_t_bill_and_option_return_calculator(170, 150, 1, 1000, 14000,.05, 1)) 
"""
def problem_20_6_t_bill_and_option_return_calculator(price_stock, strike_option, number_contracts, money_invested_options, money_invested_tbill, interest_rate_tbill, num_periods_tbill_return  ):
    tbill_return= money_invested_tbill * (1+interest_rate_tbill)**num_periods_tbill_return
    options_return= problem_20_6_option_return_calculator(price_stock, strike_option, number_contracts, money_invested_options)[0]
    
    total_money_portfolio= tbill_return+ options_return
    
    total_money_invested= money_invested_options+ money_invested_tbill
   
    percent_return_portfolio= ((total_money_portfolio-total_money_invested)/total_money_invested)*100
   
   
    return (total_money_portfolio,percent_return_portfolio )
   

"""
18-67
JCPenney Company is expected to pay a dividend in year 1 of $1.65, a dividend in year 2 of $1.97, and a dividend in year 3 of $2.54. 
After year 3, dividends are expected to grow at the rate of 8% per year. An appropriate required return for the stock is 11%.
 The stock should be worth _______ today.
 
@param dividends: a list representing the dividends until year N where it has an expected growtg rate
@param divdend_growth_rate: dividend growth rate
@param required_return: required return on the stock

Example: print(continous_dividends_then_expectedGrowth([1.65,1.97,2.54], .08, .11))
"""
def continous_dividends_then_expectedGrowth(dividends: list, divdend_growth_rate, required_return):
    present_value_stock=0
    for y,x in enumerate(dividends):
        present_value_stock+=x/(1+required_return)**(y+1)
    
    terminal_value= dividends[-1]*(1+divdend_growth_rate)/(required_return-divdend_growth_rate)
    
    present_value_stock+=terminal_value/(1+required_return)**len(dividends)
    
    return present_value_stock

"""
A firm pays a current dividend of $1.00, which is expected to grow at a rate of 5% indefinitely. 
If current value of the firm’s shares is $35.00, 
what is the required return based on the constant-growth dividend discount model (DDM)?

@param current_dividend: current dividend being paid
@param growth_rate: growth rate of dividend (indefinite)
@param share_price: current value of on share

Example: print(problem_18_6_required_return_ddm(1,.05, 35))

"""
def problem_18_6_required_return_ddm(current_dividend, growth_rate, share_price):
    return current_dividend/share_price + growth_rate

"""
 This function determines the futures price based off spot price, time to expiration, and tbill rate
 @param spot_price: spotprice of futures contract
 @param time_to_expiration: Time to maturity of the options contract
 @param tbill_rate: risk free rate IN DECIMAL FORM
 
 Example: print(problem_22_8(300,7, .06))
"""   
def problem_22_8(spot_price, time_to_expiration, tbill_rate):
    return spot_price* (1+tbill_rate)**time_to_expiration

"""
This function determines 3 different parameters from a futures contract
@param contract_settle: The price of the contract
@param margin_requirement: The margin requirement of the clearing house
@param contract_multiplier: The multipler on the contract (For options it is 100)
@param futures_price_increase: how much the contract increased to 
@param percent_falls_by: The percent loss in the value of the contract

@return: A tuple representing A: The required margin, 
                              B: The % return increase when the value of the contract increases to a set price
                              C: The % return decrease when the value of the contract increases by a percentage (like 1% decrease)
                              
Example: print(problem_22_7_refer_to_actual_data(2555, .16, 50, 2601, .01))

"""
def problem_22_7_refer_to_actual_data(contract_settle, margin_requirement, contract_multiplier, futures_price_increase, percent_falls_by):
    required_margin=(contract_settle * contract_multiplier) * margin_requirement
    
    percentage_return_net_investment= (futures_price_increase-contract_settle)* (contract_multiplier/required_margin)
    
    new_price_contract=contract_settle-(contract_settle*percent_falls_by)
    percentage_return_net_investment_percent_falls= (new_price_contract-contract_settle)* (contract_multiplier/required_margin)
    
    return (("Required margin: ",required_margin),("Percent return net investment: ", percentage_return_net_investment),('Net return price falls: ' ,percentage_return_net_investment_percent_falls))
 
"""
This function determines the payoff of a portfolio and what the riskfree rate must be
@note: Only works when the 2 strikes are the same
@param call_option_strike: strike of call option
@param put_option_strike: strike of put option
@param portfolio_net_outlay: net outlay to establish the entire portfolio
@return: Tuple representing the payoff and riskfree rate
"""   
def problem_20_24(call_option_strike, put_option_strike, portfolio_net_outlay):
    risk_free_rate=(call_option_strike/portfolio_net_outlay -1) * 100
    return (("Payoff",call_option_strike ),('Risk Free Rate: ',risk_free_rate ))
print(problem_20_24(15,15,13.9))
    