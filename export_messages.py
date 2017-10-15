from datetime import datetime
import praw

# Edit these variables:
username = "username_here"
password = "password_here"
client_id = "App_ID"
client_secret = "App_Secret"

# Program:
reddit = praw.Reddit(user_agent='Message Exporter v1 by /u/dignifiedbug', # User agent
		username = username,
		password = password,
		client_id = client_id,
		client_secret = client_secret)	

format_data = open('format.txt', 'r') # Setup files
format_string = format_data.read()
output_file = open('OUTPUT.txt', 'w')

inbox = reddit.inbox

for message in inbox.messages():
	
	created_date = datetime.fromtimestamp(message.created).date()
	
	final_output = format_string.replace('{DATE}', str(created_date))
	final_output = final_output.replace('{SUBJECT}', message.subject)
	final_output = final_output.replace('{BODY}', message.body)
	
	if message.author: # Returns default name if the original author can't be found
		final_output = final_output.replace('{AUTHOR}', message.author.name)
	else:
		final_output = final_output.replace('{AUTHOR}', 'unknown')
	
	output_file.write(final_output)

format_data.close() 
output_file.close()
