<img src="https://camo.githubusercontent.com/685e6e971f3f7790236ad22808bccb57c25a26eeb2555c60cf2aefe4dae1f0db/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d76332e342b2d677265656e"> <img src="https://camo.githubusercontent.com/b8593b8ea2157c85d33229b9ae386247de6fcedee3c630642a5c8eb3b09d87ae/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4d49542d677265656e"> <img src="https://img.shields.io/badge/status-working-blue">
# Keydrip (Key-drop reversed)

Keydrip is an innovative Python package designed to interact with Key-Drop.com, enabling users to automate various tasks with ease and efficiency. It offers functionalities such as checking account balance and redeeming codes, all while navigating through the site's security measures. Keydrip sets a new standard for convenience and functionality in the realm of online botting tools.

- [Configuration](#configuration)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Configuration

Before using Keydrip, you need to set up a configuration file. Create a `config.yaml` file in the same directory as your Python script with the following structure:

```yaml
{
   "steamLoginSecure": "get value from https://i.imgur.com/EhJ6shN.png" 
}
```

Replace the placeholder with your actual `steamLoginSecure` value from https://steamcommunity.com/.

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
