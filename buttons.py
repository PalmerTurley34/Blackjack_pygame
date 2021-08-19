import requests
import io

# image for the buttons
button_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_OroZCy9_5t6HzCiKnUG2Z1o5WlWaWsr2Rg&usqp=CAU"
r = requests.get(button_url).content
button_file = io.BytesIO(r)
# x,y coordinates for buttons
hit_me = (380, 405)
stay = (380, 455)
new_deal = (40, 405)
bid_25 = (40, 455)
bid_50 = (200, 405)
bid_100 = (200, 455)
