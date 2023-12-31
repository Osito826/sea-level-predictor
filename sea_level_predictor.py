import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    #print(df)
    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    fig, ax = plt.subplots()
    plt.scatter(x, y)

    # Create first line of best fit
    res = linregress(x, y)
    #print(res)
    x_forecast = pd.Series([i for i in range(1880, 2051)])
    #print(x_forecast)
    y_forecast = res.slope * x_forecast + res.intercept
    #print(y_forecast)
    plt.plot(x_forecast, y_forecast, "r")

    # Create second line of best fit
    new_df = df.loc[df['Year'] >= 2000]
    #print(new_df)
    new_x = new_df['Year']
    new_y = new_df['CSIRO Adjusted Sea Level']
    res_two = linregress(new_x, new_y)
    #print(res)
    x_forecast_two = pd.Series([i for i in range(2000, 2051)])
    #print(x_forecast_two)
    y_forecast_two = res_two.slope * x_forecast_two + res_two.intercept
    #print(y_forecast_two)
    plt.plot(x_forecast_two, y_forecast_two, "green")

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()