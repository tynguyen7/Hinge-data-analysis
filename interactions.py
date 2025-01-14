# Set up dictionary
id_all_interactions = {}

for index, details in df.iterrows():
    interaction_id = details['id']
    interaction_type = details['interaction_type']

    # Check if id is already in the list, setting interactions to empty list
    if interaction_id not in id_all_interactions:
        id_all_interactions[interaction_id] = {'interactions': []}

    # Accessing specific id's dictionary of interactions, then accessing the list of interactions
    id_all_interactions[interaction_id]['interactions'].append(interaction_type)

# Set up dataframe for columns id and interactions, for list of all interaction types associated with that id
interactions_df = pd.DataFrame.from_dict(id_all_interactions, orient = 'index')
interactions_df.reset_index(inplace=True)
interactions_df.rename(columns = {'index': 'id', 'interactions': 'interactions'}, inplace = True)

# Adding columns to dataframe for each individual interaction
# Setting default to 0
interactions_df['we_met'] = 0
interactions_df['outgoing_like'] = 0
interactions_df['match'] = 0
interactions_df['messages_exchanged'] = 0
interactions_df['block'] = 0
interactions_df['match_liked_you'] = 0
interactions_df['removed_from_hinge'] = 0
interactions_df['x_ed_out_from_likes'] = 0
interactions_df['like_sent_no_match'] = 0

for index, row_info in interactions_df.iterrows():

    # row_info['interactions'] accesses the list of interactions for each id
    for i in row_info['interactions']:
        if i == 'we_met':
            interactions_df.loc[index, 'we_met'] = 1

        if i == 'like':
            interactions_df.loc[index,'outgoing_like'] = 1

        if i == 'match':
            interactions_df.loc[index, 'match'] = 1

        if i == 'chats':
            interactions_df.loc[index, 'messages_exchanged'] = 1

        if i == 'block':
            interactions_df.loc[index, 'block'] = 1

        if 'match' in interactions and 'like' not in interactions:
            interactions_df.loc[index, 'match_liked_you'] = 1

        if 'block' in interactions and len(interactions) >= 2:
            interactions_df.loc[index, 'removed_from_hinge'] = 1

        if 'block' in interactions and len(interactions) == 1:
            interactions_df.loc[index, 'x_ed_out_from_likes'] = 1

        if 'like' in interactions and 'match' not in interactions:
            interactions_df.loc[index, 'like_sent_no_match'] = 1

# Dictionary summarizing total number of interactions per type
interactions_dict = {
    'met_in_real_life': 0,
    'outgoing_like': 0,
    'match': 0,
    'any_messages_exchanged': 0,
    'block': 0
    'match_liked_you': 0,
    'removed_from_hinge': 0,
    'x_ed_out_from_likes': 0,
    'like_sent_no_match': 0
}

for index, row_info in interactions_df.iterrows():
    if interactions_df.loc[index, 'we_met'] == 1:
        interactions_dict['met_in_real_life'] += 1
    if interactions_df.loc[index, 'outgoing_like'] == 1:
        interactions_dict['outgoing_like'] += 1
    if interactions_df.loc[index, 'match'] == 1:
        interactions_dict['match'] += 1
    if interactions_df.loc[index, 'messages_exchanged'] == 1:
        interactions_dict['any_messages_exchanged'] += 1
    if interactions_df.loc[index, 'block'] == 1:
        interactions_dict['block'] +=1
    if interactions_df.loc[index, 'match_liked_you'] == 1:
        interactions_dict['match_liked_you'] += 1
    if interactions_df.loc[index, 'removed_from_hinge'] == 1:
        interactions_dict['removed_from_hinge'] += 1
    if interactions_df.loc[index, 'x_ed_out_from_likes'] == 1:
        interactions_dict['x_ed_out_from_likes'] += 1
    if interaction_df.loc[index, 'like_sent_no_match'] == 1:
        interactions_dict['like_sent_no_match'] += 1

interactions_dict

# Summary in writing
print (f"Of the {interactions_dict['match']} people you matched with, {interactions_meanings_dict['match_liked_you']} actually sent the like to you!")
print (f"Of the {interactions_dict['match']} people you matched with, you removed {interactions_meanings_dict['removed_from_hinge']}...")
print (f"You removed {interactions_meanings_dict['x_ed_out_from_likes']} people from your likes.")
print (f"Of the {interactions_dict['outgoing_like']} likes you sent, you didn't match with {interactions_meanings_dict['like_sent_no_match']}")

# Sankey diagram for interactions
fig = go.Figure(data = [go.Sankey(
    node = dict(
        pad = 25,
        thickness = 15,
        line = dict(color = 'black', width = 0.5),
        label = ['Likes sent ()', 'Likes received ()', 'Removed from likes ()', 'Match! ()', 'No match ()', 'Met ()', 'Deleted ()', 'Messaged ()'],
        color = 'blue',
        # Arbitrary values for height of Sankey bars
        x = [0, 0, 0.5, 0.5, 0.5, 1, 1, 1],
        y = [0.6, .4, 0.05, 0.4, 1, 0.2, 0.7, 0.5]
    ),

    link = dict(
        source = [1, 1, 0, 0, 3, 3, 3],
        target = [2, 3, 3, 4, 5, 6, 7],
        value = [REPLACE_WITH_YOUR_VALUES],
        color = 'rgba(135, 206, 235, 0.5)'
    ))])

fig.update_layout(title_text = "Sankey Diagram for all-time Hinge data", font_size = 15)
fig.show()
