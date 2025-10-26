"""
Advanced Interactive Backtrader Backtesting Program
Features:
- Position sizing options
- Yahoo Finance data (streamlined)
- Interactive plots with zoom
- 10+ strategies plus custom builder
"""

import backtrader as bt
import pandas as pd
from datetime import datetime
import sys
import os


# ==================== POSITION SIZERS ====================

class PercentSizer(bt.Sizer):
    """Size position as percentage of portfolio value"""
    params = (('percents', 95),)
    
    def _getsizing(self, comminfo, cash, data, isbuy):
        if isbuy:
            size = int((cash * (self.params.percents / 100)) / data.close[0])
            return size
        else:
            return self.broker.getposition(data).size


class AllInSizer(bt.Sizer):
    """All-in: Use all available cash"""
    def _getsizing(self, comminfo, cash, data, isbuy):
        if isbuy:
            size = int(cash / data.close[0])
            return size
        else:
            return self.broker.getposition(data).size


class FixedAmountSizer(bt.Sizer):
    """Fixed dollar amount per trade"""
    params = (('amount', 10000),)
    
    def _getsizing(self, comminfo, cash, data, isbuy):
        if isbuy:
            size = int(self.params.amount / data.close[0])
            return size
        else:
            return self.broker.getposition(data).size


class FixedSharesSizer(bt.Sizer):
    """Fixed number of shares per trade"""
    params = (('shares', 100),)
    
    def _getsizing(self, comminfo, cash, data, isbuy):
        if isbuy:
            return self.params.shares
        else:
            return self.broker.getposition(data).size


# ==================== PRE-EXISTING STRATEGIES ====================

class SMACrossover(bt.Strategy):
    """Simple Moving Average Crossover Strategy"""
    params = (
        ('fast_period', 10),
        ('slow_period', 30),
    )

    def __init__(self):
        self.fast_ma = bt.indicators.SimpleMovingAverage(
            self.data.close, period=self.params.fast_period
        )
        self.slow_ma = bt.indicators.SimpleMovingAverage(
            self.data.close, period=self.params.slow_period
        )
        self.crossover = bt.indicators.CrossOver(self.fast_ma, self.slow_ma)

    def next(self):
        if not self.position:
            if self.crossover > 0:
                self.buy()
        elif self.crossover < 0:
            self.close()


class RSIStrategy(bt.Strategy):
    """RSI-based Strategy"""
    params = (
        ('rsi_period', 14),
        ('rsi_upper', 70),
        ('rsi_lower', 30),
    )

    def __init__(self):
        self.rsi = bt.indicators.RSI(
            self.data.close,
            period=self.params.rsi_period
        )

    def next(self):
        if not self.position:
            if self.rsi < self.params.rsi_lower:
                self.buy()
        elif self.rsi > self.params.rsi_upper:
            self.close()


class MACDStrategy(bt.Strategy):
    """MACD Strategy"""
    params = (
        ('fast_period', 12),
        ('slow_period', 26),
        ('signal_period', 9),
    )

    def __init__(self):
        self.macd = bt.indicators.MACD(
            self.data.close,
            period_me1=self.params.fast_period,
            period_me2=self.params.slow_period,
            period_signal=self.params.signal_period
        )

    def next(self):
        if not self.position:
            if self.macd.macd[0] > self.macd.signal[0]:
                self.buy()
        elif self.macd.macd[0] < self.macd.signal[0]:
            self.close()


class BuyAndHold(bt.Strategy):
    """Simple Buy and Hold Strategy"""
    
    def __init__(self):
        self.order = None

    def next(self):
        if not self.position and self.order is None:
            self.order = self.buy()


class BollingerBandsStrategy(bt.Strategy):
    """Bollinger Bands Mean Reversion Strategy"""
    params = (
        ('period', 20),
        ('devfactor', 2),
    )

    def __init__(self):
        self.bbands = bt.indicators.BollingerBands(
            self.data.close,
            period=self.params.period,
            devfactor=self.params.devfactor
        )

    def next(self):
        if not self.position:
            if self.data.close[0] < self.bbands.lines.bot[0]:
                self.buy()
        elif self.data.close[0] > self.bbands.lines.top[0]:
            self.close()


class EMACrossover(bt.Strategy):
    """Exponential Moving Average Crossover Strategy"""
    params = (
        ('fast_period', 12),
        ('slow_period', 26),
    )

    def __init__(self):
        self.fast_ema = bt.indicators.ExponentialMovingAverage(
            self.data.close, period=self.params.fast_period
        )
        self.slow_ema = bt.indicators.ExponentialMovingAverage(
            self.data.close, period=self.params.slow_period
        )
        self.crossover = bt.indicators.CrossOver(self.fast_ema, self.slow_ema)

    def next(self):
        if not self.position:
            if self.crossover > 0:
                self.buy()
        elif self.crossover < 0:
            self.close()


class StochasticStrategy(bt.Strategy):
    """Stochastic Oscillator Strategy"""
    params = (
        ('period', 14),
        ('period_dfast', 3),
        ('upperband', 80),
        ('lowerband', 20),
    )

    def __init__(self):
        self.stochastic = bt.indicators.Stochastic(
            self.data,
            period=self.params.period,
            period_dfast=self.params.period_dfast
        )

    def next(self):
        if not self.position:
            if self.stochastic.percK[0] < self.params.lowerband:
                self.buy()
        elif self.stochastic.percK[0] > self.params.upperband:
            self.close()


class MomentumStrategy(bt.Strategy):
    """Momentum Strategy"""
    params = (
        ('period', 12),
        ('threshold', 0),
    )

    def __init__(self):
        self.momentum = bt.indicators.Momentum(
            self.data.close,
            period=self.params.period
        )

    def next(self):
        if not self.position:
            if self.momentum[0] > self.params.threshold:
                self.buy()
        elif self.momentum[0] < self.params.threshold:
            self.close()


class TripleSMAStrategy(bt.Strategy):
    """Triple SMA Strategy (uses 3 moving averages)"""
    params = (
        ('fast_period', 5),
        ('medium_period', 20),
        ('slow_period', 50),
    )

    def __init__(self):
        self.fast_sma = bt.indicators.SMA(self.data.close, period=self.params.fast_period)
        self.medium_sma = bt.indicators.SMA(self.data.close, period=self.params.medium_period)
        self.slow_sma = bt.indicators.SMA(self.data.close, period=self.params.slow_period)

    def next(self):
        if not self.position:
            if self.fast_sma[0] > self.medium_sma[0] > self.slow_sma[0]:
                self.buy()
        else:
            if self.fast_sma[0] < self.medium_sma[0]:
                self.close()


class MeanReversionStrategy(bt.Strategy):
    """Mean Reversion with SMA"""
    params = (
        ('period', 20),
        ('devfactor', 2.0),
    )

    def __init__(self):
        self.sma = bt.indicators.SMA(self.data.close, period=self.params.period)
        self.stddev = bt.indicators.StandardDeviation(
            self.data.close, period=self.params.period
        )

    def next(self):
        upper_band = self.sma[0] + (self.stddev[0] * self.params.devfactor)
        lower_band = self.sma[0] - (self.stddev[0] * self.params.devfactor)
        
        if not self.position:
            if self.data.close[0] < lower_band:
                self.buy()
        elif self.data.close[0] > upper_band:
            self.close()


# ==================== CUSTOM STRATEGY BUILDER ====================

def build_custom_strategy():
    """Interactive custom strategy builder"""
    print("\n" + "="*60)
    print("CUSTOM STRATEGY BUILDER")
    print("="*60)
    print("\nLet's build your custom strategy step by step!\n")
    
    print("STEP 1: Choose your indicator")
    print("[1] SMA (Simple Moving Average)")
    print("[2] EMA (Exponential Moving Average)")
    print("[3] RSI (Relative Strength Index)")
    print("[4] MACD (Moving Average Convergence Divergence)")
    print("[5] Bollinger Bands")
    print("[6] Stochastic Oscillator")
    
    while True:
        indicator_choice = input("\nSelect indicator (1-6): ").strip()
        if indicator_choice in ['1', '2', '3', '4', '5', '6']:
            break
        print("❌ Invalid choice. Please select 1-6.")
    
    if indicator_choice in ['1', '2']:
        indicator_name = "SMA" if indicator_choice == '1' else "EMA"
        print(f"\nSTEP 2: Configure {indicator_name} parameters")
        period = get_int_input(f"Enter {indicator_name} period (default: 20): ", 20)
        
        print("\nSTEP 3: Choose trading logic")
        print("[1] Buy when price crosses ABOVE the MA")
        print("[2] Buy when price crosses BELOW the MA (contrarian)")
        logic = input("Select logic (1 or 2): ").strip()
        
        return create_ma_strategy(indicator_choice, period, logic == '1')
    
    elif indicator_choice == '3':
        print("\nSTEP 2: Configure RSI parameters")
        period = get_int_input("Enter RSI period (default: 14): ", 14)
        lower = get_int_input("Enter oversold level (default: 30): ", 30)
        upper = get_int_input("Enter overbought level (default: 70): ", 70)
        
        return create_rsi_custom_strategy(period, lower, upper)
    
    elif indicator_choice == '4':
        print("\nSTEP 2: Configure MACD parameters")
        fast = get_int_input("Enter fast period (default: 12): ", 12)
        slow = get_int_input("Enter slow period (default: 26): ", 26)
        signal = get_int_input("Enter signal period (default: 9): ", 9)
        
        return create_macd_custom_strategy(fast, slow, signal)
    
    elif indicator_choice == '5':
        print("\nSTEP 2: Configure Bollinger Bands parameters")
        period = get_int_input("Enter period (default: 20): ", 20)
        devfactor = get_float_input("Enter deviation factor (default: 2.0): ", 2.0)
        
        return create_bb_custom_strategy(period, devfactor)
    
    elif indicator_choice == '6':
        print("\nSTEP 2: Configure Stochastic parameters")
        period = get_int_input("Enter period (default: 14): ", 14)
        lower = get_int_input("Enter oversold level (default: 20): ", 20)
        upper = get_int_input("Enter overbought level (default: 80): ", 80)
        
        return create_stochastic_custom_strategy(period, lower, upper)


def get_int_input(prompt, default):
    """Get integer input with default"""
    while True:
        value = input(prompt).strip()
        if not value:
            return default
        try:
            return int(value)
        except ValueError:
            print(f"❌ Invalid input. Please enter a number.")


def get_float_input(prompt, default):
    """Get float input with default"""
    while True:
        value = input(prompt).strip()
        if not value:
            return default
        try:
            return float(value)
        except ValueError:
            print(f"❌ Invalid input. Please enter a number.")


def create_ma_strategy(indicator_type, period, cross_above):
    """Create custom MA strategy"""
    class CustomMAStrategy(bt.Strategy):
        params = (('period', period),)
        
        def __init__(self):
            if indicator_type == '1':
                self.ma = bt.indicators.SMA(self.data.close, period=self.params.period)
            else:
                self.ma = bt.indicators.EMA(self.data.close, period=self.params.period)
        
        def next(self):
            if cross_above:
                if not self.position:
                    if self.data.close[0] > self.ma[0] and self.data.close[-1] <= self.ma[-1]:
                        self.buy()
                elif self.data.close[0] < self.ma[0]:
                    self.close()
            else:
                if not self.position:
                    if self.data.close[0] < self.ma[0] and self.data.close[-1] >= self.ma[-1]:
                        self.buy()
                elif self.data.close[0] > self.ma[0]:
                    self.close()
    
    return CustomMAStrategy


def create_rsi_custom_strategy(period, lower, upper):
    """Create custom RSI strategy"""
    class CustomRSIStrategy(bt.Strategy):
        params = (
            ('period', period),
            ('lower', lower),
            ('upper', upper),
        )
        
        def __init__(self):
            self.rsi = bt.indicators.RSI(self.data.close, period=self.params.period)
        
        def next(self):
            if not self.position:
                if self.rsi[0] < self.params.lower:
                    self.buy()
            elif self.rsi[0] > self.params.upper:
                self.close()
    
    return CustomRSIStrategy


def create_macd_custom_strategy(fast, slow, signal):
    """Create custom MACD strategy"""
    class CustomMACDStrategy(bt.Strategy):
        params = (
            ('fast', fast),
            ('slow', slow),
            ('signal', signal),
        )
        
        def __init__(self):
            self.macd = bt.indicators.MACD(
                self.data.close,
                period_me1=self.params.fast,
                period_me2=self.params.slow,
                period_signal=self.params.signal
            )
        
        def next(self):
            if not self.position:
                if self.macd.macd[0] > self.macd.signal[0]:
                    self.buy()
            elif self.macd.macd[0] < self.macd.signal[0]:
                self.close()
    
    return CustomMACDStrategy


def create_bb_custom_strategy(period, devfactor):
    """Create custom Bollinger Bands strategy"""
    class CustomBBStrategy(bt.Strategy):
        params = (
            ('period', period),
            ('devfactor', devfactor),
        )
        
        def __init__(self):
            self.bbands = bt.indicators.BollingerBands(
                self.data.close,
                period=self.params.period,
                devfactor=self.params.devfactor
            )
        
        def next(self):
            if not self.position:
                if self.data.close[0] < self.bbands.lines.bot[0]:
                    self.buy()
            elif self.data.close[0] > self.bbands.lines.top[0]:
                self.close()
    
    return CustomBBStrategy


def create_stochastic_custom_strategy(period, lower, upper):
    """Create custom Stochastic strategy"""
    class CustomStochasticStrategy(bt.Strategy):
        params = (
            ('period', period),
            ('lower', lower),
            ('upper', upper),
        )
        
        def __init__(self):
            self.stochastic = bt.indicators.Stochastic(
                self.data,
                period=self.params.period
            )
        
        def next(self):
            if not self.position:
                if self.stochastic.percK[0] < self.params.lower:
                    self.buy()
            elif self.stochastic.percK[0] > self.params.upper:
                self.close()
    
    return CustomStochasticStrategy


# ==================== STRATEGY MENU ====================

STRATEGIES = {
    '1': {
        'name': 'SMA Crossover',
        'class': SMACrossover,
        'description': 'Buy when fast MA crosses above slow MA'
    },
    '2': {
        'name': 'RSI Strategy',
        'class': RSIStrategy,
        'description': 'Buy when RSI < 30, sell when RSI > 70'
    },
    '3': {
        'name': 'MACD Strategy',
        'class': MACDStrategy,
        'description': 'Buy when MACD crosses above signal line'
    },
    '4': {
        'name': 'Buy and Hold',
        'class': BuyAndHold,
        'description': 'Simply buy and hold'
    },
    '5': {
        'name': 'Bollinger Bands',
        'class': BollingerBandsStrategy,
        'description': 'Buy at lower band, sell at upper band'
    },
    '6': {
        'name': 'EMA Crossover',
        'class': EMACrossover,
        'description': 'Buy when fast EMA crosses above slow EMA'
    },
    '7': {
        'name': 'Stochastic Oscillator',
        'class': StochasticStrategy,
        'description': 'Buy when oversold, sell when overbought'
    },
    '8': {
        'name': 'Momentum Strategy',
        'class': MomentumStrategy,
        'description': 'Buy on positive momentum, sell on negative'
    },
    '9': {
        'name': 'Triple SMA',
        'class': TripleSMAStrategy,
        'description': 'Uses 3 SMAs for trend confirmation'
    },
    '10': {
        'name': 'Mean Reversion',
        'class': MeanReversionStrategy,
        'description': 'Buy when price deviates below mean'
    },
    '11': {
        'name': 'BUILD CUSTOM STRATEGY',
        'class': None,
        'description': 'Create your own custom strategy!'
    }
}


# ==================== HELPER FUNCTIONS ====================

def print_header():
    """Print program header"""
    print("\n" + "="*60)
    print(" "*12 + "ADVANCED BACKTRADER BACKTESTING")
    print("="*60 + "\n")


def get_ticker():
    """Prompt user for stock ticker"""
    while True:
        ticker = input("Enter stock ticker (e.g., AAPL, MSFT, TSLA): ").strip().upper()
        if ticker:
            return ticker
        print("❌ Ticker cannot be empty. Please try again.\n")


def get_date(prompt):
    """Prompt user for date in YYYY-MM-DD format"""
    while True:
        date_str = input(f"{prompt} (YYYY-MM-DD): ").strip()
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            return date_obj
        except ValueError:
            print("❌ Invalid date format. Please use YYYY-MM-DD (e.g., 2020-01-01)\n")


def get_initial_cash():
    """Prompt user for initial cash"""
    while True:
        cash_str = input("Enter initial cash (default: 100000): ").strip()
        if not cash_str:
            return 100000.0
        try:
            cash = float(cash_str)
            if cash > 0:
                return cash
            print("❌ Initial cash must be positive.\n")
        except ValueError:
            print("❌ Invalid number. Please enter a valid amount.\n")


def get_commission():
    """Prompt user for commission rate"""
    while True:
        comm_str = input("Enter commission rate as decimal (default: 0.001 = 0.1%): ").strip()
        if not comm_str:
            return 0.001
        try:
            comm = float(comm_str)
            if 0 <= comm < 1:
                return comm
            print("❌ Commission must be between 0 and 1.\n")
        except ValueError:
            print("❌ Invalid number. Please enter a valid commission rate.\n")


def get_position_sizer():
    """Prompt user to select position sizing method"""
    print("\n" + "="*60)
    print("POSITION SIZING:")
    print("="*60)
    print("\n[1] Percentage of Portfolio (e.g., use 95% of available cash)")
    print("[2] All-In (use 100% of available cash)")
    print("[3] Fixed Dollar Amount (e.g., $10,000 per trade)")
    print("[4] Fixed Shares (e.g., 100 shares per trade)")
    
    while True:
        choice = input("\nSelect position sizing method (1-4): ").strip()
        if choice in ['1', '2', '3', '4']:
            break
        print("❌ Invalid choice. Please select 1-4.")
    
    if choice == '1':
        while True:
            percent_str = input("Enter percentage to use (default: 95): ").strip()
            if not percent_str:
                return PercentSizer, {'percents': 95}
            try:
                percent = float(percent_str)
                if 0 < percent <= 100:
                    return PercentSizer, {'percents': percent}
                print("❌ Percentage must be between 0 and 100.")
            except ValueError:
                print("❌ Invalid number.")
    
    elif choice == '2':
        return AllInSizer, {}
    
    elif choice == '3':
        while True:
            amount_str = input("Enter dollar amount per trade (default: 10000): ").strip()
            if not amount_str:
                return FixedAmountSizer, {'amount': 10000}
            try:
                amount = float(amount_str)
                if amount > 0:
                    return FixedAmountSizer, {'amount': amount}
                print("❌ Amount must be positive.")
            except ValueError:
                print("❌ Invalid number.")
    
    elif choice == '4':
        while True:
            shares_str = input("Enter number of shares per trade (default: 100): ").strip()
            if not shares_str:
                return FixedSharesSizer, {'shares': 100}
            try:
                shares = int(shares_str)
                if shares > 0:
                    return FixedSharesSizer, {'shares': shares}
                print("❌ Shares must be positive.")
            except ValueError:
                print("❌ Invalid number.")


def display_strategy_menu():
    """Display available strategies"""
    print("\n" + "="*60)
    print("AVAILABLE STRATEGIES:")
    print("="*60)
    for key, strategy in STRATEGIES.items():
        print(f"\n[{key}] {strategy['name']}")
        print(f"    {strategy['description']}")
    print("\n" + "="*60)


def get_strategy_choice():
    """Prompt user to select a strategy"""
    while True:
        choice = input("\nSelect strategy number (1-11): ").strip()
        if choice in STRATEGIES:
            if choice == '11':
                return build_custom_strategy()
            return STRATEGIES[choice]['class']
        print("❌ Invalid choice. Please select a number between 1 and 11.")


def download_yahoo_data(ticker, start_date, end_date):
    """Download data from Yahoo Finance"""
    print(f"\n📊 Downloading data for {ticker} from Yahoo Finance...")
    try:
        import yfinance as yf
        data = yf.download(ticker, start=start_date, end=end_date, progress=False)
        if data.empty:
            print(f"❌ No data found for {ticker}. Please check the ticker and date range.")
            return None
        
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.droplevel(1)
        
        data.columns = [col.lower() if isinstance(col, str) else col for col in data.columns]
        
        print(f"✅ Successfully downloaded {len(data)} data points")
        
        if len(data) < 50:
            print(f"⚠️  Warning: Only {len(data)} data points. Some strategies need 30+ days.")
            print("    Recommendation: Use at least 1 year of data for reliable results.")
        
        return data
    except ImportError:
        print("❌ yfinance not installed. Install with: pip install yfinance")
        return None
    except Exception as e:
        print(f"❌ Error downloading data: {e}")
        return None


def run_backtest(data, strategy_class, initial_cash, commission, sizer_class, sizer_params):
    """Run the backtest using Cerebro"""
    print("\n🚀 Running backtest...\n")
    
    min_data_needed = {
        'SMACrossover': 30,
        'RSIStrategy': 14,
        'MACDStrategy': 35,
        'BollingerBandsStrategy': 20,
        'BuyAndHold': 1,
        'EMACrossover': 26,
        'StochasticStrategy': 14,
        'MomentumStrategy': 12,
        'TripleSMAStrategy': 50,
        'MeanReversionStrategy': 20,
    }
    
    strategy_name = strategy_class.__name__
    min_needed = min_data_needed.get(strategy_name, 1)
    
    if len(data) < min_needed:
        print(f"❌ Error: {strategy_name} needs at least {min_needed} data points.")
        print(f"   You only have {len(data)} data points.")
        print(f"\n💡 Solutions:")
        print(f"   1. Use a longer date range (at least 1-2 years recommended)")
        print(f"   2. Choose 'Buy and Hold' strategy (works with any data size)")
        raise ValueError(f"Insufficient data: need {min_needed} points, have {len(data)}")
    
    try:
        cerebro = bt.Cerebro()
        data_feed = bt.feeds.PandasData(dataname=data)
        cerebro.adddata(data_feed)
        cerebro.addstrategy(strategy_class)
        
        # Add position sizer
        cerebro.addsizer(sizer_class, **sizer_params)
        
        cerebro.broker.setcash(initial_cash)
        cerebro.broker.setcommission(commission=commission)
        
        cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='sharpe')
        cerebro.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')
        cerebro.addanalyzer(bt.analyzers.Returns, _name='returns')
        cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name='trades')
        
        starting_value = cerebro.broker.getvalue()
        print(f"Starting Portfolio Value: ${starting_value:,.2f}")
        
        results = cerebro.run()
        strat = results[0]
        
        ending_value = cerebro.broker.getvalue()
        print(f"Final Portfolio Value:    ${ending_value:,.2f}")
        
        return cerebro, strat, starting_value, ending_value
        
    except Exception as e:
        print(f"\n❌ Error during backtest execution: {e}")
        print(f"\n💡 Try:")
        print(f"   1. Using more data (at least 1 year)")
        print(f"   2. Choosing 'Buy and Hold' strategy for short data")
        raise


def print_results(strat, starting_value, ending_value):
    """Print backtest results and analytics"""
    print("\n" + "="*60)
    print("BACKTEST RESULTS:")
    print("="*60)
    
    total_return = ending_value - starting_value
    total_return_pct = (total_return / starting_value) * 100
    
    print(f"\n💰 Total Return: ${total_return:,.2f} ({total_return_pct:.2f}%)")
    
    try:
        sharpe = strat.analyzers.sharpe.get_analysis()
        sharpe_ratio = sharpe.get('sharperatio', None)
        if sharpe_ratio:
            print(f"📊 Sharpe Ratio: {sharpe_ratio:.3f}")
    except:
        pass
    
    try:
        drawdown = strat.analyzers.drawdown.get_analysis()
        max_dd = drawdown.get('max', {}).get('drawdown', 0)
        print(f"📉 Max Drawdown: {max_dd:.2f}%")
    except:
        pass
    
    try:
        trades = strat.analyzers.trades.get_analysis()
        total_trades = trades.get('total', {}).get('closed', 0)
        won_trades = trades.get('won', {}).get('total', 0)
        lost_trades = trades.get('lost', {}).get('total', 0)
        
        if total_trades > 0:
            win_rate = (won_trades / total_trades) * 100
            print(f"\n📈 Total Trades: {total_trades}")
            print(f"✅ Won: {won_trades} | ❌ Lost: {lost_trades}")
            print(f"🎯 Win Rate: {win_rate:.2f}%")
    except:
        pass
    
    print("\n" + "="*60)


def plot_interactive(cerebro):
    """Generate interactive plot with zoom capability"""
    print("\n📊 Generating interactive plot...")
    print("💡 Plot controls:")
    print("   - Pan: Click and drag")
    print("   - Zoom: Use mouse scroll wheel or toolbar zoom")
    print("   - Reset: Click 'Home' button in toolbar")
    print("   - Save: Click 'Save' button to export image\n")
    
    try:
        import matplotlib
        matplotlib.use('TkAgg')  # Use interactive backend
        import matplotlib.pyplot as plt
        
        # Plot with backtrader
        figs = cerebro.plot(style='candlestick', iplot=False)
        
        # Make it interactive
        plt.show()
        
    except Exception as e:
        print(f"❌ Could not generate interactive plot: {e}")
        print("💡 Trying basic plot...")
        try:
            cerebro.plot(style='candlestick')
        except:
            print("❌ Plotting failed. Continue without visualization.")


# ==================== MAIN PROGRAM ====================

def main():
    """Main program execution"""
    try:
        print_header()
        
        # Get stock info
        ticker = get_ticker()
        print()
        start_date = get_date("Enter start date")
        end_date = get_date("Enter end date")
        
        # Download data
        data = download_yahoo_data(ticker, start_date, end_date)
        if data is None:
            return
        
        # Get backtest parameters
        print()
        initial_cash = get_initial_cash()
        commission = get_commission()
        
        # Get position sizing
        sizer_class, sizer_params = get_position_sizer()
        
        # Select strategy
        display_strategy_menu()
        strategy_class = get_strategy_choice()
        
        # Run backtest
        cerebro, strat, starting_value, ending_value = run_backtest(
            data, strategy_class, initial_cash, commission, sizer_class, sizer_params
        )
        
        # Print results
        print_results(strat, starting_value, ending_value)
        
        # Interactive plot
        print("\n" + "="*60)
        show_plot = input("Would you like to see the interactive plot? (y/n): ").strip().lower()
        if show_plot == 'y':
            plot_interactive(cerebro)
        
        print("\n✅ Backtest completed successfully!")
        print("="*60 + "\n")
        
    except KeyboardInterrupt:
        print("\n\n❌ Program interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
