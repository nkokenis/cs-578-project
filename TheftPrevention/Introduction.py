from twilio.rest import verify
from Text import text
from SMS import check_user, verify_sms

line =\
"--------------------------------------------------------------------------------"
graphic=\
"""
                                      |.---------------.|
                                      ||               ||
                                      ||   -._ .-.     ||
                                      ||   -._| | |    ||
                                      ||   -._|"|"|    ||
                                      ||   -._|.-.|    ||
                                      ||_______________||
                                      /.-.-.-.-.-.-.-.-.\\
                                     /.-.-.-.-.-.-.-.-.-.\\
                                    /.-.-.-.-.-.-.-.-.-.-.\\
                                   /______/__________\___o_\ 
                                   \_______________________/
"""
msg = \
"""
                    Thank you for downloading {}{}{}Theft Prevention!!!{}
"""

print("\n"+line)
print(graphic)
print(line)
print(msg.format(text.ITALIC,text.CGREEN2,text.BOLD,text.ENDC))
print("Lets get you setup so you can be ",end="")
print("{}{}PROTECTED{}"\
    .format(text.CGREEN2,text.BOLD,text.ENDC))

res = input("\n\nHave you already setup an account with Theft Prevention before? [yes, no or idk]: ")
res = res.lower()

if('y' in res):
    print("\n\nThanks for your support :)")

elif('i' in res):
    name = input("Please enter your username: ")
    if check_user(name) is not None:
        print("You are already authenticated")
    else:
        print("No authentication present")
        print("\n\nNo worries, lets get you set up!\n\n")
        verify_sms()
    

else:
    print("\n\nOkay lets get you {}certified!{}\n".format(text.ITALIC,text.ENDC))




