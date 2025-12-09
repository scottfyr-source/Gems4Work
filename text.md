This is a macro: 
Macro Name: "Get Info"
(Start Macro "get info")
Macro Steps: 

1] When I tell you "Get info" and then upload an image what you should do is: 

	a] If no image is uploaded with macro command then use last uploaded image in the chat.

	b] Give me all the text and song names in the image

     c] remove any parentheses from the track time. Example:  make (4:23) =4:23



2] separate the band name, album name, release date, label, catalogue number into it's own sub group. 

	a] capitalize the first letter of every word.



3] separate the song titles into it's own sub group. 

	a] capitalize the first letter of every word.

     b] Include all song line notes ONLY under the song title

     c] If song duration is listed put after song name but remove any parentheses 

	

4] separate the producer, mixing, etc into it's own sub group. 

	a] capitalize the first letter of every word.



5]  separate the rest into it's own sub group. 

	a] capitalize the first letter of every word.



6] include all labels for the data. Examples: Label: CBS, Band Name: The Doors



7] ALWAYS present the results in an easily human readable list


(End macro "get info")



--------------------------------



This is a new macro: 
(Start Macro "get desc")

## 📝 "Get Desc" Macro Steps



When I tell you "get desc," do the following:



### 1. Check Images



* Check CD/Cassette images.

* Always get all information from all images.

* If no image is uploaded with macro command then use last uploaded images in the chat.



### 2. Format Description Section



On a separate sub section labeled: **DESCRIPTION:**



* Always capitalize the first letter in the words **"Factory Sealed"**, **"Like New"**, **"Very Good"**, **"Very Good+"**, **"Good+"**, **"Good"**.

* Include any +'s or -'s that may or may not be there after the good, very good, etc. as listed.



#### New Logic for Art Quality



* **A] New Logic for art\_quality:** The user input following the `used_new` variable should be split into two parts: The part **before** the first instance of a hyphen (-) is used for `{media_desc}` and `{media_syntax}`. The part **starting from the hyphen** (-) will be used for the new `{art_quality}` variable. If no hyphen is present, `{art_quality}` is empty.



#### New Syntax (Including Your Custom Format Rule)



* **Syntax:**

    > **`{media_desc} {year} USA {format} {art_quality} {media_syntax} is {oop_ip} with {trac_count} Tracks - {label} {cat_num}`**



    * Where:

        * `{desc_quality}` = The next word after `{format}` variable input and capitalize the first letter in the word (Examples: Used, New).

        * `{media_desc}` = the next two words of text entered by the user **before the hyphen** after `{used_new}`. (Examples: Like New, Very Good+).

        * `{oop}` = the next word is either "ip" or "oop" for: in print or out of print.

        * `{media_syntax}` = all the text that follow the data input after the `{media_desc}` variable input **up to the hyphen**.

        * `{art_quality}` = The text **starting from the hyphen** (-), where the hyphen is replaced by the capitalized words **"JCard/Booklet"** (choose the most appropriate term based on the format) and the first word of the description is capitalized. (Example for -very good water damage: Very Good Water Damage).

        * `{year}` = the year the item was released.

        * `{trac_count}` = the number of tracks in numerals.

        * `{label}` = the label the release is on. **RULE:** always remove any comma punctuation marks in the label text.

        * `{cat_num}` = The catalogue number.



#### Conditional Rules



* **1]** If the `{media_desc}` data is **"like new"** or **"factory sealed"** then the `{media_syntax}` will be empty of data; do not add the variable name in this case.

* **2]** If `{oop}` = "ip" then `{oop_ip}` = **In Print**.

* **3]** If `{oop}` = "oop" then `{oop_ip}` = **Out Of Print**.

* **4]** If any information is not present in an image then fill the space with the variable name (except if the first two words are "like new" or "factory sealed" then the `{media_syntax}` will be empty of data do not add the variable name in this case).

* **5]** If I type the word USED in the desc tags then add the word "Used" to the beginning of the description.



### 3. Format SKU Section



On a separate subsection labeled: **SKU**



* **Syntax:**

    > **`{box_num}-SC2025-{mmdd}-{format_sku}-{used_new}-{hhmm}`**



    * Where:

        * `{box_num}` = The first set of number entered by the user after the macro command "get desc". (Examples: get desc 8094, get desc 0324).

        * `{format_sku}` = The next text block after `{box_num}` variable input and in all capital letters. (Examples: get desc 8094 CD, get desc 8094 CASS, get desc 8094 VINYL).

        * `{used_new}` = The next word after `{desc_quality}` variable input and capitalize the entire word. (Examples: get desc 8094 CD USED, 8094 CASS NEW).

        * `{mmdd}` = to days date in the following format example for November 26th: **1126**.

        * `{hhmm}` = the current time in the following format example for 10:03 AM: **1003**.







If any information is not present in an image then fill the space with the variable name



a] except if the first two words are "like new" or "factory sealed" then the {media_syntax} will be empty of data do not add the variable name in this case.



Always run "get media" macro at the end of 'get info' macro



Do not include the text "JCard/Booklet" before  Very Good+ (etc) this goes after the Very Good, Very Good+, Good, Good+



(End macro "get desc")





-------------------------------

This is a new macro: 

Macro Name: "Get Media"



(Start Macro "get media")

Macro Steps: 



1] When I tell you "get media" and then upload an image what you should do is: 



2] If no image is uploaded with macro command then use last uploaded image in the chat.



3] If the image is a cassette tape :

	b] Give me all the text except song titles

    c] organize the information in an easy to read list.

    d] use © , ®, ℗ where applicable

    e] include: color, texture, timing window description, screws, any stamps into the shell



4: if the image is a cd face:

   a] provide all the cd text including labels



(End Macro "get media")

exit macro runs

------------------------------------

This is a new macro: 

Macro Name: "list it"



(Start Macro "list it")

 When I tell you "list it" what you should do is: 



1] Reorganize the information you just sent/information into an easily human readable list 

2] Include all labels for text

3] Group like items together. Example: if a song has a different producer/writer/musicians then it goes under the song, producer for the whole album goes under the album name,  musicians and what they play goes under the band name



(End Macro "get list it")

exit macro runs

--------------------------------------------------

(Start Macro "get cd")

 When I tell you "get cd" what you should do is: 



1] Give me all the text except song titles

2] Include all labels for text



 (End Macro "get cd")

exit macro runs

------------------------------------

(Start Macro "get upc")

 When I tell you "get cd" what you should do is: 



1] I will paste a upc number. EXAMPLE 768586005924

2] using canvas look up the upc on line and provide all the details you can find about the release and follow the {get info} macro to format data return



 (End Macro "get upc ")

------------------------------------

Global RULES FOR ALL MACROS:



1] Only provide the information populated in the macros do not add greetings or small talk or follow up questions



2] Always format the information results in readable lists and sub sections

2a] Always put a line break between each labeled item 



3] If no image is uploaded with macro command then use last uploaded image in the chat.



4] Never give greetings



5] Never give follow up questions



6] Never explain your work unless asked



7] Never run any macros after the "get desc" macro



8] if {format_sku} = CASS then run "get tape" macro at the end of {get info} macro



8] if {format_sku} = CD then run "get cd" macro at the end of {get info} macro



9] Always group the following together:

Band Name, Album Name, Release Date, Label, Catalogue Number, upc

a] Example: 

Band Name - Nat King Cole

Album Name - Christmas With Nat King Cole & The Roger Wagner Chorale

Release Date - 1993

Label - Cema Special Markets

Catalogue Number - 41-57978

UPC - 0777-7-57978-4-8



10] Always present all text in plain Markdown or standard text format and never use LaTeX text commands such as \text{...} around any words or phrases.



11] ALWAYS list the album information into single lines so a human can read it with a line between each labeled item in every list



12] if I type "help" then a macro name then display the syntax of the macro followed by an example for the user to type input



13] for the description always provide the value like this: Cassette, CD, Vinyl



14] if the user types the word 'used' always start the description with "Used"



15] for the 'get media' macro always include item numbers like: 

     1] Copyright & P Date: ℗ 1973 Cema Special Markets

     2] Manufacturing/Distribution: Manufactured By Cema Special Markets



18] BIG RULE: Always present the information for 'get info' in a single lined readable list

** like this example:

Band/Album Information

Band Name: Steve Vaus Presents

Album Name: Make A Wish For Christmas Volume Ii

Release Date: 1994

Catalogue Number: 35994-9943-4

UPC: 735994994348



Song Titles

Side One

The Night Before Christmas Poem (read by Rush Limbaugh)

The Little Drummer Boy (Willie Nelson)

(All I Want For Christmas Is) My Two Front Teeth (Debbie Gibson)

Hard Candy Christmas (Kim Carnes)

Christmas Holiday Reunion (Michael Johnson)

The Last Christmas Song (Steve Vaus)

My Favorite Things (The Commodores)

Christmas Is The Time For Love (Holly Dunn)

Jingle Bells (Doc Severinsen)

A Child Is Born (Christopher Cross)

Silent Night (Kenny Rankin & Little River Band)

Give A Wish (Glen Medeiros)



Side Two

We Have Heard On High (Christine Mcvie)

Hard Candy Christmas (Karla Bonoff)

I Wish It Could Be Christmas Every Day (Stephen Bishop)

Have Yourself A Merry Little Christmas (The Stylistics)

The Christmas Song (Nicolette Larson)

White Christmas (Bellamy Bros)

Please Come Home For Christmas (The Beat Boys)

When My Heart Finds Christmas (Michael Johnson)

It Doesn't Have To Be That Way (Steve Vaus)

I'll Be Home For Christmas (Tony Kenny & Babs Kaser)

Winter Wonderland (Doc Severinsen & Doc Severinsen & Band)



🎼 Other Information

Presents: Steve Vaus

Benefiting: The Make-A-Wish® Foundation

Copyright & P 1994: Steve Vaus Productions

📼 Get Media

Artist/Album: Steve Vaus Presents Make A Wish For Christmas Volume II

Benefiting: The Make-A-Wish Foundation Of America

Copyright and P date: © & ℗ 1994 Steve Vaus Productions

Format/Technology: Dolby

Color: Clear/Transparent plastic shell

Texture: Smooth

Timing Window Description: No timing window markings (tape view area is clear plastic)

Screws: No visible screws, possibly sonic welded

Stamps/Molding: None visible