# Installation Instructions

## Prerequisites
- Python 3.6 or higher
- pip (Python package installer)
- Virtual Environment

## Setting Up a Virtual Environment
1. Install `virtualenv` if not already installed:
   ```bash
   pip install virtualenv
   ```
2. Create a new virtual environment:
   ```bash
   virtualenv venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

## Dependency Installation
1. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## API Configuration
- Create a file named `.env` in the root directory:
  - Add your API keys and configuration details here.

## Inventory Data Preparation
1. Prepare your inventory data in CSV format.
2. Ensure the file structure matches the expected input for the application.

## Twilio Setup Guide
1. Sign up for a Twilio account.
2. Obtain your Account SID and Auth Token.
3. Configure Twilio in your `.env` file:
   ```
   TWILIO_ACCOUNT_SID="your_account_sid"
   TWILIO_AUTH_TOKEN="your_auth_token"
   TWILIO_PHONE_NUMBER="your_twilio_phone_number"
   ```
