// Stock Volume Data Tracker JavaScript

class StockVolumeTracker {
    constructor() {
        this.currentData = [];
        this.filteredData = [];
        this.currentTicker = '';
        this.initializeEventListeners();
        this.setDefaultDates();
    }

    initializeEventListeners() {
        // Search functionality
        document.getElementById('searchBtn').addEventListener('click', () => this.searchStock());
        document.getElementById('tickerInput').addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.searchStock();
        });

        // Filter functionality
        document.getElementById('applyFilters').addEventListener('click', () => this.applyFilters());
        document.getElementById('clearFilters').addEventListener('click', () => this.clearFilters());
    }

    setDefaultDates() {
        const today = new Date();
        const thirtyDaysAgo = new Date(today.getTime() - (30 * 24 * 60 * 60 * 1000));
        
        document.getElementById('dateFrom').value = thirtyDaysAgo.toISOString().split('T')[0];
        document.getElementById('dateTo').value = today.toISOString().split('T')[0];
    }

    async searchStock() {
        const ticker = document.getElementById('tickerInput').value.trim().toUpperCase();
        
        if (!ticker) {
            this.showError('Please enter a stock ticker');
            return;
        }

        this.currentTicker = ticker;
        this.showLoading(true);
        
        try {
            // Simulate API call with mock data
            const data = await this.fetchStockData(ticker);
            this.currentData = data;
            this.applyFilters();
            this.showLoading(false);
        } catch (error) {
            this.showError('Failed to fetch data for ' + ticker);
            this.showLoading(false);
        }
    }

    async fetchStockData(ticker) {
        // Simulate API delay
        await new Promise(resolve => setTimeout(resolve, 1000));
        
        // Generate mock volume data
        const data = [];
        const startDate = new Date(document.getElementById('dateFrom').value);
        const endDate = new Date(document.getElementById('dateTo').value);
        
        // Generate data for each day in the range
        for (let d = new Date(startDate); d <= endDate; d.setDate(d.getDate() + 1)) {
            const transactionsPerDay = Math.floor(Math.random() * 20) + 5; // 5-25 transactions per day
            
            for (let i = 0; i < transactionsPerDay; i++) {
                const time = new Date(d);
                time.setHours(Math.floor(Math.random() * 9) + 9); // 9 AM to 5 PM
                time.setMinutes(Math.floor(Math.random() * 60));
                time.setSeconds(Math.floor(Math.random() * 60));
                
                const volume = Math.floor(Math.random() * 10000) + 100; // 100-10100 shares
                const price = this.getRandomPrice(ticker);
                const transactionType = Math.random() > 0.5 ? 'buy' : 'sell';
                
                data.push({
                    date: d.toISOString().split('T')[0],
                    time: time.toLocaleTimeString('en-US', { 
                        hour: '2-digit', 
                        minute: '2-digit',
                        hour12: true 
                    }),
                    transactionType: transactionType,
                    volume: volume,
                    price: price,
                    totalValue: volume * price
                });
            }
        }
        
        return data.sort((a, b) => new Date(b.date + ' ' + b.time) - new Date(a.date + ' ' + a.time));
    }

    getRandomPrice(ticker) {
        // Base prices for different tickers
        const basePrices = {
            'AAPL': 150,
            'MSFT': 300,
            'GOOGL': 2500,
            'AMZN': 3000,
            'TSLA': 200,
            'META': 300,
            'NVDA': 400,
            'NFLX': 400
        };
        
        const basePrice = basePrices[ticker] || 100;
        const variation = basePrice * 0.1; // 10% variation
        return parseFloat((basePrice + (Math.random() - 0.5) * variation).toFixed(2));
    }

    applyFilters() {
        if (this.currentData.length === 0) return;

        const dateFrom = document.getElementById('dateFrom').value;
        const dateTo = document.getElementById('dateTo').value;
        const minAmount = parseFloat(document.getElementById('minAmount').value) || 0;
        const transactionType = document.getElementById('transactionType').value;

        this.filteredData = this.currentData.filter(item => {
            // Date filter
            if (dateFrom && item.date < dateFrom) return false;
            if (dateTo && item.date > dateTo) return false;
            
            // Amount filter
            if (item.totalValue < minAmount) return false;
            
            // Transaction type filter
            if (transactionType !== 'all' && item.transactionType !== transactionType) return false;
            
            return true;
        });

        this.displayResults();
    }

    clearFilters() {
        document.getElementById('dateFrom').value = '';
        document.getElementById('dateTo').value = '';
        document.getElementById('minAmount').value = '';
        document.getElementById('transactionType').value = 'all';
        
        if (this.currentData.length > 0) {
            this.filteredData = [...this.currentData];
            this.displayResults();
        }
    }

    displayResults() {
        const table = document.getElementById('volumeTable');
        const tableBody = document.getElementById('volumeTableBody');
        const resultsTitle = document.getElementById('resultsTitle');
        const resultsStats = document.getElementById('resultsStats');
        const noResults = document.getElementById('noResults');

        if (this.filteredData.length === 0) {
            table.style.display = 'none';
            noResults.style.display = 'block';
            resultsTitle.textContent = 'No data found';
            resultsStats.textContent = '';
            return;
        }

        table.style.display = 'table';
        noResults.style.display = 'none';

        // Update title and stats
        resultsTitle.textContent = `${this.currentTicker} Volume Data`;
        
        const totalVolume = this.filteredData.reduce((sum, item) => sum + item.volume, 0);
        const totalValue = this.filteredData.reduce((sum, item) => sum + item.totalValue, 0);
        const buyTransactions = this.filteredData.filter(item => item.transactionType === 'buy').length;
        const sellTransactions = this.filteredData.filter(item => item.transactionType === 'sell').length;
        
        resultsStats.innerHTML = `
            <strong>${this.filteredData.length}</strong> transactions | 
            <strong>${totalVolume.toLocaleString()}</strong> total volume | 
            <strong>$${totalValue.toLocaleString()}</strong> total value | 
            <span style="color: #28a745;"><strong>${buyTransactions}</strong> buys</span> | 
            <span style="color: #dc3545;"><strong>${sellTransactions}</strong> sells</span>
        `;

        // Populate table
        tableBody.innerHTML = '';
        this.filteredData.forEach(item => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${item.date}</td>
                <td>${item.time}</td>
                <td><span class="transaction-${item.transactionType}">${item.transactionType.toUpperCase()}</span></td>
                <td>${item.volume.toLocaleString()}</td>
                <td>$${item.price.toFixed(2)}</td>
                <td>$${item.totalValue.toLocaleString()}</td>
            `;
            tableBody.appendChild(row);
        });
    }

    showLoading(show) {
        const loading = document.getElementById('loading');
        const table = document.getElementById('volumeTable');
        const noResults = document.getElementById('noResults');
        
        if (show) {
            loading.style.display = 'block';
            table.style.display = 'none';
            noResults.style.display = 'none';
        } else {
            loading.style.display = 'none';
        }
    }

    showError(message) {
        const resultsTitle = document.getElementById('resultsTitle');
        const resultsStats = document.getElementById('resultsStats');
        const table = document.getElementById('volumeTable');
        const noResults = document.getElementById('noResults');
        
        resultsTitle.textContent = message;
        resultsStats.textContent = '';
        table.style.display = 'none';
        noResults.style.display = 'none';
    }
}

// Initialize the application when the page loads
document.addEventListener('DOMContentLoaded', () => {
    new StockVolumeTracker();
});

// Add some sample data suggestions
document.addEventListener('DOMContentLoaded', () => {
    const tickerInput = document.getElementById('tickerInput');
    const suggestions = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'META', 'NVDA', 'NFLX'];
    
    tickerInput.addEventListener('focus', () => {
        if (!tickerInput.value) {
            tickerInput.placeholder = `Try: ${suggestions.join(', ')}`;
        }
    });
    
    tickerInput.addEventListener('blur', () => {
        if (!tickerInput.value) {
            tickerInput.placeholder = 'Enter stock ticker (e.g., AAPL, MSFT, GOOGL)';
        }
    });
});
