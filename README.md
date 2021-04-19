README

With crawling the flash on Chinese bitcoin information site 8btc.com, we trained a model that can analysis the market sentiment of digital currency market. With each flash, there are 2 button under the flash: "利好"(good news) or “利空”(bad news), which means  prevailing attitude of investors as to anticipated price development in a market. We use a BERT, a pretrained model and fine-tuned it on this dataset.

#### **Introduction**

Using the flash on Chinese bitcoin information site 8btc.com to learn a model that can analysis the market sentiment of digital currency market.

With each flash, there are 2 button under the flash: "利好"(good news) or “利空”(bad news), which means what users will probably do after seeing this news.

![image-20210411212634263](C:\Users\Ivy Li\AppData\Roaming\Typora\typora-user-images\image-20210411212634263.png)

Generally, when users think that this news is a good news, he(or she) will be more inclined to buy some digital currency, and vice versa, which is a simple interpretation of the concept of **market sentiment**.

The purpose of this project is to train a model that can predict market sentiment according to the flash through machine learning, which may give some guidance to investors in the field of digital currency. :)

------

#### Data

We crawled https://www.8btc.com/flash the news on this page from 2018 to 2020, and made the following filtering on the crawled data:   

good>5 or bad>5 and |good-bad|>5,

which good and bad represent the value of the button "利好"， “利空”, respectively.

Finally, we get 2567 data.

All the data is in export.json

------

#### Model

Because the number of filtered data is not large enough, in order to improve the accuracy of the model, we decided to adopt BERT, the pretrained model.

We use the BERT of hugging face, which you can see all the details in this notebook:

https://colab.research.google.com/drive/1957XLnEc-TDTheCZnbgdr2FyWzi4SIDQ?usp=sharing

------

#### Result

Finally, we get the following result:

![image-20210411214914828](C:\Users\Ivy Li\AppData\Roaming\Typora\typora-user-images\image-20210411214914828.png)

