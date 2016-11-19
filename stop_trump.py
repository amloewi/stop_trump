
import yagmail

 # this_part@gmail.com. Ex. "amloewi" (IN QUOTES!!!)
gmail_username = "fill-this-in"

# self explanatory
gmail_password = "fill-this-in"  # Ex. "mypA55word" (WITH QUOTES!!!)

 # ex. "Alexander Loewi" (ALSO IN QUOTES!!)
 # This is what will appear as Sender in the receiver's inbox.
actual_name = "fill-this-in"

# Email header. SUPER IMPORTANT.
subject = "fill-this-in" # Ex: "Trump as President Fundamentally Unacceptable", "KKK gets their President"

# The email itself. (IN BETWEEN THE TRIPLE QUOTES) Ex. """Message!"""
# Here's a suggestion. NOTE, this will accept <html> tags for formatting.
body="""Please, please, please, save us, from a man who will never care about anyone but himself.<br>
And who will do whatever damage is necessary to get what he wants.<br>
Please save a United States in which we can have any hope, pride, or faith.
"""

mail = yagmail.SMTP({gmail_username:actual_name}, gmail_password)

#with open("newspapers.txt") as f:
with open("electors.txt") as f:
    for address in f.readlines()):
        if address[0] not in ['\n', '#']:
            try:
                mail.send(to=address.strip(),
                    subject=subject,
                    contents=body)
            except Exception as x:
                print x
