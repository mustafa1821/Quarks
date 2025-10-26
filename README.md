# Quarks - Advanced Backtesting Program

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Backtrader](https://img.shields.io/badge/backtrader-1.9.78%2B-orange)](https://www.backtrader.com/)

A professional-grade backtesting program for testing trading strategies on historical stock data. Features position sizing, interactive plots, custom strategy builder, and 10 pre-built strategies.

![Backtrader Screenshot](https://via.placeholder.com/800x400.png?text=Interactive+Backtesting+Chart)

## 🌟 Features

- **10 Pre-built Strategies** - SMA, EMA, RSI, MACD, Bollinger Bands, and more
- **Custom Strategy Builder** - Create strategies without coding
- **4 Position Sizing Methods** - Percentage, All-In, Fixed Amount, Fixed Shares
- **Interactive Plots** - Zoom, pan, and explore your results
- **Performance Analytics** - Sharpe ratio, drawdown, win rate, and more
- **Yahoo Finance Integration** - Automatic data downloads
- **Easy to Use** - Interactive prompts guide you through

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/backtrader-pro.git
cd backtrader-pro

# Install dependencies
pip install -r requirements.txt
```

### Run Your First Backtest

```bash
python backtest_program_pro.py
```

Follow the prompts:
```
Ticker: AAPL
Start date: 2020-01-01
End date: 2023-01-01
Initial cash: [press Enter for 100000]
Commission: [press Enter for 0.001]
Position sizing: 1 (Percentage)
  Percentage: 95
Strategy: 1 (SMA Crossover)
Interactive plot: y
```

## 📊 Available Strategies

| # | Strategy | Type | Description |
|---|----------|------|-------------|
| 1 | SMA Crossover | Trend | Buy when fast MA crosses above slow MA |
| 2 | RSI | Mean Reversion | Buy when oversold, sell when overbought |
| 3 | MACD | Momentum | Buy when MACD crosses above signal |
| 4 | Buy & Hold | Benchmark | Simple buy and hold |
| 5 | Bollinger Bands | Mean Reversion | Buy at lower band, sell at upper |
| 6 | EMA Crossover | Trend | Exponential MA crossover |
| 7 | Stochastic | Oscillator | Momentum-based oscillator |
| 8 | Momentum | Trend | Buy on positive momentum |
| 9 | Triple SMA | Trend | Three moving averages for confirmation |
| 10 | Mean Reversion | Mean Reversion | Statistical mean reversion |
| 11 | Custom Builder | Custom | Build your own strategy! |

## 💡 Position Sizing

Control your risk with 4 position sizing methods:

**1. Percentage of Portfolio** ⭐ Recommended
- Use a percentage of available cash (e.g., 95%)
- Balanced risk/reward approach

**2. All-In**
- Use 100% of cash on every trade
- Maximum aggressive approach

**3. Fixed Dollar Amount**
- Invest the same dollar amount per trade
- Conservative, predictable

**4. Fixed Shares**
- Buy the same number of shares each trade
- Good for testing specific quantities

## 🎮 Interactive Plots

Explore your backtest results with interactive charts:

- **Pan** - Click and drag to navigate
- **Zoom** - Scroll wheel to zoom in/out
- **Reset** - Home button to reset view
- **Save** - Export charts as images

## 📈 Example Results

```
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

## 🛠️ Custom Strategy Builder

Build strategies without writing code:

```
Select strategy: 11 (BUILD CUSTOM STRATEGY)

STEP 1: Choose indicator
  - SMA, EMA, RSI, MACD, Bollinger Bands, Stochastic

STEP 2: Configure parameters
  - Set periods, thresholds, etc.

STEP 3: Choose logic
  - Buy above/below, crossovers, etc.

Your custom strategy runs immediately!
```

## 📚 Documentation

- **README.md** - This file
- **QUICKSTART.md** - Get started in 5 minutes
- **EXAMPLES.md** - Example configurations
- **API.md** - Extend with your own strategies

## 🔧 Requirements

- Python 3.7+
- backtrader >= 1.9.78
- yfinance >= 0.2.0
- pandas >= 1.3.0
- numpy >= 1.19.0
- matplotlib >= 3.3.0

## 💻 Usage Examples

### Conservative Long-Term Test
```python
Ticker: SPY
Start: 2015-01-01
End: 2023-01-01
Cash: 100000
Position Sizing: Percentage (50%)
Strategy: Buy and Hold
```

### Aggressive Day Trading Simulation
```python
Ticker: TSLA
Start: 2020-01-01
End: 2023-01-01
Cash: 100000
Position Sizing: All-In
Strategy: Momentum
```

### Custom Strategy Example
```python
Ticker: AAPL
Start: 2020-01-01
End: 2023-01-01
Position Sizing: Fixed Amount ($10,000)
Strategy: Custom SMA (50-period)
```

## 📊 Performance Metrics

The program provides comprehensive analytics:

- **Total Return** - Absolute and percentage returns
- **Sharpe Ratio** - Risk-adjusted returns (>1 is good)
- **Max Drawdown** - Largest peak-to-trough decline
- **Win Rate** - Percentage of profitable trades
- **Trade Statistics** - Total, won, lost trades

## 🎯 Best Practices

1. **Use sufficient data** - At least 1-2 years recommended
2. **Realistic commissions** - Default 0.1% is typical
3. **Compare to benchmark** - Always test Buy & Hold
4. **Test multiple periods** - Bull, bear, and sideways markets
5. **Match real trading** - Use position sizing you'd actually use

## ⚠️ Disclaimer

This software is for educational and backtesting purposes only.

- **Not financial advice** - Consult a licensed financial advisor
- **Past performance ≠ future results** - History doesn't guarantee profits
- **Use at your own risk** - No warranty or guarantee provided
- **Paper trade first** - Test thoroughly before risking real money

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Backtrader](https://www.backtrader.com/) - Amazing backtesting library
- Data from [Yahoo Finance](https://finance.yahoo.com/) via yfinance
- Inspired by the algorithmic trading community

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/backtrader-pro/issues)
- **Documentation**: Check the docs folder
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/backtrader-pro/discussions)

## 🗺️ Roadmap

- [ ] Multi-asset portfolio backtesting
- [ ] Walk-forward optimization
- [ ] Monte Carlo simulation
- [ ] Export results to CSV/JSON
- [ ] Web-based UI
- [ ] Real-time paper trading

## ⭐ Star History

If you find this project useful, please consider giving it a star!

---

**Happy Backtesting!** 📈🚀

Made with ❤️ by the Backtrader community
