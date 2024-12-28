from flask import Flask, request, render_template
import re

app = Flask(__name__)

def extract_emails(text):
    """
    Extracts all email addresses from the given text.
    """
    # Regular expression pattern for emails
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # Find all email addresses using the regex pattern
    emails = re.findall(email_pattern, text)
    
    return emails

def filter_emails_by_domain(emails, domain):
    """
    Filters emails that belong to a specific domain.
    """
    # Filter emails by domain
    filtered_emails = [email for email in emails if email.endswith(f'@{domain}')]
    
    return filtered_emails

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the entered text and domain
        text = request.form.get('text_content')
        domain = request.form.get('domain')
        
        if text and domain:
            # Extract emails from the content
            emails = extract_emails(text)

            # Filter emails by the provided domain
            filtered_emails = filter_emails_by_domain(emails, domain)

            return render_template('index.html', filtered_emails=filtered_emails)

    return render_template('index.html', filtered_emails=None)

if __name__ == '__main__':
    app.run(debug=True)
