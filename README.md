### Getting Information From eBay using Parsing
In the file **Quiz4**, there is code which extracts specific infromation from eBay about best selling smartphones using ***requests*** and ***bs4*** modules.
Those information consists of what is product's **Name** and **Price_range** (price_from, price_to) and saves it in csv file with using ***csv module***. If price_to is not given, then the code returns its value as ***None***. (*You can see final result in eBay.csv file*).

There is also used ***time*** and ***random*** modules in order to avoid getting blocked by server. With the time module used in **for loop**, requests to server are being sent every **__X__** seconds and  **__X__** is chosen randomly from 1-15, using ***randint***.

Another module used in the code is ***re*** module, specifically ***re.sub()*** method, which removes all the special characters from string, which can't be written in **csv** file.
