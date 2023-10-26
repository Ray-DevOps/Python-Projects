
#                                   PROJECT DESCRIPTION
                       ------------------------------------------

# In this project, we are provided with a draft letter to be sent to each individual on a list of guests.
# In the draft, there is a placeholder "[Name]" which is to be replaced by the name of the individual guest.
# We are to save the letter in a folder called "ReadyToSend" and the folder is to be created in the present working directory
# Inside the folder, each letter should be saved as letter_for_<invitee>.txt. For example, if we have a "Julie" in the 
# guest list, Julie's letter should be saved in the "ReadyToSend" folder as letter_for_Julie.txt
# In this project folder, we have the draft letter in the file starting_letter.txt and the guest list in the file invited_names.txt


#                                     SOLUTION
                       ------------------------------------------
                   
import os  

os.mkdir('./ReadyToSend/')                                                                   # Weuse the os module is used to create the "ReadyToSend" directory 

names_file = open("invited_names.txt", "r")                                                  # Since the guest list is presented as a file with names in each line, we, therefore, use
invitees = names_file.readlines()                                                            # the readlines() method to return a list containing each line in the file as a list item.

for invitee in invitees:
    invitee = invitee.strip()                                                                # However, we get a wide space at the end caused by '\n'. As such we use the strip() method to get rid of the wide spaces
    draft_letter = open("starting_letter.txt")
    letter_content = draft_letter.read()                                                     # We open the draft letter, read its content, and save it in a variable called "letter_content"
    addressed_letter = letter_content.replace('[name]', invitee)                             # As we loop through the guest_list, we replace the "[Name]" placeholder in the draft letter with the actual name of each guest
    with open(f"./ReadyToSend/letter_for_{invitee}.txt", mode="w") as invitation_letter:     # We then write that to a file (in the "ReadyToSend" directory). The file for each letter is created with the name of the invitee 
        invitation_letter.write(addressed_letter)                                            # (passed dynamically using an f-string)
