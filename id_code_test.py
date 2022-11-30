# 38803160272


while True:
    try:
        isikukood = input('Please enter ID or type "exit": ')
        if isikukood.lower() == 'exit':
            break2
        int(isikukood)
        if len(isikukood) != 11:
            raise UserWarning
    except UserWarning:
        if len(isikukood) > 11:
            print('Code is too long!')
        else:
            print('Code is too short!')
        continue
    except ValueError:
        print('Code is not numeric!')
        continue
    else:
        while True:
            user_choice = input('Please choose:\n1.Get gender\n'
                                '2.Get date of birth\n3.Get region of birth\n'
                                '4.Validate\n5.Change ID\n'
                                '0.Exit\n--> ')
            if user_choice == '1':
                if isikukood[0] not in ['9', '0']:
                    if int(isikukood[0]) % 2 == 0:
                        gender = 'female'
                    else:
                        gender = 'male'
                    print('You are ' + gender)
                else:
                    print('Unable to determine gender!')
            elif user_choice == '2':
                if isikukood[0] not in ['9', '0']:
                    if isikukood[0] in ['1', '2']:
                        bcent = '18'
                    elif isikukood[0] in ['3', '4']:
                        bcent = '19'
                    elif isikukood[0] in ['5', '6']:
                        bcent = '20'
                    elif isikukood[0] in ['7', '8']:
                        bcent = '21'
                    print(f'Your date of birth is {isikukood[5:7]}.{isikukood[3:5]}.{bcent}{isikukood[1:3]}.')
                else:
                    print('Can\' determine date of birth!')
            elif user_choice == '3':
                brplace = ' Made in Estonia '
                if int(isikukood[7:10]) > 0 and not int(isikukood[7:10]) >= 10:
                    brplace = ' Kuuresaare '
                elif int(isikukood[7:10]) >= 11 and int(isikukood[7:10]) <= 19:
                    brplace = ' Tartu '
                elif int(isikukood[7:10]) >= 20 and int(isikukood[7:10]) <= 150:
                    brplace = ' Tallinn '
                elif int(isikukood[7:10]) >= 150 and int(isikukood[7:10]) <= 160:
                    brplace = ' Keila '
                elif int(isikukood[7:10]) >= 161 and int(isikukood[7:10]) <= 220:
                    brplace = ' Rapla '
                elif int(isikukood[7:10]) >= 221 and int(isikukood[7:10]) <= 270:
                    brplace = ' Ida-Virumaa '
                elif int(isikukood[7:10]) >= 270 and int(isikukood[7:10]) <= 370:
                    brplace = ' Tartu '
                elif int(isikukood[7:10]) >= 371 and int(isikukood[7:10]) <= 420:
                    brplace = ' Narva '
                elif int(isikukood[7:10]) >= 421 and int(isikukood[7:10]) <= 470:
                    brplace = ' Pärnu '
                print('Your birth region:' + brplace)
            elif user_choice == '4':
                pass
                if int(isikukood[10]) == (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
                    valid = 'OK'
                    print(' Your ID is undefined! ' + valid)
            elif user_choice == '5':
                break
            elif user_choice == '0':
                print('Good Bye')
                quit()