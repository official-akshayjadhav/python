import urllib.request
import os

cnt = 0
while True:

    try:
        print('in progress...')
        fp = urllib.request.urlopen("http://www.splitlook.com/akshayjadhav/status.php")
        mybytes = fp.read()

        mystr = mybytes.decode("utf8")
        fp.close()

        if mystr == '1':
            print('shutdown the laptop')
            os.system("shutdown 0")

        elif mystr == '2':
            print('log out the user')
            #os.system("shutdown 0")
        elif mystr == '3':
            print('sleep the laptop')

        elif mystr == '4':
            print('restart the laptop')
        #reset staus to initial mode

        fp_stop = urllib.request.urlopen("http://www.splitlook.com/akshayjadhav/reset_status.php")
        mybytes = fp_stop.read()

        mystr = mybytes.decode("utf8")
        fp_stop.close()
    except:
        print('exception '+ str(cnt))
        cnt += 1
