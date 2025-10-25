# Stock Volume Data Tracker

A modern, responsive web application for tracking and analyzing stock volume data with advanced filtering capabilities.

## Features

### 🔍 Stock Search
- Search for any stock ticker (e.g., AAPL, MSFT, GOOGL)
- Real-time data fetching with loading indicators
- Suggested popular tickers for easy access

### 📊 Volume Data Display
- Comprehensive table showing:
  - Date and time of transactions
  - Transaction type (Buy/Sell)
  - Volume (number of shares)
  - Price per share
  - Total transaction value

### 🔧 Advanced Filtering
- **Date Range Filtering**
  - Set custom start and end dates
  - Defaults to last 30 days
  - Real-time filtering

- **Dollar Amount Filtering**
  - Filter by minimum transaction value
  - Remove smaller transactions from view
  - All amounts displayed in USD

- **Transaction Type Filtering**
  - View all transactions
  - Filter to show only buy orders
  - Filter to show only sell orders

### 📈 Statistics Dashboard
- Total number of transactions
- Total volume across all transactions
- Total dollar value
- Breakdown of buy vs sell transactions

## How to Use

1. **Search for a Stock**
   - Enter a stock ticker in the search box (e.g., AAPL, MSFT, GOOGL)
   - Click the search button or press Enter
   - Wait for the data to load

2. **Apply Filters**
   - Set date range using the "From Date" and "To Date" fields
   - Enter minimum dollar amount to filter out smaller transactions
   - Select transaction type (All, Buy, or Sell)
   - Click "Apply Filters" to update the results

3. **Clear Filters**
   - Click "Clear Filters" to reset all filter settings
   - This will show all available data for the current ticker

4. **View Results**
   - Results are displayed in a sortable table
   - Statistics are shown above the table
   - Hover over rows for better visibility

## Technical Details

### Mock Data Generation
The application generates realistic mock data for demonstration purposes:
- Random transaction volumes (100-10,100 shares)
- Realistic price variations based on ticker
- Multiple transactions per day (5-25)
- Trading hours simulation (9 AM - 5 PM)

### Supported Tickers
The application includes base price data for popular stocks:
- AAPL (Apple) - ~$150
- MSFT (Microsoft) - ~$300
- GOOGL (Google) - ~$2,500
- AMZN (Amazon) - ~$3,000
- TSLA (Tesla) - ~$200
- META (Meta) - ~$300
- NVDA (NVIDIA) - ~$400
- NFLX (Netflix) - ~$400

### Responsive Design
- Mobile-friendly interface
- Adaptive table layout
- Touch-friendly controls
- Optimized for all screen sizes

## File Structure

```
stock-volume-tracker/
├── index.html          # Main HTML structure
├── styles.css          # CSS styling and responsive design
├── script.js           # JavaScript functionality
└── README.md           # This documentation
```

## Browser Compatibility

- Chrome (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers

## Future Enhancements

- Real API integration (Alpha Vantage, Yahoo Finance, etc.)
- Export functionality (CSV, PDF)
- Chart visualizations
- Historical price data
- Portfolio tracking
- Alert system for volume spikes

## Getting Started

1. Open `index.html` in your web browser
2. Enter a stock ticker to search
3. Use the filters to customize your view
4. Analyze the volume data and statistics

Enjoy exploring stock volume data with this powerful and intuitive tool!
