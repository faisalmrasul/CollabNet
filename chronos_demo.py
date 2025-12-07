import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random

# Page config
st.set_page_config(
    page_title="Chronos Bazaar",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Bangla font and styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Hind+Siliguri&display=swap');
    
    * {
        font-family: 'Hind Siliguri', sans-serif;
    }
    
    .big-font {
        font-size: 3rem !important;
        font-weight: bold;
        color: #2563eb;
    }
    
    .bangla-text {
        font-size: 1.2rem;
        line-height: 1.8;
    }
    
    .earning-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    
    .sme-card {
        background: white;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #10b981;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin: 10px 0;
    }
    
    .brand-card {
        background: #f0f9ff;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #3b82f6;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'sme_data' not in st.session_state:
    st.session_state.sme_data = {
        'balance': 2565,
        'today_earning': 110,
        'week_earning': 785,
        'month_earning': 3250,
        'posts_today': 3,
        'withdrawal_history': []
    }

if 'brand_data' not in st.session_state:
    st.session_state.brand_data = {
        'total_spent': 1250000,
        'active_campaigns': 3,
        'sme_reached': 2500,
        'platform_revenue': 500000
    }

# Generate fake SME data
def generate_sme_data():
    businesses = ['চা দোকান', 'কাপড়ের দোকান', 'রেস্টুরেন্ট', 'মোবাইল দোকান', 'ফার্মেসি']
    cities = ['ঢাকা', 'চট্টগ্রাম', 'সিলেট', 'খুলনা', 'রাজশাহী']
    
    data = []
    for i in range(50):
        data.append({
            'name': f'দোকান #{i+1}',
            'type': random.choice(businesses),
            'city': random.choice(cities),
            'daily_earning': random.randint(50, 200),
            'monthly_earning': random.randint(1500, 5000),
            'joined_days_ago': random.randint(1, 90)
        })
    return pd.DataFrame(data)

# Generate fake brand data
def generate_brand_data():
    brands = ['প্রাণ ফুডস', 'আকিজ গ্রুপ', 'ড্যানিশ', 'ওয়ালটন', 'বাংলাদেশ সিমেন্ট', 'কোকাকোলা']
    
    data = []
    for brand in brands:
        data.append({
            'brand': brand,
            'monthly_budget': random.randint(500000, 2000000),
            'active_smes': random.randint(500, 5000),
            'campaigns': random.randint(1, 5),
            'cpm': random.randint(150, 300)
        })
    return pd.DataFrame(data)

# Generate transaction history
def generate_transactions():
    transactions = []
    for i in range(20):
        days_ago = random.randint(0, 30)
        amount = random.randint(100, 1000)
        transactions.append({
            'date': (datetime.now() - timedelta(days=days_ago)).strftime('%d %b'),
            'amount': amount,
            'type': random.choice(['ব্র্যান্ড পোস্ট', 'ডেইলি টাস্ক', 'পারফরম্যান্স বোনাস', 'রেফারাল']),
            'status': 'bKash-এ পাঠানো' if random.random() > 0.3 else 'ব্যালেন্সে'
        })
    return pd.DataFrame(transactions)

# Main App
def main():
    # Sidebar
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/000000/money-bag.png", width=80)
        st.title("Chronos Bazaar")
        st.markdown("""
        <div class='bangla-text'>
        বাংলাদেশের দোকানদারদের জন্য আয়ের প্ল্যাটফর্ম
        </div>
        """, unsafe_allow_html=True)
        
        view_option = st.radio(
            "ড্যাশবোর্ড দেখুন:",
            ["এসএমই ভিউ", "ব্র্যান্ড ভিউ", "প্ল্যাটফর্ম অ্যাডমিন"]
        )
        
        st.markdown("---")
        st.markdown("""
        <div class='bangla-text'>
        📞 যোগাযোগ: ০১৭XX-XXXXXX
        📍 অবস্থান: ঢাকা, বাংলাদেশ
        </div>
        """, unsafe_allow_html=True)
    
    # Main content based on view
    if view_option == "এসএমই ভিউ":
        render_sme_view()
    elif view_option == "ব্র্যান্ড ভিউ":
        render_brand_view()
    else:
        render_admin_view()

def render_sme_view():
    st.title("🛍️ আপনার Chronos Bazaar ড্যাশবোর্ড")
    
    # Top metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class='earning-card'>
            <h3>আজকের আয়</h3>
            <h1>৳{st.session_state.sme_data['today_earning']}</h1>
            <p>৫টি টাস্ক সম্পূর্ণ</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class='earning-card' style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);">
            <h3>এই মাসের আয়</h3>
            <h1>৳{st.session_state.sme_data['month_earning']}</h1>
            <p>৩,০০০+ টাকা লক্ষ্য</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class='earning-card' style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);">
            <h3>ব্যালেন্স</h3>
            <h1>৳{st.session_state.sme_data['balance']}</h1>
            <p>bKash-এ উত্তোলনযোগ্য</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class='earning-card' style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);">
            <h3>পোস্ট সংখ্যা</h3>
            <h1>{st.session_state.sme_data['posts_today']}/৫</h1>
            <p>আজকের লক্ষ্য</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Two columns layout
    col_left, col_right = st.columns([3, 2])
    
    with col_left:
        st.subheader("📋 আজকের টাস্ক (আয় করুন)")
        
        tasks = [
            {"name": "সকালের অফার পোস্ট করুন", "reward": 20, "done": True},
            {"name": "গ্রাহকের ছবি শেয়ার করুন", "reward": 15, "done": True},
            {"name": "বিকেলের বিশেষ পোস্ট", "reward": 25, "done": True},
            {"name": "ব্র্যান্ড: প্রাণ টি এড", "reward": 50, "done": False},
            {"name": "ইন্টারেক্টিভ পোল পোস্ট", "reward": 30, "done": False}
        ]
        
        for task in tasks:
            cols = st.columns([4, 1, 1])
            cols[0].write(f"✅ {task['name']}" if task['done'] else f"⬜ {task['name']}")
            cols[1].write(f"৳{task['reward']}")
            if not task['done']:
                if cols[2].button("করুন", key=f"task_{task['name']}"):
                    st.session_state.sme_data['today_earning'] += task['reward']
                    st.session_state.sme_data['balance'] += task['reward']
                    task['done'] = True
                    st.rerun()
            else:
                cols[2].write("✅ সম্পূর্ণ")
        
        st.markdown("---")
        st.subheader("📊 আয়ের গ্রাফ")
        
        # Generate earning chart
        dates = [(datetime.now() - timedelta(days=i)).strftime('%d %b') for i in range(30, -1, -1)]
        earnings = [random.randint(80, 200) for _ in range(31)]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=earnings, mode='lines+markers', 
                                name='দৈনিক আয়', line=dict(color='#10b981', width=3)))
        fig.update_layout(title='গত ৩০ দিনের আয়', height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    with col_right:
        st.subheader("💰 bKash উত্তোলন")
        
        current_balance = st.session_state.sme_data['balance']
        st.write(f"বর্তমান ব্যালেন্স: **৳{current_balance}**")
        
        withdraw_amount = st.number_input("উত্তোলনের পরিমাণ (৳)", 
                                         min_value=100, 
                                         max_value=current_balance,
                                         value=min(500, current_balance),
                                         step=100)
        
        bkash_number = st.text_input("bKash নম্বর", placeholder="01XXXXXXXXX")
        
        if st.button("✅ bKash-এ পাঠান", type="primary", use_container_width=True):
            if bkash_number and len(bkash_number) == 11:
                st.session_state.sme_data['balance'] -= withdraw_amount
                st.session_state.sme_data['withdrawal_history'].append({
                    'date': datetime.now().strftime('%d %b %Y, %I:%M %p'),
                    'amount': withdraw_amount,
                    'number': bkash_number
                })
                st.success(f"✅ ৳{withdraw_amount} {bkash_number} নম্বরে পাঠানো হয়েছে!")
                st.balloons()
            else:
                st.error("❌ সঠিক bKash নম্বর দিন")
        
        st.markdown("---")
        st.subheader("🏆 শীর্ষ উপার্জনকারী")
        
        top_earners = [
            {"name": "রাজু (ঢাকা)", "earning": 15250, "business": "চা দোকান"},
            {"name": "সুমি (চট্টগ্রাম)", "earning": 12750, "business": "কাপড়ের দোকান"},
            {"name": "করিম (সিলেট)", "earning": 11200, "business": "রেস্টুরেন্ট"},
            {"name": "আপনি", "earning": st.session_state.sme_data['month_earning'], "business": "আপনার দোকান"}
        ]
        
        for i, earner in enumerate(top_earners):
            st.markdown(f"""
            <div class='sme-card'>
                <b>#{i+1} {earner['name']}</b><br>
                <small>{earner['business']}</small><br>
                <b style="color: #10b981;">৳{earner['earning']}</b>
            </div>
            """, unsafe_allow_html=True)

def render_brand_view():
    st.title("🏢 ব্র্যান্ড ড্যাশবোর্ড")
    
    # Brand selection
    brand = st.selectbox("ব্র্যান্ড নির্বাচন করুন", 
                        ['প্রাণ ফুডস', 'আকিজ গ্রুপ', 'ড্যানিশ', 'ওয়ালটন', 'কোকাকোলা'])
    
    # Top metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("মাসিক বাজেট", f"৳{st.session_state.brand_data['total_spent']:,.0f}")
    with col2:
        st.metric("এসএমই সংখ্যা", f"{st.session_state.brand_data['sme_reached']:,.0f}")
    with col3:
        st.metric("প্ল্যাটফর্ম রেভিনিউ", f"৳{st.session_state.brand_data['platform_revenue']:,.0f}")
    
    st.markdown("---")
    
    # Two columns
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader("🎯 নতুন ক্যাম্পেইন তৈরি করুন")
        
        with st.form("new_campaign"):
            campaign_name = st.text_input("ক্যাম্পেইনের নাম")
            target_smes = st.number_input("লক্ষ্য এসএমই সংখ্যা", min_value=100, max_value=10000, value=1000)
            budget = st.number_input("বাজেট (৳)", min_value=10000, max_value=1000000, value=100000)
            duration = st.slider("সময় (দিন)", 7, 30, 14)
            
            submitted = st.form_submit_button("ক্যাম্পেইন শুরু করুন")
            if submitted:
                st.success(f"✅ '{campaign_name}' ক্যাম্পেইন শুরু হয়েছে!")
                st.info(f"• {target_smes} এসএমই পাবে ৳{budget/target_smes:,.0f} করে\n• মোট এসএমই আয়: ৳{budget*0.6:,.0f}\n• প্ল্যাটফর্ম রেভিনিউ: ৳{budget*0.4:,.0f}")
    
    with col_right:
        st.subheader("📈 ক্যাম্পেইন পারফরম্যান্স")
        
        # Performance chart
        campaigns = ['Winter Sale', 'Eid Campaign', 'New Product Launch']
        reach = [1200, 2500, 800]
        engagement = [4.2, 5.6, 3.8]
        
        fig = go.Figure(data=[
            go.Bar(name='এসএমই সংখ্যা', x=campaigns, y=reach, marker_color='#3b82f6'),
            go.Bar(name='এঙ্গেজমেন্ট %', x=campaigns, y=engagement, marker_color='#10b981', yaxis='y2')
        ])
        
        fig.update_layout(
            title='ক্যাম্পেইন তুলনা',
            yaxis=dict(title='এসএমই সংখ্যা'),
            yaxis2=dict(title='এঙ্গেজমেন্ট %', overlaying='y', side='right'),
            barmode='group',
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    st.subheader("🗺️ লাইভ এসএমই ম্যাপ")
    
    # Generate fake map data
    map_data = pd.DataFrame({
        'lat': [23.8103 + random.uniform(-0.5, 0.5) for _ in range(100)],
        'lon': [90.4125 + random.uniform(-0.5, 0.5) for _ in range(100)],
        'size': [random.randint(1, 10) for _ in range(100)],
        'earning': [random.randint(100, 1000) for _ in range(100)]
    })
    
    fig = px.scatter_mapbox(map_data, lat="lat", lon="lon", size="size",
                           color="earning", size_max=15,
                           zoom=6, height=400,
                           color_continuous_scale=px.colors.sequential.Viridis)
    
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    
    st.plotly_chart(fig, use_container_width=True)

def render_admin_view():
    st.title("👑 প্ল্যাটফর্ম অ্যাডমিন")
    
    # Platform metrics
    col1, col2, col3, col4 = st.columns(4)
    
    col1.metric("মোট এসএমই", "2,587", "128 নতুন")
    col2.metric("মোট ব্র্যান্ড", "32", "3 নতুন")
    col3.metric("মাসিক রেভিনিউ", "৳12.5L", "24% ↑")
    col4.metric("এসএমই payout", "৳38.3L", "৳1.2L আজ")
    
    st.markdown("---")
    
    # Charts
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader("📊 এসএমই গ্রোথ")
        
        # Generate growth data
        months = ['জানু', 'ফেব্রু', 'মার্চ', 'এপ্রিল', 'মে', 'জুন']
        smes = [100, 350, 850, 1500, 2100, 2587]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=months, y=smes, mode='lines+markers',
                                line=dict(color='#8b5cf6', width=4),
                                marker=dict(size=10)))
        fig.update_layout(height=350)
        st.plotly_chart(fig, use_container_width=True)
    
    with col_right:
        st.subheader("💰 রেভিনিউ ব্রেকডাউন")
        
        sources = ['প্রাণ ফুডস', 'আকিজ', 'ড্যানিশ', 'অন্যান্য']
        revenue = [450000, 320000, 280000, 200000]
        
        fig = px.pie(values=revenue, names=sources, hole=0.4,
                    color_discrete_sequence=px.colors.sequential.RdBu)
        fig.update_layout(height=350)
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Live transactions
    st.subheader("💸 লাইভ ট্রানজেকশন")
    
    # Create a fake live feed
    if 'transactions' not in st.session_state:
        st.session_state.transactions = []
    
    if st.button("🔄 লাইভ আপডেট"):
        new_trans = {
            'time': datetime.now().strftime('%H:%M:%S'),
            'sme': f'দোকান #{random.randint(1000, 9999)}',
            'amount': random.randint(50, 500),
            'brand': random.choice(['প্রাণ', 'আকিজ', 'ড্যানিশ']),
            'status': 'Paid'
        }
        st.session_state.transactions.insert(0, new_trans)
    
    # Display transactions
    if st.session_state.transactions:
        trans_df = pd.DataFrame(st.session_state.transactions)
        st.dataframe(trans_df, use_container_width=True, hide_index=True)
    
    # Fraud detection
    st.markdown("---")
    st.subheader("🛡️ ফ্রড ডিটেকশন")
    
    col1, col2, col3 = st.columns(3)
    
    col1.metric("সন্দেহজনক একাউন্ট", "12", "-2 today")
    col2.metric("ব্লক করা পোস্ট", "47", "3 today")
    col3.metric("এক্সপার্ট রিভিউ", "5", "Needs attention")
    
    if st.button("রিপোর্ট জেনারেট করুন", type="primary"):
        st.success("✅ রিপোর্ট তৈরি হয়েছে এবং এডমিন ইমেইলে পাঠানো হয়েছে")

if __name__ == "__main__":
    main()
