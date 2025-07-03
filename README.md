# FinSight - AI-Powered Expense Tracker & Investment Advisor

FinSight is a comprehensive financial management application that combines expense tracking with AI-powered financial advice and stock investment recommendations. Built with Python, it leverages Google's Gemini AI and real-time stock market data to provide personalized financial insights.

## 🚀 Features

### Core Functionality
- **Expense Tracking**: Log and categorize your daily expenses with date tracking
- **AI Financial Advisor**: Get personalized budget recommendations using Google Gemini AI
- **Stock Investment Suggestions**: Receive real-time stock recommendations based on your budget
- **Interactive CLI**: User-friendly command-line interface for easy navigation

### AI Integration
- **Gemini AI Integration**: Uses Google's Gemini 1.5 Flash model for financial advice
- **Smart Budget Analysis**: Analyzes your income, expenses, and provides spending recommendations
- **Investment Amount Extraction**: Automatically extracts recommended investment amounts from AI responses

### Stock Market Integration
- **Real-time Stock Data**: Fetches live stock data from Financial Modeling Prep API
- **Biggest Gainers Analysis**: Identifies top-performing stocks within your budget
- **Formatted Stock Display**: Clean, tabular display of stock information

## 📋 Prerequisites

- Python 3.11 or higher
- Google Gemini API key
- Financial Modeling Prep API key

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd expense-tracker
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API keys**:
   - Get a Google Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Get a Financial Modeling Prep API key from [Financial Modeling Prep](https://financialmodelingprep.com/developer/docs/)

4. **Update API keys** in the code:
   - Replace the Gemini API key in `tracker.py` (line 9)
   - Replace the Financial Modeling Prep API key in `investment.py` (line 58)

## 🎯 Usage

### Starting the Application
```bash
python tracker.py
```

### Main Menu Options

1. **Log Expense**: Add new expenses with category, amount, and date
2. **Get Gemini Recommendation**: Receive AI-powered financial advice based on your income and expenses
3. **Recommended Stock**: View top 5 stock investment options within your budget
4. **Show Table**: Display all logged expenses in a formatted table
5. **Exit**: Close the application

### Workflow Example

1. **Log your expenses** (Option 1) - Track your spending habits
2. **Get financial advice** (Option 2) - Enter your monthly income and receive AI recommendations
3. **View investment options** (Option 3) - See stock recommendations based on your budget
4. **Review your expenses** (Option 4) - Check your spending history

## 🏗️ Project Structure

```
expense-tracker/
├── tracker.py              # Main application file with CLI interface
├── investment.py           # Stock market integration and data processing
├── test_investment.py      # Unit tests for investment functionality
├── requirements.txt        # Python dependencies
├── expenses.db            # SQLite database for expense storage
├── .github/workflows/     # GitHub Actions for code style checking
└── README.md              # This file
```

## 🔧 Technical Details

### Database Schema
- **Table**: `expenses`
- **Columns**: `category` (TEXT), `amount` (TEXT), `date` (TEXT)

### Key Components

#### `tracker.py`
- Main application logic and CLI interface
- SQLite database management
- Gemini AI integration for financial advice
- Expense logging and retrieval

#### `investment.py`
- `Investment` class for stock market operations
- Real-time stock data fetching
- Stock filtering and formatting
- `extract_amount()` function for parsing AI responses

### API Integrations

#### Google Gemini AI
- **Model**: gemini-1.5-flash
- **Purpose**: Financial advice and budget recommendations
- **System Prompt**: Financial advisor role with thoughtful recommendations

#### Financial Modeling Prep
- **Endpoint**: Biggest gainers API
- **Purpose**: Real-time stock market data
- **Data**: Stock prices, symbols, names, and percentage changes

## 🧪 Testing

Run the test suite to verify functionality:
```bash
python test_investment.py
```

### Test Coverage
- Investment data processing
- Stock information formatting
- Gemini AI integration
- Amount extraction from AI responses

## 🔍 Code Quality

The project includes automated code style checking via GitHub Actions:
- **Tool**: pycodestyle
- **Max line length**: 79 characters
- **Trigger**: On every push to the repository

## 📊 Example Output

### Expense Table
```
category | amount | date
Food | 25.50 | 2024-01-15
Transport | 15.00 | 2024-01-15
```

### Stock Recommendations
```
Company                             Ticker     Price      Change Percent
Apple Inc.                          AAPL       150.25     5.20
Microsoft Corporation               MSFT       280.10     3.15
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Ensure code passes style checks
5. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## ⚠️ Disclaimer

This application is for educational and personal use only. Investment recommendations should not be considered as financial advice. Always consult with a qualified financial advisor before making investment decisions.

## 🆘 Support

For issues or questions:
1. Check the existing issues in the repository
2. Create a new issue with detailed information
3. Include error messages and steps to reproduce

---

**FinSight** - Making financial management smarter with AI! 💰🤖
