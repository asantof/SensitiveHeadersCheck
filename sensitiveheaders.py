import argparse
import requests

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', required=True, help='URL to check headers for')
args = parser.parse_args()

# Make the request
response = requests.get(args.url)

# Check if the headers are present in the response
if 'Server' in response.headers:
    print('\033[91m' + '[!]' + '\033[0m ' + 'Server header present:', response.headers['Server'])
else:
    print('Server header not present')

if 'X-Powered-By' in response.headers:
    print('\033[91m' + '[!]' + '\033[0m ' + 'X-Powered-By header present:', response.headers['X-Powered-By'])
else:
    print('X-Powered-By header not present')

if 'X-AspNet-Version' in response.headers:
    print('\033[91m' + '[!]' + '\033[0m ' + 'X-AspNet-Version header present:', response.headers['X-AspNet-Version'])
else:
    print('X-AspNet-Version header not present')
