import smtplib

class EmailNotifier():

    def __init__(self, senderEmail, senderPassword, userList= 'userEmails.txt'):
        self.senderEmail = senderEmail
        self.password = senderPassword
        self.server = self.connectToMailServer()
        with open(userList, "r") as file:
            self.userEmails = file.readlines()
        
    def connectToMailServer(self):
        mailServer = smtplib.SMTP('smtp.gmail.com')
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(self.senderEmail, self.password)
        return mailServer
    
    def notifyUsers(self, message, dataName, reading):
        for row in self.userEmails:
            username, email = row.split(',')

            self.server.sendmail(self.senderEmail, email, message.format(username, dataName, reading))


if __name__ == "__main__":
    notifier = EmailNotifier('coreyohulse@gmail.com', 'kenshin247')

    message = 'Subejct: testing notifier \n\n Hey {}, whats up brochacho? Heres your {} reading: {}'
    notifier.notifyUsers(message, 'temperature', 20)
