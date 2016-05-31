Flask By Example - A full stack tutorial for a Flask app that calculates word-frequency pairs based on the text from a given URL.

Cloud9 Notes
    - To run from app.py
        if __name__ == '__main__':
            host = os.getenv('IP','0.0.0.0')
            port = int(os.getenv('PORT', 5000))
            app.run(host=host, port=port)
            
    - Start PostgreSQL
        sudo service postgresql start
        
    - Change the password for user ubuntu (or whatever user; ubuntu is the default in Cloud9)
        psql
        ubuntu=# \password postgres
        Enter new password: PASSWORD
        Enter new password again: PASSWORD
    - The password can be whatever you like
    
    - Add database info to .env
        * Type the below in the terminal, press Enter, and then add it to .env.
            export DATABASE_URL="postgresql://ubuntu:PASSWORD@localhost/wordcount_dev"
        * ubuntu is the username and PASSWORD is the password. If you don't include those, you get a couple errors, none of which make sense.
    
    - Pushing changes to Heroku
        * A common key error is: Permission denied (publickey). You can fix this by using keys:add to notify Heroku of your new key.
        * Type the following in the terminal and it should work
            heroku keys:add
