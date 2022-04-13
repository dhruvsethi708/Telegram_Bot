from datetime import datetime

def responses(input):
    user_msg = str(input).lower()
    print(user_msg)

    if user_msg in ('hi', 'hello', 'hey'):
        return "Hey, How's it going"
    
    if user_msg in ('who are you', 'who are u?', 'who r u?'):
        return "I am Dhruv'Bot."

    if user_msg in ('Time', 'time?', 'time'):
        now = datetime.now()
        return str(now)
    
    return 'I dont understand you'
    