import requests
import time
import argparse

print('github-contributors by OCH [v1.1] (2021/03/01)')
print('')

parser = argparse.ArgumentParser(description='Retrieve full names of contributors to github repo.')
parser.add_argument('location', metavar='L', type=str, nargs='+',
                    help='for a link like github.com/owner/repo just type owner/repo')
args = parser.parse_args()

x = requests.get('https://api.github.com/repos/%s/contributors' % (args.location[0]))

result = x.json()
print(len(result))

for contributor in result:
	name = contributor['login']
	time.sleep(0.2)
	y = requests.get('https://api.github.com/users/%s' % (name))
	if (y.json()['name'] == None):
		print(y.json()['login'])
	else:
		print(y.json()['name'])