# Contributing to Backtrader PRO

Thank you for considering contributing to Backtrader PRO! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:

1. **Clear title** - Describe the bug briefly
2. **Steps to reproduce** - How to trigger the bug
3. **Expected behavior** - What should happen
4. **Actual behavior** - What actually happens
5. **Environment** - OS, Python version, library versions
6. **Screenshots** - If applicable

**Example:**
```
Title: "Buy and Hold strategy not executing trades"

Steps to reproduce:
1. Run backtest_program_pro.py
2. Enter AAPL, 2020-2023, $10000 initial cash
3. Select Buy and Hold strategy
4. Run backtest

Expected: Should buy shares and hold
Actual: $0 return, no trades executed

Environment:
- Windows 10
- Python 3.11
- backtrader 1.9.78
```

### Suggesting Features

Feature requests are welcome! Please include:

1. **Use case** - Why is this feature needed?
2. **Proposed solution** - How should it work?
3. **Alternatives** - Other ways to achieve this?
4. **Examples** - Show how it would be used

### Submitting Pull Requests

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Make your changes**
4. **Test thoroughly**
5. **Commit with clear messages**
   ```bash
   git commit -m "Add feature: Custom indicator support"
   ```
6. **Push to your fork**
   ```bash
   git push origin feature/AmazingFeature
   ```
7. **Open a Pull Request**

## Development Guidelines

### Code Style

- Follow PEP 8 style guide
- Use meaningful variable names
- Add docstrings to functions
- Comment complex logic
- Keep functions focused and short

**Example:**
```python
def calculate_sharpe_ratio(returns, risk_free_rate=0.02):
    """
    Calculate Sharpe ratio for a series of returns.
    
    Args:
        returns: List or array of returns
        risk_free_rate: Annual risk-free rate (default: 0.02)
    
    Returns:
        float: Sharpe ratio
    """
    excess_returns = returns - risk_free_rate
    return excess_returns.mean() / excess_returns.std()
```

### Testing

Before submitting:

1. **Test your changes**
   - Run backtest with multiple strategies
   - Test with different stocks and time periods
   - Verify position sizing works correctly

2. **Check edge cases**
   - Empty data
   - Single data point
   - Invalid inputs
   - Extreme values

3. **Verify existing functionality**
   - Make sure you didn't break anything
   - Test all strategies still work
   - Check plots still display

### Commit Messages

Use clear, descriptive commit messages:

**Good:**
```
Add support for multiple position sizing methods
Fix bug where RSI strategy ignored upper threshold
Update documentation for custom strategy builder
```

**Bad:**
```
Fixed stuff
Update
Changes
```

### Documentation

When adding features:

1. **Update README.md** - Add to features list
2. **Update EXAMPLES.md** - Show how to use it
3. **Add docstrings** - Document new functions
4. **Update QUICKSTART.md** - If it affects quick start

## Areas for Contribution

### High Priority

- [ ] Add more pre-built strategies
- [ ] Improve error messages
- [ ] Add export to CSV functionality
- [ ] Better data validation
- [ ] Performance optimizations

### Medium Priority

- [ ] Multi-asset portfolio backtesting
- [ ] Walk-forward analysis
- [ ] Monte Carlo simulation
- [ ] More position sizing methods
- [ ] Custom indicator support

### Low Priority

- [ ] Web-based UI
- [ ] Real-time paper trading
- [ ] Machine learning integration
- [ ] Advanced risk metrics
- [ ] Social media integration

## Adding New Strategies

To add a new strategy:

1. **Create strategy class**
```python
class MyNewStrategy(bt.Strategy):
    """Description of what this strategy does"""
    params = (
        ('param1', default_value),
    )
    
    def __init__(self):
        # Initialize indicators
        pass
    
    def next(self):
        # Trading logic
        pass
```

2. **Add to STRATEGIES dictionary**
```python
STRATEGIES = {
    # ... existing strategies
    '12': {
        'name': 'My New Strategy',
        'class': MyNewStrategy,
        'description': 'Brief description'
    }
}
```

3. **Add to min_data_needed (if applicable)**
```python
min_data_needed = {
    # ... existing
    'MyNewStrategy': 30,  # Minimum data points needed
}
```

4. **Document it**
- Add to README.md strategy table
- Add example to EXAMPLES.md
- Add to QUICKSTART.md if appropriate

## Adding New Indicators

Custom indicators should follow backtrader's pattern:

```python
class MyIndicator(bt.Indicator):
    lines = ('signal',)
    params = (('period', 14),)
    
    def __init__(self):
        # Setup
        pass
    
    def next(self):
        # Calculate indicator value
        self.lines.signal[0] = calculation
```

## Code Review Process

Pull requests will be reviewed for:

1. **Functionality** - Does it work as intended?
2. **Code quality** - Is it well-written and maintainable?
3. **Documentation** - Is it properly documented?
4. **Testing** - Has it been tested?
5. **Style** - Does it follow project conventions?

## Community Guidelines

- Be respectful and constructive
- Help others learn
- Share knowledge
- Give credit where due
- Focus on the code, not the person

## Questions?

- Open an issue for questions
- Check existing issues first
- Be specific and clear
- Provide context

## Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Credited in release notes
- Appreciated by the community!

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to Backtrader PRO!** 🚀

Together we can make this the best backtesting tool available!
