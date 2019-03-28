# Add-on: Auto-fetch Wikipedia Summary


Hey!

## Background: 
I posted a 'tip' a while ago that takes the text from the "Back" field on your card, and when Anki shows the card, it'll go to Wikipedia and get a relevant description for you.

## Problems:
- Using JS meant time spent getting stuff from Wikipedia every time you opened a card
- Ankidroid (and I assume Anki for iPhone) wasn't working. I don't think they support AJAX calls.

## Solution:
- Use Python! We pull in the data once, so it doesn't have to be fetched over and over - AND since the data's in your decks, that fixes the mobile problem, too!

----

(Disclaimer: There are bugs that I'm still working out. This is more experimental than production-class code.)

----

## How to Set Up:
1. Go to https://github.com/davidd647/wiki-anki-addon
2. On the right, there's a green "Clone or download" button, clone or download.
3. Open Anki --> Tools --> Add-ons --> View Files
4. That will show you a folder. Each add-on has its own folder here. Add the files into a new folder
5. Restart Anki

## How to Use:
1. Make sure your card has a "Back" and a "Wiki" field.
2. Type something into the "Back" field.
3. The "Wiki" field will be automatically filled with information from Wikipedia!

-----

Issues with my approach:
- I'm not super familiar with Python. If you enter generic information into the Back field, the program errors out. I know it's because the information Wikipedia is giving me something other than a string, but I don't know how to convert the data type to a string, or just ignore the data and spit out some fallback data.
- Have to do this one-at-a-time. But I dunno... Would you even want to batch-add this information? I guess.
- The information in the Back field needs to be short. Some might find this limiting. I disagree, but acknowledge the perspective. I still think shorter cards are better for testing memory.

-----

Bonus:
I wonder what other things we could auto-populate this field with... Maybe I could get Wikimedia images on a future version or something like that. Any ideas?
