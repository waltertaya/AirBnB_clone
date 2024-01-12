print('.show(' in 'User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")')

line = 'User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")'

args = line.split('.')
temp = args[1].split('"')[1]
args[1] = temp
print(args)
