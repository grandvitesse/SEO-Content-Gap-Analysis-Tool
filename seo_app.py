import streamlit as st
import numpy as np
import pandas as pd
from pytrends.request import TrendReq

# Function to perform content gap analysis
def content_gap_analysis(keywords, mean_interest):
    # Calculate mean interest for each keyword
    keyword_interest = {keyword: mean_interest[keyword] for keyword in keywords}

    # Sort keywords by mean interest
    sorted_keywords = sorted(keyword_interest.items(), key=lambda x: x[1], reverse=True)

    return sorted_keywords

# Main function
def main():
    st.title("Watr.seo : Content Gap Analysis Tool")

    # User input for keywords
    keywords_input = st.text_input("Enter keywords (comma-separated) Disclaimer: 5-word limit:")

    if st.button("Perform Analysis"):
        # Split keywords input by comma and remove leading/trailing whitespace
        keywords = [keyword.strip() for keyword in keywords_input.split(",")]
        
        # Perform content gap analysis
        pytrends = TrendReq(hl='en-US', tz=360)
        pytrends.build_payload(keywords, cat=0, timeframe='today 5-y', geo='', gprop='')

        interest_over_time_df = pytrends.interest_over_time()
        mean_interest = interest_over_time_df.mean().to_dict()

        sorted_keywords = content_gap_analysis(keywords, mean_interest)

        # Display results
        st.write("**How it works?**")
        st.write("**Functionality**: The SEO Content Gap Analysis Tool leverages Google Trends data to categorize keywords by interest level, providing insights into trending topics for content optimization. It streamlines the process of identifying high-impact keywords")
        st.write("**Business Problem**: By enabling businesses to analyze SEO content gaps, the tool facilitates informed content strategy decisions, leading to improved search engine visibility, higher organic traffic, and enhanced online presence")
        st.write("**Mean Interest Scale:**")
        st.write("- Low: 0-25 | Moderate: 26-50 | High: 51-100")
        #st.write("- Moderate: 26-50")
        #st.write("- High: 51-100")
        st.write("------------------------------------------------------------------------------------------")
        st.subheader("SEO Content Gap Analysis Results:")
        st.write("")
        for keyword, interest in sorted_keywords:
            st.write(f"- **Keyword:** {keyword}, **Mean Interest:** {interest:.2f}")
            if interest > 50:
                st.write("     - According to Google Trends, This keyword has high search volume and is popular. It's a good candidate for creating content as it can attract a large audience.")
            elif interest > 25:
                st.write("     - According to Google Trends, This keyword has moderate search volume. While it may not be as popular as others, it still represents a significant interest and can be considered for content creation.")
            else:
                st.write("     - According to Google Trends, This keyword has low search volume and may be niche. While it may not have a large audience, targeting niche keywords can help attract highly relevant traffic.")
            st.write("")

if __name__ == "__main__":
    main()
