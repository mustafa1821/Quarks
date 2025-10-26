# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-01

### Added
- 10 pre-built trading strategies
- Custom strategy builder with 6 indicators
- 4 position sizing methods (Percentage, All-In, Fixed Amount, Fixed Shares)
- Interactive plots with zoom, pan, and save functionality
- Yahoo Finance integration for automatic data downloads
- Performance analytics (Sharpe ratio, drawdown, win rate)
- Comprehensive error handling and validation
- User-friendly interactive prompts
- Sample data file for testing

### Features

#### Strategies
1. SMA Crossover - Trend following with moving averages
2. RSI Strategy - Mean reversion using RSI indicator
3. MACD Strategy - Momentum trading with MACD
4. Buy and Hold - Simple benchmark strategy
5. Bollinger Bands - Mean reversion with bands
6. EMA Crossover - Exponential moving average crossover
7. Stochastic Oscillator - Momentum-based oscillator
8. Momentum Strategy - Price momentum trading
9. Triple SMA - Three moving average confirmation
10. Mean Reversion - Statistical mean reversion
11. Custom Builder - Build unlimited custom strategies

#### Position Sizing
- Percentage of portfolio (e.g., 95%)
- All-In (100% of cash)
- Fixed dollar amount per trade
- Fixed number of shares per trade

#### Analytics
- Total return (dollars and percentage)
- Sharpe ratio (risk-adjusted returns)
- Maximum drawdown
- Win rate and trade statistics
- Trade-by-trade analysis

#### Interactive Plots
- Zoom in/out with scroll wheel
- Pan by clicking and dragging
- Reset view with home button
- Save charts as images
- View buy/sell signals
- See winning vs. losing trades

### Documentation
- Complete README with installation and usage
- Quick start guide (QUICKSTART.md)
- Comprehensive examples (EXAMPLES.md)
- Contributing guidelines (CONTRIBUTING.md)
- MIT License
- Sample data included

### Technical
- Python 3.7+ support
- Backtrader 1.9.78+ integration
- Yahoo Finance via yfinance
- Matplotlib for interactive plotting
- Pandas for data handling
- Comprehensive error messages

## [Unreleased]

### Planned Features
- Multi-asset portfolio backtesting
- Walk-forward optimization
- Monte Carlo simulation
- Export results to CSV/JSON
- Web-based UI
- Real-time paper trading
- More position sizing methods
- Additional technical indicators
- Performance comparison tools
- Risk management features

---

For more details, see the [README](README.md) and [documentation](docs/).
