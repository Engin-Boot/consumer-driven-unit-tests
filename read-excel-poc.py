from pandas import read_excel

emaildata = read_excel('emails-to-send.xlsx', sheet_name='Sheet1',
    engine='openpyxl')

for email, hike in zip(emaildata["email"], emaildata["hike"]):
    print(f'send to {email}: hike is {hike}')
