from time import sleep
username = []
password = []
accounts = {}
aspirants = {
    'Peter': [],
    'Atiku': [],
    'Tinubu': [],
    'Rochas': []
}


def userinput(a):
    return input(a)


def display(a):
    print(a)


def welcome():
    display('OUR VOTING SYSTEM')
    user = userinput('ENTER 1. FOR LOGIN 2. FOR REGISTRATION 3. TO QUIT: ')
    if user == '1':
        sleep(2)
        display('\n')
        login()
    elif user == '2':
        sleep(2)
        display('\n')
        registration()
    elif user == '3':
        display('RESULTS WILL BE READY SOON\n')
        sleep(2)
        results()
    else:
        display('INVALID ENTRY')
        results()


def registration():
    display('REGISTRATION PANEL')
    fullname = userinput('ENTER FULL NAME: ')
    while True:
        dateofbirth = int(userinput('ENTER YEAR OF BIRTH OR 0 TO CANCEL: '))
        if (2022 - dateofbirth) < 18:
            display('YOU ARE NOT ELIGIBLE')
            continue
        elif dateofbirth == 0:
            display('TRY AGAIN NEXT YEAR')
            results()
        else:
            break
    address = userinput('ENTER ADDRESS: ')
    for x in range(3):
        user = userinput('ENTER YOUR USERNAME: ')
        if user in username:
            display('USERNAME ALREADY TAKEN')
            continue
        else:
            passs = userinput('ENTER PASSWORD')
            display('PROCESSING...')
            sleep(2)
            username.append(user)
            password.append(passs)
            accounts[user] = [fullname, dateofbirth, address]
            display('REGISTRATION SUCCESSFUL')
            users = userinput('ENTER 1. TO REGISTER AGAIN 2. TO CONTINUE')
            if users == '1':
                sleep(2)
                display('\n')
                registration()
            elif users == '2':
                sleep(2)
                display('\n')
                login()
            else:
                display('INVALID INPUT\n')
                sleep(2)
                login()

    display('ERROR CREATING ACCOUNT')
    welcome()


def login():
    display('USER LOGIN PANEL')
    for x in range(3):
        user = userinput('ENTER USER NAME: ')
        passs = userinput('ENTER PASSWORD: ')
        if user in username and passs in password:
            display('PROCESSING...')
            sleep(2)
            display('LOGIN SUCCESSFUL')
            sleep(1)
            display('\n')
            dashboard(user)
            break
        else:
            display('INVALID ACCOUNT')

    display('ERROR LOGGING USER IN')
    welcome()


def dashboard(users):
    votees = []
    display('WELCOME TO YOUR DASHBOARD ' + users)
    fname = accounts[users][0]
    a1 = aspirants['Peter']
    a2 = aspirants['Atiku']
    a3 = aspirants['Tinubu']
    a4 = aspirants['Rochas']
    if fname in a1 or fname in a2 or fname in a3 or fname in a4:
        display('YOU HAVE VOTED ALREADY, SEE RESULTS BELOW\n')
        sleep(2)
        result()
    else:
        for x in aspirants:
            votees.append(x)
        display('BELOW ARE THE ASPIRANTS YOU CAN VOTE FOR')
        display(votees)
        display('\n')

        while True:
            vote = userinput('ENTER NAME OF ASPIRANT TO CAST VOTE').title()
            if vote in aspirants:
                display('PROCESSING...')
                sleep(2)
                aspirants[vote].append(fname)
                display('YOUR VOTE HAS BEEN ENTERED. SEE RESULTS BELOW\n')
                sleep(2)
                result()
            else:
                display('ASPIRANT NOT FOUND ON OUR SYSTEM')
                continue


def result():
    display('HERE ARE THE RESULTS')
    sleep(2)
    for x, y in aspirants.items():
        print(x, 'Votes Recorded: ', len(y))

    display('HAVE A NICE DAY')
    sleep(2)
    login()


welcome()
