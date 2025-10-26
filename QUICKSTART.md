# Quick Start Guide

Get up and running with Backtrader PRO in 5 minutes!

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/backtrader-pro.git
cd backtrader-pro
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

That's it! You're ready to backtest.

## Your First Backtest

### Run the Program

```bash
python backtest_program_pro.py
```

### Follow the Prompts

The program will guide you step-by-step:

```
1. Enter stock ticker: AAPL
2. Start date: 2020-01-01
3. End date: 2023-01-01
4. Initial cash: [press Enter for 100000]
5. Commission: [press Enter for 0.001]
6. Position sizing: 1 (Percentage)
   - Percentage: 95
7. Strategy: 1 (SMA Crossover)
8. Show plot: y
```

### View Results

You'll see:
- Portfolio performance
- Sharpe ratio
- Maximum drawdown
- Win rate
- Interactive chart

## Try Different Strategies

### Strategy 1: Buy and Hold (Benchmark)
```
Strategy: 4
This is your baseline - how well would you do just holding?
```

### Strategy 2: SMA Crossover (Trend Following)
```
Strategy: 1
Catches trends by using moving average crossovers
```

### Strategy 3: RSI (Mean Reversion)
```
Strategy: 2
Buys oversold stocks, sells overbought
```

### Strategy 4: Custom (Build Your Own!)
```
Strategy: 11
Build a custom strategy with your own parameters
```

## Position Sizing Examples

### Conservative (50%)
```
Position sizing: 1
Percentage: 50
Uses half your cash per trade - lower risk
```

### Moderate (95%)
```
Position sizing: 1
Percentage: 95
Uses most of your cash - balanced approach
```

### Aggressive (All-In)
```
Position sizing: 2
Uses 100% of cash every trade - highest risk/reward
```

## Common Test Scenarios

### Test 1: Long-Term Growth
```
Ticker: SPY (S&P 500 ETF)
Start: 2015-01-01
End: 2023-01-01
Strategy: Buy and Hold
Position: 95%
```

### Test 2: Tech Stock Momentum
```
Ticker: NVDA
Start: 2020-01-01
End: 2023-01-01
Strategy: Momentum
Position: All-In
```

### Test 3: Conservative Blue Chip
```
Ticker: JNJ (Johnson & Johnson)
Start: 2020-01-01
End: 2023-01-01
Strategy: Bollinger Bands
Position: 50%
```

## Using Interactive Plots

Once the plot opens:

1. **Zoom In** - Scroll wheel or toolbar zoom button
2. **Pan Around** - Click and drag
3. **Reset View** - Click Home button
4. **Save Image** - Click Save button

### What to Look For

- **Green triangles** ▲ = Buy signals
- **Red triangles** ▼ = Sell signals
- **Blue/Red dots** = Profitable/Losing trades
- **Lines** = Strategy indicators

## Troubleshooting

### Issue: "No data found"
**Solution:** Check ticker symbol and date range
```
Common mistake: APPL instead of AAPL
Fix: Use correct ticker (always uppercase)
```

### Issue: "$0 return with Buy & Hold"
**Solution:** Increase initial cash
```
Problem: $10,000 might not buy even 1 share
Fix: Use $100,000 initial cash
```

### Issue: "Insufficient data points"
**Solution:** Use more data
```
Problem: 20 days isn't enough
Fix: Use at least 1 year (252 trading days)
```

### Issue: "Plot doesn't show"
**Solution:** Check matplotlib installation
```bash
pip install matplotlib
```

## Next Steps

1. ✅ Try all 10 pre-built strategies
2. ✅ Build a custom strategy (option 11)
3. ✅ Test different position sizing methods
4. ✅ Compare strategies on the same stock
5. ✅ Use interactive plots to learn

## Tips for Better Results

### Use Enough Data
```
❌ Bad: 1 month (20 trading days)
✅ Good: 1 year (252 trading days)
✅ Better: 3 years (756 trading days)
```

### Realistic Settings
```
Commission: 0.001 (0.1%) - typical for most brokers
Position: 95% or less - leave some cash buffer
```

### Compare to Benchmark
```
Always run Buy & Hold (Strategy 4) first
Then compare other strategies to it
```

### Test Multiple Periods
```
Bull market: 2020-2021
Bear market: 2022
Sideways: 2015-2016
```

## Sample Output

```
============================================================
               BACKTRADER BACKTESTING PROGRAM
============================================================

📊 Downloading data for AAPL from Yahoo Finance...
✅ Successfully downloaded 755 data points

🚀 Running backtest...

Starting Portfolio Value: $100,000.00
Final Portfolio Value:    $118,543.21

============================================================
BACKTEST RESULTS:
============================================================

💰 Total Return: $18,543.21 (18.54%)
📊 Sharpe Ratio: 1.234
📉 Max Drawdown: 12.34%

📈 Total Trades: 15
✅ Won: 10 | ❌ Lost: 5
🎯 Win Rate: 66.67%

============================================================
```

## Ready to Go Deeper?

Check out:
- **README.md** - Full documentation
- **EXAMPLES.md** - More examples
- **API.md** - Advanced customization

---

**You're all set! Start backtesting!** 🚀📈
