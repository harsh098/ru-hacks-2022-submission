# ru-hacks-2022-submission - Organs4Health

The purpose of our bot is to develop a database that stores data of organ donors including blood donors, where our users can access this information and enter their personal health constitutions, once the arguments are entered into the bot, it will filter out the data according the arguments, and thus providing a potential candidate. Our developers had used `nextcord` library to communicate with the Discord API and `aiosqlite3` to asynchronously access our mock database. This is just a prototype for a potential product pitch at **RUHacks 2022 hackathon**.  



  
  

# Getting Started - Dependencies

## Nextcord

**Python 3.8 or higher is required**  

**SQLite3 must be installed**

To install the library without full voice support, you can just run the following command:

```
    # Linux/macOS
    python3 -m pip install -U nextcord

    # Windows
    py -3 -m pip install -U nextcord
```  

Otherwise to get voice support you should run the following command:

```
    # Linux/macOS
    python3 -m pip install -U "nextcord[voice]"

    # Windows
    py -3 -m pip install -U nextcord[voice]
```  

To install additional packages for speedup, run the following command:

```
    # Linux/macOS
    python3 -m pip install -U "nextcord[speed]"

    # Windows
    py -3 -m pip install -U nextcord[speed]
```  

To install the development version, do the following:

```
    $ git clone https://github.com/nextcord/nextcord/
    $ cd nextcord
    $ python3 -m pip install -U .[voice]
```  

`aiosqlite` is compatible with Python 3.6 and newer.
You can install it from PyPI:

```
    $ pip install aiosqlite3
```  

   `pysqlite3` installation  
```
    $ pip install pysqlite3
```  

 # Running the bot
 You can directly use this [link](https://discord.com/api/oauth2/authorize?client_id=972315797638770689&permissions=51264&scope=bot) or set it up manually on your system
 
   
 
## Step 1 :- Clone the git repo  
```
  $ git clone https://github.com/harsh098/ru-hacks-2022-submission/edit/master/README.md
```
## Step 2 :- Add environment variables
Create your Discord Application and generate `API_KEY` using [this link](https://discord.com/developers/applications).  
Now execute the following commands  

```
  # Linux/macOS
    DISCORD_API_KEY = "put your API_KEY here"
    export DISCORD_API_KEY
  # Windows
    setx DISCORD_API_KEY "put your API_KEY here"
    
```  
## Step 3 :- Running the Bot
Run the `bot.py` file
