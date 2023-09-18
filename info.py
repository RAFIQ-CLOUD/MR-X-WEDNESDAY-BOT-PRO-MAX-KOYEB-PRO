import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


#--------------ʙᴏᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ----------#

SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '5397731'))
API_HASH = environ.get('API_HASH', '051ebba43e161aa6f6456af524bad699')
BOT_TOKEN = environ.get('BOT_TOKEN', "6298477801:AAHGajYfWfTlQN0aapA8-iwcV47rCH704vk")

#---------------ᴘᴏʀᴛ---------------#

PORT = environ.get("PORT", "8080")

#---------------ᴀʟʟ ᴘɪᴄs---------------#

CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS', 'https://telegra.ph/file/7f69fb225af0a5aab66d3.jpg https://telegra.ph/file/b857336379d4e5b629a80.jpg https://telegra.ph/file/5175945b76e7a34796904.jpg https://telegra.ph/file/786c9e7bb7a81f53cac32.jpg')).split()

#-------------ᴡᴇʟᴄᴏᴍᴇ ɪᴍᴀɢᴇ------------------#

MELCOW_IMG = environ.get('MELCOW_IMG',"hhttps://telegra.ph/file/def0a3b3dfea398a6619c.jpg")
MELCOW_VID = environ.get('MELCOW_VID',"https://telegra.ph/file/267bb982b0d931dec9fa5.mp4")

#------------ᴀᴅᴍɪɴs,ᴄʜᴀɴɴᴇʟ & ᴜsᴇʀs-----------#

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5784009732 1192029857 5861377019').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001695733718 -1001837502629 -1001849843699 -1001711364605').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '5784009732 1192029857 5861377019').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '-1001875003805')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '-1001984477877').split()]

#------------ᴍᴏɴɢᴏ-ᴅʙ ɪɴғᴏʀᴍᴀᴛᴏɪɴ-----------#

DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://MR-X-WEDNESDAY-BOT-PRO-MAX-KOYEB:MR-X-WEDNESDAY-BOT-PRO-MAX-KOYEB@cluster0.ozsflpz.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

##---------------ᴇxᴛᴇʀ ғᴇᴀᴛᴜʀᴇs-----------------##

           # ᴅᴏᴡɴʟᴏᴀᴅ ᴛᴜᴛᴏʀɪᴀʟ ʙᴜᴛᴛᴏɴ #
HOW_TO_DOWNLOAD =  environ.get('HOW_TO_DOWNLOAD', 'https://t.me/MROTTTamilLinks/10')
     
               # ᴜʀʟ sʜᴏʀᴛ-ʟɪɴᴋ #
#SHORTNER_URL = environ.get('SHORTNER_URL', 'tinyfy.in)
#SHORTNER_API = environ.get('SHORTNER_API', 'f9181a3aa6a2d189766fc1a7d3cf7813aa435eba')

      # ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ғᴏʀ ɢʀᴏᴜᴘ ᴏɴʟʏ (sᴇʟғ ᴅᴇʟᴇᴛᴇ) #
AUTO_DELETE_SECONDS = int(environ.get('AUTO_DELETE_SECONDS', "300"))
AUTO_DELETE = environ.get('AUTO_DELETE', "True")
if AUTO_DELETE == "True":
    AUTO_DELETE = True
#-------------------ᴏᴛʜᴇʀs----------------#

LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001849032747'))
MSG_ALRT = environ.get('MSG_ALRT', 'ᴍᴀᴅᴇ ᴡɪᴛʜ ❣️ ʙʏ @MR_X_MIRROR❣️')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'MR_X_MIRROR')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), False)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<b>🗂FileName : <code>{file_name}</code> \n\n🏷FileSize : <code>{file_size}</code>\n\n» New Movies :\n[MROTTTamilXOffl](https://t.me/MROTTTamilXOffl)\n\n» Movie Request 24×7 :\n[MR X MOVIES REQUEST 24×7](https://t.me/+fUGYs52Q9vxjZDFh)\n\n❤️‍🔥JOIN : @MROTTTamilXOffl</b>")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", "<b>🗂FileName : <code>{file_name}</code> \n\n🏷FileSize : <code>{file_size}</code>\n\n» New Movies :\n[MROTTTamilXOffl](https://t.me/MROTTTamilXOffl)\n\n» Movie Request 24×7 :\n[MR X MOVIES REQUEST 24×7](https://t.me/+fUGYs52Q9vxjZDFh)\n\n❤️‍🔥JOIN : @MROTTTamilXOffl</b>")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>🔖 ᴛɪᴛʟᴇ : <a href={url}>{title}</a>\n\n🎭 ɢᴇɴʀᴇs : {genres}\n🎖 ʀᴀᴛɪɴɢ : <a href={url}/ratings>{rating}</a> / 10 (ʙᴀsᴇᴅ ᴏɴ {votes} ᴜsᴇʀ ʀᴀᴛɪɴɢ.)\n\n📆 ʏᴇᴀʀ : {release_date}\n🗞 ʟᴀɴɢᴜᴀɢᴇ : {languages}\n🌎 ᴄᴏᴜɴᴛʀʏ : {countries} \n\n⚡ᴜᴘʟᴏᴀᴅᴇᴅ ʙʏ : @MROTTTamilXOffl</b>")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), False)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

##---------------------------------------------##
               # ᴜʀʟ sʜᴏʀᴛ-ʟɪɴᴋ #
class Config(object):
    SHORTENER = environ.get('SHORTENER', "")
    SHORTENER_API = environ.get('SHORTENER_API', "")
