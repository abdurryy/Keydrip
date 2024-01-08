# Keydrip

Keydrip is an innovative Python package designed to interact with Key-Drop.com, enabling users to automate various tasks with ease and efficiency. It offers functionalities such as checking account balance and redeeming codes, all while navigating through the site's security measures. Keydrip sets a new standard for convenience and functionality in the realm of online botting tools.

## Configuration

Before using Keydrip, you need to set up a configuration file. Create a `config.yaml` file in the same directory as your Python script with the following structure:

```yaml
{
   "steamLoginSecure": "get value from https://i.imgur.com/EhJ6shN.png" 
}
```

Replace the placeholder with your actual `steamLoginSecure` value.

## Installation

Install Keydrip easily using pip:

```bash
pip install keydrip
```

## Usage

Here's a quick guide to get you started with Keydrip:

1. **Initialize the Application:**

   ```python
   from keydrip import handler as KDH

   app = KDH(log=True)  # log=True will log the output to a file
   ```

2. **Get Account Balance:**

   ```python
   app.getBalance()
   ```

3. **Redeem a Golden Code:**

   ```python
   app.redeemCode("your golden code here")
   ```

Replace `"your golden code here"` with the actual code you wish to redeem.

## Contributing

Contributions to Keydrip are welcome! Please read the contributing guidelines to get started.

## License

Keydrip is MIT licensed, as found in the LICENSE file.


---

*Note: Keydrip is developed and maintained by abdurryy. This project is not affiliated with Key-Drop.com. Use Keydrip responsibly and in compliance with the website's terms of service.*
