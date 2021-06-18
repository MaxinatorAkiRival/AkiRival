import ui

def guess(answer, property):
    if answer == "yes":
        ans = True
    elif answer == "no":
        ans = False
    elif answer == "y":
        ans = True
    elif answer == "n":
        ans = False

    remv=list()

    for d in ui.db:
        if d[property] != ans:
            remv.append(d)
        
    for i in remv:
        ui.db.remove(i)

    if len(ui.db) == 1:
        print("Your character is "+ui.db[0]["name"])
        ui.tpw(ui.pynum.Infinity())



ans = input("Is your character an artist? (yes/no/y/n) ")
guess(ans, "artist")
ans = input("Is your character a cosmologist? (yes/no/y/n) ")
guess(ans, "cosmo")
ans = input("Is your character a mathematician? (yes/no/y/n) ")
guess(ans, "mathe")
ans = input("Is your character female? (yes/no/y/n) ")
guess(ans, "female")
ans = input("Is your character a relative to you? (yes/no/y/n) ")
guess(ans, "rel")
ans = input("Is your character famous? (yes/no/y/n) ")
guess(ans, "famous")
ans = input("Is your character an inventor? (yes/no/y/n) ")
guess(ans, "inventor")
ans = input("Is your character a physicist? (yes/no/y/n) ")
guess(ans, "physi")
ans = input("Is your character your aunt or uncle? (yes/no/y/n) ")
guess(ans, "au")
ans = input("Is your character australian? (yes/no/y/n) ")
guess(ans, "australian")
ans = input("Is your character american? (yes/no/y/n) ")
guess(ans, "american")
ans = input("Is your character british? (yes/no/y/n) ")
guess(ans, "british")
ans = input("Is your character asian? (yes/no/y/n) ")
guess(ans, "asian")
ans = input("Is your character under the age of 18? (yes/no/y/n) ")
guess(ans, "undereightteen")
ans = input("Is your character still alive? (yes/no/y/n) ")
guess(ans, "alive")
ans = input("Is your character in a movie? (yes/no/y/n) ")
guess(ans, "movie")
ans = input("Is your character a saint? (yes/no/y/n) ")
guess(ans, "saint")
ans = input("Is your character over the age of 27? (yes/no/y/n) ")
guess(ans, "overtwenseve")
ans = input("Is your character a theorist? (yes/no/y/n) ")
guess(ans, "theorist")
ans = input("Is your character a streamer on YouTube or Twitch? (yes/no/y/n) ")
guess(ans, "streamer")
ans = input("Is your character a YouTuber? (yes/no/y/n) ")
guess(ans, "youtuber")