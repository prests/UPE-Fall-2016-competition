import time
import requests # if not installed already, run python -m pip install requests OR pip install requests, whatever you normally do
import random
import gc

def check_fast_up():
    print("in up check")
    global json
    global solved
    x = json['player']['x']
    y = json['player']['y']
    count = 0
    moves = 0
    old_x = x
    while(1):
        if(moves>json['player']['bombRange']):
	    if(not path(0,json['opponent']['x'],json['opponent']['y'],x,y,-1,-1,4)):
		solved = False
		print("out of bomb range")
		return True
        if(count == 4):
            print("took too long")
            return False
        if(hardboard[11*(x-1)+y] == 0 and not check_enemy_bomb_loc(x-1,y) and not check_trail(x-1,y) and json['softBlockBoard'][11*(x-1)+y] == 0 and moves>0):
	    if(not path(0,json['opponent']['x'],json['opponent']['y'],x-1,y,-1,-1,4)):
		solved = False
		print("side exit")
		return True
	if(hardboard[11*(x+1)+y] == 0 and not check_enemy_bomb_loc(x+1,y) and not check_trail(x+1,y)  and json['softBlockBoard'][11*(x+1)+y] == 0 and moves>0):
	    if(not path(0,json['opponent']['x'],json['opponent']['y'],x+1,y,-1,-1,4)):
		solved = False
		print("side exit")
		return True
        else:
            if(y==1 or hardboard[11*(x)+(y-1)] == 1 or json['softBlockBoard'][11*(x)+(y-1)] == 1):
                print("wall")
                return False
            else:
                print("moved up to check")
		if(not check_enemy_bomb_loc(x,y-1) and not check_trail(x,y-1)):
		    y = y-1
		else:
		    return False
                moves = moves + 1
                count = count + 1

def check_attack_fast_up():
    print("in up check")
    global json
    global solved
    x = json['player']['x']
    y = json['player']['y']
    count = 0
    moves = 0
    old_x = x
    old_y = y
    while(1):
        if(moves>json['player']['bombRange']):
	    if(not path(0,json['opponent']['x'],json['opponent']['y'],x,y,-1,-1,4)):
		solved = False
		print("out of bomb range")
		return True
        if(count == 4):
            print("took too long")
            return False
        if(hardboard[11*(x-1)+y] == 0 and not check_all_bomb_loc(x-1,y, old_x, old_y) and not check_trail(x-1,y) and json['softBlockBoard'][11*(x-1)+y] == 0 and moves>0):
	    if(not path(0,json['opponent']['x'],json['opponent']['y'],x-1,y,-1,-1,4)):
		solved = False
		print("side exit (left)")
		return True
	if(hardboard[11*(x+1)+y] == 0 and not check_all_bomb_loc(x+1,y, old_x, old_y) and not check_trail(x+1,y) and json['softBlockBoard'][11*(x+1)+y] == 0 and moves>0):
	    if(not path(0,json['opponent']['x'],json['opponent']['y'],x+1,y,-1,-1,4)):
		solved = False
		print("side exit (right)")
		return True
        else:
            if(y==1 or hardboard[11*(x)+(y-1)] == 1 or json['softBlockBoard'][11*(x)+(y-1)] == 1):
                print("wall")
                return False
            else:
                print("moved up to check")
		if(not check_all_bomb_loc(x,y-1, old_x, old_y) and not check_trail(x,y-1)):
		    y = y-1
		else:
		    return False
                moves = moves + 1
                count = count + 1
		
def check_fast_down():
    global json
    global solved
    x = json['player']['x']
    y = json['player']['y']
    count = 0
    moves = 0
    old_x = x
    old_y = y
    while(1):
        if(moves>json['player']['bombRange']):
	    if(not path(0,json['opponent']['x'],json['opponent']['y'],x,y,-1,-1,4)):
		solved = False
		return True
        if(count == 4):
            return False
        if(hardboard[11*(x-1)+y] == 0 and not check_enemy_bomb_loc(x-1,y) and not check_trail(x-1,y) and json['softBlockBoard'][11*(x-1)+y] == 0 and moves>0):
	    if(not path(0,json['opponent']['x'],json['opponent']['y'],x-1,y,-1,-1,4)):
		solved = False
		return True
	if(hardboard[11*(x+1)+y] == 0 and not check_enemy_bomb_loc(x+1,y) and not check_trail(x+1,y) and json['softBlockBoard'][11*(x+1)+y] == 0 and moves>0):
    	    if(not path(0,json['opponent']['x'],json['opponent']['y'],x+1,y,-1,-1,4)):
		solved = False
		return True
        else:
            if(y==9 or hardboard[11*(x)+(y+1)] == 1 or json['softBlockBoard'][11*(x)+(y+1)] == 1):
                return False
            else:
		if(not check_enemy_bomb_loc(x,y+1) and not check_trail(x,y+1)):
		    y = y+1
		else:
		    return False
                moves = moves + 1
                count = count + 1 

def check_attack_fast_down():
    global json
    global solved
    x = json['player']['x']
    y = json['player']['y']
    count = 0
    moves = 0
    old_x = x
    old_y = y
    while(1):
	if(moves>json['player']['bombRange']):
	    if(not path(0,json['opponent']['x'],json['opponent']['y'],x,y,-1,-1,4)):
		solved = False
		print("out of bomb range")
		return True
	if(count == 4):
	    print("took too long")
	    return False
	if(hardboard[11*(x-1)+y] == 0 and not check_all_bomb_loc(x-1,y, old_x, old_y) and not check_trail(x-1,y) and json['softBlockBoard'][11*(x-1)+y] == 0 and moves>0):
	    if(not path(0,json['opponent']['x'],json['opponent']['y'],x-1,y,-1,-1,4)):
		solved = False
		print("side exit")
		return True
	if(hardboard[11*(x+1)+y] == 0 and not check_all_bomb_loc(x+1,y, old_x, old_y) and not check_trail(x+1,y) and json['softBlockBoard'][11*(x+1)+y] == 0 and moves>0):
	    if(not path(0,json['opponent']['x'],json['opponent']['y'],x+1,y,-1,-1,4)):
		solved = False
		print("side exit")
		return True
        else:
            if(y==9 or hardboard[11*(x)+(y+1)] == 1 or json['softBlockBoard'][11*(x)+(y+1)] == 1):
                return False
            else:
		if(not check_all_bomb_loc(x,y+1, old_x, old_y) and not check_trail(x,y+1)):
		    y = y+1
		else:
		    return False
                moves = moves + 1
                count = count + 1 
    
def check_fast_left():
    global json
    global solved
    x = json['player']['x']
    y = json['player']['y']
    count = 0
    moves = 0
    old_y = y
    while(1):
        if(moves>json['player']['bombRange']):
	    if(not path(0,json['opponent']['x'],json['opponent']['y'],x,y-1,-1,-1,4)):
		solved = False
		return True
        if(count == 4):
            return False
        if(hardboard[11*(x)+(y-1)] == 0 and not check_enemy_bomb_loc(x,y-1) and not check_trail(x,y-1) and json['softBlockBoard'][11*(x)+(y-1)] == 0 and moves>0):
	    if(not path(0,json['opponent']['x'],json['opponent']['y'],x,y-1,-1,-1,4)):
		solved = False
		return True
	if(hardboard[11*(x)+(y+1)] == 0 and not check_enemy_bomb_loc(x,y+1) and not check_trail(x,y+1) and json['softBlockBoard'][11*(x)+(y+1)] == 0 and moves>0):
	    if(not path(0,json['opponent']['x'],json['opponent']['y'],x,y+1,-1,-1,4)):
		solved = False
		return True
        else:
            if(x==1 or hardboard[11*(x-1)+(y)] == 1 or json['softBlockBoard'][11*(x-1)+(y)] == 1):
                return False
            else:
		if(not check_enemy_bomb_loc(x-1,y) and not check_trail(x-1,y)):
		    x = x-1
		else:
		    return False
                moves = moves + 1
                count = count + 1 

def check_attack_fast_left():
    global json
    global solved
    x = json['player']['x']
    y = json['player']['y']
    count = 0
    moves = 0
    old_y = y
    old_x = x
    while(1):
        if(moves>json['player']['bombRange']):
	    if(not path(0,json['opponent']['x'],json['opponent']['y'],x,y,-1,-1,4)):
		solved = False
		return True
        if(count == 4):
            return False
        if(hardboard[11*(x)+(y-1)] == 0 and not check_all_bomb_loc(x,y-1, old_x, old_y) and not check_trail(x,y-1) and json['softBlockBoard'][11*(x)+(y-1)] == 0 and moves>0):
	    if(not path(0,json['opponent']['x'],json['opponent']['y'],x,y-1,-1,-1,4)):
		solved = False
		return True
	if(hardboard[11*(x)+(y+1)] == 0 and not check_all_bomb_loc(x,y+1, old_x, old_y) and not check_trail(x,y+1) and json['softBlockBoard'][11*(x)+(y+1)] == 0 and moves>0):
	    if(not path(0,json['opponent']['x'],json['opponent']['y'],x,y+1,-1,-1,4)):
		solved = False
		return True
        else:
            if(x==1 or hardboard[11*(x-1)+(y)] == 1 or json['softBlockBoard'][11*(x-1)+(y)] == 1):
                return False
            else:
		if(not check_all_bomb_loc(x-1,y, old_x, old_y) and not check_trail(x-1,y)):
		    x = x-1
		else:
		    return False
                moves = moves + 1
                count = count + 1 

def check_fast_right():
    global json
    global solved
    x = json['player']['x']
    y = json['player']['y']
    count = 0
    moves = 0
    old_y = y
    while(1):
	if(moves>json['player']['bombRange']):
	    if(not path(0,json['opponent']['x'],json['opponent']['y'],x,y-1,-1,-1,4)):
		solved = False
		return True
	if(count == 4):
	    return False
	if(hardboard[11*(x)+(y-1)] == 0 and not check_enemy_bomb_loc(x,y-1) and not check_trail(x,y-1) and json['softBlockBoard'][11*(x)+(y-1)] == 0 and moves>0):
	    if(not path(0,json['opponent']['x'],json['opponent']['y'],x,y-1,-1,-1,4)):
		sovled = False
		return True
	if(hardboard[11*(x)+(y+1)] == 0 and not check_enemy_bomb_loc(x,y+1) and not check_trail(x,y+1) and json['softBlockBoard'][11*(x)+(y+1)] == 0 and moves>0):
	    if(not path(0,json['opponent']['x'],json['opponent']['y'],x,y+1,-1,-1,4)):
		solved = False
		return True
        else:
            if(x==9 or hardboard[11*(x+1)+(y)] == 1 or json['softBlockBoard'][11*(x+1)+(y)] == 1):
                return False
            else:
		if(not check_enemy_bomb_loc(x+1,y) and not check_trail(x+1,y)):
		    x = x+1
		else:
		    return False
                moves = moves + 1
                count = count + 1 

def check_attack_fast_right():
    global json
    global solved
    x = json['player']['x']
    y = json['player']['y']
    count = 0
    moves = 0
    old_y = y
    old_x = x
    while(1):
	if(moves>json['player']['bombRange']):
	    if(not path(0,json['opponent']['x'],json['opponent']['y'],x,y,-1,-1,4)):
		solved = False
		return True
	if(count == 4):
	    return False
	if(hardboard[11*(x)+(y-1)] == 0 and not check_all_bomb_loc(x,y-1, old_x, old_y) and not check_trail(x,y-1) and json['softBlockBoard'][11*(x)+(y-1)] == 0 and moves>0):
	    if(not path(0,json['opponent']['x'],json['opponent']['y'],x,y-1,-1,-1,4)):
		solved = False
		return True
	if(hardboard[11*(x)+(y+1)] == 0 and not check_all_bomb_loc(x,y+1, old_x, old_y) and not check_trail(x,y+1) and json['softBlockBoard'][11*(x)+(y+1)] == 0 and moves>0):
	    if(not path(0,json['opponent']['x'],json['opponent']['y'],x,y+1,-1,-1,4)):
		solved = False
		return True
        else:
            if(x==9 or hardboard[11*(x+1)+(y)] == 1 or json['softBlockBoard'][11*(x+1)+(y)] == 1):
                return False
            else:
		if(not check_all_bomb_loc(x+1,y, old_x, old_y) and not check_trail(x+1,y)):
		    x = x+1
		else:
		    return False
                moves = moves + 1
                count = count + 1  

def fast_up():
    global json
    old_x = json['player']['x']
    moves = 0
    while(json['player']['x'] == old_x):
        if(moves==json['player']['bombRange']):
            break
        if(hardboard[11*(json['player']['x']-1)+(json['player']['y'])] == 0 and json['softBlockBoard'][11*(json['player']['x']-1)+(json['player']['y'])] == 0 and moves>0 and not check_enemy_bomb_loc(json['player']['x']-1,json['player']['y']) and not check_trail(json['player']['x']-1,json['player']['y'])):
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'ml', 'devkey': "581b97a4da8dce85358c64c3"});
            json = r.json()            
        elif(hardboard[11*(json['player']['x']+1)+(json['player']['y'])] == 0 and json['softBlockBoard'][11*(json['player']['x']+1)+(json['player']['y'])] == 0 and moves>0 and not check_enemy_bomb_loc(json['player']['x']+1,json['player']['y']) and not check_trail(json['player']['x']+1,json['player']['y'])):
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mr', 'devkey': "581b97a4da8dce85358c64c3"});
            json = r.json() 
        else:
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mu', 'devkey': "581b97a4da8dce85358c64c3"});
            json = r.json() 
            moves = moves + 1

def fast_attack_up(bx, by):
    global json
    old_x = json['player']['x']
    old_y = json['player']['y']
    moves = 0
    while(json['player']['x'] == old_x):
        if(moves==json['player']['bombRange']):
            break
        if(hardboard[11*(json['player']['x']-1)+(json['player']['y'])] == 0 and json['softBlockBoard'][11*(json['player']['x']-1)+(json['player']['y'])] == 0 and moves>0 and not check_all_bomb_loc(json['player']['x']-1,json['player']['y'], bx, by) and not check_trail(json['player']['x']-1,json['player']['y'])):
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'ml', 'devkey': "581b97a4da8dce85358c64c3"});
            json = r.json()            
        elif(hardboard[11*(json['player']['x']+1)+(json['player']['y'])] == 0 and json['softBlockBoard'][11*(json['player']['x']+1)+(json['player']['y'])] == 0 and moves>0 and not check_all_bomb_loc(json['player']['x']+1,json['player']['y'], bx, by) and not check_trail(json['player']['x']+1,json['player']['y'])):
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mr', 'devkey': "581b97a4da8dce85358c64c3"});
            json = r.json() 
        else:
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mu', 'devkey': "581b97a4da8dce85358c64c3"});
            json = r.json() 
            moves = moves + 1
            
def fast_down():
    global json
    old_x = json['player']['x']
    moves = 0
    while(json['player']['x'] == old_x):
        if(moves==json['player']['bombRange']):
            break
        if((hardboard[11*(json['player']['x']-1)+(json['player']['y'])] == 0 and json['softBlockBoard'][11*(json['player']['x']-1)+(json['player']['y'])] == 0) and moves>0 and not check_enemy_bomb_loc(json['player']['x']-1,json['player']['y']) and not check_trail(json['player']['x']-1,json['player']['y'])):
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'ml', 'devkey': "581b97a4da8dce85358c64c3"});
            json = r.json()            
        elif(hardboard[11*(json['player']['x']+1)+(json['player']['y'])] == 0 and json['softBlockBoard'][11*(json['player']['x']+1)+(json['player']['y'])] == 0 and moves>0 and not check_enemy_bomb_loc(json['player']['x']+1,json['player']['y']) and not check_trail(json['player']['x']+1,json['player']['y'])):
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mr', 'devkey': "581b97a4da8dce85358c64c3"});
            json = r.json() 
        else:
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'md', 'devkey': "581b97a4da8dce85358c64c3"});
            json = r.json() 
            moves = moves + 1
    
def fast_attack_down(bx,by):
    global json
    old_x = json['player']['x']
    old_y = json['player']['y']
    moves = 0
    while(json['player']['x'] == old_x):
        if(moves==json['player']['bombRange']):
            break
        if((hardboard[11*(json['player']['x']-1)+(json['player']['y'])] == 0 and json['softBlockBoard'][11*(json['player']['x']-1)+(json['player']['y'])] == 0) and moves>0 and not check_all_bomb_loc(json['player']['x']-1,json['player']['y'], bx, by) and not check_trail(json['player']['x']-1,json['player']['y'])):
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'ml', 'devkey': "581b97a4da8dce85358c64c3"});
            json = r.json()            
        elif(hardboard[11*(json['player']['x']+1)+(json['player']['y'])] == 0 and json['softBlockBoard'][11*(json['player']['x']+1)+(json['player']['y'])] == 0 and moves>0 and not check_all_bomb_loc(json['player']['x']+1,json['player']['y'], bx, by) and not check_trail(json['player']['x']+1,json['player']['y'])):
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mr', 'devkey': "581b97a4da8dce85358c64c3"});
            json = r.json() 
        else:
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'md', 'devkey': "581b97a4da8dce85358c64c3"});
            json = r.json() 
            moves = moves + 1
            
def fast_left():
    global json
    old_y = json['player']['y']
    moves = 0
    while(json['player']['y'] == old_y):
        if(moves==json['player']['bombRange']):
            break
        if((hardboard[11*(json['player']['x'])+(json['player']['y']-1)] == 0 and json['softBlockBoard'][11*(json['player']['x'])+(json['player']['y']-1)] == 0) and moves>0 and not check_enemy_bomb_loc(json['player']['x'],json['player']['y']-1) and not check_trail(json['player']['x'],json['player']['y']-1)):
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mu', 'devkey': "581b97a4da8dce85358c64c3"});
            json = r.json()            
        elif(hardboard[11*(json['player']['x'])+(json['player']['y']+1)] == 0 and json['softBlockBoard'][11*(json['player']['x'])+(json['player']['y']+1)] == 0 and moves>0 and not check_enemy_bomb_loc(json['player']['x'],json['player']['y']+1) and not check_trail(json['player']['x'],json['player']['y']+1)):
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'md', 'devkey': "581b97a4da8dce85358c64c3"});
            json = r.json() 
        else:
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'ml', 'devkey': "581b97a4da8dce85358c64c3"});
            json = r.json() 
            moves = moves + 1

def fast_attack_left(bx,by):
    global json
    old_y = json['player']['y']
    old_x = json['player']['x']
    moves = 0
    while(json['player']['y'] == old_y):
        if(moves==json['player']['bombRange']):
            break
        if((hardboard[11*(json['player']['x'])+(json['player']['y']-1)] == 0 and json['softBlockBoard'][11*(json['player']['x'])+(json['player']['y']-1)] == 0) and moves>0 and not check_all_bomb_loc(json['player']['x'],json['player']['y']-1, bx, by) and not check_trail(json['player']['x'],json['player']['y']-1)):
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mu', 'devkey': "581b97a4da8dce85358c64c3"});
            json = r.json()            
        elif(hardboard[11*(json['player']['x'])+(json['player']['y']+1)] == 0 and json['softBlockBoard'][11*(json['player']['x'])+(json['player']['y']+1)] == 0 and moves>0 and not check_all_bomb_loc(json['player']['x'],json['player']['y']+1, bx, by) and not check_trail(json['player']['x'],json['player']['y']+1)):
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'md', 'devkey': "581b97a4da8dce85358c64c3"});
            json = r.json() 
        else:
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'ml', 'devkey': "581b97a4da8dce85358c64c3"});
            json = r.json() 
            moves = moves + 1
            
def fast_right():
    global json
    old_y = json['player']['y']
    moves = 0
    while(json['player']['y'] == old_y):
        if(moves==json['player']['bombRange']+1):
            break
        if((hardboard[11*(json['player']['x'])+(json['player']['y']-1)] == 0 and json['softBlockBoard'][11*(json['player']['x'])+(json['player']['y']-1)] == 0) and moves>0 and not check_enemy_bomb_loc(json['player']['x'],json['player']['y']-1) and not check_trail(json['player']['x'],json['player']['y']-1)):
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mu', 'devkey': "581b97a4da8dce85358c64c3"});
            json = r.json()            
        elif(hardboard[11*(json['player']['x'])+(json['player']['y']+1)] == 0 and json['softBlockBoard'][11*(json['player']['x'])+(json['player']['y']+1)] == 0 and moves>0 and not check_enemy_bomb_loc(json['player']['x'],json['player']['y']+1) and not check_trail(json['player']['x'],json['player']['y']+1)):
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'md', 'devkey': "581b97a4da8dce85358c64c3"});
            json = r.json() 
        else:
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mr', 'devkey': "581b97a4da8dce85358c64c3"});
            json = r.json() 
            moves = moves + 1

def fast_attack_right(bx,by):
    global json
    old_y = json['player']['y']
    old_x = json['player']['x']
    moves = 0
    while(json['player']['y'] == old_y):
        if(moves==json['player']['bombRange']+1):
            break
        if((hardboard[11*(json['player']['x'])+(json['player']['y']-1)] == 0 and json['softBlockBoard'][11*(json['player']['x'])+(json['player']['y']-1)] == 0) and moves>0 and not check_all_bomb_loc(json['player']['x'],json['player']['y']-1, bx, by) and not check_trail(json['player']['x'],json['player']['y']-1)):
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mu', 'devkey': "581b97a4da8dce85358c64c3"});
            json = r.json()            
        elif(hardboard[11*(json['player']['x'])+(json['player']['y']+1)] == 0 and json['softBlockBoard'][11*(json['player']['x'])+(json['player']['y']+1)] == 0 and moves>0 and not check_all_bomb_loc(json['player']['x'],json['player']['y']+1, bx, by) and not check_trail(json['player']['x'],json['player']['y']+1)):
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'md', 'devkey': "581b97a4da8dce85358c64c3"});
            json = r.json() 
        else:
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mr', 'devkey': "581b97a4da8dce85358c64c3"});
            json = r.json() 
            moves = moves + 1
    
def escape_up(direction):
    print("escaping up")
    global json
    global x
    global y
    old_x = json['player']['x']
    old_y = json['player']['y']
    sideMove = 0
    while(json['player']['x'] == old_x or json['player']['y'] == old_y):
        if(sideMove == 0 and hardboard[11*(json['player']['x']-1)+(json['player']['y'])] == 0 and json['softBlockBoard'][11*(json['player']['x']-1)+(json['player']['y'])] == 0 and not check_enemy_bomb_loc(json['player']['x']-1,json['player']['y']) and not check_trail(json['player']['x']-1,json['player']['y']) and direction == 'left'):
	    """
	    if(json['opponent']['x']==json['player']['x']-1 and json['opponent']['y']==json['player']['y']):
		
	    else:
	    """
	    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'ml', 'devkey': "581b97a4da8dce85358c64c3"});
	    json = r.json()
            print("moved left")
	    sideMove = 1
        elif(sideMove == 0 and hardboard[11*(json['player']['x']+1)+(json['player']['y'])] == 0 and json['softBlockBoard'][11*(json['player']['x']+1)+(json['player']['y'])] == 0 and not check_enemy_bomb_loc(json['player']['x']+1,json['player']['y']) and not check_trail(json['player']['x']+1,json['player']['y']) and direction == 'right'):
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mr', 'devkey': "581b97a4da8dce85358c64c3"});
            json = r.json()
            print("moved right")
	    sideMove = 1
        else:
	    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mu', 'devkey': "581b97a4da8dce85358c64c3"});
	    json = r.json()
	    print("moved up")
	    sideMove = 0

def attack_escape_up(bx,by, direction):
    print("escaping up")
    global json
    global x
    global y
    old_x = json['player']['x']
    old_y = json['player']['y']
    sideMove = 0
    while(json['player']['x'] == old_x or json['player']['y'] == old_y):
        if(sideMove == 0 and hardboard[11*(json['player']['x']-1)+(json['player']['y'])] == 0 and json['softBlockBoard'][11*(json['player']['x']-1)+(json['player']['y'])] == 0 and not check_all_bomb_loc(json['player']['x']-1,json['player']['y'], bx, by) and not check_trail(json['player']['x']-1,json['player']['y']) and direction == 'left'):
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'ml', 'devkey': "581b97a4da8dce85358c64c3"});
            json = r.json()
            print("moved left")
	    sideMove = 1
        elif(sideMove == 0 and hardboard[11*(json['player']['x']+1)+(json['player']['y'])] == 0 and json['softBlockBoard'][11*(json['player']['x']+1)+(json['player']['y'])] == 0 and not check_all_bomb_loc(json['player']['x']+1,json['player']['y'], bx, by) and not check_trail(json['player']['x']+1,json['player']['y']) and direction == 'right'):
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mr', 'devkey': "581b97a4da8dce85358c64c3"});
            json = r.json()
            print("moved right")
	    sideMove = 1
        else:
	    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mu', 'devkey': "581b97a4da8dce85358c64c3"});
	    json = r.json()
	    print("moved up")
	    sideMove = 0

def escape_down(direction):
    print("escaping down")
    global json
    global x
    global y
    old_x = json['player']['x']
    old_y = json['player']['y']
    sideMove = 0
    while(json['player']['x'] == old_x or old_y == json['player']['y']):
        if(sideMove == 0 and hardboard[11*(json['player']['x']-1)+(json['player']['y'])] == 0 and json['softBlockBoard'][11*(json['player']['x']-1)+(json['player']['y'])] == 0 and not check_enemy_bomb_loc(json['player']['x']-1,json['player']['y']) and not check_trail(json['player']['x']-1,json['player']['y']) and direction == 'left'):
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'ml', 'devkey': "581b97a4da8dce85358c64c3"});
            json = r.json()
            print("moved left")
	    sideMove = 1
        elif(sideMove == 0 and hardboard[11*(json['player']['x']+1)+(json['player']['y'])] == 0 and json['softBlockBoard'][11*(json['player']['x']+1)+(json['player']['y'])] == 0 and not check_enemy_bomb_loc(json['player']['x']+1,json['player']['y']) and not check_trail(json['player']['x']+1,json['player']['y']) and direction == 'right'):
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mr', 'devkey': "581b97a4da8dce85358c64c3"});
            json = r.json()
            print("moved right")
	    sideMove = 1
        else:
	    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'md', 'devkey': "581b97a4da8dce85358c64c3"});
	    json = r.json()
	    print("moved down")
	    sideMove = 0
    print("finished escaping down")
	
def attack_escape_down(bx,by, direction):
    print("escaping down")
    global json
    global x
    global y
    old_x = json['player']['x']
    old_y = json['player']['y']
    sideMove = 0
    while(json['player']['x'] == old_x or old_y == json['player']['y']):
        if(sideMove == 0 and hardboard[11*(json['player']['x']-1)+(json['player']['y'])] == 0 and json['softBlockBoard'][11*(json['player']['x']-1)+(json['player']['y'])] == 0 and not check_all_bomb_loc(json['player']['x']-1,json['player']['y'], bx, by) and not check_trail(json['player']['x']-1,json['player']['y']) and direction == 'left'):
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'ml', 'devkey': "581b97a4da8dce85358c64c3"});
            json = r.json()
            print("moved left")
	    sideMove = 1
        elif(sideMove == 0 and hardboard[11*(json['player']['x']+1)+(json['player']['y'])] == 0 and json['softBlockBoard'][11*(json['player']['x']+1)+(json['player']['y'])] == 0 and not check_all_bomb_loc(json['player']['x']+1,json['player']['y'], bx, by) and not check_trail(json['player']['x']+1,json['player']['y']) and direction == 'right'):
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mr', 'devkey': "581b97a4da8dce85358c64c3"});
            json = r.json()
            print("moved right")
	    sideMove = 1
        else:
	    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'md', 'devkey': "581b97a4da8dce85358c64c3"});
	    json = r.json()
	    print("moved down")
	    sideMove = 0

def check_for_soft():
    global json
    global x
    global y
    if(json['softBlockBoard'][11*(json['player']['x'])+(json['player']['y']-1)] == 1):
        print("soft block above")
        return True
    elif(json['softBlockBoard'][11*(json['player']['x'])+(json['player']['y']+1)] == 1):
        print(json['softBlockBoard'][11*(json['player']['x']+1)+(json['player']['y'])])
        print("soft block below")
        return True
    elif(json['softBlockBoard'][11*(json['player']['x']-1)+(json['player']['y'])] == 1):
        print("soft block left")
        return True
    elif(json['softBlockBoard'][11*(json['player']['x']+1)+(json['player']['y'])] == 1):
        print("soft block right")
        return True
    else:
        return False
    
def check_easy_bomb():
    global solved
    global json
    global x
    global y
    if(hardboard[11*(x-1)+(y-1)] == 0 and not check_enemy_bomb_loc(x-1,y-1) and not check_trail(x-1,y-1) and json['softBlockBoard'][11*(x-1)+(y-1)] == 0 and ((hardboard[11*(x)+(y-1)] == 0 and not check_enemy_bomb_loc(x,y-1) and not check_trail(x,y-1) and json['softBlockBoard'][11*(x)+(y-1)] == 0) or (hardboard[11*(x-1)+(y)] == 0 and not check_enemy_bomb_loc(x-1,y) and not check_trail(x-1,y) and json['softBlockBoard'][11*(x-1)+(y)] == 0))):
	if(not path(0,json['opponent']['x'],json['opponent']['y'],x-1,y-1,-1,-1,3)):
	    solved = False
	    print("can place (escape top left)")
	    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'b', 'devkey': "581b97a4da8dce85358c64c3"});
	    json = r.json()
	    escape_up('left')
	    return True
	solved = False
    if(hardboard[11*(x+1)+(y-1)] == 0 and not check_enemy_bomb_loc(x+1,y-1) and not check_trail(x+1,y-1) and json['softBlockBoard'][11*(x+1)+(y-1)] == 0 and((hardboard[11*(x)+(y-1)] == 0 and not check_enemy_bomb_loc(x,y-1) and not check_trail(x,y-1) and json['softBlockBoard'][11*(x)+(y-1)] == 0) or (hardboard[11*(x+1)+(y)] == 0 and not check_enemy_bomb_loc(x+1,y) and not check_trail(x+1,y) and json['softBlockBoard'][11*(x+1)+(y)] == 0))):
	if(not path(0,json['opponent']['x'],json['opponent']['y'],x+1,y-1,-1,-1,3)):
	    solved = False
	    print("can place (escape top right)")
	    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'b', 'devkey': "581b97a4da8dce85358c64c3"});
	    json = r.json()
	    escape_up('right')
	    return True
	solved = False
    if(hardboard[11*(x-1)+(y+1)] == 0 and not check_enemy_bomb_loc(x-1,y+1) and not check_trail(x-1,y+1) and json['softBlockBoard'][11*(x-1)+(y+1)] == 0 and ((hardboard[11*(x)+(y+1)] == 0 and not check_enemy_bomb_loc(x,y+1) and not check_trail(x,y+1) and json['softBlockBoard'][11*(x)+(y+1)] == 0) or (hardboard[11*(x-1)+(y)] == 0 and not check_enemy_bomb_loc(x-1,y) and not check_trail(x-1,y) and json['softBlockBoard'][11*(x-1)+(y)] == 0))):
	if(not path(0,json['opponent']['x'],json['opponent']['y'],x-1,y+1,-1,-1,2)):
	    solved = False
	    print("can place (escape bottom left)")
	    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'b', 'devkey': "581b97a4da8dce85358c64c3"});
	    json = r.json()
	    escape_down('left')
	    return True
	solved = False
    if(hardboard[11*(x+1)+(y+1)] == 0 and not check_enemy_bomb_loc(x+1,y+1) and not check_trail(x+1,y+1) and not check_trail(x+1,y+1) and json['softBlockBoard'][11*(x+1)+(y+1)] == 0 and ((hardboard[11*(x)+(y+1)] == 0 and not check_enemy_bomb_loc(x,y+1) and not check_trail(x,y+1) and json['softBlockBoard'][11*(x)+(y+1)] == 0) or (hardboard[11*(x+1)+(y)] == 0 and not check_enemy_bomb_loc(x+1,y) and not check_trail(x+1,y) and json['softBlockBoard'][11*(x+1)+(y)] == 0))):
	if(not path(0,json['opponent']['x'],json['opponent']['y'],x+1,y+1,-1,-1,2)):
	    solved = False
	    print("can place (escape bottom right)") 
	    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'b', 'devkey': "581b97a4da8dce85358c64c3"});
	    json = r.json()
	    escape_down('right')
	    return True
	solved = False
    else:
        return False

def check_attack_easy_bomb():
    global json
    global solved
    global x
    global y
    if(hardboard[11*(x-1)+(y-1)] == 0 and not check_all_bomb_loc(x-1,y-1,-1,-1) and not check_trail(x-1,y-1) and json['softBlockBoard'][11*(x-1)+(y-1)] == 0 and ((hardboard[11*(x)+(y-1)] == 0 and not check_all_bomb_loc(x,y-1,-1,-1) and not check_trail(x,y-1) and json['softBlockBoard'][11*(x)+(y-1)] == 0) or (hardboard[11*(x-1)+(y)] == 0 and not check_all_bomb_loc(x-1,y,-1,-1) and not check_trail(x-1,y) and json['softBlockBoard'][11*(x-1)+(y)] == 0))):
	if(not path(0,json['opponent']['x'],json['opponent']['y'],x-1,y-1,-1,-1,3)):
	    solved = False
	    print("can place (escape top left)")
	    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'b', 'devkey': "581b97a4da8dce85358c64c3"});
	    json = r.json()
	    attack_escape_up(json['player']['x'],json['player']['y'],'left')
	    return True
	solved = False
    if(hardboard[11*(x+1)+(y-1)] == 0 and not check_all_bomb_loc(x+1,y-1,-1,-1) and not check_trail(x+1,y-1) and json['softBlockBoard'][11*(x+1)+(y-1)] == 0 and ((hardboard[11*(x)+(y-1)] == 0 and not check_all_bomb_loc(x,y-1,-1,-1) and not check_trail(x,y-1) and json['softBlockBoard'][11*(x)+(y-1)] == 0) or (hardboard[11*(x+1)+(y)] == 0 and not check_all_bomb_loc(x+1,y,-1,-1) and not check_trail(x+1,y) and json['softBlockBoard'][11*(x+1)+(y)] == 0))):
	if(not path(0,json['opponent']['x'],json['opponent']['y'],x-1,y-1,-1,-1,3)):
	    solved = False
	    print("can place (escape top right)")
	    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'b', 'devkey': "581b97a4da8dce85358c64c3"});
	    json = r.json()
	    attack_escape_up(json['player']['x'],json['player']['y'],'right')
	    return True
	solved = False
    if(hardboard[11*(x-1)+(y+1)] == 0 and not check_all_bomb_loc(x-1,y+1,-1,-1) and not check_trail(x-1,y+1) and json['softBlockBoard'][11*(x-1)+(y+1)] == 0 and ((hardboard[11*(x)+(y+1)] == 0 and not check_all_bomb_loc(x,y+1,-1,-1) and not check_trail(x,y+1)  and json['softBlockBoard'][11*(x)+(y+1)] == 0 ) or (hardboard[11*(x-1)+(y)] == 0 and not check_all_bomb_loc(x-1,y,-1,-1) and not check_trail(x-1,y) and json['softBlockBoard'][11*(x-1)+(y)] == 0))):
	if(not path(0,json['opponent']['x'],json['opponent']['y'],x-1,y+1,-1,-1,3)):
	    solved = False
	    print("can place (escape bottom left)")
	    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'b', 'devkey': "581b97a4da8dce85358c64c3"});
	    json = r.json()
	    attack_escape_down(json['player']['x'],json['player']['y'],'left')
	    return True
	solved = False
    if(hardboard[11*(x+1)+(y+1)] == 0 and not check_all_bomb_loc(x+1,y+1,-1,-1) and not check_trail(x+1,y+1) and json['softBlockBoard'][11*(x+1)+(y+1)] == 0 and((hardboard[11*(x)+(y+1)] == 0 and not check_all_bomb_loc(x,y+1,-1,-1) and not check_trail(x,y+1) and json['softBlockBoard'][11*(x)+(y+1)] == 0 ) or (hardboard[11*(x+1)+(y)] == 0 and not check_all_bomb_loc(x+1,y,-1,-1) and not check_trail(x+1,y) and json['softBlockBoard'][11*(x+1)+(y)] == 0))):
	if(not path(0,json['opponent']['x'],json['opponent']['y'],x+1,y+1,-1,-1,3)):
	    solved = False
	    print("can place (escape bottom right)") 
	    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'b', 'devkey': "581b97a4da8dce85358c64c3"});
	    json = r.json()
	    attack_escape_down(json['player']['x'],json['player']['y'],'right')
	    return True
	solved = False
    else:
        return False

def check_long_bomb():
    #global json
    if(check_fast_up()):
        r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'b', 'devkey': "581b97a4da8dce85358c64c3"});
        json = r.json()
        print("escape fast up")
        fast_up()
        return True
    elif(check_fast_down()):
        r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'b', 'devkey': "581b97a4da8dce85358c64c3"});
        json = r.json()
        fast_down()
        print("escape fast down")
        return True
    elif(check_fast_left()):
        r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'b', 'devkey': "581b97a4da8dce85358c64c3"});
        json = r.json()   
        fast_left()
        print("escape fast left")
        return True
    elif(check_fast_right()):
        r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'b', 'devkey': "581b97a4da8dce85358c64c3"});
        json = r.json()   
        fast_right()
        print("escape fast right")
        return True
    else:
        return False

def check_attack_long_bomb():
    #global json
    if(check_attack_fast_up()):
        r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'b', 'devkey': "581b97a4da8dce85358c64c3"});
        json = r.json()
        print("escape fast up")
        fast_attack_up(json['player']['x'],json['player']['y'])
        return True
    elif(check_attack_fast_down()):
        r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'b', 'devkey': "581b97a4da8dce85358c64c3"});
        json = r.json()
        fast_attack_down(json['player']['x'],json['player']['y'])
        print("escape fast down")
        return True
    elif(check_attack_fast_left()):
        r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'b', 'devkey': "581b97a4da8dce85358c64c3"});
        json = r.json()   
        fast_attack_left(json['player']['x'],json['player']['y'])
        print("escape fast left")
        return True
    elif(check_attack_fast_right()):
        r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'b', 'devkey': "581b97a4da8dce85358c64c3"});
        json = r.json()   
        fast_attack_right(json['player']['x'],json['player']['y'])
        print("escape fast right")
        return True
    else:
        return False

def check_enemy_bomb():
    global json
    global enemymax
    global player
    print("checking enemy bomb")
    print("Enemy bomb count: " +str(json['opponent']['bombCount']))
    for i in json['bombMap']:
	tmp_arr = i.split(',')
	if(json['bombMap'][i]['owner'] != player):
	    if(abs(int(tmp_arr[0]) - json['player']['x']) <= json['opponent']['bombRange'] and json['player']['y'] == int(tmp_arr[1])):
		return True
	    if(abs(int(tmp_arr[1]) - json['player']['y']) <= json['opponent']['bombRange'] and json['player']['x'] == int(tmp_arr[0])):
		return True
    print("no enemy bomb")
    return False

def check_enemy_bomb_loc(x,y):
    global json
    global enemymax
    global player
    print("checking enemy bomb")
    print("Enemy bomb count: " +str(json['opponent']['bombCount']))
    for i in json['bombMap']:
	tmp_arr = i.split(',')
	if(json['bombMap'][i]['owner'] != player):
	    if(abs(int(tmp_arr[0]) - x) <= json['opponent']['bombRange'] and y == int(tmp_arr[1])):
		return True
	    if(abs(int(tmp_arr[1]) - y) <= json['opponent']['bombRange'] and x == int(tmp_arr[0])):
		return True
    print("no enemy bomb")
    return False

def check_all_bomb_loc(x,y, bx, by):
    global json
    global enemymax
    global player
    print("checking enemy bomb")
    print("Enemy bomb count: " +str(json['opponent']['bombCount']))
    for i in json['bombMap']:
	tmp_arr = i.split(',')
	if(int(tmp_arr[0]) == int(bx) and int(tmp_arr[1]) == int(by)):
	    continue
	elif(abs(int(tmp_arr[0]) - x) <= json['opponent']['bombRange'] and y == int(tmp_arr[1])):
	    return True
	elif(abs(int(tmp_arr[1]) - y) <= json['opponent']['bombRange'] and x == int(tmp_arr[0])):
	    return True
    print("no enemy bomb")
    return False
"""
    if(json['opponent']['bombCount'] < enemymax):
        if(abs(json['opponent']['x'] - json['player']['x']) <= json['opponent']['bombRange']):
            return True
        if(abs(json['opponent']['y'] - json['player']['y']) <= json['opponent']['bombRange']):
            return True
    else:
        print("no enemy bomb")
        return False
"""
def find_bomb_close(x,y):
    global json
    global enemymax
    global player
    print("checking enemy bomb")
    print("Enemy bomb count: " +str(json['opponent']['bombCount']))
    for i in json['bombMap']:
	tmp_arr = i.split(',')
	if(abs(int(tmp_arr[0]) - json['player']['x']) <= json['opponent']['bombRange'] and json['player']['y'] == int(tmp_arr[1])):
	    return tmp_arr
	elif(abs(int(tmp_arr[1]) - json['player']['y']) <= json['opponent']['bombRange'] and json['player']['x'] == int(tmp_arr[0])):
	    return tmp_arr
    tmp_arr[0] = -1
    tmp_arr[1] = -1
    return tmp_arr

def gtfo():
    global bombmax
    global json
    x = json['opponent']['x']
    y = json['opponent']['y']
    print('bomb in question: ('+str(x)+','+str(y)+')')
    tmp_arr = find_bomb_close(json['player']['x'],json['player']['y'])
    if(tmp_arr[0] > json['player']['x'] and json['player']['y'] == tmp_arr[1]):
	left = True
        while(json['player']['y'] == tmp_arr[1]):
            if(hardboard[11*(json['player']['x'])+(json['player']['y']-1)] == 0 and json['softBlockBoard'][11*(json['player']['x'])+(json['player']['y']-1)] == 0 and not check_all_bomb_loc(json['player']['x'],json['player']['y']-1,-1,-1) and not check_trail(json['player']['x'],json['player']['y']-1) and not(json['player']['x'] == x and json['player']['y']-1 == y) and not(json['player']['x'] == tmp_arr[0] and json['player']['y']-1 == tmp_arr[1])):
		    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mu', 'devkey': "581b97a4da8dce85358c64c3"});
		    json = r.json()
            elif(hardboard[11*(json['player']['x'])+(json['player']['y']+1)] == 0 and json['softBlockBoard'][11*(json['player']['x'])+(json['y']+1)] == 0 and not check_all_bomb_loc(json['player']['x'],json['player']['y']+1,-1,-1) and not check_trail(json['x'],json['player']['y']+1) and not(json['player']['x'] == x and json['player']['y']+1 == y) and not(json['player']['x'] == tmp_arr[0] and json['player']['y']+1 == tmp_arr[1])):
                r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'md', 'devkey': "581b97a4da8dce85358c64c3"}); 
		json = r.json()
            elif(hardboard[11*(x-1)+(y)] == 0 and json['softBlockBoard'][11*(json['player']['x']-1)+(json['player']['y'])] == 0 and left and not check_all_bomb_loc(json['player']['x']-1,json['player']['y'],-1,-1) and not check_trail(json['player']['x']-1,json['player']['y']) and not(json['player']['x']-1 == x and json['player']['y'] == y) and not(json['player']['x']-1 == tmp_arr[0] and json['player']['y'] == tmp_arr[1])):
                r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'ml', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
	    elif(check_portal_escape()):
		portal_escape()
            else:
                left = False
                r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mr', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
    elif(tmp_arr[0] < json['player']['x'] and json['player']['y'] == tmp_arr[1]):
	right = True
        while(json['player']['y'] == tmp_arr[1]):
            if(hardboard[11*(json['player']['x'])+(json['player']['y']-1)] == 0 and json['softBlockBoard'][11*(json['player']['x'])+(json['player']['y']-1)] == 0 and not check_all_bomb_loc(json['player']['x'],json['player']['y']-1,-1,-1) and not check_trail(json['player']['x'],json['player']['y']-1) and not(json['player']['x'] == x and json['player']['y']-1 == y) and not(json['player']['x'] == tmp_arr[0] and json['player']['y']-1 == tmp_arr[1])):
                r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mu', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
            elif(hardboard[11*(json['player']['x'])+(json['player']['y']+1)] == 0 and json['softBlockBoard'][11*(json['player']['x'])+(json['player']['y']+1)] == 0 and not check_all_bomb_loc(json['player']['x'],json['player']['y']+1,-1,-1) and not check_trail(json['player']['x'],json['player']['y']+1) and not(json['player']['x'] == x and json['player']['y']+1 == y) and not(json['player']['x'] == tmp_arr[0] and json['player']['y']+1 == tmp_arr[1])):
                r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'md', 'devkey': "581b97a4da8dce85358c64c3"});  
		json = r.json()
            elif(hardboard[11*(json['player']['x']+1)+(json['player']['y'])] == 0 and json['softBlockBoard'][11*(json['player']['x']+1)+(json['player']['y'])] == 0 and right and not check_all_bomb_loc(json['player']['x']+1,json['player']['y'],-1,-1) and not check_trail(json['player']['x']+1,json['player']['y']) and not(json['player']['x']+1 == x and json['player']['y'] == y) and not(json['player']['x']+1 == tmp_arr[0] and json['player']['y'] == tmp_arr[1])):
                r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mr', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
	    elif(check_portal_escape()):
		portal_escape()
            else:
                right = False
                r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'ml', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
    elif(tmp_arr[1] > json['player']['y'] and json['player']['x'] == tmp_arr[0]):
	up = True
        while(json['player']['x'] == tmp_arr[0]):
            if(hardboard[11*(json['player']['x']-1)+(json['player']['y'])] == 0 and json['softBlockBoard'][11*(json['player']['x']-1)+(json['player']['y'])] == 0 and not check_all_bomb_loc(json['player']['x']-1,json['player']['y'],-1,-1) and not check_trail(json['player']['x']-1,json['player']['y']) and not(json['player']['x']-1 == x and json['player']['y'] == y) and not(json['player']['x']-1 == tmp_arr[0] and json['player']['y']-1 == tmp_arr[1])):
                r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'ml', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
            elif(hardboard[11*(json['player']['x']+1)+(json['player']['y'])] == 0 and json['softBlockBoard'][11*(json['player']['x']+1)+(json['player']['y'])] == 0 and not check_all_bomb_loc(json['player']['x']+1,json['player']['y'],-1,-1) and not check_trail(json['player']['x']+1,json['player']['y']) and not(json['player']['x']+1 == x and json['player']['y'] == y) and not(json['player']['x']+1 == tmp_arr[0] and json['player']['y'] == tmp_arr[1])):
                r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mr', 'devkey': "581b97a4da8dce85358c64c3"});  
		json = r.json()
            elif(hardboard[11*(json['player']['x'])+(json['player']['y']-1)] == 0 and json['softBlockBoard'][11*(json['player']['x'])+(json['player']['y']-1)] == 0 and up and not check_all_bomb_loc(json['player']['x'],json['player']['y']-1,-1,-1) and not check_trail(json['player']['x'],json['player']['y']-1) and not(json['player']['x'] == x and json['player']['y']-1 == y) and not(json['player']['x'] == tmp_arr[0] and json['player']['y']-1 == tmp_arr[1])):
                r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mu', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
	    elif(check_portal_escape()):
		portal_escape()
            else:
                up = False
                r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'md', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
    elif(tmp_arr[1] < json['player']['y'] and json['player']['x'] == tmp_arr[0]):
	down = True
        while(json['player']['x'] == x):
            if(hardboard[11*(json['player']['x']-1)+(json['player']['y'])] == 0 and json['softBlockBoard'][11*(json['player']['x']-1)+(json['player']['y'])] == 0 and not check_all_bomb_loc(json['player']['x']-1,json['player']['y'],-1,-1) and not check_trail(json['player']['x']-1,json['player']['y']) and not(json['player']['x']-1 == x and json['player']['y'] == y) and not(json['player']['x']-1 == tmp_arr[0] and json['player']['y'] == tmp_arr[1])):
                r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'ml', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
            elif(hardboard[11*(json['player']['x']+1)+(json['player']['y'])] == 0 and json['softBlockBoard'][11*(json['player']['x']+1)+(json['player']['y'])] == 0 and not check_all_bomb_loc(json['player']['x']+1,json['player']['y'],-1,-1) and not check_trail(json['player']['x']+1,json['player']['y']) and not(json['player']['x']+1 == x and json['player']['y'] == y) and not(json['player']['x']+1 == tmp_arr[0] and json['player']['y'] == tmp_arr[1])):
                r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mr', 'devkey': "581b97a4da8dce85358c64c3"}); 
		json = r.json()
            elif(hardboard[11*(json['player']['x'])+(json['player']['y']+1)] == 0 and json['softBlockBoard'][11*(json['player']['x'])+(json['player']['y']+1)] == 0 and down and not check_all_bomb_loc(json['player']['x'],json['player']['y']+1,-1,-1) and not check_trail(json['player']['x'],josn['player']['y']+1) and not(json['player']['x'] == x and json['player']['y']+1 == y) and not(json['player']['x'] == tmp_arr[0] and json['player']['y']+1 == tmp_arr[1])):
                r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'md', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
	    elif(check_portal_escape()):
		portal_escape()
            else:
                down = False
                r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mu', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
    else:
        while(json['opponent']['bombCount'] ==  0):
            wait()
        wait()

def check_enemy():
    global json
    if(json['player']['y'] == json['opponent']['y'] and abs(json['player']['x']-json['opponent']['x'])<=json['player']['bombRange']):
        return True
    if(json['player']['x'] == json['opponent']['x'] and abs(json['player']['y']-json['opponent']['y'])<=json['player']['bombRange']):
        return True
    else:
        return False

def napalm():
    global json
    global solved
    i = 0
    if(json['player']['x'] == json['opponent']['x'] or json['player']['x'] == json['opponent']['x']+1):
        while(i <= 2):
            if(hardboard[11*(json['player']['x']-i)+json['player']['y']] == 1 or json['softBlockBoard'][11*(json['player']['x']-i)+json['player']['y']] == 1):
                break
            if(i==2):
                if(hardboard[11*(json['player']['x']-i)+(json['player']['y']-1)] == 0 and json['softBlockBoard'][11*(json['player']['x']-i)+(json['player']['y']-1)] == 0 and not check_enemy_bomb_loc(json['player']['x']-i,json['player']['y']-1) and not check_trail(json['player']['x']-i,json['player']['y']-1) and not path(json['player']['x']-i,json['player']['y']-1)):
		    solved = False
                    napalm_left()
                    return True
                if(hardboard[11*(json['player']['x']-i)+(json['player']['y']+1)] == 0 and json['softBlockBoard'][11*(json['player']['x']-i)+(json['player']['y']+1)] == 0 and not check_enemy_bomb_loc(json['player']['x']-i,json['player']['y']+1) and not check_trail(json['player']['x']-i,json['player']['y']+1) and not path(json['player']['x']-i,json['player']['y']+1)):
		    solved = False
                    napalm_left()
                    return True
            i=i+1
    i = 0
    if(json['player']['x'] == json['opponent']['x'] or json['player']['x'] == json['opponent']['x']-1):
        while(i <= 2):
            if(hardboard[11*(json['player']['x']+i)+json['player']['y']] == 1 or json['softBlockBoard'][11*(json['player']['x']+i)+json['player']['y']] == 1):
                break
            if(i==2):
                if(hardboard[11*(json['player']['x']+i)+(json['player']['y']-1)] == 0 and json['softBlockBoard'][11*(json['player']['x']+i)+(json['player']['y']-1)] == 0 and not check_enemy_bomb_loc(json['player']['x']+i,json['player']['y']-1) and not check_trail(json['player']['x']+i,json['player']['y']-1) and not path(json['player']['x']+i,json['player']['y']-1)):
                    napalm_right()
		    solved = False
                    return True
                if(hardboard[11*(json['player']['x']+i)+(json['player']['y']+1)] == 0 and json['softBlockBoard'][11*(json['player']['x']+i)+(json['player']['y']+1)] == 0 and not check_enemy_bomb_loc(json['player']['x']+i,json['player']['y']+1) and not check_trail(json['player']['x']+i,json['player']['y']+1) and not path(json['player']['x']+i,json['player']['y']+1)):
		    solved = False
                    napalm_right()
                    return True
            i=i+1
    i = 0
    if(json['player']['y'] == json['opponent']['y'] or json['player']['y'] == json['opponent']['y']+1):
        while(i <= 2):
            if(hardboard[11*(json['player']['x'])+(json['player']['y']-i)] == 1 or json['softBlockBoard'][11*(json['player']['x'])+(json['player']['y']-i)] == 1):
                break
            if(i==2):
                if(hardboard[11*(json['player']['x']-1)+(json['player']['y']-i)] == 0 and json['softBlockBoard'][11*(json['player']['x']-1)+(json['player']['y']-i)] == 0 and not check_enemy_bomb_loc(json['player']['x']-1,json['player']['y']-i) and not check_trail(json['player']['x']-1,json['player']['y']-i) and not path(json['player']['x']-1,json['player']['y']-i)):
		    solved = False
                    napalm_up()
                    return True
                if(hardboard[11*(json['player']['x']+1)+(json['player']['y']-i)] == 0 and json['softBlockBoard'][11*(json['player']['x']+1)+(json['player']['y']-i)] == 0 and not check_enemy_bomb_loc(json['player']['x']+1,json['player']['y']-i) and not check_trail(json['player']['x']+1,json['player']['y']-i) and not path(json['player']['x']+1,json['player']['y']-i)):
		    solved = False
                    napalm_up()
                    return True
            i=i+1
    i = 0
    if(json['player']['y'] == json['opponent']['y'] or json['player']['y'] == json['opponent']['y']-1):
        while(i <= 2):
            if(hardboard[11*(json['player']['x'])+(json['player']['y']+i)] == 1 or json['softBlockBoard'][11*(json['player']['x'])+(json['player']['y']+i)] == 1):
                break
            if(i==2):
                if(hardboard[11*(json['player']['x']-1)+(json['player']['y']+i)] == 0 and json['softBlockBoard'][11*(json['player']['x']-1)+(json['player']['y']+i)] == 0 and not check_enemy_bomb_loc(json['player']['x']-1,json['player']['y']+i) and not check_trail(json['player']['x']-1,json['player']['y']+i) and not path(json['player']['x']-1,json['player']['y']+i)):
		    solved = False
                    napalm_down()
                    return True
                if(hardboard[11*(json['player']['x']+1)+(json['player']['y']+i)] == 0 and json['softBlockBoard'][11*(json['player']['x']+1)+(json['player']['y']+i)] == 0 and not check_enemy_bomb_loc(json['player']['x']+1,json['player']['y']+i) and not check_trail(json['player']['x']-1,json['player']['y']+i) and not path(json['player']['x']+1,json['player']['y']+i)):
		    solved = False
                    napalm_down()
                    return True
            i=i+1
    return False

def napalm_left():
    print("napalm left")
    global json
    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'b', 'devkey': "581b97a4da8dce85358c64c3"});
    json = r.json()
    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'ml', 'devkey': "581b97a4da8dce85358c64c3"});
    json = r.json()
    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'b', 'devkey': "581b97a4da8dce85358c64c3"});
    json = r.json()
    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'ml', 'devkey': "581b97a4da8dce85358c64c3"});
    json = r.json()
    if(hardboard[11*(json['player']['x'])+(json['player']['y']-1)] == 0 and json['softBlockBoard'][11*(json['player']['x'])+(json['player']['y']-1)] == 0 and not check_enemy_bomb_loc(json['player']['x'],json['player']['y']-1) and not check_trail(json['player']['x'],json['player']['y']-1)):
        r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mu', 'devkey': "581b97a4da8dce85358c64c3"});
        json = r.json()  
    else:
        r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'md', 'devkey': "581b97a4da8dce85358c64c3"});
        json = r.json()
    
def napalm_right():
    print("napalm right")
    global json
    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'b', 'devkey': "581b97a4da8dce85358c64c3"});
    json = r.json()
    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mr', 'devkey': "581b97a4da8dce85358c64c3"});
    json = r.json()
    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'b', 'devkey': "581b97a4da8dce85358c64c3"});
    json = r.json()
    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mr', 'devkey': "581b97a4da8dce85358c64c3"});
    json = r.json()
    if(hardboard[11*(json['player']['x'])+(json['player']['y']-1)] == 0 and json['softBlockBoard'][11*(json['player']['x'])+(json['player']['y']-1)] == 0 and not check_enemy_bomb_loc(json['player']['x'],json['player']['y']-1) and not check_trail(json['player']['x'],json['player']['y']-1)):
        r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mu', 'devkey': "581b97a4da8dce85358c64c3"});
        json = r.json()  
    else:
        r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'md', 'devkey': "581b97a4da8dce85358c64c3"});
        json = r.json()
        
def napalm_up():
    print("napalm up")
    global json
    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'b', 'devkey': "581b97a4da8dce85358c64c3"});
    json = r.json()
    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mu', 'devkey': "581b97a4da8dce85358c64c3"});
    json = r.json()
    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'b', 'devkey': "581b97a4da8dce85358c64c3"});
    json = r.json()
    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mu', 'devkey': "581b97a4da8dce85358c64c3"});
    json = r.json()
    if(hardboard[11*(json['player']['x']-1)+(json['player']['y'])] == 0 and json['softBlockBoard'][11*(json['player']['x']-1)+(json['player']['y'])] == 0 and not check_enemy_bomb_loc(json['player']['x']-1,json['player']['y']) and not check_trail(json['player']['x']-1,json['player']['y'])):
        r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'ml', 'devkey': "581b97a4da8dce85358c64c3"});
        json = r.json()  
    else:
        r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mr', 'devkey': "581b97a4da8dce85358c64c3"});
        json = r.json()

def napalm_down():
    print("napalm down")
    global json
    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'b', 'devkey': "581b97a4da8dce85358c64c3"});
    json = r.json()
    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'md', 'devkey': "581b97a4da8dce85358c64c3"});
    json = r.json()
    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'b', 'devkey': "581b97a4da8dce85358c64c3"});
    json = r.json()
    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'md', 'devkey': "581b97a4da8dce85358c64c3"});
    json = r.json()
    if(hardboard[11*(json['player']['x']-1)+(json['player']['y'])] == 0 and json['softBlockBoard'][11*(json['player']['x']-1)+(json['player']['y'])] == 0 and not check_enemy_bomb_loc(json['player']['x']-1,json['player']['y']) and not check_trail(json['player']['x']-1,json['player']['y'])):
        r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'ml', 'devkey': "581b97a4da8dce85358c64c3"});
        json = r.json()  
    else:
        r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mr', 'devkey': "581b97a4da8dce85358c64c3"});
        json = r.json()
	
def path(distance, x, y, wx, wy, ox, oy, num):
    global json
    global solved
    if(distance > num):
	return False
    if(wx==x and wy==y and not solved):
	solved = True
	return True
    if(x==1 and y==1):
	if(hardboard[11*(x+1)+(y)] == 0 and json['softBlockBoard'][11*(x+1)+(y)] == 0 and (x+1!=ox or y!=oy) and not solved):
	    path(distance+1,x+1,y,wx,wy,x,y,num)
	if(hardboard[11*(x)+(y+1)] == 0 and json['softBlockBoard'][11*(x)+(y+1)] == 0 and (x!=ox or y+1!=oy) and not solved):
	    path(distance+1,x,y+1,wx,wy,x,y,num)
    elif(x==1 and y==9):
	if(hardboard[11*(x+1)+(y)] == 0 and json['softBlockBoard'][11*(x+1)+(y)] == 0 and (x+1!=ox or y!=oy) and not solved):
	    path(distance+1,x+1,y,wx,wy,x,y,num)
	if(hardboard[11*(x)+(y-1)] == 0 and json['softBlockBoard'][11*(x)+(y-1)] == 0 and (x!=ox or y-1!=oy) and not solved):
	    path(distance+1,x,y-1,wx,wy,x,y,num)
    elif(x==9 and y==1):
	if(hardboard[11*(x-1)+(y)] == 0 and json['softBlockBoard'][11*(x-1)+(y)] == 0 and (x-1!=ox or y!=oy) and not solved):
	    path(distance+1,x-1,y,wx,wy,x,y,num)
	if(hardboard[11*(x)+(y+1)] == 0 and json['softBlockBoard'][11*(x)+(y+1)] == 0 and (x!=ox or y+1!=oy) and not solved):
	    path(distance+1,x,y+1,wx,wy,x,y,num)
    elif(x==9 and y==9):
	if(hardboard[11*(x-1)+(y)] == 0 and json['softBlockBoard'][11*(x-1)+(y)] == 0 and (x-1!=ox or y!=oy) and not solved):
	    path(distance+1,x-1,y,wx,wy,x,y,num)
	if(hardboard[11*(x)+(y-1)] == 0 and json['softBlockBoard'][11*(x)+(y-1)] == 0 and (x!=ox or y-1!=oy) and not solved):
	    path(distance+1,x,y-1,wx,wy,x,y,num)
    elif(x==1):
	if(hardboard[11*(x)+(y-1)] == 0 and json['softBlockBoard'][11*(x)+(y-1)] == 0 and (x!=ox or y-1!=oy) and not solved):
	    path(distance+1,x,y-1,wx,wy,x,y,num)
	if(hardboard[11*(x)+(y+1)] == 0 and json['softBlockBoard'][11*(x)+(y+1)] == 0 and (x!=ox or y+1!=oy) and not solved):
	    path(distance+1,x,y+1,wx,wy,x,y,num)
	if(hardboard[11*(x+1)+(y)] == 0 and json['softBlockBoard'][11*(x+1)+(y)] == 0 and (x+1!=ox or y!=oy) and not solved):
	    path(distance+1,x+1,y,wx,wy,x,y,num)
    elif(x==9):
	if(hardboard[11*(x)+(y-1)] == 0 and json['softBlockBoard'][11*(x)+(y-1)] == 0 and (x!=ox or y-1!=oy) and not solved):
	    path(distance+1,x,y-1,wx,wy,x,y,num)
	if(hardboard[11*(x)+(y+1)] == 0 and json['softBlockBoard'][11*(x)+(y+1)] == 0 and (x!=ox or y+1!=oy) and not solved):
	    path(distance+1,x,y+1,wx,wy,x,y,num)
	if(hardboard[11*(x-1)+(y)] == 0 and json['softBlockBoard'][11*(x-1)+(y)] == 0 and (x-1!=ox or y!=oy) and not solved):
	    path(distance+1,x-1,y,wx,wy,x,y,num)
    elif(y==1):
	if(hardboard[11*(x-1)+(y)] == 0 and json['softBlockBoard'][11*(x-1)+(y)] == 0 and (x-1!=ox or y!=oy) and not solved):
	    path(distance+1,x-1,y,wx,wy,x,y,num)
	if(hardboard[11*(x+1)+(y)] == 0 and json['softBlockBoard'][11*(x+1)+(y)] == 0 and (x+1!=ox or y!=oy) and not solved):
	    path(distance+1,x+1,y,wx,wy,x,y,num)
	if(hardboard[11*(x)+(y+1)] == 0 and json['softBlockBoard'][11*(x)+(y+1)] == 0 and (x!=ox or y+1!=oy) and not solved):
	    path(distance+1,x,y+1,wx,wy,x,y,num)
    elif(y==9):
	if(hardboard[11*(x-1)+(y)] == 0 and json['softBlockBoard'][11*(x-1)+(y)] == 0 and (x-1!=ox or y!=oy) and not solved):
	    path(distance+1,x-1,y,wx,wy,x,y,num)
	if(hardboard[11*(x+1)+(y)] == 0 and json['softBlockBoard'][11*(x+1)+(y)] == 0 and (x+1!=ox or y!=oy) and not solved):
	    path(distance+1,x+1,y,wx,wy,x,y,num)
	if(hardboard[11*(x)+(y-1)] == 0 and json['softBlockBoard'][11*(x)+(y-1)] == 0 and (x!=ox or y-1!=oy) and not solved):
	    path(distance+1,x,y-1,wx,wy,x,y,num)
    else:
	if(hardboard[11*(x-1)+(y)] == 0 and json['softBlockBoard'][11*(x-1)+(y)] == 0 and (x-1!=ox or y!=oy) and not solved):
	    path(distance+1,x-1,y,wx,wy,x,y,num)
	if(hardboard[11*(x+1)+(y)] == 0 and json['softBlockBoard'][11*(x+1)+(y)] == 0 and (x+1!=ox or y!=oy) and not solved):
	    path(distance+1,x+1,y,wx,wy,x,y,num)
	if(hardboard[11*(x)+(y-1)] == 0 and json['softBlockBoard'][11*(x)+(y-1)] == 0 and (x!=ox or y-1!=oy) and not solved):
	    path(distance+1,x,y-1,wx,wy,x,y,num)
	if(hardboard[11*(x)+(y+1)] == 0 and json['softBlockBoard'][11*(x)+(y+1)] == 0 and (x!=ox or y+1!=oy) and not solved):
	    path(distance+1,x,y+1,wx,wy,x,y,num)

def move():
    global json
    global oldMove
    global player
    possibleMoving = ['mu', 'ml', 'mr', 'md']
    print("can't place")
    #"""
    while(1):
	if(player==0):
	    if(hardboard[11*(json['player']['x'])+(json['player']['y']+1)] == 0 and json['softBlockBoard'][11*(json['player']['x'])+(json['player']['y']+1)] ==0 and oldMove != "md" and not check_enemy_bomb_loc(json['player']['x'],json['player']['y']+1) and not check_trail(json['player']['x'],json['player']['y']+1) and not check_portal_kill(json['player']['x'],json['player']['y']+1,False)):
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'md', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
		break
	    elif(hardboard[11*(json['player']['x']+1)+(json['player']['y'])] == 0 and json['softBlockBoard'][11*(json['player']['x']+1)+(json['player']['y'])] == 0 and oldMove != "mr" and not check_enemy_bomb_loc(json['player']['x']+1,json['player']['y']) and not check_trail(json['player']['x']+1,json['player']['y']) and not check_portal_kill(json['player']['x']+1,json['player']['y'],False)):
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mr', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
		break
	    elif(hardboard[11*(json['player']['x']-1)+(json['player']['y'])] == 0 and json['softBlockBoard'][11*(json['player']['x']-1)+(json['player']['y'])] == 0 and not check_enemy_bomb_loc(json['player']['x']-1,json['player']['y']) and not check_trail(json['player']['x']-1,json['player']['y']) and not check_portal_kill(json['player']['x']-1,json['player']['y'],False)):
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'ml', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()  
		oldMove = "mr"
		break
	    elif(oldMove == "mr"):
		oldMove = ""
		continue
	    elif(hardboard[11*(json['player']['x'])+(json['player']['y']-1)] == 0 and json['softBlockBoard'][11*(json['player']['x'])+(json['player']['y']-1)] == 0 and not check_enemy_bomb_loc(json['player']['x'],json['player']['y']-1) and not check_trail(json['player']['x'],json['player']['y']-1) and not check_portal_kill(json['player']['x'],json['player']['y']-1,False)):
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mu', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()  
		oldMove = "md"
		break
	    elif(oldMove == "md"):
		oldMove = ""
	    else:
		if(check_enemy_bomb()):
		    portal_escape()
		else:
		    wait()
	else:
	    if(hardboard[11*(json['player']['x'])+(json['player']['y']-1)] == 0 and json['softBlockBoard'][11*(json['player']['x'])+(json['player']['y']-1)] ==0 and oldMove != "mu" and not check_enemy_bomb_loc(json['player']['x'],json['player']['y']-1) and not check_trail(json['player']['x'],json['player']['y']-1) and not check_portal_kill(json['player']['x'],json['player']['y']-1,False)):
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mu', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
		break
	    elif(hardboard[11*(json['player']['x']-1)+(json['player']['y'])] == 0 and json['softBlockBoard'][11*(json['player']['x']-1)+(json['player']['y'])] == 0 and oldMove != "ml" and not check_enemy_bomb_loc(json['player']['x']-1,json['player']['y']) and not check_trail(json['player']['x']-1,json['player']['y']) and not check_portal_kill(json['player']['x']-1,json['player']['y'],False)):
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'ml', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
		break
	    elif(hardboard[11*(json['player']['x']+1)+(json['player']['y'])] == 0 and json['softBlockBoard'][11*(json['player']['x']+1)+(json['player']['y'])] == 0 and not check_enemy_bomb_loc(json['player']['x']+1,json['player']['y']) and not check_trail(json['player']['x']+1,json['player']['y']) and not check_portal_kill(json['player']['x']+1,json['player']['y'],False)):
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mr', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()  
		oldMove = "ml"
		break
	    elif(oldMove == "ml"):
		oldMove = ""
		continue
	    elif(hardboard[11*(json['player']['x'])+(json['player']['y']+1)] == 0 and json['softBlockBoard'][11*(json['player']['x'])+(json['player']['y']+1)] == 0 and not check_enemy_bomb_loc(json['player']['x'],json['player']['y']+1) and not check_trail(json['player']['x'],json['player']['y']+1) and not check_portal_kill(json['player']['x'],json['player']['y']+1,False)):
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'md', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()  
		oldMove = "mu"
		break
	    elif(oldMove == "mu"):
		oldMove = ""
	    else:
		if(check_enemy_bomb()):
		    portal_escape()
		else:
		    wait()
    """
    randomMove = random.randint(0,len(possibleMoving)-1)
    print("Move:"+possibleMoving[randomMove])
    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': possibleMoving[randomMove], 'devkey': "581b97a4da8dce85358c64c3"});
    json = r.json()
    """   
def check_bomb_direction():
    global json
    global enemymax
    global player
    print("checking enemy bomb")
    print("Enemy bomb count: " +str(json['opponent']['bombCount']))
    for i in json['bombMap']:
	tmp_arr = i.split(',')
	if(json['bombMap'][i]['owner'] != player):
	    if(abs(int(tmp_arr[0]) - json['player']['x']) <= json['opponent']['bombRange'] and json['player']['y'] == int(tmp_arr[1])):
		print("same level")
		return True
	    if(abs(int(tmp_arr[1]) - json['player']['y']) <= json['opponent']['bombRange'] and json['player']['x'] == int(tmp_arr[0])):
		print("diff level")
		return False

def check_portal_escape():
    global json
    can = 0
    if(check_enemy_bomb()):
	if(check_bomb_direction()):
	    if(hardboard[11*(json['player']['x'])+(json['player']['y']-1)] == 1 or json['softBlockBoard'][11*(json['player']['x'])+(json['player']['y']-1)] == 1):
		can = 1
	    elif(hardboard[11*(json['player']['x'])+(json['player']['y']+1)] == 1 or json['softBlockBoard'][11*(json['player']['x'])+(json['player']['y']+1)] == 1):
		can = 1
	    elif(hardboard[11*(json['player']['x']-1)+(json['player']['y'])] == 1 or json['softBlockBoard'][11*(json['player']['x']-1)+(json['player']['y'])] == 1):
		can = 1
	    elif(hardboard[11*(json['player']['x']+1)+(json['player']['y'])] == 1 or json['softBlockBoard'][11*(json['player']['x']+1)+(json['player']['y'])] == 1):
		can = 1
	    else:
		can = 0
	else:
	    if(hardboard[11*(json['player']['x']-1)+(json['player']['y'])] == 1 or json['softBlockBoard'][11*(json['player']['x']-1)+(json['player']['y'])] == 1):
		can = 1
	    elif(hardboard[11*(json['player']['x']+1)+(json['player']['y'])] == 1 or json['softBlockBoard'][11*(json['player']['x']+1)+(json['player']['y'])] == 1):
		can = 1
	    elif(hardboard[11*(json['player']['x'])+(json['player']['y']-1)] == 1 or json['softBlockBoard'][11*(json['player']['x'])+(json['player']['y']-1)] == 1):
		can = 1
	    elif(hardboard[11*(json['player']['x'])+(json['player']['y']+1)] == 1 or json['softBlockBoard'][11*(json['player']['x'])+(json['player']['y']+1)] == 1):
		can = 1
	    else:
		can = 0
    if(can == 1):
	if(json['player']['bluePortal']['direction']==0):
	    if(check_portal_kill(json['player']['x']-1,json['player']['y'],False)):
		return False
	    return True
	if(json['player']['bluePortal']['direction']==1):
	    if(check_portal_kill(json['player']['x'],json['player']['y']-1,False)):
		return False
	    return True
	if(json['player']['bluePortal']['direction']==2):
	    if(check_portal_kill(json['player']['x']+1,json['player']['y'],False)):
		return False
	    return True
	if(json['player']['bluePortal']['direction']==3):
	    if(check_portal_kill(json['player']['x'],json['player']['y']+1,False)):
		return False
	    return True
    else:
	return False

def portal_escape():
    global json
    if(check_enemy_bomb()):
	if(check_bomb_direction()):
	    if(hardboard[11*(json['player']['x'])+(json['player']['y']-1)] == 1 or json['softBlockBoard'][11*(json['player']['x'])+(json['player']['y']-1)] == 1):
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'tu', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'op', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mu', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
	    elif(hardboard[11*(json['player']['x'])+(json['player']['y']+1)] == 1 or json['softBlockBoard'][11*(json['player']['x'])+(json['player']['y']+1)] == 1):
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'td', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'op', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'md', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
	    elif(hardboard[11*(json['player']['x']-1)+(json['player']['y'])] == 1 or json['softBlockBoard'][11*(json['player']['x']-1)+(json['player']['y'])] == 1):
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'tl', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'op', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'ml', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
	    elif(hardboard[11*(json['player']['x']+1)+(json['player']['y'])] == 1 or json['softBlockBoard'][11*(json['player']['x']+1)+(json['player']['y'])] == 1):
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'tr', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'op', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mr', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
	else:
	    if(hardboard[11*(json['player']['x']-1)+(json['player']['y'])] == 1 or json['softBlockBoard'][11*(json['player']['x']-1)+(json['player']['y'])] == 1):
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'tl', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'op', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'ml', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
	    elif(hardboard[11*(json['player']['x']+1)+(json['player']['y'])] == 1 or json['softBlockBoard'][11*(json['player']['x']+1)+(json['player']['y'])] == 1):
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'tr', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'op', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mr', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
	    elif(hardboard[11*(json['player']['x'])+(json['player']['y']-1)] == 1 or json['softBlockBoard'][11*(json['player']['x'])+(json['player']['y']-1)] == 1):
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'tu', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'op', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mu', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
	    elif(hardboard[11*(json['player']['x'])+(json['player']['y']+1)] == 1 or json['softBlockBoard'][11*(json['player']['x'])+(json['player']['y']+1)] == 1):
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'td', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'op', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'md', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()

def wait():
    global json
    global bombmax
    global item
    if(check_all_bomb_loc(json['player']['x'],json['player']['y'],-1,-1)):
	    portal_escape()
    elif(json['player']['coins']>=5):
        if(item == 0 and json['player']['bombRange']<7):
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'buy_range', 'devkey': "581b97a4da8dce85358c64c3"});
	    json = r.json()
            item = 1
        elif(item==1 and json['player']['bombPierce']<4):
            r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'buy_pierce', 'devkey': "581b97a4da8dce85358c64c3"});
	    json = r.json()
            item = 0
        else:
	    if(bombmax ==2):
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'buy_count', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
		bombmax = bombmax+1
		print("bombmax: " + str(bombmax))
	    else:
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'buy_pierce', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
    else:
        r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': ' ', 'devkey': "581b97a4da8dce85358c64c3"});
	json = r.json()
    print("bomb down")
    print("item1: " +str(item))

def check_trail(x,y):
    global json
    for i in json['trailMap']:
	tmp_arr = i.split(',')
	if(int(tmp_arr[0])==x and int(tmp_arr[1])==y):
	    return True
    return False
   
def check_portal_kill(x,y,attack):
    global json
    global player
    player1 = 0
    p1bp = ''
    p1bo = 0
    p1op = ''
    p1oo = 0
    player2 = 0
    p2bp = ''
    p2bo = 0
    p2op = ''
    p2oo = 0
    for i in json['portalMap']:
	for j in json['portalMap'][i]:
	    if(json['portalMap'][i][j]['owner'] == 0):
		if(json['portalMap'][i][j]['portalColor'] == 'blue'):
		    p1bp = i
		    p1ob = int(j)
		else:
		    p1op = i
		    p1oo = int(j)
		player1 = player1+1
	    else:
		if(json['portalMap'][i][j]['portalColor'] == 'blue'):
		    p2bp = i
		    p2ob = int(j)
		else:
		    p2op = i
		    p200 = int(j)
		player2 = player2+1
    tmp_p1bp = p1bp.split(',')
    tmp_p1op = p1op.split(',')
    tmp_p2bp = p2bp.split(',')
    tmp_p2op = p2op.split(',')
    if(player1 == 2):
	for i in json['bombMap']:
	    tmp_arr = i.split(',')
	    #p1 bp first
	    if(int(tmp_p1bp[0]) == int(tmp_arr[0])):
		if((check_trail(int(tmp_p1op[0]),int(tmp_p1op[1])) or check_all_bomb_loc(int(tmp_p1op[0]),int(tmp_p1op[1]),-1,-1)) and player == 0 and attack):
		    return True
		if(int(tmp_p1bp[1]) > int(tmp_arr[1]) and p1bo == 1 and (int(tmp_p1bp[1])-1-int(tmp_arr[1])) < json['opponent']['bombRange']):
		    if(int(tmp_p1op[0]) == x):
			if(tmp_p1op[1] > y and p1oo == 1 and ((int(tmp_p1bp[1])-1-int(tmp_arr[1]))+(int(tmp_p1op[1])-y) <= json['opponent']['bombRange'])):
			    return True
			if(tmp_p1op[1] < y and p1oo == 3 and ((int(tmp_p1bp[1])-1-int(tmp_arr[1]))+(y-int(tmp_p1op[1])) <= json['opponent']['bombRange'])):
			    return True
		    if(int(tmp_p1op[1]) == y):
			if(tmp_p1op[0] > x and p1oo == 0 and ((int(tmp_p1bp[1])-1-int(tmp_arr[1]))+(int(tmp_p1op[0])-x) <= json['opponent']['bombRange'])):
			    return True
			if(tmp_p1op[0] > x and p1oo == 2 and ((int(tmp_p1bp[1])-1-int(tmp_arr[1]))+(x-int(tmp_p1op[0])) <= json['opponent']['bombRange'])):
			    return True
		if(int(tmp_p1bp[1]) < int(tmp_arr[1]) and p1bo == 3 and (int(tmp_arr[1])-int(tmp_p1bp[1])+1) < json['opponent']['bombRange']):
		    if(int(tmp_p1op[0]) == x):
			if(tmp_p1op[1] > y and p1oo == 1 and ((int(tmp_arr[1])-int(tmp_p1bp[1])+1)+(int(tmp_p1op[1])-y) <= json['opponent']['bombRange'])):
			    return True
			if(tmp_p1op[1] < y and p1oo == 3 and ((int(tmp_arr[1])-int(tmp_p1bp[1])+1)+(y-int(tmp_p1op[1])) <= json['opponent']['bombRange'])):
			    return True
		    if(int(tmp_p1op[1]) == y):
			if(tmp_p1op[0] > x and p1oo == 0 and ((int(tmp_arr[1])-int(tmp_p1bp[1])+1)+(int(tmp_p1op[0])-x) <= json['opponent']['bombRange'])):
			    return True
			if(tmp_p1op[0] > x and p1oo == 2 and ((int(tmp_arr[1])-int(tmp_p1bp[1])+1)+(x-int(tmp_p1op[0])) <= json['opponent']['bombRange'])):
			    return True
	    if(int(tmp_p1bp[1]) == int(tmp_arr[1])):
		if(int(tmp_p1bp[0]) > int(tmp_arr[0]) and p1bo == 0 and (int(tmp_p1bp[0])-1-int(tmp_arr[0])) < json['opponent']['bombRange']):
		    if(int(tmp_p1op[0]) == x):
			if(tmp_p1op[1] > y and p1oo == 1 and ((int(tmp_p1bp[0])-1-int(tmp_arr[0]))+(int(tmp_p1op[1])-y) <= json['opponent']['bombRange'])):
			    return True
			if(tmp_p1op[1] < y and p1oo == 3 and ((int(tmp_p1bp[0])-1-int(tmp_arr[0]))+(y-int(tmp_p1op[1])) <= json['opponent']['bombRange'])):
			    return True
		    if(int(tmp_p1op[1]) == y):
			if(tmp_p1op[0] > x and p1oo == 0 and ((int(tmp_p1bp[0])-1-int(tmp_arr[0]))+(int(tmp_p1op[0])-x) <= json['opponent']['bombRange'])):
			    return True
			if(tmp_p1op[0] > x and p1oo == 2 and ((int(tmp_p1bp[0])-1-int(tmp_arr[0]))+(x-int(tmp_p1op[0])) <= json['opponent']['bombRange'])):
			    return True
		if(int(tmp_p1bp[0]) < int(tmp_arr[0]) and p1bo == 2 and (int(tmp_arr[0])-int(tmp_p1bp[0])+1) < json['opponent']['bombRange']):
		    if(int(tmp_p1op[0]) == x):
			if(tmp_p1op[1] > y and p1oo == 1 and ((int(tmp_arr[0])-int(tmp_p1bp[0])+1)+(int(tmp_p1op[1])-y) <= json['opponent']['bombRange'])):
			    return True
			if(tmp_p1op[1] < y and p1oo == 3 and ((int(tmp_arr[0])-int(tmp_p1bp[1])+1)+(y-int(tmp_p1op[1])) <= json['opponent']['bombRange'])):
			    return True
		    if(int(tmp_p1op[1]) == y):
			if(tmp_p1op[0] > x and p1oo == 0 and ((int(tmp_arr[0])-int(tmp_p1bp[0])+1)+(int(tmp_p1op[0])-x) <= json['opponent']['bombRange'])):
			    return True
			if(tmp_p1op[0] > x and p1oo == 2 and ((int(tmp_arr[0])-int(tmp_p1bp[0])+1)+(x-int(tmp_p1op[0])) <= json['opponent']['bombRange'])):
			    return True
	    #p1 op first
	    if(int(tmp_p1op[0]) == int(tmp_arr[0])):
		if(int(tmp_p1op[1]) > int(tmp_arr[1]) and p1oo == 1 and (int(tmp_p1op[1])-1-int(tmp_arr[1])) < json['opponent']['bombRange']):
		    if(int(tmp_p1bp[0]) == x):
			if(tmp_p1bp[1] > y and p1bo == 1 and ((int(tmp_p1op[1])-1-int(tmp_arr[1]))+(int(tmp_p1bp[1])-y) <= json['opponent']['bombRange'])):
			    return True
			if(tmp_p1bp[1] < y and p1bo == 3 and ((int(tmp_p1op[1])-1-int(tmp_arr[1]))+(y-int(tmp_p1bp[1])) <= json['opponent']['bombRange'])):
			    return True
		    if(int(tmp_p1bp[1]) == y):
			if(tmp_p1bp[0] > x and p1bo == 0 and ((int(tmp_p1op[1])-1-int(tmp_arr[1]))+(int(tmp_p1bp[0])-x) <= json['opponent']['bombRange'])):
			    return True
			if(tmp_p1bp[0] > x and p1bo == 2 and ((int(tmp_p1op[1])-1-int(tmp_arr[1]))+(x-int(tmp_p1bp[0])) <= json['opponent']['bombRange'])):
			    return True
		if(int(tmp_p1op[1]) < int(tmp_arr[1]) and p1oo == 3 and (int(tmp_arr[1])-int(tmp_p1op[1])+1) < json['opponent']['bombRange']):
		    if(int(tmp_p1bp[0]) == x):
			if(tmp_p1bp[1] > y and p1bo == 1 and ((int(tmp_arr[1])-int(tmp_p1op[1])+1)+(int(tmp_p1bp[1])-y) <= json['opponent']['bombRange'])):
			    return True
			if(tmp_p1bp[1] < y and p1bo == 3 and ((int(tmp_arr[1])-int(tmp_p1op[1])+1)+(y-int(tmp_p1bp[1])) <= json['opponent']['bombRange'])):
			    return True
		    if(int(tmp_p1bp[1]) == y):
			if(tmp_p1bp[0] > x and p1bo == 0 and ((int(tmp_arr[1])-int(tmp_p1op[1])+1)+(int(tmp_p1bp[0])-x) <= json['opponent']['bombRange'])):
			    return True
			if(tmp_p1bp[0] > x and p1bo == 2 and ((int(tmp_arr[1])-int(tmp_p1op[1])+1)+(x-int(tmp_p1bp[0])) <= json['opponent']['bombRange'])):
			    return True
	    if(int(tmp_p1op[1]) == int(tmp_arr[1])):
		if(int(tmp_p1op[0]) > int(tmp_arr[0]) and p1oo == 0 and (int(tmp_p1op[0])-1-int(tmp_arr[0])) < json['opponent']['bombRange']):
		    if(int(tmp_p1bp[0]) == x):
			if(tmp_p1bp[1] > y and p1bo == 1 and ((int(tmp_p1op[0])-1-int(tmp_arr[0]))+(int(tmp_p1bp[1])-y) <= json['opponent']['bombRange'])):
			    return True
			if(tmp_p1bp[1] < y and p1bo == 3 and ((int(tmp_p1op[0])-1-int(tmp_arr[0]))+(y-int(tmp_p1bp[1])) <= json['opponent']['bombRange'])):
			    return True
		    if(int(tmp_p1bp[1]) == y):
			if(tmp_p1bp[0] > x and p1bo == 0 and ((int(tmp_p1op[0])-1-int(tmp_arr[0]))+(int(tmp_p1bp[0])-x) <= json['opponent']['bombRange'])):
			    return True
			if(tmp_p1bp[0] > x and p1bo == 2 and ((int(tmp_p1op[0])-1-int(tmp_arr[0]))+(x-int(tmp_p1bp[0])) <= json['opponent']['bombRange'])):
			    return True
		if(int(tmp_p1op[0]) < int(tmp_arr[0]) and p1oo == 2 and (int(tmp_arr[0])-int(tmp_p1op[0])+1) < json['opponent']['bombRange']):
		    if(int(tmp_p1bp[0]) == x):
			if(tmp_p1bp[1] > y and p1bo == 1 and ((int(tmp_arr[0])-int(tmp_p1op[0])+1)+(int(tmp_p1bp[1])-y) <= json['opponent']['bombRange'])):
			    return True
			if(tmp_p1bp[1] < y and p1bo == 3 and ((int(tmp_arr[0])-int(tmp_p1op[1])+1)+(y-int(tmp_p1bp[1])) <= json['opponent']['bombRange'])):
			    return True
		    if(int(tmp_p1bp[1]) == y):
			if(tmp_p1bp[0] > x and p1bo == 0 and ((int(tmp_arr[0])-int(tmp_p1op[0])+1)+(int(tmp_p1bp[0])-x) <= json['opponent']['bombRange'])):
			    return True
			if(tmp_p1bp[0] > x and p1bo == 2 and ((int(tmp_arr[0])-int(tmp_p1op[0])+1)+(x-int(tmp_p1bp[0])) <= json['opponent']['bombRange'])):
			    return True
    if(player2 == 2):
	for i in json['bombMap']:
	    tmp_arr = i.split(',')
	    #p2 bp first
	    if(int(tmp_p2bp[0]) == int(tmp_arr[0])):
		if((check_trail(int(tmp_p2op[0]),int(tmp_p2op[1])) or check_all_bomb_loc(int(tmp_p2op[0]),int(tmp_p2op[1]),-1,-1)) and player == 1 and attack):
		    return True
		if(int(tmp_p2bp[1]) > int(tmp_arr[1]) and p2bo == 1 and (int(tmp_p2bp[1])-1-int(tmp_arr[1])) < json['opponent']['bombRange']):
		    if(int(tmp_p2op[0]) == x):
			if(tmp_p2op[1] > y and p2oo == 1 and ((int(tmp_p2bp[1])-1-int(tmp_arr[1]))+(int(tmp_p2op[1])-y) <= json['opponent']['bombRange'])):
			    return True
			if(tmp_p2op[1] < y and p2oo == 3 and ((int(tmp_p2bp[1])-1-int(tmp_arr[1]))+(y-int(tmp_p2op[1])) <= json['opponent']['bombRange'])):
			    return True
		    if(int(tmp_p2op[1]) == y):
			if(tmp_p2op[0] > x and p2oo == 0 and ((int(tmp_p2bp[1])-1-int(tmp_arr[1]))+(int(tmp_p2op[0])-x) <= json['opponent']['bombRange'])):
			    return True
			if(tmp_p2op[0] > x and p2oo == 2 and ((int(tmp_p2bp[1])-1-int(tmp_arr[1]))+(x-int(tmp_p2op[0])) <= json['opponent']['bombRange'])):
			    return True
		if(int(tmp_p2bp[1]) < int(tmp_arr[1]) and p2bo == 3 and (int(tmp_arr[1])-int(tmp_p2bp[1])+1) < json['opponent']['bombRange']):
		    if(int(tmp_p2op[0]) == x):
			if(tmp_p2op[1] > y and p2oo == 1 and ((int(tmp_arr[1])-int(tmp_p2bp[1])+1)+(int(tmp_p2op[1])-y) <= json['opponent']['bombRange'])):
			    return True
			if(tmp_p2op[1] < y and p2oo == 3 and ((int(tmp_arr[1])-int(tmp_p2bp[1])+1)+(y-int(tmp_p2op[1])) <= json['opponent']['bombRange'])):
			    return True
		    if(int(tmp_p2op[1]) == y):
			if(tmp_p2op[0] > x and p2oo == 0 and ((int(tmp_arr[1])-int(tmp_p2bp[1])+1)+(int(tmp_p2op[0])-x) <= json['opponent']['bombRange'])):
			    return True
			if(tmp_p2op[0] > x and p2oo == 2 and ((int(tmp_arr[1])-int(tmp_p2bp[1])+1)+(x-int(tmp_p2op[0])) <= json['opponent']['bombRange'])):
			    return True
	    if(int(tmp_p2bp[1]) == int(tmp_arr[1])):
		if(int(tmp_p2bp[0]) > int(tmp_arr[0]) and p2bo == 0 and (int(tmp_p2bp[0])-1-int(tmp_arr[0])) < json['opponent']['bombRange']):
		    if(int(tmp_p2op[0]) == x):
			if(tmp_p2op[1] > y and p2oo == 1 and ((int(tmp_p2bp[0])-1-int(tmp_arr[0]))+(int(tmp_p2op[1])-y) <= json['opponent']['bombRange'])):
			    return True
			if(tmp_p2op[1] < y and p2oo == 3 and ((int(tmp_p2bp[0])-1-int(tmp_arr[0]))+(y-int(tmp_p2op[1])) <= json['opponent']['bombRange'])):
			    return True
		    if(int(tmp_p2op[1]) == y):
			if(tmp_p2op[0] > x and p2oo == 0 and ((int(tmp_p2bp[0])-1-int(tmp_arr[0]))+(int(tmp_p2op[0])-x) <= json['opponent']['bombRange'])):
			    return True
			if(tmp_p2op[0] > x and p2oo == 2 and ((int(tmp_p2bp[0])-1-int(tmp_arr[0]))+(x-int(tmp_p2op[0])) <= json['opponent']['bombRange'])):
			    return True
		if(int(tmp_p2bp[0]) < int(tmp_arr[0]) and p2bo == 2 and (int(tmp_arr[0])-int(tmp_p2bp[0])+1) < json['opponent']['bombRange']):
		    if(int(tmp_p2op[0]) == x):
			if(tmp_p2op[1] > y and p2oo == 1 and ((int(tmp_arr[0])-int(tmp_p2bp[0])+1)+(int(tmp_p2op[1])-y) <= json['opponent']['bombRange'])):
			    return True
			if(tmp_p2op[1] < y and p2oo == 3 and ((int(tmp_arr[0])-int(tmp_p2bp[1])+1)+(y-int(tmp_p2op[1])) <= json['opponent']['bombRange'])):
			    return True
		    if(int(tmp_p2op[1]) == y):
			if(tmp_p2op[0] > x and p2oo == 0 and ((int(tmp_arr[0])-int(tmp_p2bp[0])+1)+(int(tmp_p2op[0])-x) <= json['opponent']['bombRange'])):
			    return True
			if(tmp_p2op[0] > x and p2oo == 2 and ((int(tmp_arr[0])-int(tmp_p2bp[0])+1)+(x-int(tmp_p2op[0])) <= json['opponent']['bombRange'])):
			    return True
	    #p2 op first
	    if(int(tmp_p2op[0]) == int(tmp_arr[0])):
		if(int(tmp_p2op[1]) > int(tmp_arr[1]) and p2oo == 1 and (int(tmp_p2op[1])-1-int(tmp_arr[1])) < json['opponent']['bombRange']):
		    if(int(tmp_p2bp[0]) == x):
			if(tmp_p2bp[1] > y and p2bo == 1 and ((int(tmp_p2op[1])-1-int(tmp_arr[1]))+(int(tmp_p2bp[1])-y) <= json['opponent']['bombRange'])):
			    return True
			if(tmp_p2bp[1] < y and p2bo == 3 and ((int(tmp_p2op[1])-1-int(tmp_arr[1]))+(y-int(tmp_p2bp[1])) <= json['opponent']['bombRange'])):
			    return True
		    if(int(tmp_p2bp[1]) == y):
			if(tmp_p2bp[0] > x and p2bo == 0 and ((int(tmp_p2op[1])-1-int(tmp_arr[1]))+(int(tmp_p2bp[0])-x) <= json['opponent']['bombRange'])):
			    return True
			if(tmp_p2bp[0] > x and p2bo == 2 and ((int(tmp_p2op[1])-1-int(tmp_arr[1]))+(x-int(tmp_p2bp[0])) <= json['opponent']['bombRange'])):
			    return True
		if(int(tmp_p2op[1]) < int(tmp_arr[1]) and p2oo == 3 and (int(tmp_arr[1])-int(tmp_p2op[1])+1) < json['opponent']['bombRange']):
		    if(int(tmp_p2bp[0]) == x):
			if(tmp_p2bp[1] > y and p2bo == 1 and ((int(tmp_arr[1])-int(tmp_p2op[1])+1)+(int(tmp_p2bp[1])-y) <= json['opponent']['bombRange'])):
			    return True
			if(tmp_p2bp[1] < y and p2bo == 3 and ((int(tmp_arr[1])-int(tmp_p2op[1])+1)+(y-int(tmp_p2bp[1])) <= json['opponent']['bombRange'])):
			    return True
		    if(int(tmp_p2bp[1]) == y):
			if(tmp_p2bp[0] > x and p2bo == 0 and ((int(tmp_arr[1])-int(tmp_p2op[1])+1)+(int(tmp_p2bp[0])-x) <= json['opponent']['bombRange'])):
			    return True
			if(tmp_p2bp[0] > x and p2bo == 2 and ((int(tmp_arr[1])-int(tmp_p2op[1])+1)+(x-int(tmp_p2bp[0])) <= json['opponent']['bombRange'])):
			    return True
	    if(int(tmp_p2op[1]) == int(tmp_arr[1])):
		if(int(tmp_p2op[0]) > int(tmp_arr[0]) and p2oo == 0 and (int(tmp_p2op[0])-1-int(tmp_arr[0])) < json['opponent']['bombRange']):
		    if(int(tmp_p2bp[0]) == x):
			if(tmp_p2bp[1] > y and p2bo == 1 and ((int(tmp_p2op[0])-1-int(tmp_arr[0]))+(int(tmp_p2bp[1])-y) <= json['opponent']['bombRange'])):
			    return True
			if(tmp_p2bp[1] < y and p2bo == 3 and ((int(tmp_p2op[0])-1-int(tmp_arr[0]))+(y-int(tmp_p2bp[1])) <= json['opponent']['bombRange'])):
			    return True
		    if(int(tmp_p2bp[1]) == y):
			if(tmp_p2bp[0] > x and p2bo == 0 and ((int(tmp_p2op[0])-1-int(tmp_arr[0]))+(int(tmp_p2bp[0])-x) <= json['opponent']['bombRange'])):
			    return True
			if(tmp_p2bp[0] > x and p2bo == 2 and ((int(tmp_p2op[0])-1-int(tmp_arr[0]))+(x-int(tmp_p2bp[0])) <= json['opponent']['bombRange'])):
			    return True
		if(int(tmp_p2op[0]) < int(tmp_arr[0]) and p2oo == 2 and (int(tmp_arr[0])-int(tmp_p2op[0])+1) < json['opponent']['bombRange']):
		    if(int(tmp_p2bp[0]) == x):
			if(tmp_p2bp[1] > y and p2bo == 1 and ((int(tmp_arr[0])-int(tmp_p2op[0])+1)+(int(tmp_p2bp[1])-y) <= json['opponent']['bombRange'])):
			    return True
			if(tmp_p2bp[1] < y and p2bo == 3 and ((int(tmp_arr[0])-int(tmp_p2op[1])+1)+(y-int(tmp_p2bp[1])) <= json['opponent']['bombRange'])):
			    return True
		    if(int(tmp_p2bp[1]) == y):
			if(tmp_p2bp[0] > x and p2bo == 0 and ((int(tmp_arr[0])-int(tmp_p2op[0])+1)+(int(tmp_p2bp[0])-x) <= json['opponent']['bombRange'])):
			    return True
			if(tmp_p1bp[0] > x and p2bo == 2 and ((int(tmp_arr[0])-int(tmp_p2op[0])+1)+(x-int(tmp_p2bp[0])) <= json['opponent']['bombRange'])):
			    return True
    else:
	return False
def new_bp():
    print("new blue portal")
    global json
    x = json['player']['x']
    y = json['player']['y']
    if(json['player']['orientation'] == 0 and hardboard[11*(x-1)+y] == 1):
	    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'bp', 'devkey': "581b97a4da8dce85358c64c3"});
    elif(json['player']['orientation'] == 1 and hardboard[11*(x)+(y-1)] == 1):
	r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'bp', 'devkey': "581b97a4da8dce85358c64c3"});
    elif(json['player']['orientation'] == 2 and hardboard[11*(x+1)+y] == 1):
	r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'bp', 'devkey': "581b97a4da8dce85358c64c3"});
    elif(json['player']['orientation'] == 3 and hardboard[11*(x)+(y+1)] == 1):
	r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'bp', 'devkey': "581b97a4da8dce85358c64c3"});
    elif(hardboard[11*(x-1)+y] == 1):
	r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'tl', 'devkey': "581b97a4da8dce85358c64c3"});
	r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'bp', 'devkey': "581b97a4da8dce85358c64c3"});
    elif(hardboard[11*(x+1)+y] == 1):
	r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'tr', 'devkey': "581b97a4da8dce85358c64c3"});
	r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'bp', 'devkey': "581b97a4da8dce85358c64c3"});
    elif(hardboard[11*(x)+(y-1)] == 1):
	r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'tu', 'devkey': "581b97a4da8dce85358c64c3"});
	r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'bp', 'devkey': "581b97a4da8dce85358c64c3"});
    elif(hardboard[11*(x)+(y+1)] == 1):
	r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'td', 'devkey': "581b97a4da8dce85358c64c3"});
	r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'bp', 'devkey': "581b97a4da8dce85358c64c3"});
    
def check_around_portal():
    global json
    if(json['player']['bluePortal']['direction'] == 0):
	if(hardboard[11*(json['player']['bluePortal']['x']-1)+(json['player']['bluePortal']['y']+1)] == 0 and not check_enemy_bomb_loc(json['player']['bluePortal']['x']-1,json['player']['bluePortal']['y']+1) and not check_trail(json['player']['bluePortal']['x']-1,json['player']['bluePortal']['y']+1) and json['softBlockBoard'][11*(json['player']['bluePortal']['x']-1)+(json['player']['bluePortal']['y']+1)] == 0):
	    return True
	if(hardboard[11*(json['player']['bluePortal']['x']-1)+(json['player']['bluePortal']['y']-1)] == 0 and not check_enemy_bomb_loc(json['player']['bluePortal']['x']-1,json['player']['bluePortal']['y']-1) and not check_trail(json['player']['bluePortal']['x']-1,json['player']['bluePortal']['y']-1) and json['softBlockBoard'][11*(json['player']['bluePortal']['x']-1)+(json['player']['bluePortal']['y']-1)] == 0):
	    return True
    if(json['player']['bluePortal']['direction'] == 1):
	if(hardboard[11*(json['player']['bluePortal']['x']-1)+(json['player']['bluePortal']['y']-1)] == 0 and not check_enemy_bomb_loc(json['player']['bluePortal']['x']-1,json['player']['bluePortal']['y']-1) and not check_trail(json['player']['bluePortal']['x']-1,json['player']['bluePortal']['y']-1) and json['softBlockBoard'][11*(json['player']['bluePortal']['x']-1)+(json['player']['bluePortal']['y']-1)] == 0):
	    return True
	if(hardboard[11*(json['player']['bluePortal']['x']+1)+(json['player']['bluePortal']['y']-1)] == 0 and not check_enemy_bomb_loc(json['player']['bluePortal']['x']+1,json['player']['bluePortal']['y']-1) and not check_trail(json['player']['bluePortal']['x']+1,json['player']['bluePortal']['y']-1) and json['softBlockBoard'][11*(json['player']['bluePortal']['x']+1)+(json['player']['bluePortal']['y']-1)] == 0):
	    return True
    if(json['player']['bluePortal']['direction'] == 2):
	if(hardboard[11*(json['player']['bluePortal']['x']+1)+(json['player']['bluePortal']['y']+1)] == 0 and not check_enemy_bomb_loc(json['player']['bluePortal']['x']+1,json['player']['bluePortal']['y']+1) and not check_trail(json['player']['bluePortal']['x']+1,json['player']['bluePortal']['y']+1) and json['softBlockBoard'][11*(json['player']['bluePortal']['x']+1)+(json['player']['bluePortal']['y']+1)] == 0):
	    return True
	if(hardboard[11*(json['player']['bluePortal']['x']+1)+(json['player']['bluePortal']['y']-1)] == 0 and not check_enemy_bomb_loc(json['player']['bluePortal']['x']+1,json['player']['bluePortal']['y']-1) and not check_trail(json['player']['bluePortal']['x']+1,json['player']['bluePortal']['y']-1) and json['softBlockBoard'][11*(json['player']['bluePortal']['x']+1)+(json['player']['bluePortal']['y']-1)] == 0):
	    return True
    if(json['player']['bluePortal']['direction'] == 3):
	if(hardboard[11*(json['player']['bluePortal']['x']-1)+(json['player']['bluePortal']['y']+1)] == 0 and not check_enemy_bomb_loc(json['player']['bluePortal']['x']-1,json['player']['bluePortal']['y']+1) and not check_trail(json['player']['bluePortal']['x']-1,json['player']['bluePortal']['y']+1) and json['softBlockBoard'][11*(json['player']['bluePortal']['x']-1)+(json['player']['bluePortal']['y']+1)] == 0):
	    return True
	if(hardboard[11*(json['player']['bluePortal']['x']+1)+(json['player']['bluePortal']['y']+1)] == 0 and not check_enemy_bomb_loc(json['player']['bluePortal']['x']+1,json['player']['bluePortal']['y']+1) and not check_trail(json['player']['bluePortal']['x']+1,json['player']['bluePortal']['y']+1) and json['softBlockBoard'][11*(json['player']['bluePortal']['x']+1)+(json['player']['bluePortal']['y']+1)] == 0):
	    return True
    return False
    
def move_portal():
    global json
    if(json['player']['bluePortal']['direction'] == 0):
	if(hardboard[11*(json['player']['bluePortal']['x']-1)+(json['player']['bluePortal']['y']+1)] == 0 and not check_enemy_bomb_loc(json['player']['bluePortal']['x']-1,json['player']['bluePortal']['y']+1) and not check_trail(json['player']['bluePortal']['x']-1,json['player']['bluePortal']['y']+1) and json['softBlockBoard'][11*(json['player']['bluePortal']['x']-1)+(json['player']['bluePortal']['y']+1)] == 0 and not check_portal_kill(json['player']['bluePortal']['x']-1, json['player']['bluePortal']['y']+1, False)):
	    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'md', 'devkey': "581b97a4da8dce85358c64c3"});
	    json = r.json()
	elif(hardboard[11*(json['player']['bluePortal']['x']-1)+(json['player']['bluePortal']['y']-1)] == 0 and not check_enemy_bomb_loc(json['player']['bluePortal']['x']-1,json['player']['bluePortal']['y']-1) and not check_trail(json['player']['bluePortal']['x']-1,json['player']['bluePortal']['y']-1) and json['softBlockBoard'][11*(json['player']['bluePortal']['x']-1)+(json['player']['bluePortal']['y']-1)] == 0 and not check_portal_kill(json['player']['bluePortal']['x']-1, json['player']['bluePortal']['y']-1, False)):
	    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mu', 'devkey': "581b97a4da8dce85358c64c3"});
	    json = r.json()
	else:
	    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'op', 'devkey': "581b97a4da8dce85358c64c3"});
	    json = r.json()
    if(json['player']['bluePortal']['direction'] == 1):
	if(hardboard[11*(json['player']['bluePortal']['x']-1)+(json['player']['bluePortal']['y']-1)] == 0 and not check_enemy_bomb_loc(json['player']['bluePortal']['x']-1,json['player']['bluePortal']['y']-1) and not check_trail(json['player']['bluePortal']['x']-1,json['player']['bluePortal']['y']-1) and json['softBlockBoard'][11*(json['player']['bluePortal']['x']-1)+(json['player']['bluePortal']['y']-1)] == 0 and not check_portal_kill(json['player']['bluePortal']['x']-1, json['player']['bluePortal']['y']-1, False)):
	    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'ml', 'devkey': "581b97a4da8dce85358c64c3"});
	    json = r.json()
	elif(hardboard[11*(json['player']['bluePortal']['x']+1)+(json['player']['bluePortal']['y']-1)] == 0 and not check_enemy_bomb_loc(json['player']['bluePortal']['x']+1,json['player']['bluePortal']['y']-1) and not check_trail(json['player']['bluePortal']['x']+1,json['player']['bluePortal']['y']-1) and json['softBlockBoard'][11*(json['player']['bluePortal']['x']+1)+(json['player']['bluePortal']['y']-1)] == 0 and not check_portal_kill(json['player']['bluePortal']['x']+1, json['player']['bluePortal']['y']+1, False)):
	    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mr', 'devkey': "581b97a4da8dce85358c64c3"});
	    json = r.json()
	else:
	    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'op', 'devkey': "581b97a4da8dce85358c64c3"});
	    json = r.json()
    if(json['player']['bluePortal']['direction'] == 2):
	if(hardboard[11*(json['player']['bluePortal']['x']+1)+(json['player']['bluePortal']['y']+1)] == 0 and not check_enemy_bomb_loc(json['player']['bluePortal']['x']+1,json['player']['bluePortal']['y']+1) and not check_trail(json['player']['bluePortal']['x']+1,json['player']['bluePortal']['y']+1) and json['softBlockBoard'][11*(json['player']['bluePortal']['x']+1)+(json['player']['bluePortal']['y']+1)] == 0 and not check_portal_kill(json['player']['bluePortal']['x']+1, json['player']['bluePortal']['y']+1, False)):
	    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'md', 'devkey': "581b97a4da8dce85358c64c3"});
	    json = r.json()
	elif(hardboard[11*(json['player']['bluePortal']['x']+1)+(json['player']['bluePortal']['y']-1)] == 0 and not check_enemy_bomb_loc(json['player']['bluePortal']['x']+1,json['player']['bluePortal']['y']-1) and not check_trail(json['player']['bluePortal']['x']+1,json['player']['bluePortal']['y']-1) and json['softBlockBoard'][11*(json['player']['bluePortal']['x']+1)+(json['player']['bluePortal']['y']-1)] == 0 and not check_portal_kill(json['player']['bluePortal']['x']+1, json['player']['bluePortal']['y']-1, False)):
	    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mu', 'devkey': "581b97a4da8dce85358c64c3"});
	    json = r.json()
	else:
	    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'op', 'devkey': "581b97a4da8dce85358c64c3"});
	    json = r.json()
    if(json['player']['bluePortal']['direction'] == 3):
	if(hardboard[11*(json['player']['bluePortal']['x']-1)+(json['player']['bluePortal']['y']+1)] == 0 and not check_enemy_bomb_loc(json['player']['bluePortal']['x']-1,json['player']['bluePortal']['y']+1) and not check_trail(json['player']['bluePortal']['x']-1,json['player']['bluePortal']['y']+1) and json['softBlockBoard'][11*(json['player']['bluePortal']['x']-1)+(json['player']['bluePortal']['y']+1)] == 0 and not check_portal_kill(json['player']['bluePortal']['x']-1, json['player']['bluePortal']['y']+1, False)):
	    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'ml', 'devkey': "581b97a4da8dce85358c64c3"});
	    json = r.json()
	elif(hardboard[11*(json['player']['bluePortal']['x']+1)+(json['player']['bluePortal']['y']+1)] == 0 and not check_enemy_bomb_loc(json['player']['bluePortal']['x']+1,json['player']['bluePortal']['y']+1) and not check_trail(json['player']['bluePortal']['x']+1,json['player']['bluePortal']['y']+1) and json['softBlockBoard'][11*(json['player']['bluePortal']['x']+1)+(json['player']['bluePortal']['y']+1)] == 0 and not check_portal_kill(json['player']['bluePortal']['x']+1, json['player']['bluePortal']['y']+1, False)):
	    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'mr', 'devkey': "581b97a4da8dce85358c64c3"});
	    json = r.json()
	else:
	    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'op', 'devkey': "581b97a4da8dce85358c64c3"});
	    json = r.json()
    


r = requests.post('http://aicomp.io/api/games/search', data={'devkey': "581b97a4da8dce85358c64c3" , 'username': "pandemic2all"}) # search for new game
json = r.json() # when request comes back, that means you've found a match! (validation if server goes down?)
print(json)
gameID = json['gameID']
playerID = json['playerID']
output = {'state': 'in progress'}
hardboard = json['hardBlockBoard']
oldMove = ""
bombmax = 1
player = 0
enemyBombs = []
bombDown = 0
enemymax = 1
item = 0
solved = False
increment = 0
if(json['player']['x'] == 1):
    player = 0
    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'tu', 'devkey': "581b97a4da8dce85358c64c3"});
    json = r.json()
    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'bp', 'devkey': "581b97a4da8dce85358c64c3"});
    json = r.json()
else:
    player = 1
    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'td', 'devkey': "581b97a4da8dce85358c64c3"});
    json = r.json()
    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'bp', 'devkey': "581b97a4da8dce85358c64c3"});
    json = r.json()
while output['state'] != 'complete':
    x = json['player']['x']
    y = json['player']['y']
    if(json['player']['bombCount']< bombmax):
        while(json['player']['bombCount']< bombmax):
            wait()
            print("item2: " + str(item))
        wait()
        print("item2: " + str(item))
    else:
        if(check_enemy_bomb()):
	    """
            if(check_attack_easy_bomb()):
                print("counter easy bomb")
            if(check_attack_long_bomb()):
                print("counter long bomb")
            else:
	    """
	    gtfo()
        if(check_enemy()):
            if(bombmax>=2):
                if(napalm()):
                    print("NAPALM")
                    while(json['player']['bombCount'] < bombmax):
                        r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': ' ', 'devkey': "581b97a4da8dce85358c64c3"});
                        json = r.json()
                    r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': ' ', 'devkey': "581b97a4da8dce85358c64c3"});
                    json = r.json()
            if(check_attack_easy_bomb()):
                print("attack easy bomb")
            elif(check_attack_long_bomb()):
                print("attack long bomb")
	    elif(not check_portal_kill(json['player']['x'],json['player']['y'], True) and check_around_portal()):
		print("portal attack")
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'b', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
		portal_escape()
		move_portal()
	    else:
		gtfo()
	elif(increment%5==0):
	    new_bp()	
        elif(check_for_soft()):
            if(check_easy_bomb()):
                print("easy bomb")
            elif(check_long_bomb()):
                print("long bomb")
	    elif(not check_portal_kill(json['player']['x'],json['player']['y'], True) and check_around_portal()):
		print("portal attack")
		r = requests.post('http://aicomp.io/api/games/submit/' + gameID, data={'playerID': playerID, 'move': 'b', 'devkey': "581b97a4da8dce85358c64c3"});
		json = r.json()
		portal_escape()
		move_portal()
            else:
                move()
        else:
            move()
    print(json)
    output = json
    increment = increment +1
print("out of loop")