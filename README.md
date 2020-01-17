# rainbow6-teamspeak3-bot
Script to show user's statistic from Rainbow 6: Siege in his TeamSpeak description. Based on r6tab.com, PyTS3.
This is not a serious, full-fledged project. This is more of an idea for TeamSpek users and Rainbow Six players. Or an example of using PyTS3.

Need `ts3` library: `pip3 install ts3`
# Run server
Run example: `python3 bot.py 192.168.1.1(server IP) serveradmin(ServerQuery username) 1A2b3C4V(ServerQuery password) "TeamSpeak Bot"(bot's nickname on server)`.

In file `r6Stat` are stored user's database ID on server and his ID in Rainbow6.
# Get user's database ID
In standart TS3 theme database ID not show. You must install custom theme. I recomended [Darcula](https://www.myteamspeak.com/addons/1bf5ca7a-f4ff-4848-a6f7-c08aa360c4fb)

[Example image](/images/ts3.png "Example")
# Get user's Rainbow 6: Siege ID
Go to r6tab.com, find user by id and go to his profile. URL must be like this: `https://r6tab.com/d381494a-4a8d-4d10-81b1-e1c0d3392dca`
After `https://r6tab.com/` is ID. In this case `d381494a-4a8d-4d10-81b1-e1c0d3392dca`
