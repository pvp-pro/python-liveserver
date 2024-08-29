#will cause lag modify to help after all im just 10


"""
python Live Server
Original Idea
Might cause lag though

2 day project by a single dev thats 10(me)
"""


"""
Step 1: set fileDir to the file that will be connected to live server
Step 2: set up fileDir2 to this file directory
Step 3: on the fileDir file put your code in a server function - def server():
Step 4: run the code on your terminal - run liveserver.py not the other file

WARNING: this wont work on all os's as i tested it on chromeos
"""

fileDir = 'Your linked file dir here'
fileDir2 = 'liveserver.py directory'

sfd = fileDir
lsfd = fileDir2
testing = True
livefile = open(lsfd, 'r').readlines()
serverfile = open(sfd, 'r').readlines()

print('\033c', end='', flush=True)

def server():
    return ''

def code():
  rc = True
  while True:
       if serverfile == open(sfd, 'r').readlines():
         if rc:
            main()
            rc = False
       elif livefile == open(lsfd, 'r').readlines():
         print('\033c', end='', flush=True)
         import os
         os.system(f'cd {os.getcwd()} && python liveserver.py')   
       else:
           print('\033c', end='', flush=True)
           import os
           os.system(f'cd {os.getcwd()} && python liveserver.py')
       

def main():
      try:
        from file import server
        server()
      except Exception as e:
         print(e)


while testing:
  if serverfile == open(sfd, 'r').readlines():
    code()
    testing = False
  elif livefile == open(lsfd, 'r').readlines():
         print('\033c', end='', flush=True)
         import os
         os.system(f'cd {os.getcwd()} && python liveserver.py')   
  else:
     print('\033c', end='', flush=True)
     import os
     os.system(f'cd {os.getcwd()} && python liveserver.py')