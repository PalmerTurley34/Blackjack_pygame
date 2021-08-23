from fonts import game_font

# font for game use
dealer_hand = game_font.render('Dealer Hand:', 1, 'white')
player_hand = game_font.render('Your Hand:', 1, 'white')
player_money = game_font.render('Your Money:', 1, 'white')
player_bid = game_font.render('Your Bid:', 1, 'white')

# instruction text to be diplayed at the top of the screen
game_start = game_font.render('Press "New Deal" to play!', 1, 'white')
place_bid = game_font.render('Bid $25, $50, or $100', 1, 'white')
bust = game_font.render('BUST!!', 1, 'white')
win = game_font.render('YOU WIN!!', 1, 'white')
lose = game_font.render('YOU LOSE!', 1, 'white')
stay_or_hit_me = game_font.render('Stay or Hit me?', 1, 'white')