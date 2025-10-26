# Advanced Backtesting Program - New Features Guide

## 🎉 What's New

The advanced version includes:
- **10 pre-built strategies** (up from 5!)
- **Custom Strategy Builder** - Create your own strategies without coding!
- All the original features you know and love

## 🚀 New Strategies Added

### 6. EMA Crossover
- **How it works**: Like SMA Crossover but uses Exponential Moving Average (more responsive)
- **Best for**: Faster trend detection
- **Min data**: 26 days

### 7. Stochastic Oscillator
- **How it works**: Measures momentum, buys when oversold (<20), sells when overbought (>80)
- **Best for**: Range-bound markets
- **Min data**: 14 days

### 8. Momentum Strategy
- **How it works**: Buys when price momentum is positive
- **Best for**: Strong trending markets
- **Min data**: 12 days

### 9. Triple SMA
- **How it works**: Uses 3 moving averages for trend confirmation
- **Best for**: Reducing false signals
- **Min data**: 50 days

### 10. Mean Reversion
- **How it works**: Buys when price deviates far below the average
- **Best for**: Choppy, oscillating markets
- **Min data**: 20 days

## ✨ Custom Strategy Builder

The **coolest new feature** - build your own strategy with a guided wizard!

### How to Use

1. Run the program: `python backtest_program_advanced.py`
2. When prompted, select strategy **11 (BUILD CUSTOM STRATEGY)**
3. Follow the step-by-step wizard

### Example Session

```
Select strategy number (1-11): 11

============================================================
CUSTOM STRATEGY BUILDER
============================================================

Let's build your custom strategy step by step!

STEP 1: Choose your indicator
[1] SMA (Simple Moving Average)
[2] EMA (Exponential Moving Average)
[3] RSI (Relative Strength Index)
[4] MACD (Moving Average Convergence Divergence)
[5] Bollinger Bands
[6] Stochastic Oscillator

Select indicator (1-6): 1

STEP 2: Configure SMA parameters
Enter SMA period (default: 20): 50

STEP 3: Choose trading logic
[1] Buy when price crosses ABOVE the MA
[2] Buy when price crosses BELOW the MA (contrarian)
Select logic (1 or 2): 1

✅ Custom strategy created!
```

Then the program runs your custom strategy just like any pre-built one!

## 🎯 Custom Strategy Options

### Option 1: SMA/EMA Strategy
**Parameters you control:**
- Period (how many days to average)
- Logic (buy when price crosses above/below MA)

**Example use cases:**
- 50-day SMA, buy above = Long-term trend following
- 10-day SMA, buy below = Short-term mean reversion

### Option 2: RSI Strategy
**Parameters you control:**
- RSI Period (default: 14)
- Oversold level (default: 30)
- Overbought level (default: 70)

**Example use cases:**
- RSI 14, 30/70 = Standard settings
- RSI 7, 20/80 = More sensitive, wider bands

### Option 3: MACD Strategy
**Parameters you control:**
- Fast period (default: 12)
- Slow period (default: 26)
- Signal period (default: 9)

**Example use cases:**
- 12/26/9 = Standard MACD
- 5/13/5 = Faster, more signals

### Option 4: Bollinger Bands
**Parameters you control:**
- Period (default: 20)
- Deviation factor (default: 2.0)

**Example use cases:**
- 20 period, 2.0 dev = Standard BB
- 20 period, 2.5 dev = Wider bands, fewer signals

### Option 5: Stochastic
**Parameters you control:**
- Period (default: 14)
- Oversold level (default: 20)
- Overbought level (default: 80)

**Example use cases:**
- 14 period, 20/80 = Standard
- 14 period, 30/70 = Less extreme signals

## 📊 Complete Strategy List

| # | Strategy | Type | Min Data | Complexity |
|---|----------|------|----------|------------|
| 1 | SMA Crossover | Trend | 30 days | ⭐ Easy |
| 2 | RSI | Mean Reversion | 14 days | ⭐ Easy |
| 3 | MACD | Momentum | 35 days | ⭐⭐ Medium |
| 4 | Buy & Hold | Benchmark | 1 day | ⭐ Easy |
| 5 | Bollinger Bands | Mean Reversion | 20 days | ⭐⭐ Medium |
| 6 | EMA Crossover | Trend | 26 days | ⭐ Easy |
| 7 | Stochastic | Oscillator | 14 days | ⭐⭐ Medium |
| 8 | Momentum | Trend | 12 days | ⭐ Easy |
| 9 | Triple SMA | Trend | 50 days | ⭐⭐⭐ Advanced |
| 10 | Mean Reversion | Mean Reversion | 20 days | ⭐⭐ Medium |
| 11 | **Custom** | **Your Choice!** | **Varies** | ⭐ to ⭐⭐⭐ |

## 💡 Strategy Selection Guide

### For Beginners
Start with:
- **Strategy 4** (Buy & Hold) - Understand the baseline
- **Strategy 1** (SMA Crossover) - Simple trend following
- **Strategy 11** (Custom with SMA) - Build your first custom strategy

### For Trending Markets (Bull/Bear)
Use:
- **Strategy 1** (SMA Crossover)
- **Strategy 6** (EMA Crossover)
- **Strategy 8** (Momentum)
- **Strategy 9** (Triple SMA)

### For Sideways/Choppy Markets
Use:
- **Strategy 2** (RSI)
- **Strategy 5** (Bollinger Bands)
- **Strategy 7** (Stochastic)
- **Strategy 10** (Mean Reversion)

### For All Markets
Try:
- **Strategy 3** (MACD) - Adapts to different conditions
- **Strategy 11** (Custom) - Tune parameters for current market

## 🔧 Quick Start Examples

### Example 1: Test All Pre-built Strategies
```powershell
# Run the program 10 times with the same data
# but different strategies (1-10)
# Compare which performs best!

python backtest_program_advanced.py
# Data: AAPL, 2020-2023
# Strategy: 1 (SMA Crossover)

python backtest_program_advanced.py
# Data: AAPL, 2020-2023  
# Strategy: 2 (RSI)

# ... repeat for strategies 3-10
```

### Example 2: Build a Conservative Custom Strategy
```
Strategy: 11 (Custom)
Indicator: 1 (SMA)
Period: 200 (very long-term)
Logic: 1 (buy above)

Result: Very conservative, few trades, follows major trends
```

### Example 3: Build an Aggressive Custom Strategy
```
Strategy: 11 (Custom)
Indicator: 2 (EMA)
Period: 10 (short-term)
Logic: 1 (buy above)

Result: Many trades, responds quickly to price changes
```

### Example 4: Build a Mean Reversion Custom Strategy
```
Strategy: 11 (Custom)
Indicator: 3 (RSI)
Period: 7 (sensitive)
Oversold: 20 (very oversold)
Overbought: 80 (very overbought)

Result: Catches extreme price movements
```

## 📈 Comparing Strategies

**Pro Tip**: Run the same stock/date range with different strategies and compare:

| Strategy | Return | Sharpe | Max DD | Trades | Win Rate |
|----------|--------|--------|---------|---------|----------|
| Buy & Hold | 15.2% | 0.85 | 18% | 1 | 100% |
| SMA Cross | 22.3% | 1.12 | 12% | 15 | 67% |
| RSI | 18.7% | 0.98 | 15% | 28 | 54% |
| Custom SMA-50 | 19.5% | 1.05 | 14% | 8 | 75% |

This helps you:
- See which strategy works best for that stock
- Understand risk vs. reward
- Choose the right tool for the job

## 🎓 Learning Path

### Week 1: Learn the Pre-built Strategies
1. Test strategies 1-10 on AAPL (2020-2023)
2. Note which performs best
3. Understand when each strategy works

### Week 2: Experiment with Custom Strategies
1. Build a custom SMA strategy with different periods (10, 20, 50, 100, 200)
2. Compare results
3. Learn how period affects performance

### Week 3: Advanced Customization
1. Try different RSI thresholds (20/80, 30/70, 40/60)
2. Test Bollinger Band widths (1.5, 2.0, 2.5, 3.0)
3. Optimize MACD parameters

### Week 4: Real-World Application
1. Pick your 3 best strategies
2. Test on different stocks (tech, finance, retail)
3. See which strategies are stock-specific vs. universal

## 🚨 Important Notes

### About Custom Strategies
- ✅ Great for learning how parameters affect results
- ✅ Lets you tune strategies to specific stocks/markets
- ❌ Can lead to overfitting if you optimize too much
- ❌ Past performance ≠ future results

### Best Practices
1. **Always compare to Buy & Hold** - It's your benchmark
2. **Test on multiple stocks** - Don't optimize for just one
3. **Use realistic parameters** - Extreme values rarely work in practice
4. **Consider transaction costs** - More trades = more commissions
5. **Check drawdowns** - High returns with high drawdowns = risky

## 🔄 Upgrading from Basic Version

If you used the basic version (`backtest_program_enhanced.py`):

**What's the same:**
- All 5 original strategies (1-5)
- Yahoo Finance and CSV support
- Same data inputs and outputs
- Same performance metrics

**What's new:**
- 5 additional strategies (6-10)
- Custom strategy builder (11)
- More flexibility and options

**You can use both!** The basic version is simpler, the advanced version has more options.

## 🎯 Next Steps

1. Download [backtest_program_advanced.py](computer:///mnt/user-data/outputs/backtest_program_advanced.py)
2. Run it with: `python backtest_program_advanced.py`
3. Try the new strategies (6-10)
4. Build your first custom strategy (option 11)
5. Compare results across different strategies
6. Find what works best for your favorite stocks!

Happy backtesting! 🚀📈
