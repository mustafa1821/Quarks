"""
Streamlit Frontend for Advanced Stock Backtesting System
Run with: streamlit run backtest_app.py
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set page config
st.set_page_config(
    page_title="Stock Backtesting Tool",
    page_icon="📈",
    layout="wide"
)

class Backtester:
    def __init__(self, initial_capital=10000, commission=0.001):
        self.initial_capital = initial_capital
        self.commission = commission
        self.trades = []
        self.equity_curve = []
        
    def generate_sample_data(self, days=500, start_date='2023-01-01'):
        """Generate synthetic OHLCV data"""
        dates = pd.date_range(start=start_date, periods=days, freq='D')
        price = 400
        data = []
        
        for date in dates:
            change = (np.random.random() - 0.48) * 10
            price = max(price + change, 100)
            
            high = price + np.random.random() * 5
            low = price - np.random.random() * 5
            open_price = low + np.random.random() * (high - low)
            close = low + np.random.random() * (high - low)
            volume = int(50000000 + np.random.random() * 20000000)
            
            data.append({
                'date': date,
                'open': round(open_price, 2),
                'high': round(high, 2),
                'low': round(low, 2),
                'close': round(close, 2),
                'volume': volume
            })
        
        df = pd.DataFrame(data)
        df.set_index('date', inplace=True)
        return df
    
    def calculate_sma(self, data, period):
        return data['close'].rolling(window=period).mean()
    
    def calculate_ema(self, data, period):
        return data['close'].ewm(span=period, adjust=False).mean()
    
    def calculate_rsi(self, data, period=14):
        delta = data['close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi
    
    def calculate_macd(self, data, fast=12, slow=26, signal=9):
        ema_fast = data['close'].ewm(span=fast, adjust=False).mean()
        ema_slow = data['close'].ewm(span=slow, adjust=False).mean()
        macd_line = ema_fast - ema_slow
        signal_line = macd_line.ewm(span=signal, adjust=False).mean()
        histogram = macd_line - signal_line
        return macd_line, signal_line, histogram
    
    def calculate_stochastic(self, data, period=14, k_period=3, d_period=3):
        low_min = data['low'].rolling(window=period).min()
        high_max = data['high'].rolling(window=period).max()
        k = 100 * ((data['close'] - low_min) / (high_max - low_min))
        k = k.rolling(window=k_period).mean()
        d = k.rolling(window=d_period).mean()
        return k, d
    
    def calculate_ad(self, data):
        mfm = ((data['close'] - data['low']) - (data['high'] - data['close'])) / (data['high'] - data['low'])
        mfv = mfm * data['volume']
        ad = mfv.cumsum()
        return ad
    
    def run_backtest(self, data, strategy_params):
        """Run backtest with specified parameters"""
        short_window = strategy_params.get('short_window', 20)
        long_window = strategy_params.get('long_window', 50)
        stop_loss = strategy_params.get('stop_loss', 5) / 100
        take_profit = strategy_params.get('take_profit', 15) / 100
        position_size = strategy_params.get('position_size', 100) / 100
        
        use_rsi = strategy_params.get('use_rsi', False)
        use_ema = strategy_params.get('use_ema', False)
        use_macd = strategy_params.get('use_macd', False)
        use_stochastic = strategy_params.get('use_stochastic', False)
        use_ad = strategy_params.get('use_ad', False)
        
        # Calculate indicators
        data['sma_short'] = self.calculate_sma(data, short_window)
        data['sma_long'] = self.calculate_sma(data, long_window)
        
        if use_rsi:
            rsi_period = strategy_params.get('rsi_period', 14)
            rsi_oversold = strategy_params.get('rsi_oversold', 30)
            rsi_overbought = strategy_params.get('rsi_overbought', 70)
            data['rsi'] = self.calculate_rsi(data, rsi_period)
        
        if use_ema:
            ema_short = strategy_params.get('ema_short', 12)
            ema_long = strategy_params.get('ema_long', 26)
            data['ema_short'] = self.calculate_ema(data, ema_short)
            data['ema_long'] = self.calculate_ema(data, ema_long)
        
        if use_macd:
            macd_fast = strategy_params.get('macd_fast', 12)
            macd_slow = strategy_params.get('macd_slow', 26)
            macd_signal = strategy_params.get('macd_signal', 9)
            data['macd'], data['macd_signal'], data['macd_hist'] = self.calculate_macd(
                data, macd_fast, macd_slow, macd_signal
            )
        
        if use_stochastic:
            stoch_period = strategy_params.get('stoch_period', 14)
            stoch_k = strategy_params.get('stoch_k', 3)
            stoch_d = strategy_params.get('stoch_d', 3)
            stoch_oversold = strategy_params.get('stoch_oversold', 20)
            stoch_overbought = strategy_params.get('stoch_overbought', 80)
            data['stoch_k'], data['stoch_d'] = self.calculate_stochastic(
                data, stoch_period, stoch_k, stoch_d
            )
        
        if use_ad:
            data['ad'] = self.calculate_ad(data)
        
        # Trading loop
        capital = self.initial_capital
        position = 0
        entry_price = 0
        self.trades = []
        equity = []
        
        for i in range(long_window, len(data)):
            current_price = data['close'].iloc[i]
            current_equity = capital + (position * current_price if position > 0 else 0)
            
            equity.append({
                'date': data.index[i],
                'equity': current_equity,
                'price': current_price
            })
            
            # BUY LOGIC
            if position == 0:
                buy_signal = (data['sma_short'].iloc[i] > data['sma_long'].iloc[i] and 
                             data['sma_short'].iloc[i-1] <= data['sma_long'].iloc[i-1])
                
                if use_rsi and not pd.isna(data['rsi'].iloc[i]):
                    buy_signal = buy_signal and (data['rsi'].iloc[i] < rsi_oversold)
                
                if use_ema and not pd.isna(data['ema_short'].iloc[i]):
                    buy_signal = buy_signal and (data['ema_short'].iloc[i] > data['ema_long'].iloc[i])
                
                if use_macd and not pd.isna(data['macd'].iloc[i]):
                    buy_signal = buy_signal and (data['macd'].iloc[i] > data['macd_signal'].iloc[i])
                
                if use_stochastic and not pd.isna(data['stoch_k'].iloc[i]):
                    buy_signal = buy_signal and (data['stoch_k'].iloc[i] < stoch_oversold)
                
                if use_ad and not pd.isna(data['ad'].iloc[i]) and i > 0:
                    buy_signal = buy_signal and (data['ad'].iloc[i] > data['ad'].iloc[i-1])
                
                if buy_signal:
                    shares = int((capital * position_size) / current_price)
                    if shares > 0:
                        cost = shares * current_price
                        commission_cost = cost * self.commission
                        capital -= (cost + commission_cost)
                        position = shares
                        entry_price = current_price
                        
                        self.trades.append({
                            'date': data.index[i],
                            'type': 'BUY',
                            'price': current_price,
                            'shares': shares,
                            'value': cost,
                            'commission': commission_cost
                        })
            
            # SELL LOGIC
            elif position > 0:
                price_change = (current_price - entry_price) / entry_price
                sell_signal = (data['sma_short'].iloc[i] < data['sma_long'].iloc[i] and 
                              data['sma_short'].iloc[i-1] >= data['sma_long'].iloc[i-1])
                stop_loss_hit = price_change <= -stop_loss
                take_profit_hit = price_change >= take_profit
                
                if use_rsi and not pd.isna(data['rsi'].iloc[i]):
                    sell_signal = sell_signal or (data['rsi'].iloc[i] > rsi_overbought)
                
                if use_ema and not pd.isna(data['ema_short'].iloc[i]):
                    sell_signal = sell_signal or (data['ema_short'].iloc[i] < data['ema_long'].iloc[i] and 
                                                  data['ema_short'].iloc[i-1] >= data['ema_long'].iloc[i-1])
                
                if use_macd and not pd.isna(data['macd'].iloc[i]):
                    sell_signal = sell_signal or (data['macd'].iloc[i] < data['macd_signal'].iloc[i] and 
                                                  data['macd'].iloc[i-1] >= data['macd_signal'].iloc[i-1])
                
                if use_stochastic and not pd.isna(data['stoch_k'].iloc[i]):
                    sell_signal = sell_signal or (data['stoch_k'].iloc[i] > stoch_overbought)
                
                if use_ad and not pd.isna(data['ad'].iloc[i]) and i > 1:
                    sell_signal = sell_signal or (data['ad'].iloc[i] < data['ad'].iloc[i-1] and 
                                                  data['ad'].iloc[i-1] < data['ad'].iloc[i-2])
                
                if sell_signal or stop_loss_hit or take_profit_hit:
                    proceeds = position * current_price
                    commission_cost = proceeds * self.commission
                    capital += (proceeds - commission_cost)
                    pnl = proceeds - (position * entry_price)
                    pnl_percent = price_change * 100
                    
                    reason = 'Signal'
                    if stop_loss_hit:
                        reason = 'Stop Loss'
                    elif take_profit_hit:
                        reason = 'Take Profit'
                    
                    self.trades.append({
                        'date': data.index[i],
                        'type': 'SELL',
                        'price': current_price,
                        'shares': position,
                        'value': proceeds,
                        'commission': commission_cost,
                        'pnl': pnl,
                        'pnl_percent': pnl_percent,
                        'reason': reason
                    })
                    
                    position = 0
                    entry_price = 0
        
        # Close position at end
        if position > 0:
            final_price = data['close'].iloc[-1]
            proceeds = position * final_price
            commission_cost = proceeds * self.commission
            capital += (proceeds - commission_cost)
            
            self.trades.append({
                'date': data.index[-1],
                'type': 'SELL',
                'price': final_price,
                'shares': position,
                'value': proceeds,
                'commission': commission_cost,
                'pnl': proceeds - (position * entry_price),
                'pnl_percent': ((final_price - entry_price) / entry_price) * 100,
                'reason': 'End of Period'
            })
        
        self.equity_curve = pd.DataFrame(equity)
        self.final_capital = capital
        
        return self.calculate_metrics(data), data
    
    def calculate_metrics(self, data):
        """Calculate performance metrics"""
        trades_df = pd.DataFrame(self.trades)
        sell_trades = trades_df[trades_df['type'] == 'SELL']
        
        total_return = ((self.final_capital - self.initial_capital) / self.initial_capital) * 100
        total_trades = len(sell_trades)
        winning_trades = len(sell_trades[sell_trades['pnl'] > 0])
        losing_trades = len(sell_trades[sell_trades['pnl'] < 0])
        win_rate = (winning_trades / total_trades * 100) if total_trades > 0 else 0
        
        gross_profit = sell_trades[sell_trades['pnl'] > 0]['pnl'].sum()
        gross_loss = abs(sell_trades[sell_trades['pnl'] < 0]['pnl'].sum())
        profit_factor = (gross_profit / gross_loss) if gross_loss > 0 else 0
        
        equity_values = self.equity_curve['equity'].values
        running_max = np.maximum.accumulate(equity_values)
        drawdown = (running_max - equity_values) / running_max * 100
        max_drawdown = drawdown.max()
        
        returns = self.equity_curve['equity'].pct_change().dropna()
        sharpe_ratio = (returns.mean() / returns.std() * np.sqrt(252)) if returns.std() > 0 else 0
        
        buy_hold_return = ((data['close'].iloc[-1] - data['close'].iloc[50]) / data['close'].iloc[50]) * 100
        
        return {
            'initial_capital': self.initial_capital,
            'final_capital': self.final_capital,
            'total_return': total_return,
            'total_trades': total_trades,
            'winning_trades': winning_trades,
            'losing_trades': losing_trades,
            'win_rate': win_rate,
            'profit_factor': profit_factor,
            'max_drawdown': max_drawdown,
            'sharpe_ratio': sharpe_ratio,
            'buy_hold_return': buy_hold_return,
            'alpha': total_return - buy_hold_return,
            'total_commissions': trades_df['commission'].sum()
        }


# STREAMLIT UI
def main():
    st.title("📈 Advanced Stock Backtesting Tool")
    st.markdown("Test your trading strategies with multiple technical indicators")
    
    # Sidebar configuration
    st.sidebar.header("⚙️ Strategy Configuration")
    
    # Basic parameters
    st.sidebar.subheader("Basic Parameters")
    initial_capital = st.sidebar.number_input("Initial Capital ($)", value=10000, min_value=1000, step=1000)
    short_window = st.sidebar.slider("Short SMA Window", 5, 50, 20)
    long_window = st.sidebar.slider("Long SMA Window", 20, 200, 50)
    stop_loss = st.sidebar.slider("Stop Loss (%)", 1, 20, 5)
    take_profit = st.sidebar.slider("Take Profit (%)", 5, 50, 15)
    position_size = st.sidebar.slider("Position Size (%)", 10, 100, 100)
    commission = st.sidebar.slider("Commission (%)", 0.0, 1.0, 0.1, 0.05)
    
    # Technical indicators
    st.sidebar.subheader("📊 Technical Indicators")
    
    use_rsi = st.sidebar.checkbox("Use RSI", value=False)
    if use_rsi:
        rsi_period = st.sidebar.slider("RSI Period", 7, 21, 14)
        rsi_oversold = st.sidebar.slider("RSI Oversold", 20, 40, 30)
        rsi_overbought = st.sidebar.slider("RSI Overbought", 60, 80, 70)
    
    use_ema = st.sidebar.checkbox("Use EMA", value=False)
    if use_ema:
        ema_short = st.sidebar.slider("EMA Short", 5, 20, 12)
        ema_long = st.sidebar.slider("EMA Long", 20, 50, 26)
    
    use_macd = st.sidebar.checkbox("Use MACD", value=False)
    if use_macd:
        macd_fast = st.sidebar.slider("MACD Fast", 8, 16, 12)
        macd_slow = st.sidebar.slider("MACD Slow", 20, 35, 26)
        macd_signal = st.sidebar.slider("MACD Signal", 7, 12, 9)
    
    use_stochastic = st.sidebar.checkbox("Use Stochastic", value=False)
    if use_stochastic:
        stoch_period = st.sidebar.slider("Stochastic Period", 10, 21, 14)
        stoch_oversold = st.sidebar.slider("Stoch Oversold", 10, 30, 20)
        stoch_overbought = st.sidebar.slider("Stoch Overbought", 70, 90, 80)
    
    use_ad = st.sidebar.checkbox("Use A/D Line", value=False)
    
    # Run backtest button
    if st.sidebar.button("▶️ Run Backtest", type="primary"):
        with st.spinner("Running backtest..."):
            # Initialize backtester
            bt = Backtester(initial_capital=initial_capital, commission=commission/100)
            
            # Generate data
            data = bt.generate_sample_data(days=500)
            
            # Build strategy params
            strategy_params = {
                'short_window': short_window,
                'long_window': long_window,
                'stop_loss': stop_loss,
                'take_profit': take_profit,
                'position_size': position_size,
                'use_rsi': use_rsi,
                'use_ema': use_ema,
                'use_macd': use_macd,
                'use_stochastic': use_stochastic,
                'use_ad': use_ad
            }
            
            if use_rsi:
                strategy_params.update({
                    'rsi_period': rsi_period,
                    'rsi_oversold': rsi_oversold,
                    'rsi_overbought': rsi_overbought
                })
            
            if use_ema:
                strategy_params.update({
                    'ema_short': ema_short,
                    'ema_long': ema_long
                })
            
            if use_macd:
                strategy_params.update({
                    'macd_fast': macd_fast,
                    'macd_slow': macd_slow,
                    'macd_signal': macd_signal
                })
            
            if use_stochastic:
                strategy_params.update({
                    'stoch_period': stoch_period,
                    'stoch_k': 3,
                    'stoch_d': 3,
                    'stoch_oversold': stoch_oversold,
                    'stoch_overbought': stoch_overbought
                })
            
            # Run backtest
            metrics, data_with_indicators = bt.run_backtest(data, strategy_params)
            
            # Store results in session state
            st.session_state.metrics = metrics
            st.session_state.equity_curve = bt.equity_curve
            st.session_state.trades = pd.DataFrame(bt.trades)
            st.session_state.data = data_with_indicators
    
    # Display results
    if 'metrics' in st.session_state:
        metrics = st.session_state.metrics
        
        # Performance metrics
        st.header("📊 Performance Metrics")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "Total Return", 
                f"{metrics['total_return']:+.2f}%",
                f"${metrics['final_capital'] - metrics['initial_capital']:,.2f}"
            )
        
        with col2:
            st.metric("Sharpe Ratio", f"{metrics['sharpe_ratio']:.2f}")
        
        with col3:
            st.metric("Win Rate", f"{metrics['win_rate']:.1f}%")
        
        with col4:
            st.metric("Max Drawdown", f"-{metrics['max_drawdown']:.2f}%")
        
        col5, col6, col7, col8 = st.columns(4)
        
        with col5:
            st.metric("Total Trades", metrics['total_trades'])
        
        with col6:
            st.metric("Profit Factor", f"{metrics['profit_factor']:.2f}")
        
        with col7:
            st.metric("Alpha vs Buy & Hold", f"{metrics['alpha']:+.2f}%")
        
        with col8:
            st.metric("Commissions", f"${metrics['total_commissions']:,.2f}")
        
        # Equity curve chart
        st.header("📈 Equity Curve")
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=st.session_state.equity_curve['date'],
            y=st.session_state.equity_curve['equity'],
            mode='lines',
            name='Portfolio Value',
            line=dict(color='blue', width=2)
        ))
        
        fig.add_hline(
            y=metrics['initial_capital'],
            line_dash="dash",
            line_color="red",
            annotation_text="Initial Capital"
        )
        
        fig.update_layout(
            title="Portfolio Value Over Time",
            xaxis_title="Date",
            yaxis_title="Value ($)",
            hovermode='x unified',
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Trade history
        st.header("📋 Trade History")
        
        trades_df = st.session_state.trades
        
        # Format the dataframe for display
        display_df = trades_df.copy()
        display_df['date'] = display_df['date'].dt.strftime('%Y-%m-%d')
        display_df['price'] = display_df['price'].apply(lambda x: f"${x:.2f}")
        display_df['value'] = display_df['value'].apply(lambda x: f"${x:,.2f}")
        
        if 'pnl' in display_df.columns:
            display_df['pnl'] = display_df['pnl'].apply(lambda x: f"${x:,.2f}" if pd.notna(x) else "-")
            display_df['pnl_percent'] = display_df['pnl_percent'].apply(lambda x: f"{x:+.2f}%" if pd.notna(x) else "-")
        
        st.dataframe(display_df, use_container_width=True, height=400)
        
        # Download button
        csv = trades_df.to_csv(index=False)
        st.download_button(
            label="📥 Download Trade History (CSV)",
            data=csv,
            file_name="backtest_trades.csv",
            mime="text/csv"
        )
    
    else:
        st.info("👈 Configure your strategy in the sidebar and click 'Run Backtest' to see results")
        
        # Display example
        st.subheader("🎯 How to Use")
        st.markdown("""
        1. **Set Initial Capital** - Your starting investment amount
        2. **Configure SMA Windows** - Short and long moving average periods
        3. **Set Risk Parameters** - Stop loss and take profit levels
        4. **Enable Technical Indicators** - Add RSI, EMA, MACD, Stochastic, or A/D filters
        5. **Click Run Backtest** - See your strategy performance!
        
        **Pro Tip:** Start with just SMA crossover, then add indicators one at a time to see their impact.
        """)


if __name__ == "__main__":
    main()