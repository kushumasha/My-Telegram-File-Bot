# script.py

class Script:
    # Start Message
    START_TEXT = """
👋 **Hello, {mention}!** I am a Auto Filter Bot.

I can search for files from my database (A dedicated channel) and provide them to you.

**How to use me?**
1. Add me to your group / Search Here ( PM )
2. Simply type the name of the movie or file you want to search.
3. I will show you the search results with buttons.
4. Click the button of your choice, and I will send the file to your private chat!

**To get started, please select your preferred language below.** 👇
"""

    # Language Selection
    LANGUAGE_SELECT_TEXT = "🇮🇳 Please select your language:"

    # "Not Found" message in Bengali (as requested)
    NOT_FOUND_TEXT_BENGALI = """
🥲 দুঃখিত! আপনার কাঙ্ক্ষিত ফাইলটি খুঁজে পাওয়া যায়নি।

**Result পাবি কি করে? তুই তো কোনোদিন পড়াশোনা করিসনি!** 
আরে, পড়াশোনা কর আর দেশকে সামলা। আমি জানি তুই তাও করবি না, তাই তোর জন্য এই নে, গুগল-এ সার্চ করে নে। 👇
"""

    # Generic "File Not Found" message
    FILE_NOT_FOUND_TEXT = "🤷‍♂️ Sorry, this file is not found in my database. Please contact my admin: @{admin}"

    # After selecting a language
    LANGUAGE_SET_TEXT = "✅ Your language has been set to **{language}**."

    # Search results message
    SEARCH_RESULTS_TEXT = "🔍 Here are the results for **'{query}'**:"

    # Help and About
    HELP_TEXT = """
**How can I help you?**

- **Add me to a group:** I work when you search for a file name in a group I am in.
- **Search:** Just type the file name. Example: `Pushpa`
- **/start:** To see this welcome message and change language.

For any issues, contact my admin.
"""
    ABOUT_TEXT = """
**About Me**

- **Name:** Nobita X Flix Auto Filter Bot
- **Function:** To find files from a specific channel and deliver them to users.
- **Developer:** You can mention your name here!
- **Contact:** @{admin}
"""
    # Indian Languages for the selection menu
    INDIAN_LANGUAGES = {
        'en': 'English',
        'bn': 'বাংলা (Bengali)',
        'hi': 'हिन्दी (Hindi)',
        'ta': 'தமிழ் (Tamil)',
        'te': 'తెలుగు (Telugu)',
        'ml': 'മലയാളം (Malayalam)',
        'kn': 'ಕನ್ನಡ (Kannada)',
        'gu': 'ગુજરાતી (Gujarati)',
        'mr': 'मराठी (Marathi)',
        'pa': 'ਪੰਜਾਬੀ (Punjabi)'
    }