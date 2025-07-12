import matplotlib as plt
import numpy as np
import scipy as sp
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller


def jump_diffusion_model(data, mu, sigma, lam, jump_mean, jump_std, T=1, dt=1/252):
         """
    Simulates a jump diffusion model for stock prices.

    Parameters:
    - data: DataFrame containing historical stock prices.
    - mu: Drift term (expected return).
    - sigma: Volatility of the stock.
    - lam: Intensity of the jumps (average number of jumps per unit time).
    - jump_mean: Mean of the jump size.
    - jump_std: Standard deviation of the jump size.
    - T: Total time period for simulation.
    - dt: Time step for simulation.

    Returns:
    - DataFrame with simulated stock prices.
    """
    
    n_steps = int(T / dt)
    t = np.linspace(0, T, n_steps)
    
    # Generate Brownian motion
    W = np.random.normal(0, np.sqrt(dt), n_steps)
    W = np.cumsum(W)  # Cumulative sum to simulate Brownian motion
    
    # Generate jumps
    N = np.random.poisson(lam * t)  # Number of jumps
    J = np.random.normal(jump_mean, jump_std, N.sum())  # Jump sizes
    J_idx = np.random.choice(n_steps, N.sum(), replace=True)  # Randomly assign jumps to time steps
    
    # Create price path
    S = np.zeros(n_steps)
    S[0] = data['Close'].iloc[-1]  # Start from last known price
    
    for i in range(1, n_steps):
        S[i] = S[i-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * W[i-1])
        if i in J_idx:
            S[i] += J[J_idx == i].sum()  # Add jump if it occurs at this step
    
    return pd.DataFrame({'Time': t, 'Price': S})