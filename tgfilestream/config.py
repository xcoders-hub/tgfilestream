# tgfilestream - A Telegram bot that can stream Telegram files to users over HTTP.
# Copyright (C) 2019 Tulir Asokan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import sys
import os

from yarl import URL

try:
    port = 8080
except ValueError:
    port = -1
if not 1 <= port <= 65535:
    print("Please make sure the PORT environment variable is an integer between 1 and 65535")
    sys.exit(1)

try:
    api_id = 1064864
    api_hash = "5f3eeab0e6108731551e6a93598b654c"
except (KeyError, ValueError):
    print("Please set the TG_API_ID and TG_API_HASH environment variables correctly")
    print("You can get your own API keys at https://my.telegram.org/apps")
    sys.exit(1)

trust_headers = 'false'
host = "localhost"
public_url = URL("http://99.79.161.5:8080")

session_name = os.environ.get("TG_SESSION_NAME", "tgfilestream")

log_config = os.environ.get("LOG_CONFIG")
debug = bool(os.environ.get("DEBUG"))

try:
    # The per-user ongoing request limit
    request_limit = 5
except ValueError:
    print("Please make sure the REQUEST_LIMIT environment variable is an integer")
    sys.exit(1)

try:
    # The per-DC connection limit
    connection_limit =20
except ValueError:
    print("Please make sure the CONNECTION_LIMIT environment variable is an integer")
    sys.exit(1)


start_message = "Send an image or file to get a link to download it"
group_chat_message = os.environ.get("TG_G_C_MESG", "Sorry. But, I only work in private.")

tg_bot_token = 1474320325:AAH0Vhrfp17020xgpOFMffzjfNN6TGi4E2Y"
