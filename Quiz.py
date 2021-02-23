print('Welcome')

ans = input('Are you ready to play (yes/no): ')
score = 0
total_q = 4

if ans.lower() =='yes':
    ans = input('1. What is the best Programming language? ')
    if ans.lower() == 'python':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

    ans = input('2. what is 15 * 2? ')
    if ans.lower() == '30':
         score += 1
         print('Correct')
    else:
        print('Incorrect')

    ans = input('3. Which is the best Game in the World? ')
    if ans.lower() == 'pubg':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

print('Thank you for playing, you got ', score, "question correc. ")
mark = (score/total_q) * 100

print("Mark: ",mark)
print("Goodbye")
