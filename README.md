# Text Review Sentiment Analysis with Azure AI

This project demonstrates how to use Azure's Text Analytics API to analyze the sentiment of text reviews and calculate a positive review score. The project reads text files from a specified folder, performs sentiment analysis, and provides a summary of positive reviews.

## Prerequisites

- Python 3.6 or higher
- An Azure account with access to the Text Analytics API
- Azure credentials (`AI_SERVICE_ENDPOINT` and `AI_SERVICE_KEY`) stored in a `.env` file

## Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/text-review-sentiment-analysis.git
   cd text-review-sentiment-analysis
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root directory with your Azure credentials:

   ```env
   AI_SERVICE_ENDPOINT=your_endpoint_here
   AI_SERVICE_KEY=your_key_here
   ```

5. Create a `reviews` folder in the project root directory and add your text files with reviews.

## Usage

Run the `main.py` script to analyze the reviews:

```bash
python main.py
```

The script will read all text files in the `reviews` folder, perform sentiment analysis on each review, and print the results. It will also calculate and display the positive review score.

## Example Output

```
-------------
review1.txt

This product is amazing! It has really improved my life.

Sentiment: positive

-------------
review2.txt

I did not like this product. It did not work as expected.

Sentiment: negative

Total reviews: 2
Positive reviews: 1
Positive review score: 50.00%
```
