from dotenv import load_dotenv
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

def main():
    try:
        # Get Configuration Settings
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')

        # Create client using endpoint and key
        credential = AzureKeyCredential(ai_key)
        ai_client = TextAnalyticsClient(endpoint=ai_endpoint, credential=credential)

        # Analyze each text file in the reviews folder
        reviews_folder = 'reviews'
        positive_review_count = 0
        total_reviews = 0

        for file_name in os.listdir(reviews_folder):
            # Read the file contents
            print('\n-------------\n' + file_name)
            text = open(os.path.join(reviews_folder, file_name), encoding='utf8').read()
            print('\n' + text)

            # Get sentiment
            sentiment_analysis = ai_client.analyze_sentiment(documents=[text])[0]
            print("\nSentiment: {}".format(sentiment_analysis.sentiment))

            if sentiment_analysis.sentiment == 'positive':
                positive_review_count += 1
            
            total_reviews += 1

        # Calculate the positive review score
        if total_reviews > 0:
            positive_review_score = (positive_review_count / total_reviews) * 100
        else:
            positive_review_score = 0

        print(f"\nTotal reviews: {total_reviews}")
        print(f"Positive reviews: {positive_review_count}")
        print(f"Positive review score: {positive_review_score:.2f}%")

    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    main()
