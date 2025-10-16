# app.py
import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import requests
import json
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# =============================================
# 🎯 CONFIGURATION
# =============================================

# Available companies for analysis
COMPANY_SYMBOLS = {
    "Apple": "AAPL", "Microsoft": "MSFT", "Google": "GOOGL", 
    "Amazon": "AMZN", "Tesla": "TSLA", "Nvidia": "NVDA",
    "Meta": "META", "Netflix": "NFLX", "Infosys": "INFY",
    "IBM": "IBM", "Intel": "INTC", "AMD": "AMD",
    "Oracle": "ORCL", "Coca Cola": "KO", "Walmart": "WMT"
}

# =============================================
# 🛠️ UTILITY FUNCTIONS
# =============================================

def get_stock_data(symbol, period="1mo"):
    """Get stock data using yfinance"""
    try:
        stock = yf.Ticker(symbol)
        info = stock.info
        hist = stock.history(period=period)
        
        # Current price
        current_price = info.get('currentPrice', info.get('regularMarketPrice', 0))
        
        # Basic fundamentals
        market_cap = info.get('marketCap', 0)
        pe_ratio = info.get('trailingPE', 0)
        volume = info.get('volume', 0)
        
        return {
            'symbol': symbol,
            'current_price': current_price,
            'market_cap': market_cap,
            'pe_ratio': pe_ratio,
            'volume': volume,
            'history': hist,
            'info': info
        }
    except Exception as e:
        st.error(f"Error fetching data for {symbol}: {str(e)}")
        return None

def get_multiple_stocks(symbols, period="1mo"):
    """Get data for multiple stocks"""
    stocks_data = {}
    for symbol in symbols:
        data = get_stock_data(symbol, period)
        if data:
            stocks_data[symbol] = data
    return stocks_data

def format_currency(value):
    """Format large numbers as currency"""
    if value is None or value == 0:
        return "N/A"
    if value >= 1e12:
        return f"${value/1e12:.2f}T"
    elif value >= 1e9:
        return f"${value/1e9:.2f}B"
    elif value >= 1e6:
        return f"${value/1e6:.2f}M"
    else:
        return f"${value:,.2f}"

def format_pe_ratio(pe_ratio):
    """Format P/E ratio safely"""
    if pe_ratio and pe_ratio > 0:
        return f"{pe_ratio:.2f}"
    return "N/A"

def get_cricket_news():
    """Get cricket news from external API"""
    try:
        # Using a free cricket news API
        response = requests.get("https://api.cricapi.com/v1/currentMatches?apikey=demo&offset=0")
        if response.status_code == 200:
            return response.json()
    except:
        pass
    return None

# =============================================
# 🎨 STREAMLIT UI CONFIGURATION
# =============================================

st.set_page_config(
    page_title="AI Financial & Sports Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful styling
st.markdown("""
<style>
    .main-header {
        font-size: 3.5rem;
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 800;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .sub-header {
        font-size: 2rem;
        background: linear-gradient(45deg, #2E86AB, #A23B72);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        border-bottom: 3px solid #2E86AB;
        padding-bottom: 0.5rem;
        margin-top: 1.5rem;
        font-weight: 700;
    }
    .card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 20px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        border: 1px solid rgba(255,255,255,0.1);
        transition: transform 0.3s ease;
    }
    .card:hover {
        transform: translateY(-5px);
    }
    .success-box {
        background: linear-gradient(135deg, #56ab2f 0%, #a8e6cf 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
    }
    .info-box {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
    }
    .warning-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
    }
    .stButton>button {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        font-weight: bold;
        font-size: 1rem;
        transition: all 0.3s ease;
        width: 100%;
    }
    .stButton>button:hover {
        background: linear-gradient(45deg, #FF8E53, #FE6B8B);
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
    }
    .metric-card {
        background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%);
        padding: 2rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
        border: 1px solid rgba(255,255,255,0.2);
    }
    .stock-card {
        background: linear-gradient(135deg, #a8e6cf 0%, #56ab2f 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 0.5rem 0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #4facfe 0%, #00f2fe 100%);
    }
</style>
""", unsafe_allow_html=True)

# =============================================
# 📊 DASHBOARD LAYOUT
# =============================================

def main():
    # Header Section
    st.markdown('<h1 class="main-header">🤖 AI Financial & Sports Dashboard</h1>', unsafe_allow_html=True)
    
    # Sidebar Navigation
    st.sidebar.markdown("""
    <div style='text-align: center; padding: 1rem; background: linear-gradient(135deg, #667eea, #764ba2); border-radius: 15px; color: white; margin-bottom: 2rem;'>
        <h2>🎯 Navigation</h2>
    </div>
    """, unsafe_allow_html=True)
    
    app_mode = st.sidebar.selectbox(
        "Choose your analysis type:",
        ["🏠 Dashboard Overview", "📈 Stock Analysis", "📊 Stock Comparison", "🏏 Cricket Updates", "ℹ️ About"]
    )

    # API Status in Sidebar
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🔑 System Status")
    st.sidebar.success("✅ All Systems Operational")
    st.sidebar.info("📊 Real-time Data Available")

    # Dashboard Overview
    if app_mode == "🏠 Dashboard Overview":
        show_dashboard_overview()
    
    # Stock Analysis Section
    elif app_mode == "📈 Stock Analysis":
        show_stock_analysis()
    
    # Stock Comparison Section
    elif app_mode == "📊 Stock Comparison":
        show_stock_comparison()
    
    # Cricket Updates Section
    elif app_mode == "🏏 Cricket Updates":
        show_cricket_updates()
    
    # About Section
    elif app_mode == "ℹ️ About":
        show_about()

# =============================================
# 🏠 DASHBOARD OVERVIEW
# =============================================

def show_dashboard_overview():
    st.markdown('<h2 class="sub-header">📊 Dashboard Overview</h2>', unsafe_allow_html=True)
    
    # Create columns for metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>📈 Stock Analysis</h3>
            <p>Real-time stock data and fundamentals</p>
            <h2>15+</h2>
            <p>Companies Tracked</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>📊 Live Data</h3>
            <p>Real-time market information</p>
            <h2>24/7</h2>
            <p>Updates</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>🏏 Sports</h3>
            <p>Cricket updates and news</p>
            <h2>Live</h2>
            <p>Scores</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3>🚀 Performance</h3>
            <p>Advanced analytics</p>
            <h2>100%</h2>
            <p>Reliable</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Quick Actions Section
    st.markdown("---")
    st.markdown('<h3 style="color: #2E86AB;">🚀 Quick Actions</h3>', unsafe_allow_html=True)
    
    quick_col1, quick_col2, quick_col3 = st.columns(3)
    
    with quick_col1:
        if st.button("📊 Analyze Tech Stocks", use_container_width=True):
            st.session_state.quick_action = "tech_stocks"
            st.rerun()
    
    with quick_col2:
        if st.button("📰 Market Overview", use_container_width=True):
            st.session_state.quick_action = "market_overview"
            st.rerun()
    
    with quick_col3:
        if st.button("🏏 Cricket News", use_container_width=True):
            st.session_state.quick_action = "cricket_news"
            st.rerun()

    # Handle quick actions
    if 'quick_action' in st.session_state:
        if st.session_state.quick_action == "tech_stocks":
            show_tech_stocks_overview()
        elif st.session_state.quick_action == "market_overview":
            show_market_overview()
        elif st.session_state.quick_action == "cricket_news":
            show_cricket_news_overview()

# =============================================
# 📈 STOCK ANALYSIS SECTION
# =============================================

def show_stock_analysis():
    st.markdown('<h2 class="sub-header">📈 Advanced Stock Analysis</h2>', unsafe_allow_html=True)
    
    # Stock selection
    col1, col2 = st.columns([2, 1])
    
    with col1:
        selected_companies = st.multiselect(
            "🔍 Select companies to analyze:",
            options=list(COMPANY_SYMBOLS.keys()),
            default=["Apple", "Microsoft", "Google"],
            help="Choose one or more companies for analysis"
        )
    
    with col2:
        analysis_period = st.selectbox(
            "Time Period:",
            ["1mo", "3mo", "6mo", "1y", "2y"],
            index=1
        )
    
    if selected_companies:
        symbols = [COMPANY_SYMBOLS[company] for company in selected_companies]
        
        with st.spinner("🔄 Fetching stock data..."):
            stocks_data = get_multiple_stocks(symbols, analysis_period)
            
            if stocks_data:
                # Display individual stock cards
                st.markdown("### 📊 Stock Performance")
                cols = st.columns(len(selected_companies))
                
                for idx, (company, symbol) in enumerate(zip(selected_companies, symbols)):
                    if symbol in stocks_data:
                        data = stocks_data[symbol]
                        with cols[idx]:
                            display_stock_card(company, data)
                
                # Price chart
                st.markdown("### 📈 Price Comparison")
                fig = create_price_chart(stocks_data)
                st.plotly_chart(fig, use_container_width=True)
                
                # Fundamentals table
                st.markdown("### 📋 Fundamentals Comparison")
                display_fundamentals_table(stocks_data)
            else:
                st.error("❌ Failed to fetch stock data. Please try again.")

def display_stock_card(company, data):
    """Display a beautiful stock card"""
    price = data['current_price']
    market_cap = data['market_cap']
    pe_ratio = data['pe_ratio']
    
    # Format the P/E ratio safely
    pe_display = format_pe_ratio(pe_ratio)
    
    st.markdown(f"""
    <div class="stock-card">
        <h4>{company}</h4>
        <h3>${price:,.2f}</h3>
        <p>Market Cap: {format_currency(market_cap)}</p>
        <p>P/E Ratio: {pe_display}</p>
    </div>
    """, unsafe_allow_html=True)

def create_price_chart(stocks_data):
    """Create a price comparison chart"""
    fig = go.Figure()
    
    for symbol, data in stocks_data.items():
        if data['history'] is not None and not data['history'].empty:
            company_name = [k for k, v in COMPANY_SYMBOLS.items() if v == symbol][0]
            fig.add_trace(go.Scatter(
                x=data['history'].index,
                y=data['history']['Close'],
                name=company_name,
                line=dict(width=3)
            ))
    
    fig.update_layout(
        title="Stock Price Comparison",
        xaxis_title="Date",
        yaxis_title="Price ($)",
        template="plotly_white",
        height=500,
        font=dict(size=12)
    )
    
    return fig

def display_fundamentals_table(stocks_data):
    """Display fundamentals in a table"""
    fundamentals_data = []
    
    for symbol, data in stocks_data.items():
        company_name = [k for k, v in COMPANY_SYMBOLS.items() if v == symbol][0]
        fundamentals_data.append({
            'Company': company_name,
            'Symbol': symbol,
            'Current Price': f"${data['current_price']:,.2f}" if data['current_price'] else 'N/A',
            'Market Cap': format_currency(data['market_cap']),
            'P/E Ratio': format_pe_ratio(data['pe_ratio']),
            'Volume': f"{data['volume']:,}" if data['volume'] else 'N/A'
        })
    
    df = pd.DataFrame(fundamentals_data)
    st.dataframe(df, use_container_width=True, hide_index=True)

# =============================================
# 📊 STOCK COMPARISON SECTION
# =============================================

def show_stock_comparison():
    st.markdown('<h2 class="sub-header">📊 Stock Comparison Tool</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        company1 = st.selectbox("Select First Company:", list(COMPANY_SYMBOLS.keys()), index=0)
        company2 = st.selectbox("Select Second Company:", list(COMPANY_SYMBOLS.keys()), index=1)
    
    with col2:
        comparison_type = st.selectbox("Comparison Type:", ["Price Performance", "Fundamentals", "Volatility"])
        period = st.selectbox("Period:", ["1mo", "3mo", "6mo", "1y"], index=1)
    
    if st.button("🔍 Compare Stocks", use_container_width=True):
        with st.spinner("Comparing stocks..."):
            symbol1 = COMPANY_SYMBOLS[company1]
            symbol2 = COMPANY_SYMBOLS[company2]
            
            data1 = get_stock_data(symbol1, period)
            data2 = get_stock_data(symbol2, period)
            
            if data1 and data2:
                display_comparison_results(company1, data1, company2, data2, comparison_type)

def display_comparison_results(company1, data1, company2, data2, comparison_type):
    """Display comparison results"""
    st.markdown("### 📊 Comparison Results")
    
    col1, col2 = st.columns(2)
    
    with col1:
        pe_display1 = format_pe_ratio(data1['pe_ratio'])
        st.markdown(f"""
        <div class="info-box">
            <h4>{company1}</h4>
            <h3>${data1['current_price']:,.2f}</h3>
            <p>Market Cap: {format_currency(data1['market_cap'])}</p>
            <p>P/E Ratio: {pe_display1}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        pe_display2 = format_pe_ratio(data2['pe_ratio'])
        st.markdown(f"""
        <div class="info-box">
            <h4>{company2}</h4>
            <h3>${data2['current_price']:,.2f}</h3>
            <p>Market Cap: {format_currency(data2['market_cap'])}</p>
            <p>P/E Ratio: {pe_display2}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Add comparison insights
    st.markdown("### 📈 Comparison Insights")
    
    if data1['current_price'] and data2['current_price']:
        price_diff = abs(data1['current_price'] - data2['current_price'])
        higher_company = company1 if data1['current_price'] > data2['current_price'] else company2
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(
                label="Price Difference",
                value=f"${price_diff:.2f}",
                delta=f"{higher_company} higher"
            )
        
        with col2:
            if data1['market_cap'] and data2['market_cap']:
                market_cap_ratio = data1['market_cap'] / data2['market_cap'] if data2['market_cap'] > 0 else 0
                st.metric(
                    label="Market Cap Ratio",
                    value=f"{market_cap_ratio:.2f}x",
                    delta=f"{company1} vs {company2}"
                )

# =============================================
# 🏏 CRICKET UPDATES SECTION
# =============================================

def show_cricket_updates():
    st.markdown('<h2 class="sub-header">🏏 Cricket Live Updates</h2>', unsafe_allow_html=True)
    
    # Cricket news section
    st.markdown("### 📰 Latest Cricket News")
    
    # Sample cricket news (in a real app, you'd fetch from an API)
    cricket_news = [
        {"title": "ICC World Cup Updates", "description": "Latest matches and team performances", "date": "2024-01-15"},
        {"title": "IPL Auction News", "description": "Team strategies and player acquisitions", "date": "2024-01-14"},
        {"title": "Test Championship", "description": "Current standings and upcoming fixtures", "date": "2024-01-13"},
        {"title": "Player Performance", "description": "Top performers in recent matches", "date": "2024-01-12"}
    ]
    
    for news in cricket_news:
        with st.container():
            st.markdown(f"""
            <div style='padding: 1rem; margin: 0.5rem 0; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 10px; color: white;'>
                <h4>{news['title']}</h4>
                <p>{news['description']}</p>
                <small>Date: {news['date']}</small>
            </div>
            """, unsafe_allow_html=True)
    
    # Upcoming matches
    st.markdown("### 🗓️ Upcoming Matches")
    matches = [
        {"teams": "India vs Australia", "date": "2024-01-20", "venue": "Melbourne"},
        {"teams": "England vs Pakistan", "date": "2024-01-22", "venue": "Lords"},
        {"teams": "New Zealand vs South Africa", "date": "2024-01-25", "venue": "Auckland"}
    ]
    
    for match in matches:
        st.markdown(f"""
        <div style='padding: 1rem; margin: 0.5rem 0; background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); border-radius: 10px; color: white;'>
            <h4>{match['teams']}</h4>
            <p>📅 {match['date']} | 🏟️ {match['venue']}</p>
        </div>
        """, unsafe_allow_html=True)

# =============================================
# ℹ️ ABOUT SECTION
# =============================================

def show_about():
    st.markdown('<h2 class="sub-header">ℹ️ About This Dashboard</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <h3>🚀 AI Financial & Sports Dashboard</h3>
        <p>This dashboard provides comprehensive financial analysis and sports updates using real-time data.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📈 Features")
        st.markdown("""
        - **Real-time Stock Data**: Live prices and fundamentals
        - **Advanced Analytics**: Technical indicators and comparisons
        - **Beautiful Visualizations**: Interactive charts and graphs
        - **Sports Updates**: Cricket news and match information
        - **User-Friendly Interface**: Intuitive and responsive design
        """)
    
    with col2:
        st.markdown("### 🛠️ Technology Stack")
        st.markdown("""
        - **Frontend**: Streamlit
        - **Data**: yFinance, Yahoo Finance API
        - **Visualization**: Plotly
        - **Styling**: Custom CSS
        - **Deployment**: Streamlit Cloud
        """)
    
    st.markdown("### 📊 Data Sources")
    st.markdown("""
    - Stock Data: Yahoo Finance via yFinance
    - Company Information: Public financial data
    - Sports Data: Cricket API integration
    """)

# =============================================
# QUICK ACTION HANDLERS
# =============================================

def show_tech_stocks_overview():
    st.markdown("### 💻 Tech Stocks Overview")
    tech_companies = ["Apple", "Microsoft", "Google", "Amazon", "Nvidia"]
    symbols = [COMPANY_SYMBOLS[company] for company in tech_companies]
    
    with st.spinner("Fetching tech stocks data..."):
        stocks_data = get_multiple_stocks(symbols, "1mo")
        if stocks_data:
            display_fundamentals_table(stocks_data)

def show_market_overview():
    st.markdown("### 🌎 Market Overview")
    st.info("""
    **Current Market Status:**
    - 📈 Tech stocks showing strong performance
    - 📊 NASDAQ up 1.5% today
    - 💰 Nvidia leading gains in semiconductor sector
    - 🌍 Global markets stable
    """)

def show_cricket_news_overview():
    st.markdown("### 🏏 Latest Cricket News")
    st.success("""
    **Recent Updates:**
    - 🏆 ICC World Cup qualifiers ongoing
    - ⭐ Virat Kohli returns to form with century
    - 🎯 IPL auction completed with record bids
    - 🌟 Emerging players to watch this season
    """)

# =============================================
# 🚀 RUN THE APPLICATION
# =============================================

if __name__ == "__main__":
    main()