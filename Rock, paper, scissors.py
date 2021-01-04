#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


# create list of options 
choices = ['rock', 'paper', 'scissors']


# In[3]:


# computer choice
pc = choices[random.randint(0,2)]


# In[4]:


# set player to false to initiate
player = False


# In[5]:


# keep score
player_score = 0
pc_score = 0

# keep rounds
rounds = 0


# In[6]:


best_of = int(input('Best of: '))



while player == False:
# set player to true
# request input choice for player
    player = input('Rock, paper or scissors? ').lower()
    
    # outcome tie
    if player == pc:
        print('TIE!!!')
        rounds += 1
    
    # outcome rock
    elif player == 'rock':
        if pc == 'paper':
            print(f'You LOSE!! {pc} beats {player}')
            pc_score += 1
        elif pc == 'scissors':
            print(f'You WIN!! {player} beats {pc}')
            player_score += 1
        rounds += 1
            
    # outcome paper
    elif player == 'paper':
        if pc == 'rock':
            print(f'You WIN!! {player} beats {pc}')
            player_score += 1
        elif pc == 'scissors':
            print(f'You LOSE!! {pc} beats {player}')
            pc_score += 1
        rounds += 1
    
    # outcome scissors
    elif player == 'scissors':
        if pc == 'rock':
            print(f'You LOSE!! {pc} beats {player}')
            pc_score += 1
        elif pc == 'paper':
            print(f'You WIN!! {player} beats {pc}')
            player_score += 1
        rounds += 1
            
    else:
        print('INVALID CHOICE!!!')
    
    
    
    # display rounds and scores
    print(f'Round {rounds}:')
    print(f'Score:')
    print(f'  Player {player_score} | Computer {pc_score}')
    print('\n')
    
    
    
    # best of 3
    # reset player to false to continue loop
    if player_score == best_of:
        print('YOU WIN!!!')
        
    elif pc_score == best_of:
        print('YOU LOSE!!!')
    
    else:
        player = False
        pc = choices[random.randint(0,2)]

