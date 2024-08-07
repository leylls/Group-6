from ft_end_ascii_decorators import *
from ft_end_input_utils import *
from time import sleep


username = "Georgia" # Mock name - actual data to be extracted from db with get_username()

@new_user_ascii
def new_user_setup_dialogue():
    """
    Full CLI dialogue to set up the main details of the new user (user_name + email_pref + user_email).
    :return: None
    """
    print("I see that you are new around here.".center(60))
    print("How about we set up a few things first?\n".center(60))
    print("For example, what is your name?".center(60))
    user_name = get_user_input()
    #TODO add name into DB
    print(f"Great! Nice to meet you {user_name}.".center(60))
    print("We can notify you by email of any price drop\n"
          "within the range of your choice,\n"
          "would you like to set it up?".center(60))
    email_pref = ""
    while not choice_validation(email_pref, str):
        # While the answer cannot be validated, then keep asking the user until valid answer
        try:
            email_pref = clean(get_user_input("y_n"))
            if email_pref == "y":
                pass
                #TODO func to set_up_email_notifications
            elif email_pref == "n":
                print("All good, you can always set up email notifications\n"
                      "later on the [4]Email notifications page.".center(60))
        except ValueError:
            print("Let's try again")
    print("""\n** ** ** ** ** ** **

                         Oki doke!
       Now that you know how to use {PriceTracking app},
               it's time to jump into business!

                       € * £ * ¥ * $""") #TODO perhaps apps name will change?


@main_menu_ascii
def welcome_back_text(menu_options):
    """
    Welcome CLI text for returning user.
    :param menu_options:
    :return:
    """
    #username = get_username()    # Unfinished func - To code with Shaira
    if username == "visitor":
        print("It seems like we had an issue getting your name from the database."
              "\nWe suggest you to reset your user details :) ")
    else:
        print(f"Welcome back {username}!".center(60))
    print("What would you like".center(60)+"\n"+"to do today?".center(60))
    menu_options()

@main_menu_ascii
def main_menu_text(menu_options):
    """
    Main Menu's CLI text.
    :param menu_options: - Only to be inserted main_menu options
    :return: None
    """
    print("""                        \\  MAIN MENU  /

                  What would you like to do?""")
    menu_options()

def main_menu_options():
    """
    Main Menu's CLI options.
    :return: None
    """
    print(("""\n               [ 1 ]  Track a new product
               [ 2 ]  My tracked products
               [ 3 ]  App settings
               [ 4 ]  Email notifications
               [ 5 ]  Help
               [ 0 ]  Exit""").center(60))


@menu_option_ascii(1, "Track a new product")
def opt_1_track_new_dialogue():
    print(""" """) #TODO Set up options for this task
    pass

@menu_option_ascii(2, "My tracked products")
def opt_2_tracked_prod_dialogue():
    print(""" """) #TODO Set up options for this task
    pass

@menu_option_ascii(3, "App settings")
def opt_3_app_settings_dialoge():
    print(""" """) #TODO Set up options for this task
    pass

@menu_option_ascii(4, "Email notifications")
def opt_4_email_notifications_dialogue():
    print(""" """) #TODO Set up options for this task
    pass

@menu_option_ascii(5, "My tracked products")
def opt_5_help_dialogue():
    print(""" """) #TODO Set up options for this task
    pass


@goodbye_ascii
def goodbye():
    """
    It prints a nice goodbye message and keeps the app running for a few seconds before exiting.
    :return:
    """
    print("""                 **    Thank you for using    **
                        PriceTrackingApp!
                            *   *   *""")
    sleep(4)
    quit()