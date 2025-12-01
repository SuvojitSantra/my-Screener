import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Set Page Config
st.set_page_config(
    page_title="MarketPro Guide",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1e293b;
    }
    .sub-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #475569;
    }
    .metric-card {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("MarketPro Guide")
    st.caption("Screener.in Mastery & Tools")
    
    selected_page = st.radio(
        "Navigate",
        ["Overview & Basics", "Find Multibaggers", "Swing Trading Setup", "Run Live Screener", "Best Alternatives"]
    )
    
    st.divider()
    st.info("**Pro Tip:** Always cross-verify data with annual reports.")

# --- DATA FUNCTIONS ---
@st.cache_data
def get_stock_data(tickers, period="1y"):
    """Fetches stock data for a list of tickers."""
    data = {}
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker + ".NS") # Appending .NS for NSE
            hist = stock.history(period=period)
            info = stock.info
            if not hist.empty:
                data[ticker] = {
                    "history": hist,
                    "info": info
                }
        except Exception as e:
            continue
    return data

# Sample list of popular stocks for the screener demo
SAMPLE_TICKERS = [
    "RELIANCE", "TCS", "HDFCBANK", "INFY", "ITC", "BAJFINANCE", "LT", "ASIANPAINT", 
    "TITAN", "TATAMOTORS", "SUNPHARMA", "NTPC", "POWERGRID", "TATASTEEL", "COALINDIA",
    "SBIN", "ICICIBANK", "BHARTIARTL", "HCLTECH", "KOTAKBANK", "WIPRO", "ULTRACEMCO",
    "MARUTI", "AXISBANK", "ONGC"
]

# --- PAGES ---

if selected_page == "Overview & Basics":
    st.markdown('<div class="main-header">Mastering Stock Screening in India</div>', unsafe_allow_html=True)
    st.write("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **Screener.in** is the gold standard for fundamental analysis in the Indian stock market. 
        While it excels at finding long-term compounders ("Multibaggers"), it requires specific queries to unlock its potential.
        
        This guide bridges the gap between raw data and actionable insights.
        """)
        
        st.subheader("The Screening Workflow")
        st.markdown("""
        1.  **Define Strategy**: Decide if you want Growth, Value, or Swing trades.
        2.  **Run Query**: Input strict criteria filters.
        3.  **Analyze Results**: Manually verify the list.
        """)

    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>Primary Goal</h3>
            <p style="font-size: 1.2rem; font-weight: bold;">Filter Noise</p>
            <p>Reduce 5000+ companies to 20-30 high-quality businesses.</p>
        </div>
        <br>
        <div class="metric-card">
            <h3>Data Points</h3>
            <p style="font-size: 1.2rem; font-weight: bold;">10+ Years</p>
            <p>Historical P&L, Balance Sheets, and Cash Flows.</p>
        </div>
        """, unsafe_allow_html=True)

elif selected_page == "Find Multibaggers":
    st.markdown('<div class="main-header">Finding Multibaggers</div>', unsafe_allow_html=True)
    st.write("---")
    
    st.markdown("""
    A "Multibagger" is a stock that returns several times its initial investment (10x, 20x). 
    To find these, you need companies with **low market cap**, **high growth rates**, **high capital efficiency**, and **reasonable valuations**.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("The Golden Query")
        st.code("""
Market Capitalization < 5000 AND
Sales growth 3Years > 15 AND
Profit growth 3Years > 20 AND
Return on capital employed > 20 AND
Debt to equity < 0.5 AND
Promoter holding > 50 AND
Pledged percentage < 5
        """, language="sql")
        
        st.success("Copy this into Screener.in")
        
        with st.expander("Key Metrics Explained"):
            st.markdown("""
            - **Market Cap < 5000 Cr**: Easier for small companies to double.
            - **ROCE > 20%**: High return on capital.
            - **Promoter Holding > 50%**: Skin in the game.
            """)

    with col2:
        st.subheader("Ideal Growth Trajectory")
        # Mock chart for visualization
        years = ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5']
        price = [100, 110, 150, 250, 500]
        earnings = [10, 12, 18, 28, 45]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=years, y=price, name='Stock Price', fill='tozeroy'))
        fig.add_trace(go.Scatter(x=years, y=earnings, name='Earnings (EPS)', line=dict(dash='dash')))
        fig.update_layout(title="Price follows Earnings (eventually)", hovermode="x unified")
        st.plotly_chart(fig, use_container_width=True)

elif selected_page == "Swing Trading Setup":
    st.markdown('<div class="main-header">Swing Trading Strategy</div>', unsafe_allow_html=True)
    st.write("---")
    
    st.markdown("""
    Screener.in is primarily a fundamental tool, but it can be used for **Positional Swing Trading** 
    (holding for weeks/months) by combining Price Strength with Fundamental Safety.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("The 'Volume Shock' Setup")
        st.markdown("Look for stocks near 52-week highs with sudden volume expansion.")
        
        # Mock Volume Chart
        days = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5 (Breakout)']
        vol = [5000, 4800, 5200, 4500, 15000]
        price_swing = [100, 101, 99, 100, 108]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(x=days, y=vol, name='Volume', marker_color=['#cbd5e1']*4 + ['#f59e0b']))
        fig.add_trace(go.Scatter(x=days, y=price_swing, name='Price', yaxis='y2', line=dict(color='#0f172a')))
        
        fig.update_layout(
            yaxis=dict(title='Volume'),
            yaxis2=dict(title='Price', overlaying='y', side='right'),
            title="Volume Breakout Pattern"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Technical Query")
        st.code("""
Current Price > 0.90 * High Price All Time AND
Current Price < High Price All Time AND
Market Capitalization > 500 AND
Quarterly Profit var > 10 AND
Debt to equity < 1
        """, language="sql")
        st.warning("Note: Screener cannot filter by 'Yesterday's Volume'. Use Chartink for that.")

elif selected_page == "Run Live Screener":
    st.markdown('<div class="main-header">Live Market Screener</div>', unsafe_allow_html=True)
    st.write("---")
    
    st.markdown("""
    This tool fetches **real-time data** for a sample of top Indian stocks using the Yahoo Finance API.
    You can filter them based on live metrics.
    """)
    
    if st.button("Fetch Live Data (This may take a moment)"):
        with st.spinner("Fetching data from NSE..."):
            stock_data = get_stock_data(SAMPLE_TICKERS)
            
            # Process data into a DataFrame
            rows = []
            for ticker, data in stock_data.items():
                info = data['info']
                hist = data['history']
                current_price = hist['Close'].iloc[-1]
                prev_close = hist['Close'].iloc[-2] if len(hist) > 1 else current_price
                change_pct = ((current_price - prev_close) / prev_close) * 100
                
                rows.append({
                    "Ticker": ticker,
                    "Price": round(current_price, 2),
                    "Change %": round(change_pct, 2),
                    "Market Cap (Cr)": round(info.get('marketCap', 0) / 10000000, 2), # Convert to Crores roughly
                    "PE Ratio": round(info.get('trailingPE', 0), 2),
                    "Volume": info.get('volume', 0)
                })
            
            df = pd.DataFrame(rows)
            st.session_state['screener_df'] = df
            st.success("Data Fetched!")

    if 'screener_df' in st.session_state:
        df = st.session_state['screener_df']
        
        # Filters
        col1, col2, col3 = st.columns(3)
        with col1:
            min_pe = st.number_input("Min P/E", value=0)
            max_pe = st.number_input("Max P/E", value=100)
        with col2:
            min_mcap = st.number_input("Min Market Cap (Cr)", value=0)
        with col3:
            pos_change = st.checkbox("Only Positive Change %")
            
        # Apply Filters
        filtered_df = df[
            (df['PE Ratio'] >= min_pe) & 
            (df['PE Ratio'] <= max_pe) & 
            (df['Market Cap (Cr)'] >= min_mcap)
        ]
        
        if pos_change:
            filtered_df = filtered_df[filtered_df['Change %'] > 0]
            
        st.dataframe(filtered_df, use_container_width=True)
        
        st.caption(f"Showing {len(filtered_df)} stocks matching criteria.")

elif selected_page == "Best Alternatives":
    st.markdown('<div class="main-header">Alternative Tools</div>', unsafe_allow_html=True)
    st.write("---")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("### Screener.in")
        st.caption("Best For: Fundamentals")
        st.write("✅ 10-Year Data")
        st.write("✅ Custom Ratios")
        
    with col2:
        st.markdown("### Chartink")
        st.caption("Best For: Technicals")
        st.write("✅ Complex Screener")
        st.write("✅ 'Crossed above' logic")
        
    with col3:
        st.markdown("### TradingView")
        st.caption("Best For: Charting")
        st.write("✅ Best Charts")
        st.write("✅ Pine Script")
        
    with col4:
        st.markdown("### Trendlyne")
        st.caption("Best For: Analysis")
        st.write("✅ DVM Scores")
        st.write("✅ SWOT Analysis")
