from flask import Flask, render_template, request
import smtplib

app = Flask("app")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    recipient = 'recipient@example.com'  # Specify the recipient's email address

    sender_name = request.form['name']
    sender_email = request.form['email']

    subject = 'Greetings from the Web App!'
    message = f"Dear {sender_name},\n\nThis is a pre-composed email message from our web app.\n\nRegards,\nThe Web App Team"

    try:
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)  # Update with your email provider's SMTP server details
        smtp_server.starttls()
        smtp_server.login('your_email@example.com', 'your_password')  # Update with your email login credentials

        smtp_server.sendmail(sender_email, recipient, f'Subject: {subject}\n\n{message}')
        smtp_server.quit()

        return 'Email sent successfully!'
    except Exception as e:
        return f'Error occurred while sending the email: {str(e)}'

if __name__ == '__main__':
    app.run()
