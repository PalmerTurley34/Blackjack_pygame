import requests
import io
import pygame.font as font

# image for the buttons
button_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_OroZCy9_5t6HzCiKnUG2Z1o5WlWaWsr2Rg&usqp=CAU"
r = requests.get(button_url).content
button_file = io.BytesIO(r)
# font for the text on the buttons
button_font = font.SysFont('comicsans', 20, True)
# info for all the buttons (coordinates and text)
hit_me = (380, 405)
stay = (380, 455)
new_deal = (40, 405)
bid_25 = (40, 455)
bid_50 = (200, 405)
bid_100 = (200, 455)

hit_me_text = button_font.render('Hit Me', 1, (0,0,0))
stay_text = button_font.render('Stay', 1, (0,0,0))
new_deal_text = button_font.render('New Deal', 1, 'black')
bid_25_text = button_font.render('Bid $25', 1, 'black')
bid_50_text = button_font.render('Bid $50', 1, 'black')
bid_100_text = button_font.render('Bid $100', 1, 'black')

# keep track of which buttons are active at each stage of the game
new_deal_active = True
hit_me_active = False
stay_active = False
bid_25_active = False
bid_50_active = False
bid_100_active = False