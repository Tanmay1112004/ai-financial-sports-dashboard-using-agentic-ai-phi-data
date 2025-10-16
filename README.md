# 🤖 AI Financial & Sports Dashboard

![Dashboard Preview](https://github.com/Tanmay1112004/ai-financial-sports-dashboard-using-agentic-ai-phi-data/blob/main/ai-financial-sports-dashboard-using-agentic-ai-phi-data/screenshots/Screenshot%202025-10-16%20142900.png)
![Dashboard Preview](https://github.com/Tanmay1112004/ai-financial-sports-dashboard-using-agentic-ai-phi-data/blob/main/ai-financial-sports-dashboard-using-agentic-ai-phi-data/screenshots/Screenshot%202025-10-16%20143043.png)
![Dashboard Preview](https://github.com/Tanmay1112004/ai-financial-sports-dashboard-using-agentic-ai-phi-data/blob/main/ai-financial-sports-dashboard-using-agentic-ai-phi-data/screenshots/Screenshot%202025-10-16%20143402.png)
![Dashboard Preview](https://github.com/Tanmay1112004/ai-financial-sports-dashboard-using-agentic-ai-phi-data/blob/main/ai-financial-sports-dashboard-using-agentic-ai-phi-data/screenshots/Screenshot%202025-10-16%20143147.png)
![Dashboard Preview](https://github.com/Tanmay1112004/ai-financial-sports-dashboard-using-agentic-ai-phi-data/blob/main/ai-financial-sports-dashboard-using-agentic-ai-phi-data/screenshots/Screenshot%202025-10-16%20143537.png)
![Dashboard Preview](https://github.com/Tanmay1112004/ai-financial-sports-dashboard-using-agentic-ai-phi-data/blob/main/ai-financial-sports-dashboard-using-agentic-ai-phi-data/screenshots/Screenshot%202025-10-16%20143701.png)

A comprehensive Streamlit application that combines real-time financial analysis with sports updates in a beautiful, interactive dashboard. Get stock market insights and cricket updates all in one place!

## ✨ Features

### 📈 Financial Analysis
- **Real-time Stock Data**: Live prices from 15+ major companies
- **Interactive Charts**: Beautiful Plotly visualizations
- **Fundamentals Comparison**: P/E ratios, market cap, and volume analysis
- **Multi-Company Analysis**: Compare multiple stocks simultaneously
- **Historical Data**: 1 month to 2 years of price history

### 🏏 Sports Updates
- **Cricket News**: Latest match updates and tournament information
- **Match Schedules**: Upcoming cricket fixtures
- **Player Performance**: Recent statistics and highlights
- **Live Scores**: Real-time match updates (API integration ready)

### 🎨 User Experience
- **Beautiful UI**: Gradient designs and smooth animations
- **Responsive Design**: Works perfectly on all screen sizes
- **Quick Actions**: One-click analysis for common queries
- **Real-time Updates**: Live data refreshing

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Streamlit
- Yahoo Finance API access

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-financial-sports-dashboard.git
   cd ai-financial-sports-dashboard
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:8501`

### Environment Setup (Optional)
Create a `.env` file for API keys (future enhancements):
```env
GROQ_API_KEY=your_groq_key_here
GEMINI_API_KEY=your_gemini_key_here
CRICKET_API_KEY=your_cricket_api_key
```

## 📊 Supported Companies

| Company | Symbol | Sector |
|---------|--------|--------|
| Apple | AAPL | Technology |
| Microsoft | MSFT | Technology |
| Google | GOOGL | Technology |
| Amazon | AMZN | E-commerce |
| Tesla | TSLA | Automotive |
| Nvidia | NVDA | Semiconductor |
| Meta | META | Social Media |
| Netflix | NFLX | Entertainment |
| Infosys | INFY | IT Services |
| IBM | IBM | Technology |
| Intel | INTC | Semiconductor |
| AMD | AMD | Semiconductor |
| Oracle | ORCL | Software |
| Coca Cola | KO | Beverages |
| Walmart | WMT | Retail |

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Data Processing**: Pandas, yFinance
- **Visualization**: Plotly
- **Styling**: Custom CSS
- **Data Sources**: Yahoo Finance API
- **Deployment**: Streamlit Cloud, Heroku, AWS

## 📁 Project Structure

```
ai-financial-sports-dashboard/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── README.md             # Project documentation
├── assets/               # Images and screenshots
└── examples/             # Usage examples
```

## 🎯 Usage Examples

### Stock Analysis
- Compare multiple tech stocks
- Analyze fundamentals and performance
- View interactive price charts

### Market Overview
- Quick insights into market trends
- Sector performance analysis
- Real-time price movements

### Cricket Updates
- Latest match scores
- Tournament schedules
- Player statistics

## 🔧 Configuration

### Adding New Companies
Edit the `COMPANY_SYMBOLS` dictionary in `app.py`:

```python
COMPANY_SYMBOLS = {
    "New Company": "SYMBOL",
    # ... existing companies
}
```

### Customizing Time Periods
Modify the period options in the stock analysis section:

```python
analysis_period = st.selectbox(
    "Time Period:",
    ["1mo", "3mo", "6mo", "1y", "2y", "5y"]  # Added 5y option
)
```

## 🌐 Deployment

### Streamlit Cloud (Recommended)
1. Fork this repository
2. Visit [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your GitHub account
4. Deploy the app from this repository

### Local Deployment
```bash
streamlit run app.py
```

### Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Areas for Contribution
- Additional data sources
- New visualization types
- Enhanced sports coverage
- Mobile app development
- API integrations

## 🐛 Troubleshooting

### Common Issues

1. **Module Not Found Error**
   ```bash
   pip install -r requirements.txt
   ```

2. **Data Fetching Errors**
   - Check internet connection
   - Verify Yahoo Finance API status
   - Try different time periods

3. **Performance Issues**
   - Clear Streamlit cache
   - Reduce number of selected companies
   - Use shorter time periods

### Getting Help
- Open an [issue](https://github.com/yourusername/ai-financial-sports-dashboard/issues)
- Check existing discussions
- Review the documentation

## 📈 Future Enhancements

- [ ] **Real-time Alerts**: Price movement notifications
- [ ] **Portfolio Tracking**: Personal investment tracking
- [ ] **More Sports**: Football, basketball, tennis coverage
- [ ] **Advanced Analytics**: Technical indicators, ML predictions
- [ ] **Mobile App**: React Native/iOS/Android version
- [ ] **API Development**: REST API for data access
- [ ] **User Accounts**: Personalized dashboards
- [ ] **Export Features**: PDF reports, Excel exports

## 🏆 Showcase

### Screenshots
| Stock Analysis | Cricket Updates | Dashboard Overview |
|----------------|-----------------|-------------------|
| ![Stock Analysis](examples/stock-analysis.png) | ![Cricket](examples/cricket-updates.png) | ![Dashboard](examples/dashboard-overview.png) |

### Live Demo
Check out our live deployment: [Live Demo Link](https://your-app.streamlit.app)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Yahoo Finance** for providing free financial data
- **Streamlit** for the amazing framework
- **Plotly** for interactive visualizations
- **yFinance** Python library
- **Contributors** and the open-source community

## 📞 Contact

- **Developer**: Your Name
- **Email**: tanmaykshirsagar001@gmail.com
- **Twitter**: [@yourhandle](https://twitter.com/tanmay)
- **LinkedIn**: [Your Profile](https://linkedin.com/in/tanmay-kshirsagar)

---

<div align="center">

**If you find this project helpful, please give it a ⭐!**

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/ai-financial-sports-dashboard&type=Date)](https://star-history.com/#yourusername/ai-financial-sports-dashboard&Date)

</div>
```

## 📋 Additional Files

### `.env.example`
```env
# API Keys for Enhanced Features
GROQ_API_KEY=your_groq_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
CRICKET_API_KEY=your_cricket_api_key_here
FINNHUB_API_KEY=your_finnhub_key_here

# Application Settings
DEBUG_MODE=False
CACHE_DURATION=300
```

### `.gitignore`
```gitignore
# Environment variables
.env
.env.local

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Streamlit
.streamlit/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log
logs/

# Data
data/
*.csv
*.json
*.xlsx
```



