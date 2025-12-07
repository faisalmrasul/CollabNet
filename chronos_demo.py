# **Chronos Bazaar - Complete Content Creation Platform**

Here's an enhanced Streamlit prototype with **full content creation capabilities** (text, images, video) using AI models:

```python
import streamlit as st
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import base64
from io import BytesIO
from PIL import Image
import json

# Page config
st.set_page_config(
    page_title="Chronos Bazaar - Content Creator",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS with Bangla support
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;500;600;700&display=swap');
    
    * {
        font-family: 'Hind Siliguri', sans-serif;
    }
    
    .content-card {
        background: white;
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        border-left: 5px solid #3b82f6;
    }
    
    .video-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 15px;
    }
    
    .ai-badge {
        background: #10b981;
        color: white;
        padding: 5px 10px;
        border-radius: 20px;
        font-size: 0.8rem;
        display: inline-block;
        margin: 5px;
    }
    
    .post-preview {
        border: 2px solid #e5e7eb;
        border-radius: 10px;
        padding: 20px;
        background: #f9fafb;
        margin: 15px 0;
    }
    
    .social-media-icon {
        font-size: 1.5rem;
        margin-right: 10px;
    }
    
    .bangla-text {
        font-size: 1.1rem;
        line-height: 1.8;
        text-align: right;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for content
if 'created_content' not in st.session_state:
    st.session_state.created_content = []
if 'templates' not in st.session_state:
    st.session_state.templates = load_templates()

def load_templates():
    return {
        'restaurant': {
            'name': 'রেস্টুরেন্ট টেমপ্লেট',
            'colors': ['#FF6B6B', '#4ECDC4', '#FFD166'],
            'fonts': ['Hind Siliguri', 'Kalpurush'],
            'elements': ['food_image', 'price_tag', 'discount_badge']
        },
        'fashion': {
            'name': 'ফ্যাশন বুটিক টেমপ্লেট',
            'colors': ['#FF6B6B', '#118AB2', '#EF476F'],
            'fonts': ['Hind Siliguri', 'Siyam Rupali'],
            'elements': ['model_pose', 'new_arrival', 'price_slash']
        },
        'electronics': {
            'name': 'ইলেকট্রনিক্স দোকান',
            'colors': ['#06D6A0', '#118AB2', '#073B4C'],
            'fonts': ['Hind Siliguri', 'AdorshoLipi'],
            'elements': ['product_3d', 'tech_specs', 'warranty_badge']
        }
    }

def main():
    # Sidebar Navigation
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/000000/video-editing.png", width=80)
        st.title("Chronos Bazaar")
        
        menu = st.radio(
            "নেভিগেশন মেনু",
            ["🏠 ড্যাশবোর্ড", "🎨 কন্টেন্ট ক্রিয়েট", "📱 পোস্ট প্রিভিউ", "📊 পারফরম্যান্স", "💰 আয় করুন"]
        )
        
        st.markdown("---")
        
        # Quick Stats
        st.subheader("📈 আজকের স্ট্যাটস")
        st.metric("তৈরি কন্টেন্ট", f"{len(st.session_state.created_content)}")
        st.metric("আজকের আয়", "৳225")
        st.metric("এঙ্গেজমেন্ট", "4.8%")
        
        st.markdown("---")
        
        # Quick Actions
        st.subheader("⚡ কুইক অ্যাকশন")
        if st.button("🔄 নতুন কন্টেন্ট আইডিয়া", use_container_width=True):
            st.session_state.generate_idea = True
        
        if st.button("📸 রেডিমেট টেমপ্লেট", use_container_width=True):
            st.session_state.use_template = True

    # Main Content Area
    if menu == "🏠 ড্যাশবোর্ড":
        show_dashboard()
    elif menu == "🎨 কন্টেন্ট ক্রিয়েট":
        show_content_creator()
    elif menu == "📱 পোস্ট প্রিভিউ":
        show_post_preview()
    elif menu == "📊 পারফরম্যান্স":
        show_performance()
    elif menu == "💰 আয় করুন":
        show_earnings()

def show_dashboard():
    st.title("🎯 Chronos Bazaar - AI Content Creator")
    
    # Welcome Message
    st.markdown("""
    <div class="content-card">
        <h2>স্বাগতম! আপনার AI কন্টেন্ট এসিস্ট্যান্ট</h2>
        <p class="bangla-text">এক ক্লিকে টেক্সট, ইমেজ এবং ভিডিও কন্টেন্ট তৈরি করুন। শুধু আপনার ব্যবসার ধরন বলুন, বাকিটা আমরা করব!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick Create Section
    st.subheader("🚀 দ্রুত শুরু করুন")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="content-card">
            <h3>📝 টেক্সট কন্টেন্ট</h3>
            <p>অটো বাংলা ক্যাপশন, হ্যাশট্যাগ, পোস্ট আইডিয়া</p>
            <button style="background:#3b82f6; color:white; border:none; padding:10px; border-radius:5px; width:100%;">
                তৈরি করুন
            </button>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="content-card">
            <h3>🖼️ গ্রাফিক্স ডিজাইন</h3>
            <p>সোশ্যাল মিডিয়া পোস্ট, ব্যানার, ফ্লায়ার</p>
            <button style="background:#10b981; color:white; border:none; padding:10px; border-radius:5px; width:100%;">
                তৈরি করুন
            </button>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="content-card">
            <h3>🎥 শর্ট ভিডিও</h3>
            <p>TikTok/Reels, প্রোডাক্ট ডেমো, টিউটোরিয়াল</p>
            <button style="background:#8b5cf6; color:white; border:none; padding:10px; border-radius:5px; width:100%;">
                তৈরি করুন
            </button>
        </div>
        """, unsafe_allow_html=True)
    
    # Recent Content
    st.subheader("🔄 সাম্প্রতিক তৈরি কন্টেন্ট")
    
    if st.session_state.created_content:
        for content in st.session_state.created_content[-3:]:
            display_content_card(content)
    else:
        st.info("এখনো কোনো কন্টেন্ট তৈরি করা হয়নি। উপরের বাটন ক্লিক করে শুরু করুন!")

def show_content_creator():
    st.title("🎨 AI কন্টেন্ট ক্রিয়েটর")
    
    # Create tabs for different content types
    tab1, tab2, tab3, tab4 = st.tabs(["📝 টেক্সট", "🖼️ ইমেজ", "🎥 ভিডিও", "📦 কম্বো প্যাক"])
    
    with tab1:
        create_text_content()
    
    with tab2:
        create_image_content()
    
    with tab3:
        create_video_content()
    
    with tab4:
        create_combo_pack()

def create_text_content():
    st.subheader("📝 AI টেক্সট কন্টেন্ট জেনারেটর")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        business_type = st.selectbox(
            "আপনার ব্যবসার ধরন",
            ["রেস্টুরেন্ট/ক্যাফে", "ফ্যাশন/কাপড়", "ইলেকট্রনিক্স", "পাঠশালা/টিউশন", "স্বাস্থ্য/বিউটি", "অন্যান্য"]
        )
        
        content_type = st.selectbox(
            "কন্টেন্ট টাইপ",
            ["সোশ্যাল মিডিয়া পোস্ট", "প্রোডাক্ট ডেসক্রিপশন", "গ্রাহক রিভিউ রেসপন্স", 
             "বিশেষ অফার ঘোষণা", "ফেস্টিভ্যাল গ্রিটিং", "কোম্পানি আপডেট"]
        )
        
        tone = st.select_slider(
            "টোন সিলেক্ট করুন",
            options=["অফিশিয়াল", "বন্ধুত্বপূর্ণ", "উত্সাহপূর্ণ", "পেশাদার", "মজাদার"]
        )
        
        keywords = st.text_input("কীওয়ার্ডস (কমা দিয়ে আলাদা করুন)", "বিশেষ অফার, ছাড়, নতুন প্রোডাক্ট")
    
    with col2:
        st.markdown("""
        <div style="background:#f0f9ff; padding:20px; border-radius:10px; margin-top:20px;">
            <h4>⚡ AI সুপারিশ:</h4>
            <p>• ঈদের জন্য বিশেষ পোস্ট তৈরি করুন</p>
            <p>• গ্রাহকদের সাথে ইন্টারেক্টিভ কন্টেন্ট</p>
            <p>• ভিডিও ক্যাপশন অটো জেনারেট করুন</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Generate Button
    if st.button("🤖 AI দিয়ে কন্টেন্ট জেনারেট করুন", type="primary", use_container_width=True):
        with st.spinner("AI আপনার কন্টেন্ট তৈরি করছে..."):
            # Simulate AI generation
            generated_content = generate_ai_text(business_type, content_type, tone, keywords)
            
            # Display generated content
            st.markdown("### ✅ তৈরি হয়েছে!")
            
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown("#### 📄 জেনারেটেড কন্টেন্ট:")
                st.markdown(f"""
                <div class="post-preview">
                    <h4>{generated_content['headline']}</h4>
                    <p>{generated_content['body']}</p>
                    <p><strong>হ্যাশট্যাগ:</strong> {generated_content['hashtags']}</p>
                    <p><strong>টোন:</strong> {tone}</p>
                    <p><strong>শব্দ সংখ্যা:</strong> {generated_content['word_count']}</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("#### 📱 প্ল্যাটফর্ম:")
                platforms = st.multiselect(
                    "শেয়ার করার জন্য প্ল্যাটফর্ম",
                    ["Facebook", "Instagram", "TikTok", "WhatsApp", "YouTube"],
                    default=["Facebook", "Instagram"]
                )
                
                if st.button("💾 কন্টেন্ট সেভ করুন", use_container_width=True):
                    content_item = {
                        'type': 'text',
                        'business': business_type,
                        'content': generated_content,
                        'platforms': platforms,
                        'created_at': datetime.now().strftime("%d %b %Y, %I:%M %p"),
                        'earning': 25  # Fixed earning for text content
                    }
                    st.session_state.created_content.append(content_item)
                    st.success(f"✅ কন্টেন্ট সেভ করা হয়েছে! আয় যোগ হয়েছে: ৳25")

def create_image_content():
    st.subheader("🖼️ AI ইমেজ ডিজাইন জেনারেটর")
    
    # Template Selection
    st.markdown("### ১. টেমপ্লেট সিলেক্ট করুন")
    
    template_cols = st.columns(3)
    for i, (key, template) in enumerate(st.session_state.templates.items()):
        with template_cols[i]:
            if st.button(f"🎨 {template['name']}", key=f"template_{key}", use_container_width=True):
                st.session_state.selected_template = key
    
    if 'selected_template' in st.session_state:
        selected = st.session_state.templates[st.session_state.selected_template]
        
        st.markdown(f"### ২. '{selected['name']}' টেমপ্লেট কাস্টোমাইজ করুন")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Text Inputs
            headline = st.text_input("হেডলাইন", "বিশেষ অফার!")
            subheading = st.text_input("সাবহেডিং", "শুধু এই সপ্তাহে")
            offer_text = st.text_input("অফার টেক্সট", "৫০% ছাড়")
            button_text = st.text_input("বাটন টেক্সট", "অর্ডার করুন")
            
            # Upload image
            uploaded_file = st.file_uploader("আপনার প্রোডাক্ট/লোগো ছবি আপলোড করুন", 
                                           type=['png', 'jpg', 'jpeg'])
        
        with col2:
            # Color Customization
            st.markdown("#### 🎨 কালার সেটিংস")
            bg_color = st.color_picker("ব্যাকগ্রাউন্ড কালার", selected['colors'][0])
            text_color = st.color_picker("টেক্সট কালার", "#FFFFFF")
            button_color = st.color_picker("বাটন কালার", selected['colors'][1])
            
            # Font Selection
            font = st.selectbox("ফন্ট সিলেক্ট করুন", selected['fonts'])
        
        st.markdown("---")
        
        # Generate Image Button
        if st.button("🖼️ AI ইমেজ ডিজাইন তৈরি করুন", type="primary", use_container_width=True):
            with st.spinner("AI আপনার ইমেজ ডিজাইন তৈরি করছে..."):
                # Simulate image generation
                st.markdown("### 🎨 আপনার ডিজাইন প্রিভিউ")
                
                # Create a mock image design
                col1, col2, col3 = st.columns([2, 1, 1])
                
                with col1:
                    # Mock design visualization
                    st.markdown(f"""
                    <div style="
                        background: {bg_color};
                        border-radius: 15px;
                        padding: 30px;
                        color: {text_color};
                        height: 400px;
                        display: flex;
                        flex-direction: column;
                        justify-content: space-between;
                        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                    ">
                        <div>
                            <h1 style="font-size: 2.5rem; margin: 0;">{headline}</h1>
                            <h2 style="font-size: 1.5rem; margin: 10px 0 30px 0;">{subheading}</h2>
                        </div>
                        
                        <div style="
                            background: rgba(255,255,255,0.2);
                            padding: 20px;
                            border-radius: 10px;
                            text-align: center;
                        ">
                            <h3 style="font-size: 3rem; margin: 0;">{offer_text}</h3>
                            <p style="font-size: 1.2rem;">সকল প্রোডাক্টে</p>
                        </div>
                        
                        <button style="
                            background: {button_color};
                            color: white;
                            border: none;
                            padding: 15px 30px;
                            border-radius: 50px;
                            font-size: 1.2rem;
                            font-weight: bold;
                            cursor: pointer;
                            margin-top: 30px;
                        ">{button_text}</button>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    st.markdown("#### 📱 সোশ্যাল মিডিয়া সাইজ")
                    sizes = st.multiselect(
                        "সিলেক্ট সাইজ",
                        ["Facebook Post (1200×630)", "Instagram Square (1080×1080)", 
                         "Instagram Story (1080×1920)", "Twitter Post (1200×675)"],
                        default=["Facebook Post (1200×630)"]
                    )
                
                with col3:
                    st.markdown("#### 💰 আয়ের সুযোগ")
                    earning = 50 if len(sizes) > 1 else 30
                    st.metric("এই ডিজাইনের আয়", f"৳{earning}")
                    
                    if st.button("💾 ডিজাইন সেভ করুন", use_container_width=True):
                        content_item = {
                            'type': 'image',
                            'template': selected['name'],
                            'design': {
                                'headline': headline,
                                'subheading': subheading,
                                'offer': offer_text,
                                'colors': [bg_color, text_color, button_color],
                                'font': font
                            },
                            'sizes': sizes,
                            'created_at': datetime.now().strftime("%d %b %Y, %I:%M %p"),
                            'earning': earning
                        }
                        st.session_state.created_content.append(content_item)
                        st.success(f"✅ ডিজাইন সেভ করা হয়েছে! আয় যোগ হয়েছে: ৳{earning}")

def create_video_content():
    st.subheader("🎥 AI ভিডিও কন্টেন্ট জেনারেটর")
    
    st.markdown("""
    <div class="video-card">
        <h3>🚀 ১৫ সেকেন্ডের মধ্যে ভিডিও তৈরি করুন</h3>
        <p>AI আপনার স্ক্রিপ্ট লিখবে, ভয়েসওভার তৈরি করবে এবং ভিডিও এডিট করবে!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Video Creation Steps
    steps = st.columns(4)
    
    steps[0].markdown("### 1️⃣")
    steps[0].markdown("**টপিক সিলেক্ট**")
    
    steps[1].markdown("### 2️⃣")
    steps[1].markdown("**স্ক্রিপ্ট জেনারেট**")
    
    steps[2].markdown("### 3️⃣")
    steps[2].markdown("**মিডিয়া অ্যাড**")
    
    steps[3].markdown("### 4️⃣")
    steps[3].markdown("**ভিডিও রেন্ডার**")
    
    st.markdown("---")
    
    # Video Topic Selection
    topic = st.selectbox(
        "ভিডিও টপিক সিলেক্ট করুন",
        ["প্রোডাক্ট ডেমো", "গ্রাহক টেস্টিমোনিয়াল", "হাউ-টু টিউটোরিয়াল", 
         "বিশেষ অফার", "কোম্পানি স্টোরি", "ইভেন্ট কভারেজ"]
    )
    
    # Video Style
    style = st.selectbox(
        "ভিডিও স্টাইল",
        ["TikTok/Reels Style", "YouTube Shorts", "Instagram Story", 
         "Facebook Video", "Professional Promo"]
    )
    
    # Duration
    duration = st.slider("ভিডিও ডিউরেশন (সেকেন্ড)", 10, 60, 15)
    
    # Media Upload
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📸 ছবি/ভিডিও আপলোড")
        media_files = st.file_uploader(
            "আপলোড করুন (ছবি/ভিডিও)",
            type=['jpg', 'png', 'mp4', 'mov'],
            accept_multiple_files=True
        )
        
        if media_files:
            st.success(f"{len(media_files)} টি ফাইল আপলোড হয়েছে")
    
    with col2:
        st.markdown("#### 🎵 ব্যাকগ্রাউন্ড মিউজিক")
        music_options = ["Upbeat Energetic", "Calm Background", "Trending TikTok", "No Music"]
        music = st.selectbox("মিউজিক সিলেক্ট করুন", music_options)
        
        st.markdown("#### 🗣️ ভয়েসওভার")
        voice = st.selectbox("ভয়েস টাইপ", ["পুরুষ (বাংলা)", "মহিলা (বাংলা)", "ইংরেজি"])
        auto_caption = st.checkbox("অটো বাংলা ক্যাপশন", value=True)
    
    # Generate Video Button
    if st.button("🎬 AI ভিডিও তৈরি করুন", type="primary", use_container_width=True):
        with st.spinner("AI আপনার ভিডিও তৈরি করছে..."):
            # Simulate video processing
            progress_bar = st.progress(0)
            
            for i in range(100):
                progress_bar.progress(i + 1)
                # Simulate processing time
                import time
                time.sleep(0.02)
            
            st.markdown("### 🎉 আপনার ভিডিও তৈরি হয়েছে!")
            
            # Mock video player
            st.markdown("""
            <div style="
                background: #000;
                border-radius: 10px;
                padding: 20px;
                text-align: center;
                margin: 20px 0;
            ">
                <div style="
                    width: 100%;
                    height: 400px;
                    background: linear-gradient(45deg, #667eea, #764ba2);
                    border-radius: 10px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    color: white;
                    font-size: 2rem;
                ">
                    ▶️ AI Generated Video
                </div>
                <div style="color: white; margin-top: 15px;">
                    <span>⏱️ {duration}s</span>
                    <span style="margin: 0 20px;">🎵 {music}</span>
                    <span>🗣️ {voice}</span>
                </div>
            </div>
            """.format(duration=duration, music=music, voice=voice), unsafe_allow_html=True)
            
            # Video details and earnings
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### 📊 ভিডিও ডিটেইলস")
                details = {
                    "টপিক": topic,
                    "স্টাইল": style,
                    "ডিউরেশন": f"{duration} সেকেন্ড",
                    "মিডিয়া ফাইল": len(media_files) if media_files else 0,
                    "ক্যাপশন": "হ্যাঁ" if auto_caption else "না"
                }
                
                for key, value in details.items():
                    st.write(f"**{key}:** {value}")
            
            with col2:
                st.markdown("#### 💰 আয়ের সুযোগ")
                video_earning = 75 + (len(media_files) * 5) if media_files else 75
                st.metric("এই ভিডিওর আয়", f"৳{video_earning}")
                
                platforms = st.multiselect(
                    "প্ল্যাটফর্ম সিলেক্ট করুন",
                    ["TikTok", "YouTube Shorts", "Instagram Reels", "Facebook Video"],
                    default=["TikTok", "Instagram Reels"]
                )
                
                if st.button("💾 ভিডিও সেভ করুন", use_container_width=True):
                    content_item = {
                        'type': 'video',
                        'topic': topic,
                        'style': style,
                        'duration': duration,
                        'platforms': platforms,
                        'created_at': datetime.now().strftime("%d %b %Y, %I:%M %p"),
                        'earning': video_earning
                    }
                    st.session_state.created_content.append(content_item)
                    st.success(f"✅ ভিডিও সেভ করা হয়েছে! আয় যোগ হয়েছে: ৳{video_earning}")

def create_combo_pack():
    st.subheader("📦 কম্বো প্যাক - টেক্সট + ইমেজ + ভিডিও")
    
    st.markdown("""
    <div class="content-card">
        <h3>🚀 সম্পূর্ণ কন্টেন্ট প্যাকেজ</h3>
        <p>এক ক্লিকে সব ধরণের কন্টেন্ট তৈরি করুন: টেক্সট পোস্ট + গ্রাফিক্স + শর্ট ভিডিও</p>
        <span class="ai-badge">AI সুপারিশ</span>
        <span class="ai-badge">টাইম সেভার</span>
        <span class="ai-badge">হাই আয়</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Campaign Theme
    theme = st.selectbox(
        "ক্যাম্পেইন থিম সিলেক্ট করুন",
        ["ঈদ সেল", "বর্ষা সেল", "নতুন বছরের অফার", "গ্র্যান্ড ওপেনিং", 
         "সপ্তাহব্যাপী ছাড়", "ফেস্টিভ্যাল স্পেশাল"]
    )
    
    # Business Details
    col1, col2 = st.columns(2)
    
    with col1:
        business_name = st.text_input("ব্যবসার নাম", "রাজুর ফ্যাশন হাউস")
        offer_details = st.text_area("অফার ডিটেইলস", "সকল প্রোডাক্টে ৫০% ছাড়, ৩ দিনের জন্য")
        primary_color = st.color_picker("প্রাইমারি কালার", "#FF6B6B")
    
    with col2:
        campaign_duration = st.selectbox("ক্যাম্পেইন ডিউরেশন", ["৩ দিন", "১ সপ্তাহ", "২ সপ্তাহ", "১ মাস"])
        target_platforms = st.multiselect(
            "টার্গেট প্ল্যাটফর্ম",
            ["Facebook", "Instagram", "TikTok", "YouTube", "WhatsApp"],
            default=["Facebook", "Instagram", "TikTok"]
        )
        upload_logo = st.file_uploader("লোগো আপলোড করুন", type=['png', 'jpg'])
    
    st.markdown("---")
    
    # Preview Package
    if st.button("👁️ কম্বো প্যাক প্রিভিউ দেখুন", use_container_width=True):
        st.markdown("### 📦 আপনার কম্বো প্যাকেজ কন্টেন্ট:")
        
        # Text Content Preview
        with st.expander("📝 টেক্সট কন্টেন্ট", expanded=True):
            st.markdown(f"""
            **হেডলাইন:** {theme} - {business_name}
            
            **বডি:** {offer_details}
            
            **হ্যাশট্যাগ:** #{business_name.replace(' ', '')} #{theme.replace(' ', '')} #{campaign_duration.replace(' ', '')}
            
            **প্ল্যাটফর্ম:** {', '.join(target_platforms)}
            """)
        
        # Image Content Preview
        with st.expander("🖼️ ইমেজ কন্টেন্ট"):
            col1, col2 = st.columns(2)
            with col1:
                # Mock image 1
                st.markdown(f"""
                <div style="
                    background: {primary_color};
                    height: 200px;
                    border-radius: 10px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    color: white;
                    font-weight: bold;
                    margin: 10px 0;
                ">
                    {business_name}<br>{theme}
                </div>
                """, unsafe_allow_html=True)
            with col2:
                # Mock image 2
                st.markdown(f"""
                <div style="
                    background: #4ECDC4;
                    height: 200px;
                    border-radius: 10px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    color: white;
                    font-weight: bold;
                    margin: 10px 0;
                ">
                    {offer_details}
                </div>
                """, unsafe_allow_html=True)
        
        # Video Content Preview
        with st.expander("🎥 ভিডিও কন্টেন্ট"):
            st.markdown(f"""
            **ভিডিও টাইপ:** {theme} প্রমোশনাল ভিডিও
            
            **ডিউরেশন:** ১৫-৩০ সেকেন্ড
            
            **স্টাইল:** {random.choice(['TikTok Trend', 'Professional', 'Casual'])}
            
            **ইনক্লুড:** লোগো, অফার ডিটেইলস, CTA বাটন
            """)
        
        # Earnings and Action
        st.markdown("---")
        col1, col2 = st.columns([2, 1])
        
        with col1:
            total_earning = 150  # Base for combo pack
            st.metric("💵 কম্বো প্যাক আয়", f"৳{total_earning}")
            st.info("""
            **আয়ের বিস্তারিত:**
            • টেক্সট কন্টেন্ট: ৳25
            • ইমেজ ডিজাইন (২টি): ৳50
            • ভিডিও কন্টেন্ট: ৳75
            • কম্বো বোনাস: ৳20
            """)
        
        with col2:
            if st.button("✅ কম্বো প্যাক তৈরি করুন", type="primary", use_container_width=True):
                content_item = {
                    'type': 'combo',
                    'theme': theme,
                    'business': business_name,
                    'offer': offer_details,
                    'platforms': target_platforms,
                    'created_at': datetime.now().strftime("%d %b %Y, %I:%M %p"),
                    'earning': total_earning,
                    'components': ['text', 'image1', 'image2', 'video']
                }
                st.session_state.created_content.append(content_item)
                st.success(f"✅ কম্বো প্যাক তৈরি করা হয়েছে! মোট আয়: ৳{total_earning}")
                st.balloons()

def generate_ai_text(business_type, content_type, tone, keywords):
    """Generate AI text content based on inputs"""
    templates = {
        "রেস্টুরেন্ট/ক্যাফে": {
            "headline": ["বিশেষ অফার!", "নতুন মেনু আইটেম", "গ্রাহকদের জন্য বিশেষ উপহার"],
            "body": [
                "আমাদের রেস্টুরেন্টে আজ বিশেষ অফার চলছে! সকল আইটেমে ৩০% ছাড়। শুধু আজকের জন্য।",
                "নতুন মেনু আইটেম যোগ করা হয়েছে। আসুন স্বাদ নিয়ে দেখুন!",
                "আজ রাতের ডিনারে বিশেষ উপহার পাবেন। আসুন পরিবার নিয়ে আমাদের রেস্টুরেন্টে।"
            ]
        },
        "ফ্যাশন/কাপড়": {
            "headline": ["নতুন কালেকশন!", "সিজন সেল", "বিশেষ ছাড়"],
            "body": [
                "নতুন কালেকশনের কাপড় এসেছে দোকানে। আজই দেখতে আসুন।",
                "সিজন শেষের সেল চলছে। সকল প্রোডাক্টে ৫০% পর্যন্ত ছাড়।",
                "সপ্তাহব্যাপী বিশেষ অফার। শুধু স্টোর ভিজিটরদের জন্য।"
            ]
        }
    }
    
    # Get template based on business type
    biz_template = templates.get(business_type, templates["রেস্টুরেন্ট/ক্যাফে"])
    
    # Generate content
    content = {
        'headline': random.choice(biz_template['headline']),
        'body': random.choice(biz_template['body']),
        'hashtags': "#বিশেষঅফার #বাংলাদেশ #দোকান #সেল " + " ".join([f"#{kw.strip()}" for kw in keywords.split(",")[:3]]),
        'word_count': random.randint(50, 150)
    }
    
    return content

def show_post_preview():
    st.title("📱 সোশ্যাল মিডিয়া প্রিভিউ")
    
    if not st.session_state.created_content:
        st.info("এখনো কোনো কন্টেন্ট তৈরি করা হয়নি। প্রথমে কন্টেন্ট তৈরি করুন!")
        return
    
    # Select content to preview
    content_options = [f"{i+1}. {c['type'].title()} - {c.get('business', c.get('theme', 'Content'))} ({c['created_at']})" 
                      for i, c in enumerate(st.session_state.created_content)]
    
    selected_idx = st.selectbox(
        "প্রিভিউ দেখতে কন্টেন্ট সিলেক্ট করুন",
        range(len(content_options)),
        format_func=lambda x: content_options[x]
    )
    
    selected_content = st.session_state.created_content[selected_idx]
    
    # Display preview based on content type
    st.markdown(f"### 🎨 {selected_content['type'].title()} কন্টেন্ট প্রিভিউ")
    
    # Platform selection for preview
    platform = st.radio(
        "প্ল্যাটফর্ম প্রিভিউ",
        ["Facebook", "Instagram", "TikTok", "YouTube"],
        horizontal=True
    )
    
    # Platform-specific preview
    st.markdown(f"""
    <div style="
        background: {'#1877F2' if platform == 'Facebook' else 
                    '#E4405F' if platform == 'Instagram' else
                    '#000000' if platform == 'TikTok' else
                    '#FF0000'};
        color: white;
        padding: 15px;
        border-radius: 10px 10px 0 0;
        display: flex;
        align-items: center;
        font-weight: bold;
    ">
        <span class="social-media-icon">
            {'📘' if platform == 'Facebook' else 
             '📷' if platform == 'Instagram' else
             '🎵' if platform == 'TikTok' else '▶️'}
        </span>
        {platform} পোস্ট প্রিভিউ
    </div>
    
    <div class="post-preview" style="border-top: none; border-radius: 0 0 10px 10px;">
        <div style="display: flex; align-items: center; margin-bottom: 15px;">
            <div style="
                width: 50px;
                height: 50px;
                background: #3b82f6;
                border-radius: 50%;
                margin-right: 10px;
            "></div>
            <div>
                <strong>আপনার ব্যবসার নাম</strong><br>
                <small>Just now • 🌍</small>
            </div>
        </div>
        
        <p>{selected_content.get('content', {}).get('body', selected_content.get('offer', 'কন্টেন্ট বডি...'))}</p>
        
        <div style="
            background: #e5e7eb;
            height: {'150px' if selected_content['type'] == 'text' else '300px'};
            border-radius: 10px;
