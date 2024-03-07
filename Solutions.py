from scipy.stats import norm
import numpy as np

########################################################

# Given data
S0 = 250  # current stock price
X = 260   # strike price
r = 0.04  # risk-free interest rate
sigma = 0.4  # volatility
t = 2  # time to maturity in years

# Black-Scholes formula components
d1 = (np.log(S0 / X) + (r + (sigma**2) / 2) * t) / (sigma * np.sqrt(t))
d2 = d1 - sigma * np.sqrt(t)

# Price of the call option
C = (S0 * norm.cdf(d1)) - (X * np.exp(-r * t) * norm.cdf(d2))
C

# Answer: 59.696101566963506

### With Dividend yeild option ##########################

# # Constants for the new computation
# S0 = 250  # Current stock price
# K = 260   # Strike price
# r = 0.04  # Risk-free interest rate
# sigma = 0.4  # Volatility
# T = 2  # Time to maturity (in years)
# q = 0  # Dividend yield

# # Black-Scholes formula components for a call option
# d1 = (np.log(S0 / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
# d2 = d1 - sigma * np.sqrt(T)

# # Price of the call option
# C_call = S0 * np.exp(-q * T) * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
# C_call


### Question 2 ###########################################

# Given parameters
K = 270  # Strike price for the cash-or-nothing option
Δt = 0.5  # Time step in years (6 months)

# Calculating the up and down factors and the risk-neutral probability
u = np.exp(sigma * np.sqrt(Δt))  # Up factor
d = 1 / u  # Down factor
q = (np.exp(r * Δt) - d) / (u - d)  # Risk-neutral probability

# Calculating stock prices at the end of the tree
S_uu = S0 * u**2  # Stock price after two up movements
S_ud = S0 * u * d  # Stock price after one up and one down movement (or vice versa)
S_dd = S0 * d**2  # Stock price after two down movements

# Calculating the payoffs for a cash-or-nothing option at the end of one year
payoff_uu = 500 if S_uu < K else 0
payoff_ud = 500 if S_ud < K else 0
payoff_dd = 500 if S_dd < K else 0

# Discounting the payoffs to present value using risk-neutral probabilities
option_price = (payoff_uu * q**2 + 2 * payoff_ud * q * (1 - q) + payoff_dd * (1 - q)**2) * np.exp(-r)
option_price

# Answer: 376.52293345590033

### Question 3 ###########################################

# Updated strike price for this derivative
K_new = 260

# Calculating the payoffs for the derivative at the end of one year
# Using the stock prices at the end of the tree calculated previously (S_uu, S_ud, S_dd)
payoff_uu_new = np.sqrt(max(K_new - S_uu, 0))
payoff_ud_new = np.sqrt(max(K_new - S_ud, 0))
payoff_dd_new = np.sqrt(max(K_new - S_dd, 0))

# Discounting the new payoffs to present value using the risk-neutral probabilities
option_price_new = (payoff_uu_new * q**2 + 2 * payoff_ud_new * q * (1 - q) + payoff_dd_new * (1 - q)**2) * np.exp(-r)
option_price_new
