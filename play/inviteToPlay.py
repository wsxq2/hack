def inviteToPlay(YouTomorrowFree=True,YouLikeBadminton=True):
    if YouTomorrowFree == True:
        if YouLikeBadminton == True:
            return "Let's play badminton together!"
        elif YouLikePingpong == True:
            return "Let's play PingPong together!"
    return ""

print inviteToPlay()
