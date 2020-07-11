#!/usr/bin/env python
# coding: utf-8

# In[1]:


diskon = 0
qty=int(input("Banyak Barang ?"))
harga=int(input("Harga Barang?"))
jumlah=qty*harga
if jumlah >100000:
    diskon=jumlah*0.1
bayar=jumlah-diskon
print ("Bayar =Rp. ",bayar)


# In[ ]:




