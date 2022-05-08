# ru-hacks-2022-submission - Organs4Health

The purpose of our bot is to develop a database that stores data of organ donors including blood donors, where our users can access this information and enter their personal health constitutions, once the arguments are entered into the bot, it will filter out the data according the arguments, and thus providing a potential candidate. Our developers had used `nextcord` library to communicate with the Discord API and `aiosqlite3` to asynchronously access our mock database. This is just a prototype for a potential product pitch at **RUHacks 2022 hackathon**.  



  
  
---------------
# Getting Started - Dependencies

Nextcord
----------

**Python 3.8 or higher is required**

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

