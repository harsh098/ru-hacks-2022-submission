# ru-hacks-2022-submission

The purpose of our bot is to develop a database that stores data of organ donors including blood donors, where our a users can access this information and enter their personal health constitutions, once the arguments are entered into the bot, it will then filter out the data according the arguments, thus providing a potential candidate. Our developers had used nextcord to the Discord API and with this connection our bot had various mock potential donor's data inputted inside its lightweight sqlite database with Python as our main programming language. 



# Getting Started - Dependencies

Nextcord
----------

**Python 3.8 or higher is required**

To install the library without full voice support, you can just run the following command:

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U nextcord

    # Windows
    py -3 -m pip install -U nextcord

Otherwise to get voice support you should run the following command:

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U "nextcord[voice]"

    # Windows
    py -3 -m pip install -U nextcord[voice]

To install additional packages for speedup, run the following command:

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U "nextcord[speed]"

    # Windows
    py -3 -m pip install -U nextcord[speed]


To install the development version, do the following:

.. code:: sh

    $ git clone https://github.com/nextcord/nextcord/
    $ cd nextcord
    $ python3 -m pip install -U .[voice]
    
    
    
----------

aiosqlite is compatible with Python 3.6 and newer.
You can install it from PyPI:

.. code-block:: bash

    $ pip install aiosqlite3
    
----------
    Pysqlite3
    
    .. code-block:: bash

    $ pip3 install pysqlite3

