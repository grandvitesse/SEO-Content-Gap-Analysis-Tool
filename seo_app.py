from typing import Iterable
import streamlit as st
from pytrends.request import TrendReq

# Function to perform content gap analysis
def content_gap_analysis(keywords):
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload(keywords, cat=0, timeframe='today 5-y', geo='', gprop='')

    interest_over_time_df = pytrends.interest_over_time()
    mean_interest = interest_over_time_df.mean()

    # Calculate mean interest for each keyword
    keyword_interest = {}
    for keyword in keywords:
        keyword_interest[keyword] = mean_interest[keyword]

    # Sort keywords by mean interest
    sorted_keywords = sorted(keyword_interest.items(), key=lambda x: x[1], reverse=True)

    return sorted_keywords

# Main function
def main():
    st.title("SEO Content Gap Analysis Tool")

    # User input for keywords
    keywords_input = st.text_input("Enter keywords (comma-separated) Disclaimer: 5-word limit:")

    if st.button("Perform Analysis"):
        # Split keywords input by comma and remove leading/trailing whitespace
        keywords = [keyword.strip() for keyword in keywords_input.split(",")]

        # Perform content gap analysis
        sorted_keywords = content_gap_analysis(keywords)

        # Display results
     
        st.write("**Mean Interest Scale:**")
        st.write("- Low: 0-25")
        st.write("- Moderate: 26-50")
        st.write("- High: 51-100")
        st.write("")
        st.subheader("Content Gap Analysis Results:")
        #st.write("**Disclaimer: Analysis Results: **")
        st.write("")
        for keyword, interest in sorted_keywords:
            st.write(f"- **Keyword:** {keyword}, **Mean Interest:** {interest:.2f}")
            #st.write("   - ")
            if interest > 50:
                st.write("     - According to Google Trends, This keyword has high search volume and is popular. It's a good candidate for creating content as it can attract a large audience.")
            elif interest > 25:
                st.write("     - According to Google Trends, This keyword has moderate search volume. While it may not be as popular as others, it still represents a significant interest and can be considered for content creation.")
            else:
                st.write("     - According to Google Trends, This keyword has low search volume and may be niche. While it may not have a large audience, targeting niche keywords can help attract highly relevant traffic.")
            st.write("")
            st.write("")

if __name__ == "__main__":
    main()







