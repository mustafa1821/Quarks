# Usage Examples

Practical examples for different trading scenarios and use cases.

## Table of Contents
- [Stock Selection Examples](#stock-selection-examples)
- [Position Sizing Examples](#position-sizing-examples)
- [Strategy Examples](#strategy-examples)
- [Time Period Examples](#time-period-examples)
- [Custom Strategy Examples](#custom-strategy-examples)

## Stock Selection Examples

### Example 1: Blue Chip Stock (Apple)
```
Ticker: AAPL
Start: 2020-01-01
End: 2023-01-01
Cash: 100000
Commission: 0.001
Position: 95%
Strategy: SMA Crossover

Expected: Steady growth with moderate volatility
Good for: Learning the basics
```

### Example 2: High Growth Tech (NVIDIA)
```
Ticker: NVDA
Start: 2020-01-01
End: 2023-01-01
Cash: 100000
Commission: 0.001
Position: All-In
Strategy: Momentum

Expected: High returns, high volatility
Good for: Testing aggressive strategies
```

### Example 3: Stable Dividend Stock (Johnson & Johnson)
```
Ticker: JNJ
Start: 2020-01-01
End: 2023-01-01
Cash: 100000
Commission: 0.001
Position: 50%
Strategy: Buy and Hold

Expected: Stable, consistent returns
Good for: Conservative testing
```

### Example 4: ETF (S&P 500)
```
Ticker: SPY
Start: 2015-01-01
End: 2023-01-01
Cash: 100000
Commission: 0.001
Position: 95%
Strategy: Buy and Hold

Expected: Market-level returns
Good for: Benchmark comparison
```

### Example 5: Volatile Stock (Tesla)
```
Ticker: TSLA
Start: 2020-01-01
End: 2023-01-01
Cash: 100000
Commission: 0.001
Position: 75%
Strategy: RSI

Expected: High volatility, good for mean reversion
Good for: Testing oscillator strategies
```

## Position Sizing Examples

### Conservative Trader
```
Position Sizing: 1 (Percentage)
Percentage: 30-50%

Pros:
- Lower risk
- Preserves capital
- Good for volatile stocks

Cons:
- Lower potential returns
- Many opportunities missed

Use when:
- Learning
- Testing new strategies
- Trading volatile stocks
```

### Moderate Trader
```
Position Sizing: 1 (Percentage)
Percentage: 70-85%

Pros:
- Balanced risk/reward
- Good capital utilization
- Flexible

Cons:
- Still leaves some cash idle

Use when:
- Most backtesting
- Realistic simulation
- Moderate risk tolerance
```

### Aggressive Trader
```
Position Sizing: 2 (All-In)

Pros:
- Maximum returns
- Full capital utilization
- See true potential

Cons:
- Maximum risk
- No buffer for mistakes
- Unrealistic for most traders

Use when:
- Testing maximum potential
- Academic analysis
- Small account simulation
```

### Fixed Dollar Amount
```
Position Sizing: 3 (Fixed Amount)
Amount: 10000-20000

Pros:
- Predictable position sizes
- Easy risk management
- Good for diversification

Cons:
- Capital not fully utilized
- Fixed regardless of account size

Use when:
- Testing specific dollar amounts
- Simulating limited capital deployment
- Risk-controlled testing
```

## Strategy Examples

### Example 1: Trend Following (SMA Crossover)

**When to use:**
- Bull markets
- Trending stocks
- Long-term holds

**Settings:**
```
Strategy: 1 (SMA Crossover)
Stock: AAPL
Period: 2020-2023
Position: 95%

Expected Result:
- Catches major trends
- 10-15 trades
- Win rate: 55-65%
```

### Example 2: Mean Reversion (RSI)

**When to use:**
- Range-bound markets
- Volatile stocks
- Short-term trading

**Settings:**
```
Strategy: 2 (RSI)
Stock: TSLA
Period: 2021-2023
Position: 75%

Expected Result:
- Many trades (20-40)
- Quick entries/exits
- Win rate: 50-60%
```

### Example 3: Momentum Trading

**When to use:**
- Strong trending markets
- High momentum stocks
- Bull markets

**Settings:**
```
Strategy: 8 (Momentum)
Stock: NVDA
Period: 2020-2023
Position: All-In

Expected Result:
- Rides strong trends
- Fewer trades (5-10)
- High returns if trend is strong
```

### Example 4: Conservative (Bollinger Bands)

**When to use:**
- Learning
- Volatile markets
- Mean reversion

**Settings:**
```
Strategy: 5 (Bollinger Bands)
Stock: SPY
Period: 2020-2023
Position: 50%

Expected Result:
- Moderate trades (15-25)
- Controlled risk
- Stable returns
```

### Example 5: Benchmark (Buy and Hold)

**When to use:**
- Always! (as comparison)
- Testing market returns
- Simple baseline

**Settings:**
```
Strategy: 4 (Buy and Hold)
Stock: Any
Period: Any
Position: 95%

Expected Result:
- Single trade
- Stock's total return
- Baseline for comparison
```

## Time Period Examples

### Example 1: Bull Market Test
```
Start: 2020-03-01 (COVID bottom)
End: 2021-12-31 (pre-2022 crash)

Characteristics:
- Strong uptrend
- Most strategies work
- High returns

Good for:
- Testing trend-following strategies
- Seeing maximum potential
```

### Example 2: Bear Market Test
```
Start: 2022-01-01
End: 2022-12-31

Characteristics:
- Downtrend
- Most strategies struggle
- Tests resilience

Good for:
- Testing defensive strategies
- Finding robust strategies
- Risk assessment
```

### Example 3: Full Cycle Test
```
Start: 2019-01-01
End: 2023-01-01

Characteristics:
- Bull, bear, and recovery
- Complete market cycle
- Realistic testing

Good for:
- Most backtests
- Comprehensive analysis
- Realistic expectations
```

### Example 4: Long-Term Test
```
Start: 2015-01-01
End: 2023-01-01

Characteristics:
- 8 years of data
- Multiple cycles
- Statistical significance

Good for:
- Serious analysis
- Strategy validation
- Long-term viability
```

### Example 5: Short-Term Test
```
Start: 2023-01-01
End: 2023-12-31

Characteristics:
- Recent data
- Current market
- Quick test

Good for:
- Recent performance
- Quick validation
- Current market conditions
```

## Custom Strategy Examples

### Example 1: Long-Term SMA
```
Strategy: 11 (Custom)
Indicator: 1 (SMA)
Period: 200
Logic: 1 (Buy above)

Use case:
- Very long-term trend following
- Few trades
- Low turnover

Expected:
- 2-5 trades per year
- Catches major trends only
```

### Example 2: Aggressive RSI
```
Strategy: 11 (Custom)
Indicator: 3 (RSI)
Period: 7
Oversold: 20
Overbought: 80

Use case:
- Fast mean reversion
- Many trades
- High activity

Expected:
- 30-50 trades per year
- Quick entries/exits
```

### Example 3: Tight Bollinger Bands
```
Strategy: 11 (Custom)
Indicator: 5 (Bollinger Bands)
Period: 20
Deviation: 1.5

Use case:
- Frequent signals
- Narrow bands
- Active trading

Expected:
- 20-30 trades per year
- More signals than standard
```

### Example 4: Slow MACD
```
Strategy: 11 (Custom)
Indicator: 4 (MACD)
Fast: 26
Slow: 52
Signal: 18

Use case:
- Long-term signals
- Fewer false signals
- Patient trading

Expected:
- 5-10 trades per year
- Higher win rate
```

## Complete Workflow Examples

### Workflow 1: Compare Strategies
```bash
# Test 1: Buy and Hold
python backtest_program_pro.py
Ticker: AAPL, Period: 2020-2023, Strategy: 4
Result: +85%

# Test 2: SMA Crossover
python backtest_program_pro.py
Ticker: AAPL, Period: 2020-2023, Strategy: 1
Result: +92%

# Test 3: RSI
python backtest_program_pro.py
Ticker: AAPL, Period: 2020-2023, Strategy: 2
Result: +78%

# Conclusion: SMA Crossover outperformed!
```

### Workflow 2: Optimize Position Sizing
```bash
# Test 1: 50% sizing
Result: +12% return, 8% max drawdown

# Test 2: 75% sizing
Result: +18% return, 12% max drawdown

# Test 3: 95% sizing
Result: +22% return, 16% max drawdown

# Test 4: All-In
Result: +25% return, 20% max drawdown

# Conclusion: 75% gives best risk/reward
```

### Workflow 3: Multi-Stock Comparison
```bash
# Test AAPL
Result: +85%, Sharpe: 1.2

# Test MSFT
Result: +72%, Sharpe: 1.1

# Test GOOGL
Result: +95%, Sharpe: 1.3

# Test NVDA
Result: +150%, Sharpe: 1.4

# Conclusion: NVDA had best risk-adjusted returns
```

## Tips for Each Example

### When Testing Strategies
- Always compare to Buy & Hold
- Use same time period for all tests
- Use same position sizing
- Document results

### When Testing Position Sizing
- Use same strategy for all tests
- Use same stock and period
- Compare risk vs. reward
- Consider your real risk tolerance

### When Testing Stocks
- Use same strategy and sizing
- Use same time period
- Consider volatility differences
- Note correlation with market

### When Testing Time Periods
- Test both bull and bear markets
- Use realistic recent data
- Consider at least 1 year minimum
- Look for consistency across periods

---

These examples should give you a solid foundation for backtesting various scenarios! 📈🚀
