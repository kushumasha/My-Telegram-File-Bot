# bot.py

import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from googletrans import Translator, LANGUAGES

# Local imports
from config import Config
from script import Script

# Initialize Google Translator
translator = Translator()

# A simple in-memory dictionary to store user language preferences
# For a production bot, use a database like SQLite or MongoDB
user_languages = {}

# Initialize the Pyrogram Client
bot = Client(
    "FileFinderBot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

# --- Command Handlers ---

@bot.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    mention = message.from_user.mention
    
    # Start message with language selection button
    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🇮🇳 Select Language", callback_data="select_language")],
            [
                InlineKeyboardButton("❓ Help", callback_data="help"),
                InlineKeyboardButton("ℹ️ About", callback_data="about")
            ]
        ]
    )
    
    await message.reply_photo(
        photo=Config.START_PIC,
        caption=Script.START_TEXT.format(mention=mention),
        reply_markup=buttons
    )


# --- Callback Query Handler ---

@bot.on_callback_query()
async def callback_query_handler(client: Client, query):
    user_id = query.from_user.id
    data = query.data

    if data == "select_language":
        buttons = []
        # Create buttons for each language
        for code, name in Script.INDIAN_LANGUAGES.items():
            buttons.append([InlineKeyboardButton(name, callback_data=f"lang_{code}")])
        
        await query.message.edit_caption(
            caption=Script.LANGUAGE_SELECT_TEXT,
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    elif data.startswith("lang_"):
        lang_code = data.split("_")[1]
        user_languages[user_id] = lang_code
        lang_name = Script.INDIAN_LANGUAGES.get(lang_code, "Unknown")
        await query.answer(f"Language set to {lang_name}!", show_alert=True)
        # Edit message back to start
        mention = query.from_user.mention
        buttons = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🇮🇳 Change Language", callback_data="select_language")],
                [
                    InlineKeyboardButton("❓ Help", callback_data="help"),
                    InlineKeyboardButton("ℹ️ About", callback_data="about")
                ]
            ]
        )
        await query.message.edit_caption(
            caption=Script.START_TEXT.format(mention=mention),
            reply_markup=buttons
        )

    elif data.startswith("get_file_"):
        try:
            # Format: get_file_{channel_id}_{message_id}
            _, channel_id, msg_id = data.split("_")
            channel_id = int(channel_id)
            msg_id = int(msg_id)

            # Copy the file to the user's PM
            await client.copy_message(
                chat_id=query.from_user.id,
                from_chat_id=channel_id,
                message_id=msg_id
            )
            await query.answer("✅ File sent! Check your PM.", show_alert=True)
        except Exception as e:
            print(e)
            await query.answer("❌ Error: Could not send the file.", show_alert=True)

    elif data == "help":
        await query.message.edit_caption(caption=Script.HELP_TEXT, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="back_to_start")]]))
    
    elif data == "about":
        await query.message.edit_caption(caption=Script.ABOUT_TEXT.format(admin=Config.CONTACT_ADMIN), reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="back_to_start")]]))

    elif data == "back_to_start":
        mention = query.from_user.mention
        buttons = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🇮🇳 Select Language", callback_data="select_language")],
                [
                    InlineKeyboardButton("❓ Help", callback_data="help"),
                    InlineKeyboardButton("ℹ️ About", callback_data="about")
                ]
            ]
        )
        await query.message.edit_caption(caption=Script.START_TEXT.format(mention=mention), reply_markup=buttons)


# --- Message Handler for Searching Files in Groups ---

@bot.on_message(filters.group & filters.text & ~filters.command("/"))
async def group_search_handler(client: Client, message: Message):
    query = message.text
    search_results = []
    
    # Search for messages in the file store channel
    async for msg in client.search_messages(chat_id=Config.FILE_STORE_CHANNEL, query=query):
        if msg.document or msg.video or msg.audio: # Check if the message is a file
            file_name = msg.document.file_name if msg.document else msg.video.file_name if msg.video else "Audio File"
            
            # Create a button for each file found
            button = InlineKeyboardButton(
                text=f"🎬 {file_name}", # Emoji for visual appeal
                callback_data=f"get_file_{Config.FILE_STORE_CHANNEL}_{msg.id}"
            )
            search_results.append([button])
    
    if search_results:
        # If files are found, show them as buttons
        await message.reply_text(
            text=Script.SEARCH_RESULTS_TEXT.format(query=query),
            reply_markup=InlineKeyboardMarkup(search_results),
            quote=True
        )
    else:
        # If no files are found, send the special "not found" message
        user_id = message.from_user.id
        target_lang = user_languages.get(user_id, 'bn') # Default to Bengali

        try:
            # Translate the Bengali base text to the user's selected language
            translated_text = translator.translate(Script.NOT_FOUND_TEXT_BENGALI, dest=target_lang).text
        except Exception as e:
            print(f"Translation Error: {e}")
            # Fallback to the original Bengali text if translation fails
            translated_text = Script.NOT_FOUND_TEXT_BENGALI

        # Create Google search link
        google_search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        
        buttons = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🔍 Go Google", url=google_search_url)]
            ]
        )
        
        await message.reply_text(
            text=translated_text,
            reply_markup=buttons,
            quote=True
        )


# --- Run the Bot ---
if __name__ == "__main__":
    print("Bot is starting...")
    bot.run()
    print("Bot has stopped.")