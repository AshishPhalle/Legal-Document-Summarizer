Legal Document Summary Generator
Overview
The Legal Document Summary Generator is a web application designed to help users analyze legal documents by extracting key information, generating summaries, identifying clauses and obligations, assessing risks, and providing regulatory updates. The app leverages various libraries and APIs to offer a comprehensive analysis of uploaded PDF documents.

Features
PDF Upload: Users can upload legal documents in PDF format.
Text Extraction: Extracts text from the uploaded PDF for analysis.
Summary Generation: Generates a concise summary of the document.
Clause Detection: Identifies key legal clauses within the document.
Obligation Detection: Detects hidden obligations and dependencies.
Risk Analysis: Assesses risks associated with the document and provides an overall risk score.
Regulatory Updates: Fetches and displays the latest updates related to GDPR.
Email Reports: Allows users to send generated reports via email.
Interactive Chatbot: Users can ask questions about the document, and the chatbot provides answers based on the content.
Technologies Used
Python: The main programming language used for backend logic.
Streamlit: A framework for building web applications in Python.
Langchain Groq: For generating summaries and answering questions.
Google Sheets API: For storing updates in Google Sheets.
BeautifulSoup: For web scraping to fetch GDPR recitals.
Matplotlib: For visualizing detected clauses and risks.
FPDF: For generating PDF reports.
Installation
Clone the repository:
bash

Copy
git clone https://github.com/yourusername/legal-document-summary-generator.git
cd legal-document-summary-generator
Create and activate a virtual environment (optional but recommended):
bash

Copy
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:
bash

Copy
pip install -r requirements.txt
Set up environment variables:
Create a .env file in the root directory and add your API keys and email credentials:

Copy
GROQ_API_KEY=your_groq_api_key
SENDER_EMAIL=your_email@example.com
SENDER_PASSWORD=your_email_password
Run the application:
bash

Copy
streamlit run app.py
Usage
Open the application in your web browser.
Upload a legal document in PDF format.
Navigate through the tabs to view extracted text, summaries, detected clauses, hidden obligations, risk analysis, regulatory updates, and the interactive chatbot.
Optionally, send the report via email.
Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please create a pull request or open an issue.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Streamlit
Langchain
PyPDF2
BeautifulSoup
Matplotlib
gspread
Feel free to reach out if you have any questions or need further assistance!
