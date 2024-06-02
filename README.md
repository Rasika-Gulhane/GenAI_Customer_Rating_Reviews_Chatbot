# Customer Rating and Reviews 
Presentation:
https://docs.google.com/presentation/d/1TBFcqwmlkASCjVz30orn6nLID7nBTwu6x9vXs8_Twz8/edit#slide=id.g2e21f1f6657_0_354


- Sentiment Analysis with NLP 
- AI RAG Chatbot for review related queries on huge dataset

### Introduction:
This project involves the analysis of customer reviews for a generic online retailer to extract meaningful insights and improve product offerings. The process includes data preparation, text processing, sentiment analysis, topic modeling, and the identification of pain points and highlights. We utilized various Python libraries such as pandas, nltk, vaderSentiment, sklearn, and gensim for natural language processing and analysis tasks. The insights are presented through a user-friendly Streamlit app, which provides a comprehensive overview of review sentiments, key topics discussed by customers, and visualizations like sentiment distributions and word clouds. This analysis aims to help the retailer understand customer feedback better, address common issues, and highlight positive aspects of their products. The final Streamlit app is deployed on Streamlit Cloud, enabling easy sharing and accessibility for stakeholders.
Additionally, a LLM base chatbot feature is integrated using LangChain and OpenAI's GPT-4 to facilitate interactive queries and provide dynamic insights from the review data.


The data is reviews for a generic online retailer. We would like you to focus on the following items:

- Generate detailed insights that go beyond overall sentiment
- Identify pain points and what are working/not working for the products
- Write readable and reusable code
- added Streamlit UI
- Added Generative AI RAG pipeline for Chatbot that give complete information of data and Sentiment analysis


### How to run the project for UI:

**Data Analysis and visualization with NLP and Visalization technique:**
1. Inside the python/ conda environmnet install all required libraries
`
pip install -r requirements.txt
`
`
run strea.lit source/data_preprocessing.py
`

**Ratinga nd Sentiment Reviews Chatbot**

1. Create Vecore database using AstraDB for data storage and similarity meassures
- Login to AstraDB and create database collectionand your accessing keys as follows:
    - OPENAI_API_KEY= 'xyz'
    - ASTRA_DB_API_ENDPOINT= 'xyz'
    - ASTRA_DB_APPLICATION_TOKEN= 'xyz'
    - ASTRA_DB_KEYSPACE= default_keyspace

2. Add this keys to environment by creating file .env
3. To chat with AI chatbot:
`
run python app.py
`

