import gmailnator

csrf_token, email = gmailnator.generate_email()
print(f'Email: {email}')
print(f'Token: {csrf_token}')
input('Send email, wait a few minutes to ensure that it has been received then press enter to continue...')
emails = gmailnator.check_emails(csrf_token, email)
print(f'Got {len(emails)} emails')
for mail in emails:
    print(f'Subject: {mail["subject"]}')
    print(f'Body: {mail["body"]}')
    print(f'Link: {mail["link"]}')
    print(f'Time: {mail["time"]}')
    print(f'Full body: {gmailnator.get_message(mail["link"], csrf_token)}')
