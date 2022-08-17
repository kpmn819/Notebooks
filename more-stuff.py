class Port():
    def __init__(self, p_num, input, state= None):
        self.p_num = p_num
        self.input = input
  
        # need to setup gpio port here
        if self.input:
            if os.name != 'nt':
                GPIO.setup(p_num, GPIO.IN, pull_up_down = GPIO.PUD_UP)
            else:
                pass
        else:
            if os.name != 'nt':
                GPIO.setup(p_num, GPIO.OUT)
            else:
                pass
    def change_state(self):
        if not self.input:
            if self.state:
                self.state = False
            else:
                self.state = True
        else:
            pass
    def out_high(self):
        if not self.input:
            self.state = True
        else:
            pass
    def out_low(self):
        if not self.input:
            self.state = False
        else:
            pass
    def read_state(self):
        if self.input:
            # read the port
            return self.state
        else:
            pass
    def change_config(config):
        if config == 'free_and_pay':
            pass
        if config == 'five_on':
            pass
        if config == 'three_on':
            pass


def main():
    
    try:
        init()
        while 1 == 1:
            global curr_game
        
            try:
                curr_game
            except NameError:
                    print('no curr_game defined')
            else:
                print('previus game deleted')
                del curr_game
            try:
                game_loop()
            except timeout_decorator.TimeoutError:
                continue

        
    except KeyboardInterrupt:
        #cleanup at end of program
        print('   Shutdown')
        #
        # GPIO.cleanup()

if __name__ == '__main__':
    main()


#!/usr/bin/python


import sqlite3
from datetime import datetime
from config import pi_db

def db_start():
    
    global curs
    global conn
    #conn = sqlite3.connect('game_db.db')
    #conn = sqlite3.connect('/home/pi/game_web/game/db.sqlite3')
    conn = sqlite3.connect(pi_db)


    curs = conn.cursor()

def db_close():
    curs.close()
    conn.close()    

def game_write(data):
    global curs
    global conn
    try:
        curs.execute("INSERT INTO game_code_game(name,dtime,score,free) VALUES(?,?,?,?);", data)
        conn.commit()
        curs.execute("SELECT MAX(id) FROM game_code_game;")
        this_game = curs.fetchone()
        #return this game's number for use in turns
        return this_game[0]
    except sqlite3.OperationalError as e:
        print(e)

def get_game():
    try:
        curs.execute("SELECT MAX(id) FROM game_code_game;")
        this_game = curs.fetchone()
        #return this game's number for use in turns
        return this_game[0]
    except sqlite3.OperationalError as e:
        print(e)
     
def turn_write(data):
    try:
        curs.execute("INSERT INTO game_code_qna(game_id,q_number,question,answer,correct) VALUES(?,?,?,?,?);", data)
        conn.commit() 
    except sqlite3.OperationalError as e:
        print(e)
def game_over(final_score):
    try:
        curs.execute("UPDATE game_code_game SET score=? WHERE id=?;", final_score)
        conn.commit() 
    except sqlite3.OperationalError as e:
        print(e)

