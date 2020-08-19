#!/usr/bin/env python
# coding: utf-8

# In[21]:


user_age = float(input('enter your age: '))
if user_age < 18:
    print('not eligible to vote')
elif user_age > 100:
    print('not eligible to vote')
else:s
    print('eligible to vote')
        


# In[23]:


user_age = float(input('enter your age: '))
if user_age in range(18,101):
    print('eligible to vote')
else:
    print('not eligible to vote')


# In[24]:


country = input('name of country: ').upper()
total_goods_bought = float(input('total number of goods bought: '))
price_of_shipping_US = (total_goods_bought*2)
price_of_shipping_EUROPE = (total_goods_bought*4)
if country == 'US':
    if price_of_shipping_US < 25:
        print(price_of_shipping_US,'\nShipment is free')
    else:
        print(price_of_shipping_US)
elif country == 'EUROPE':
    if price_of_shipping_EUROPE < 25:
        print(price_of_shipping_EUROPE,'\nShipment is free')
    else:
        print(price_of_shipping_EUROPE)
else:
    print('enter a valid country')


# In[ ]:




