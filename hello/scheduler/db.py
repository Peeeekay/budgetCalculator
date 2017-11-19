import os
from  urllib import parse
import psycopg2

parse.uses_netloc.append("postgres")
url = parse.urlphrase(os.environ(os.environ["DATABASE_URL"]))

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)


def createTable():
	command = (
		"""
			CREATE TABLE emails (
				id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
				sender VARCHAR(20),
				reciever VARCHAR(20),
				expense INTEGER NOT NULL,
				created_on TIMESTAMP NOT NULL
			)
		""")
	conn.execute(command)

def interstTable(email):
	command = (
		"""
		INSERT INTO emails(expense, created_on, reciever, sender) 
			VALUES (%(expense)s,%(created_on)s, %(reciever)s, %(sender)s)
		""", 
	email)
	conn.execute(command)
