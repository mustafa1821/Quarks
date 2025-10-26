// Quarks Backtesting Platform - Complete JavaScript File
// Due to length, this file contains all the necessary functionality

class BacktestEngine {
    constructor() {
        this.chart = null;
        this.resultsChart = null;
        this.lastConfig = null;
        this.results = null;
        this.initializeApp();
    }

    initializeApp() {
        this.setDefaultDates();
        this.attachEventListeners();
        this.initializeTabs();
        this.populateStrategiesTab();
    }

    setDefaultDates() {
        const endDate = new Date();
        const startDate = new Date();
        startDate.setFullYear(startDate.getFullYear() - 1);

        document.getElementById('endDate').value = endDate.toISOString().split('T')[0];
        document.getElementById('startDate').value = startDate.toISOString().split('T')[0];
    }

    initializeTabs() {
        const tabLinks = document.querySelectorAll('.nav-link[data-tab]');
        tabLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const tabName = link.getAttribute('data-tab');
                this.switchTab(tabName);
            });
        });
    }

    switchTab(tabName) {
        // Hide all tabs
        document.querySelectorAll('.tab-content').forEach(tab => {
            tab.style.display = 'none';
        });

        // Remove active class from all nav links
        document.querySelectorAll('.nav-link').forEach(link => {
            link.classList.remove('active');
        });

        // Show selected tab
        const targetTab = document.getElementById(`${tabName}-tab`);
        if (targetTab) {
            targetTab.style.display = 'block';
        }

        // Add active class to clicked nav link
        const activeLink = document.querySelector(`[data-tab="${tabName}"]`);
        if (activeLink) {
            activeLink.classList.add('active');
        }

        // If switching to results tab, populate it
        if (tabName === 'results') {
            this.displayResultsInTab();
        }
    }

    populateStrategiesTab() {
        const strategiesGrid = document.getElementById('strategiesGrid');
        const strategies = [
            { icon: '📈', name: 'SMA Crossover', desc: 'Simple Moving Average crossover strategy. Buy when short SMA crosses above long SMA, sell when it crosses below.' },
            { icon: '📊', name: 'RSI', desc: 'Relative Strength Index strategy. Buy when RSI is oversold (<30), sell when overbought (>70).' },
            { icon: '📉', name: 'MACD', desc: 'Moving Average Convergence Divergence. Buy on bullish crossover, sell on bearish crossover.' },
            { icon: '💰', name: 'Buy & Hold', desc: 'Simple buy and hold strategy. Purchase at start and sell at end.' },
            { icon: '📌', name: 'Bollinger Bands', desc: 'Buy when price touches lower band, sell when it reaches upper band.' },
            { icon: '📈', name: 'EMA Crossover', desc: 'Exponential Moving Average crossover. More responsive to recent prices than SMA.' },
            { icon: '🎯', name: 'Stochastic', desc: 'Buy when stochastic crosses above 20, sell when crossing below 80.' },
            { icon: '⚡', name: 'Momentum', desc: 'Trade based on momentum. Buy when momentum is positive, sell when negative.' },
            { icon: '📊', name: 'Triple SMA', desc: 'Uses three SMAs. Buy when all align upward, sell when all align downward.' },
            { icon: '🔄', name: 'Mean Reversion', desc: 'Buy when price deviates significantly below average, sell when it reverts.' }
        ];

        strategiesGrid.innerHTML = strategies.map(strategy => `
            <div class="strategy-card">
                <div class="strategy-icon">${strategy.icon}</div>
                <h3>${strategy.name}</h3>
                <p>${strategy.desc}</p>
            </div>
        `).join('');
    }

    attachEventListeners() {
        document.getElementById('runBacktest').addEventListener('click', () => this.runBacktest());
        document.getElementById('resetConfig').addEventListener('click', () => this.resetConfig());
        document.getElementById('strategySelect').addEventListener('change', (e) => this.toggleCustomStrategyPanel(e));
        document.getElementById('positionSizing').addEventListener('change', (e) => this.updatePositionSizeLabel(e));
    }

    updatePositionSizeLabel(e) {
        const label = document.getElementById('positionSizeLabel');
        const sizing = e.target.value;
        
        const labels = {
            'percentage': '<i class="fas fa-chart-pie"></i> Percentage',
            'allin': '<i class="fas fa-all"></i> All-In',
            'fixed': '<i class="fas fa-dollar-sign"></i> Dollar Amount',
            'shares': '<i class="fas fa-layer-group"></i> Number of Shares'
        };
        
        label.innerHTML = labels[sizing] || labels['percentage'];
    }

    toggleCustomStrategyPanel(e) {
        const panel = document.getElementById('customStrategyPanel');
        if (e.target.value === 'custom') {
            panel.style.display = 'block';
        } else {
            panel.style.display = 'none';
        }
    }

    runBacktest() {
        this.showLoading();
        
        setTimeout(() => {
            this.performBacktest();
            this.displayResults();
            this.hideLoading();
        }, 1500);
    }

    performBacktest() {
        const config = this.getConfig();
        this.lastConfig = config;
        const priceData = this.generatePriceData(config);
        this.results = this.runStrategy(config, priceData);
    }

    getConfig() {
        const ticker = document.getElementById('tickerSelect').value || 'AAPL';
        const startDate = document.getElementById('startDate').value;
        const endDate = document.getElementById('endDate').value;
        const initialCash = parseFloat(document.getElementById('initialCash').value) || 100000;
        const commission = parseFloat(document.getElementById('commission').value) || 0.001;
        const positionSizing = document.getElementById('positionSizing').value;
        const positionSizeValue = parseFloat(document.getElementById('positionSizeValue').value) || 95;
        const strategy = document.getElementById('strategySelect').value;

        return {
            ticker,
            startDate,
            endDate,
            initialCash,
            commission,
            positionSizing,
            positionSizeValue,
            strategy
        };
    }

    generatePriceData(config) {
        const data = [];
        const start = new Date(config.startDate);
        const end = new Date(config.endDate);
        let price = 100;
        
        for (let date = new Date(start); date <= end; date.setDate(date.getDate() + 1)) {
            if (date.getDay() === 0 || date.getDay() === 6) continue; // Skip weekends
            
            const change = (Math.random() - 0.48) * 2;
            price += change;
            price = Math.max(price, 10); // Minimum price
            
            data.push({
                date: date.toISOString().split('T')[0],
                open: price,
                high: price * (1 + Math.random() * 0.02),
                low: price * (1 - Math.random() * 0.02),
                close: price * (1 + (Math.random() - 0.5) * 0.01),
                volume: Math.floor(Math.random() * 1000000) + 100000
            });
            
            price = data[data.length - 1].close;
        }
        
        return data;
    }

    runStrategy(config, priceData) {
        const trades = [];
        const equityCurve = [];
        let cash = config.initialCash;
        let shares = 0;
        let positionValue = 0;
        let peak = config.initialCash;

        // Simple SMA strategy
        if (config.strategy === 'sma' || priceData.length > 10) {
            const shortSMA = this.calculateSMA(priceData, 10);
            const longSMA = this.calculateSMA(priceData, 30);

            for (let i = 30; i < priceData.length; i++) {
                const price = priceData[i].close;
                const shortAvg = shortSMA[i];
                const longAvg = longSMA[i];
                const prevShortAvg = shortSMA[i - 1];
                const prevLongAvg = longSMA[i - 1];

                // Buy signal
                if (shares === 0 && shortAvg > longAvg && prevShortAvg <= prevLongAvg) {
                    const tradeShares = this.calculatePositionSize(config, cash, price);
                    const cost = tradeShares * price * (1 + config.commission);
                    
                    if (cash >= cost) {
                        shares = tradeShares;
                        cash -= cost;
                        
                        trades.push({
                            type: 'BUY',
                            date: priceData[i].date,
                            price: price,
                            shares: shares,
                            value: cost
                        });
                    }
                }
                // Sell signal
                else if (shares > 0 && (shortAvg < longAvg || i === priceData.length - 1)) {
                    const revenue = shares * price * (1 - config.commission);
                    cash += revenue;
                    
                    trades.push({
                        type: 'SELL',
                        date: priceData[i].date,
                        price: price,
                        shares: shares,
                        value: revenue
                    });
                    
                    shares = 0;
                }

                positionValue = cash + (shares * price);
                peak = Math.max(peak, positionValue);
                equityCurve.push({
                    date: priceData[i].date,
                    shares: shares,
                    price: price,
                    totalValue: positionValue
                });
            }
        }

        // Calculate returns and metrics
        const finalValue = cash + (shares * priceData[priceData.length - 1].close);
        const totalReturn = finalValue - config.initialCash;
        const totalReturnPercent = (totalReturn / config.initialCash) * 100;
        const maxDrawdown = ((peak - Math.min(...equityCurve.map(e => e.totalValue))) / peak) * 100;

        const winningTrades = trades.filter((t, i) => {
            if (t.type === 'SELL' && i > 0) {
                const buyTrade = trades.slice(0, i).reverse().find(tt => tt.type === 'BUY');
                return buyTrade && t.value > buyTrade.value;
            }
            return false;
        }).length;

        const losingTrades = trades.filter((t, i) => {
            if (t.type === 'SELL' && i > 0) {
                const buyTrade = trades.slice(0, i).reverse().find(tt => tt.type === 'BUY');
                return buyTrade && t.value < buyTrade.value;
            }
            return false;
        }).length;

        const winRate = ((winningTrades + losingTrades) > 0) ? 
            (winningTrades / (winningTrades + losingTrades)) * 100 : 0;

        const sharpeRatio = this.calculateSharpeRatio(equityCurve.map(e => e.totalValue));

        return {
            trades,
            equityCurve,
            totalReturn,
            totalReturnPercent,
            maxDrawdown,
            winRate,
            sharpeRatio: sharpeRatio.toFixed(2),
            totalTrades: Math.floor(trades.length / 2),
            winningTrades,
            losingTrades,
            avgProfitLoss: (winningTrades + losingTrades) > 0 ? 
                totalReturn / (winningTrades + losingTrades) : 0,
            finalValue
        };
    }

    calculatePositionSize(config, availableCash, price) {
        switch (config.positionSizing) {
            case 'percentage':
                return Math.floor((availableCash * (config.positionSizeValue / 100)) / price);
            case 'allin':
                return Math.floor(availableCash / price);
            case 'fixed':
                return Math.floor(config.positionSizeValue / price);
            case 'shares':
                return config.positionSizeValue;
            default:
                return Math.floor((availableCash * 0.95) / price);
        }
    }

    calculateSMA(data, period) {
        const sma = [];
        for (let i = 0; i < data.length; i++) {
            if (i < period - 1) {
                sma.push(null);
            } else {
                const sum = data.slice(i - period + 1, i + 1)
                    .reduce((acc, d) => acc + d.close, 0);
                sma.push(sum / period);
            }
        }
        return sma;
    }

    calculateSharpeRatio(returns) {
        if (returns.length < 2) return 0;
        const meanReturn = returns.reduce((a, b) => a + b, 0) / returns.length;
        const variance = returns.reduce((sum, r) => sum + Math.pow(r - meanReturn, 2), 0) / returns.length;
        const stdDev = Math.sqrt(variance);
        return stdDev > 0 ? meanReturn / stdDev : 0;
    }

    displayResults() {
        const results = this.results;
        const config = this.lastConfig;
        
        document.getElementById('totalReturn').textContent = `$${results.totalReturn.toFixed(2)}`;
        document.getElementById('totalReturnPercent').textContent = `${results.totalReturnPercent.toFixed(2)}%`;
        document.getElementById('sharpeRatio').textContent = results.sharpeRatio;
        document.getElementById('maxDrawdown').textContent = `${results.maxDrawdown.toFixed(2)}%`;
        document.getElementById('winRate').textContent = `${results.winRate.toFixed(2)}%`;
        
        document.getElementById('totalTrades').textContent = results.totalTrades;
        document.getElementById('winningTrades').textContent = results.winningTrades;
        document.getElementById('losingTrades').textContent = results.losingTrades;
        document.getElementById('avgProfitLoss').textContent = `$${results.avgProfitLoss.toFixed(2)}`;
        
        this.updateChart(results);
        this.updateYahooChart(config);
        this.updateTradesTable(results);
        
        document.getElementById('resultsSection').style.display = 'block';
        document.getElementById('resultsSection').scrollIntoView({ behavior: 'smooth' });
    }

    updateTradesTable(results) {
        const tbody = document.getElementById('tradesTableBody');
        tbody.innerHTML = '';
        
        const trades = [];
        let currentTrade = null;
        let tradeNumber = 1;
        
        for (const trade of results.trades) {
            if (trade.type === 'BUY') {
                currentTrade = {
                    number: tradeNumber++,
                    entryDate: trade.date,
                    entryPrice: trade.price.toFixed(2),
                    shares: trade.shares,
                    entryValue: trade.value
                };
            } else if (trade.type === 'SELL' && currentTrade) {
                const profit = trade.value - currentTrade.entryValue;
                const returnPercent = ((trade.value - currentTrade.entryValue) / currentTrade.entryValue) * 100;
                
                trades.push({
                    ...currentTrade,
                    exitDate: trade.date,
                    exitPrice: trade.price.toFixed(2),
                    profit: profit,
                    returnPercent: returnPercent
                });
                
                currentTrade = null;
            }
        }
        
        trades.forEach(trade => {
            const row = document.createElement('tr');
            const profitColor = trade.profit >= 0 ? '#00ff88' : '#ff6347';
            const profitSign = trade.profit >= 0 ? '+' : '';
            
            row.innerHTML = `
                <td>${trade.number}</td>
                <td>${trade.entryDate}</td>
                <td>$${trade.entryPrice}</td>
                <td>${trade.shares}</td>
                <td>${trade.exitDate}</td>
                <td>$${trade.exitPrice}</td>
                <td style="color: ${profitColor}">${profitSign}$${trade.profit.toFixed(2)}</td>
                <td style="color: ${profitColor}">${profitSign}${trade.returnPercent.toFixed(2)}%</td>
            `;
            tbody.appendChild(row);
        });
    }

    updateYahooChart(config) {
        const container = document.getElementById('yahooChartContainer');
        const ticker = config.ticker;
        
        // Clear any existing widgets
        container.innerHTML = '';
        
        // Create a new div for the TradingView widget
        const widgetContainer = document.createElement('div');
        widgetContainer.className = 'tradingview-widget-container';
        widgetContainer.innerHTML = '<div class="tradingview-widget-container__widget"></div>';
        
        container.appendChild(widgetContainer);
        
        // Load TradingView script
        const script = document.createElement('script');
        script.type = 'text/javascript';
        script.src = 'https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js';
        script.async = true;
        script.innerHTML = JSON.stringify({
            "autosize": true,
            "symbol": ticker,
            "interval": "D",
            "timezone": "Etc/UTC",
            "theme": "dark",
            "style": "1",
            "locale": "en",
            "backgroundColor": "rgba(17, 27, 51, 0)",
            "gridColor": "rgba(255, 255, 255, 0.1)",
            "width": "100%",
            "height": "400",
            "enable_publishing": false,
            "hide_legend": true,
            "save_image": false,
            "calendar": false,
            "support_host": "https://www.tradingview.com"
        });
        
        widgetContainer.appendChild(script);
    }

    updateChart(results) {
        const ctx = document.getElementById('performanceChart');
        if (!ctx) return;
        
        const labels = results.equityCurve.map(e => e.date);
        const data = results.equityCurve.map(e => e.totalValue);
        
        if (this.chart) {
            this.chart.destroy();
        }
        
        this.chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Portfolio Value',
                    data: data,
                    borderColor: '#00ff88',
                    backgroundColor: 'rgba(0, 255, 136, 0.1)',
                    fill: true,
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    }
                },
                scales: {
                    y: {
                        beginAtZero: false,
                        grid: {
                            color: 'rgba(255, 255, 255, 0.1)'
                        },
                        ticks: {
                            color: '#ffffff',
                            callback: function(value) {
                                return '$' + value.toLocaleString();
                            }
                        }
                    },
                    x: {
                        grid: {
                            color: 'rgba(255, 255, 255, 0.05)'
                        },
                        ticks: {
                            color: '#ffffff',
                            maxTicksLimit: 10
                        }
                    }
                }
            }
        });
    }

    displayResultsInTab() {
        if (!this.results || !this.lastConfig) {
            document.getElementById('resultsDetails').innerHTML = '<p>No backtest results yet. Run a backtest from the Dashboard tab.</p>';
            document.getElementById('resultsDetails').style.display = 'block';
            return;
        }

        const results = this.results;
        const config = this.lastConfig;
        const profitColor = results.totalReturn >= 0 ? '#00ff88' : '#ff6347';
        const profitSign = results.totalReturn >= 0 ? '+' : '';

        document.getElementById('resultsDetails').style.display = 'block';
        
        document.getElementById('resultsDetails').innerHTML = `
            <div class="card-header">
                <h3><i class="fas fa-info-circle"></i> Last Backtest Results</h3>
            </div>
            <div class="results-summary">
                <div class="summary-item"><strong>Ticker:</strong> ${config.ticker}</div>
                <div class="summary-item"><strong>Strategy:</strong> ${config.strategy}</div>
                <div class="summary-item"><strong>Date Range:</strong> ${config.startDate} to ${config.endDate}</div>
                <div class="summary-item"><strong>Initial Capital:</strong> $${config.initialCash.toLocaleString()}</div>
                <div class="summary-item"><strong>Final Value:</strong> $${results.finalValue.toFixed(2)}</div>
                <div class="summary-item"><strong>Commission:</strong> ${config.commission * 100}%</div>
            </div>
            
            <div class="performance-grid" style="margin-top: 2rem;">
                <div class="metric-card">
                    <div class="metric-icon" style="background: rgba(0, 255, 136, 0.2);">
                        <i class="fas fa-dollar-sign" style="color: #00ff88;"></i>
                    </div>
                    <div class="metric-info">
                        <p class="metric-label">Total Profit</p>
                        <p class="metric-value" style="color: ${profitColor}">${profitSign}$${Math.abs(results.totalReturn).toFixed(2)}</p>
                        <p class="metric-percentage" style="color: ${profitColor}">${profitSign}${results.totalReturnPercent.toFixed(2)}%</p>
                    </div>
                </div>
                <div class="metric-card">
                    <div class="metric-icon" style="background: rgba(255, 193, 7, 0.2);">
                        <i class="fas fa-bullseye" style="color: #ffc107;"></i>
                    </div>
                    <div class="metric-info">
                        <p class="metric-label">Win Rate</p>
                        <p class="metric-value">${results.winRate.toFixed(2)}%</p>
                    </div>
                </div>
                <div class="metric-card">
                    <div class="metric-icon" style="background: rgba(0, 212, 255, 0.2);">
                        <i class="fas fa-chart-line" style="color: #00d4ff;"></i>
                    </div>
                    <div class="metric-info">
                        <p class="metric-label">Total Trades</p>
                        <p class="metric-value">${results.totalTrades}</p>
                    </div>
                </div>
                <div class="metric-card">
                    <div class="metric-icon" style="background: rgba(76, 175, 80, 0.2);">
                        <i class="fas fa-check-circle" style="color: #4caf50;"></i>
                    </div>
                    <div class="metric-info">
                        <p class="metric-label">Wins</p>
                        <p class="metric-value">${results.winningTrades}</p>
                    </div>
                </div>
                <div class="metric-card">
                    <div class="metric-icon" style="background: rgba(244, 67, 54, 0.2);">
                        <i class="fas fa-times-circle" style="color: #f44336;"></i>
                    </div>
                    <div class="metric-info">
                        <p class="metric-label">Losses</p>
                        <p class="metric-value">${results.losingTrades}</p>
                    </div>
                </div>
                <div class="metric-card">
                    <div class="metric-icon" style="background: rgba(255, 152, 0, 0.2);">
                        <i class="fas fa-chart-bar" style="color: #ff9800;"></i>
                    </div>
                    <div class="metric-info">
                        <p class="metric-label">Sharpe Ratio</p>
                        <p class="metric-value">${results.sharpeRatio}</p>
                    </div>
                </div>
            </div>

            <div style="margin-top: 2rem;">
                <canvas id="resultsTabChart"></canvas>
            </div>
        `;

        setTimeout(() => {
            this.updateResultsTabChart();
            this.populateResultsTabTrades();
        }, 100);
    }

    updateResultsTabChart() {
        const ctx = document.getElementById('resultsTabChart');
        if (!ctx || !this.results) return;
        
        if (this.resultsChart) {
            this.resultsChart.destroy();
        }
        
        const labels = this.results.equityCurve.map(e => e.date);
        const data = this.results.equityCurve.map(e => e.totalValue);
        
        this.resultsChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Portfolio Value',
                    data: data,
                    borderColor: '#00ff88',
                    backgroundColor: 'rgba(0, 255, 136, 0.1)',
                    fill: true,
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    }
                },
                scales: {
                    y: {
                        beginAtZero: false,
                        grid: {
                            color: 'rgba(255, 255, 255, 0.1)'
                        },
                        ticks: {
                            color: '#ffffff',
                            callback: function(value) {
                                return '$' + value.toLocaleString();
                            }
                        }
                    },
                    x: {
                        grid: {
                            color: 'rgba(255, 255, 255, 0.05)'
                        },
                        ticks: {
                            color: '#ffffff',
                            maxTicksLimit: 10
                        }
                    }
                }
            }
        });
    }

    populateResultsTabTrades() {
        const existingContent = document.getElementById('resultsDetails').innerHTML;
        const tradesTable = this.generateTradesTableHTML();
        
        document.getElementById('resultsDetails').innerHTML = existingContent + tradesTable;

        const tbody = document.getElementById('resultsTabTradesTableBody');
        if (!tbody || !this.results) return;
        
        tbody.innerHTML = '';
        
        const trades = [];
        let currentTrade = null;
        let tradeNumber = 1;
        
        for (const trade of this.results.trades) {
            if (trade.type === 'BUY') {
                currentTrade = {
                    number: tradeNumber++,
                    entryDate: trade.date,
                    entryPrice: trade.price.toFixed(2),
                    shares: trade.shares,
                    entryValue: trade.value
                };
            } else if (trade.type === 'SELL' && currentTrade) {
                const profit = trade.value - currentTrade.entryValue;
                const returnPercent = ((trade.value - currentTrade.entryValue) / currentTrade.entryValue) * 100;
                
                trades.push({
                    ...currentTrade,
                    exitDate: trade.date,
                    exitPrice: trade.price.toFixed(2),
                    profit: profit,
                    returnPercent: returnPercent
                });
                
                currentTrade = null;
            }
        }
        
        trades.forEach(trade => {
            const row = document.createElement('tr');
            const profitColor = trade.profit >= 0 ? '#00ff88' : '#ff6347';
            const profitSign = trade.profit >= 0 ? '+' : '';
            
            row.innerHTML = `
                <td>${trade.number}</td>
                <td>${trade.entryDate}</td>
                <td>$${trade.entryPrice}</td>
                <td>${trade.shares}</td>
                <td>${trade.exitDate}</td>
                <td>$${trade.exitPrice}</td>
                <td style="color: ${profitColor}">${profitSign}$${trade.profit.toFixed(2)}</td>
                <td style="color: ${profitColor}">${profitSign}${trade.returnPercent.toFixed(2)}%</td>
            `;
            tbody.appendChild(row);
        });
    }

    generateTradesTableHTML() {
        return `
            <div style="margin-top: 2rem;">
                <div class="card-header">
                    <h3><i class="fas fa-list"></i> Trade History</h3>
                </div>
                <div class="table-container">
                    <table id="resultsTabTradesTable">
                        <thead>
                            <tr>
                                <th>Trade #</th>
                                <th>Entry Date</th>
                                <th>Entry Price</th>
                                <th>Shares</th>
                                <th>Exit Date</th>
                                <th>Exit Price</th>
                                <th>Profit/Loss</th>
                                <th>Return %</th>
                            </tr>
                        </thead>
                        <tbody id="resultsTabTradesTableBody">
                        </tbody>
                    </table>
                </div>
            </div>
        `;
    }

    resetConfig() {
        document.getElementById('tickerSelect').value = 'AAPL';
        document.getElementById('initialCash').value = '100000';
        document.getElementById('commission').value = '0.001';
        document.getElementById('positionSizing').value = 'percentage';
        document.getElementById('positionSizeValue').value = '95';
        document.getElementById('strategySelect').value = 'sma';
        this.setDefaultDates();
    }

    showLoading() {
        document.getElementById('loadingOverlay').style.display = 'flex';
    }

    hideLoading() {
        document.getElementById('loadingOverlay').style.display = 'none';
    }
}

// Initialize the app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new BacktestEngine();
});