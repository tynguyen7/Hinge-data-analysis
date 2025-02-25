# Hinge-data-analysis
Cleaning, exploratory analysis, and data visualization of Hinge user data

### Cleaning ###
The **cleaning file** cleans the json file obtained from the Hinge download, creating a dataframe used in other files for exploratory analysis and data visualization. The columns include _id, interaction_type, and details_. _id_ is a value representing one user that you have interacted with, whether it is simply one outgoing like or a like, match, and chat with one individual. _interaction_type_ is a list (match, like, chats, or block) that identifies the total interactions that you had with a single individual. _value_ contains timestamp information, 'body' of the chats if relevant, and 'comment' left with a like if relevant.

### Data exploration and visualizations ###
The **chats analysis file** creates a dataframe for all chat interactions. The columns include _id, chat_body, and timestamp_. Each row represents one 'body' of chat, thus there may be multiple rows with the same id. In this file, you may create a word cloud of most used words in your chats. <br>
Further analysis is done on the time of day messages are sent, creating two plots: 1) date vs. count of outgoing messages, and 2) time period (late night, morning, afternoon, evening) vs. count of outgoing messages.

#### Word cloud ####
![Image](https://github.com/user-attachments/assets/49590122-3ee5-4149-aeb7-2c7ccb20ca07)

#### Chat plots ####
![Image](https://github.com/user-attachments/assets/90cb7ad8-c630-404d-ad55-c9f0899d79e8)

![Image](https://github.com/user-attachments/assets/92c4850b-a55a-48ed-8f4d-94290221e02b)

The **interactions file** also creates a dataframe for all interaction types. It is all-encompassing and has columns _we_met, outgoing_like, match, messages_exchanged, block, match_liked_you, removed_from_hinge, x_ed_out_from_likes, and like_sent_no_match_.  There are a few summary statements, such as "_Of the {X} people you matched with {Y} actually sent the like to you!_".  Further, the file includes a Sankey diagram to demonstrate the flow of interactions, from like to match to chat.

<img width="676" alt="Image" src="https://github.com/user-attachments/assets/02d71ca0-2ffe-4fa2-a96b-5e15e6fc3a68" />

Note: I assumed the definition of some of these columns due to a lack of information on how to accurately interpret the interactions from the app itself. For example, I interpreted an interaction that had a match included, but no like (where I interpreted all "like" interactions as outgoing) as _match_liked_you_, because there was a match and no outgoing like, thus it was an incoming like.
