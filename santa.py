import hashlib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#def hash(name):
#	return (sum(map(ord, name))%20)

#def hash2(name):
#	return (sum(map(ord,name)))




def main():
	names = dict([('Sally', ''),('Cal',''),('Brobo', ''),('Sol',''),('Kal',''),('Jerrico',''),('Hoot',''),('Byebye','')])

	md5hashes = []
	lukeHashes = []

	for name in names:
		md5hashed = hashlib.md5(name.encode('utf-16')).hexdigest()
		sha256hashed = hashlib.sha256(name.encode('utf-16')).hexdigest()
		md5hashes.append((md5hashed, name))
		lukeHashes.append((sha256hashed, name))
	lukeHashes.sort()
	index = 0
	for name1 in md5hashes:
		names[name1[1]] = lukeHashes[index][1]
		index+= 1
	goodMatching = True
	for name in names:
		if name == names[name]:
			goodMatching = False
	if goodMatching:
		s = smtplib.SMTP(host='smtp.gmail.com', port=587)
		s.starttls()
		s.login('youremailhere@example.com', 'youremailpasswordhere')

		emails = dict([('Sally', 'sally@fake.com'),('Cal','cal@yup.com'),('Brobo', 'brobo@no.com'),('Sol','sol@sun.com'),('Kal','kal@yeah.com'),('Jerrico','jj44@kk.com'),('Hoot','hoot@giveahoot.com'),('Byebye','bye@hello.net')])
		for name in names:

		    msg = MIMEMultipart()
		    message = 'Dear {0},\n \nYou have {1} for Secret Santa 2018. This has been generated with some fancy maths, but you should not concern yourself with the details. Even though Luke wrote the program to assign names, he does not know who you have. The source code is secret; no one can try to guess who has who... (looking at you, Emma). \n \nMerry Christmas! \n \n With Love, \n Secret Santa Bot'.format(name, names[name])
		    print(message)
		    msg['From']='youremailhere@example.com'
		    msg['To']= emails[name] 
		    msg['Subject'] = 'Secret Santa 2018'
		    #print(name, emails[name])
		    msg.attach(MIMEText(message, 'plain'))

		    s.send_message(msg)

		    del msg





if __name__ == '__main__':
	main()
