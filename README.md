# Stripe-Charge-

A Python script for processing Stripe payments with automated payment method creation and order placement.

## Overview

This project demonstrates how to interact with the Stripe API to create payment methods and process charges. The script automates the payment flow by creating a Stripe payment method and placing an order on a merchant's website.

**Created by:** @diwazz

## Features

- ✅ Automated Stripe payment method creation
- ✅ Integration with Stripe API v1
- ✅ Support for card payments (number, CVC, expiration date)
- ✅ Automatic order placement with billing information
- ✅ Detailed console output with progress indicators
- ✅ Error handling and validation

## Requirements

- Python 3.8 or higher
- `requests` library
- Valid Stripe API credentials

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sumitduster-iMac/Stripe-Charge-.git
cd Stripe-Charge-
```

2. Install required dependencies:
```bash
pip install requests
```

## Usage

Run the script from the command line:

```bash
python Stripe4$.py
```

### Input Format

When prompted, enter card details in the following format:
```
number|month|year|cvc
```

**Example:**
```
4242424242424242|12|2025|123
```

Where:
- `number`: Credit card number
- `month`: Expiration month (MM format, e.g., 12)
- `year`: Expiration year (YYYY format, e.g., 2025)
- `cvc`: Card security code (3-4 digits)

### Execution Flow

The script performs the following steps:

1. **[1/2] Creating Stripe Payment Method**
   - Sends card details to Stripe API
   - Generates unique identifiers (GUID, MUID, SID)
   - Returns a payment method ID

2. **[2/2] Placing Order**
   - Uses the payment method ID to place an order
   - Submits billing information
   - Processes the payment

## Output

The script provides real-time feedback:

```
Stripe Charge Script By @diwazz

Enter card details in the format: number|month|year|cvc
Card: 4242424242424242|12|2025|123

Starting the process...

➡️ [1/2] Creating Stripe Payment Method...
✅ Success! Payment Method ID: pm_xxxxxxxxxxxxx

➡️ [2/2] Placing order...
✅ --- CHARGE SUCCESSFUL --- ✅

--- Final Response from Server ---
{response data}
```

## Security & Legal Notice

⚠️ **IMPORTANT DISCLAIMER:**

- This script is for **educational purposes only**
- Only use with your own payment credentials and test cards
- Do not use this script for unauthorized payment processing
- Always comply with Stripe's Terms of Service and applicable laws
- Use Stripe's test mode and test cards for development/testing
- The author is not responsible for any misuse of this code

**Stripe Test Cards:** For testing, use Stripe's official test card numbers available at https://stripe.com/docs/testing

## Configuration

The script includes hardcoded configuration for:
- Stripe API key (publishable key)
- Merchant endpoint URL
- Billing address defaults

**Note:** For production use, these values should be:
- Stored in environment variables
- Configured through a separate config file
- Never hardcoded in the source code

## Dependencies

- **requests**: For making HTTP requests to Stripe and merchant APIs
- **uuid**: For generating unique identifiers
- **urllib.parse**: For URL encoding form data

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2026 Gun Park | @GauZann

## Credits

- **Script Author:** @diwazz
- **Copyright Holder:** Gun Park | @GauZann
- **Repository:** [Stripe-Charge-](https://github.com/sumitduster-iMac/Stripe-Charge-)

## Support

For issues, questions, or contributions, please open an issue on the GitHub repository.

## Disclaimer

This software is provided "as is", without warranty of any kind. Use at your own risk. Always ensure you have proper authorization before processing payments.
