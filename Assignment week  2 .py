#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[10]:


n = int(input('enter your number: '))
if n % 2 == 1:
    print('weird')
elif n % 2 == 0:
    if n in range(2,5):
        print('not weird')
if n % 2 == 0:
    if n in range(6,20):
        print('weird')
if n % 2 == 0:
    if n > 20:
        print('not weird')


# # Question 2

# In[23]:


user_age = float(input('enter your age: '))
if user_age in range(18,101):
    print('eligible to vote')
else:
    print('not eligible to vote')


# # Question 3

# In[9]:


country = input('name of country: ').upper()
total_goods_bought = float(input('total number of goods bought: '))
price_of_shipping_US = (total_goods_bought*2)
price_of_shipping_EUROPE = (total_goods_bought*4)
if country == 'US':
    if price_of_shipping_US < 25:
        print('price of shipping: ',price_of_shipping_US,'\nShipment is free')
    else:
        print('price of shipping: ',price_of_shipping_US)
elif country == 'EUROPE':
    if price_of_shipping_EUROPE < 25:
        print('price of shipping: ',price_of_shipping_EUROPE,'\nShipment is free')
    else:
        print('price of shipping: ',price_of_shipping_EUROPE)
else:
    print('enter a valid country')


# In[ ]:




