from mailjet_rest import Client

class PriceAlert:
    def __init__(self, api_key, api_secret, sender_email):
        self.mailjet = Client(auth=(api_key, api_secret), version='v3.1')
        self.sender_email = sender_email

    @staticmethod
    def format_price(price, curr):
        return f"{curr}{price:.2f}"

    @staticmethod
    def is_valid_email(email):
        if "@" in email:
            username, domain = email.split("@", 1)
            if len(username) > 0 and "." in domain and len(domain.split(".")[-1]) > 1:
                return True
        raise ValueError(f"The email address '{email}' is not valid.")

    def send_alert(self, recipient_email, name, product_name, current_price, threshold_price, product_url, currency):
        subject = f"Price Alert: {product_name}"
        text_content = self._create_text_content(product_name, current_price, threshold_price)
        html_content = self._create_html_content(name, product_name, current_price, threshold_price, product_url, currency, recipient_email)

        data = {
            'Messages': [
                {
                    "From": {
                        "Email": self.sender_email,
                        "Name": "Price Alert"
                    },
                    "To": [
                        {
                            "Email": recipient_email,
                            "Name": "Valued Customer"
                        }
                    ],
                    "Subject": subject,
                    "TextPart": text_content,
                    "HTMLPart": html_content
                }
            ]
        }

        result = self.mailjet.send.create(data=data)

        if result.status_code == 200:
            print(f"Email sent successfully to {recipient_email}")
        else:
            print(f"Failed to send email. Status code: {result.status_code}")
            print(result.json())

    def _create_text_content(self, product_name, current_price, threshold_price):
        return f"The price of {product_name} has fallen below your price threshold!\n\nCurrent price: ${current_price:.2f}\nYour price threshold: ${threshold_price:.2f}"

    def _create_html_content(self, name, product_name, current_price, threshold_price, product_url, currency, recipient_email):
        return f"""
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
        </head>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; margin: 0; padding: 0; background-color: #f0f0f0;">
            <table cellpadding="0" cellspacing="0" border="0" width="100%" style="background-color: #f0f0f0;">
                <tr>
                    <td align="center" style="padding: 20px 0;">
                        <table cellpadding="0" cellspacing="0" border="0" width="600" style="background-color: #fff; border: 1px solid #ddd; border-radius: 4px;">
                            <tr>
                                <td style="padding: 40px;">
                                    <h1 style="color: #1a5f7a; font-size: 24px; margin: 0 0 20px; text-align: center;">Price Alert</h1>
                                    <p style="margin: 0 0 20px;">Dear {name},</p>
                                    <p style="margin: 0 0 20px;">Great news! The price of <strong>{product_name}</strong> has dropped below your set threshold.</p>
                                    <table cellpadding="10" cellspacing="0" border="0" width="100%" style="background-color: #f8f8f8; border-radius: 4px;">
                                        <tr>
                                            <td><strong>Current price:</strong></td>
                                            <td style="text-align: right;"><strong style="color: #1a5f7a; font-size: 18px;">{self.format_price(current_price, currency)}</strong></td>
                                        </tr>
                                        <tr>
                                            <td><strong>Your threshold:</strong></td>
                                            <td style="text-align: right;"><strong style="font-size: 18px;">{self.format_price(threshold_price, currency)}</strong></td>
                                        </tr>
                                    </table>
                                    <p style="margin: 20px 0;">Don't miss this opportunity to save!</p>
                                    <table cellpadding="0" cellspacing="0" border="0" width="100%">
                                        <tr>
                                            <td align="center" style="padding: 20px 0;">
                                                <a href="{product_url}" style="background-color: #1a5f7a; color: white; padding: 12px 24px; text-decoration: none; font-weight: bold; border-radius: 4px; display: inline-block;">View Product</a>
                                            </td>
                                        </tr>
                                    </table>
                                    <p style="font-size: 12px; text-align: center; color: #666; margin-top: 40px;">
                                        This email was sent to: {recipient_email}<br>
                                    </p>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </body>
        </html>
        """

# run lines 105-111 to check this code works
# if __name__ == "__main__":
#     api_key = 'your_api_key'
#     api_secret = 'your_secret_key'
#     sender_email = "group6.cfgdegree24@gmail.com"
#
#     price_alert = PriceAlert(api_key, api_secret, sender_email)
#     price_alert.send_alert("recipienttest6@gmail.com", "Valued Customer", "Example Product", 30.00, 40.00, "https://www.amazon.co.uk/", "£")