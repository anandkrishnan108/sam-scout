import pandas
import discord
import csv

# print("Hello World")

client = discord.Client()
pandas.set_option('expand_frame_repr', False)
df = pandas.read_csv('players_22.csv')
commands_name = []
commands_index = []
command_counter = 0

long_names = []
short_names = []
ages = []
nationalities = []
overalls = []
potentials = []
current_clubs = []
parent_clubs = []
positions = []
transfer_values = []
wages = []
urls = []
preferred_feet = []

results = []


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    commands_name.clear()
    commands_index.clear()
    results.clear()
    short_names.clear()
    long_names.clear()
    nationalities.clear()
    ages.clear()
    overalls.clear()
    potentials.clear()
    current_clubs.clear()
    parent_clubs.clear()
    positions.clear()
    transfer_values.clear()
    wages.clear()
    urls.clear()
    preferred_feet.clear()

    user_input = message.content
    for i in user_input.split():
        if i.startswith("$"):
            index = user_input.index(i)
            commands_name.append(i)
            commands_index.append(index)
    num_commands = len(commands_name)
    print(commands_name)
    # print(commands_index)

    for c in commands_name:
        #    await message.channel.send('Hello!')
        if c == '$name':  # if user input contains the command $name
            # print('name block is running')
            position_of_command = commands_name.index(c)
            starting_index = commands_index[position_of_command] + 6  # index of first letter of name
            if position_of_command + 1 == num_commands:  # if this is the last command of the string
                ending_index = len(user_input)
            else:  # if there are more commands, then this string will end before the start of the next command
                ending_index = commands_index[position_of_command + 1]
            name = user_input[starting_index:ending_index]  # user entered name
            # await message.channel.send(input[ending_index])
            # if name[-1] == ' ':
            #    name = name[:-1]
            # await message.channel.send(name)
            # filter = df['short_name']
            # lastCSdf = df[filter == 'L. Messi']
            # results.append(lastCSdf)
            # lastCSdf.to_csv('players_22.csv', index=False, quoting=1)
            # await message.channel.send(resultswith open('Share.csv', 'r', newline='') as csvDataFile:
            with open('players_22.csv', 'r', newline='', encoding="utf8") as csvDataFile:  # links to csv file
                csv_reader = csv.DictReader(csvDataFile)
                for index, row in enumerate(csv_reader):  # loops through csv file
                    if row['short_name'] == name:  # if the user entered name is in the csv file
                        long_names.append(row['long_name'])
                        short_names.append(row['short_name'])
                        ages.append(row['age'])
                        nationalities.append(row['nationality_name'])
                        overalls.append(row['overall'])
                        potentials.append(row['potential'])
                        current_clubs.append(row['club_name'])
                        if row['club_loaned_from'] == '':
                            parent_clubs.append("NA")
                        else:
                            parent_clubs.append(row['club_loaned_from'])
                        positions.append(row['player_positions'])
                        transfer_values.append(row['value_eur'])
                        wages.append(row['wage_eur'])
                        urls.append(row['player_url'])
                        preferred_feet.append(row['preferred_foot'])

        elif c == '$nationality':
            # print('nationality block is running')
            position_of_command = commands_name.index(c)
            starting_index = commands_index[commands_name.index('$nationality')] + 13
            if position_of_command + 1 == num_commands:  # if this is the last command of the string
                ending_index = len(user_input)
            else:  # if there are more commands, then this string will end before the start of the next command
                ending_index = commands_index[position_of_command + 1]

            nationality = user_input[starting_index:ending_index]  # user entered name
            nationality = nationality.strip()
            print("nationality: " + nationality)
            # await message.channel.send(nationality)
            with open('players_22.csv', 'r', newline='', encoding="utf8") as csvDataFile:  # links to csv file
                csv_reader = csv.DictReader(csvDataFile)
                for index, row in enumerate(csv_reader):  # loops through csv file
                    if row['nationality_name'] == nationality:  # if the user entered name is in the csv file
                        long_names.append(row['long_name'])
                        short_names.append(row['short_name'])
                        ages.append(row['age'])
                        nationalities.append(row['nationality_name'])
                        overalls.append(row['overall'])
                        potentials.append(row['potential'])
                        current_clubs.append(row['club_name'])
                        if row['club_loaned_from'] == '':
                            parent_clubs.append("NA")
                        else:
                            parent_clubs.append(row['club_loaned_from'])
                        positions.append(row['player_positions'])
                        transfer_values.append(row['value_eur'])
                        wages.append(row['wage_eur'])
                        urls.append(row['player_url'])
                        preferred_feet.append(row['preferred_foot'])

        elif c == '$foot':
            position_of_command = commands_name.index(c)
            starting_index = commands_index[commands_name.index('$foot')] + 6
            if position_of_command + 1 == num_commands:  # if this is the last command of the string
                ending_index = len(user_input)
            else:  # if there are more commands, then this string will end before the start of the next command
                ending_index = commands_index[position_of_command + 1]

            foot = user_input[starting_index:ending_index].capitalize().strip()
            # print("foot: " + foot)
            with open('players_22.csv', 'r', newline='', encoding="utf8") as csvDataFile:  # links to csv file
                csv_reader = csv.DictReader(csvDataFile)
                for index, row in enumerate(csv_reader):  # loops through csv file
                    if row['preferred_foot'] == foot:
                        long_names.append(row['long_name'])
                        short_names.append(row['short_name'])
                        ages.append(row['age'])
                        nationalities.append(row['nationality_name'])
                        overalls.append(row['overall'])
                        potentials.append(row['potential'])
                        current_clubs.append(row['club_name'])
                        if row['club_loaned_from'] == '':
                            parent_clubs.append("NA")
                        else:
                            parent_clubs.append(row['club_loaned_from'])
                        positions.append(row['player_positions'])
                        transfer_values.append(row['value_eur'])
                        wages.append(row['wage_eur'])
                        urls.append(row['player_url'])
                        preferred_feet.append(row['preferred_foot'])

        elif c == '$club':
            position_of_command = commands_name.index(c)
            starting_index = commands_index[commands_name.index('$club')] + 6
            # print(starting_index)
            if position_of_command + 1 == num_commands:  # if this is the last command of the string
                ending_index = len(user_input)
            else:  # if there are more commands, then this string will end before the start of the next command
                ending_index = commands_index[position_of_command + 1]
            current_club = user_input[starting_index:ending_index]
            current_club = current_club.strip()
            # print("current club: " + current_club)
            with open('players_22.csv', 'r', newline='', encoding="utf8") as csvDataFile:  # links to csv file
                csv_reader = csv.DictReader(csvDataFile)
                for index, row in enumerate(csv_reader):  # loops through csv file
                    if row['club_name'] == current_club:
                        long_names.append(row['long_name'])
                        short_names.append(row['short_name'])
                        ages.append(row['age'])
                        nationalities.append(row['nationality_name'])
                        overalls.append(row['overall'])
                        potentials.append(row['potential'])
                        current_clubs.append(row['club_name'])
                        if row['club_loaned_from'] == '':
                            parent_clubs.append("NA")
                        else:
                            parent_clubs.append(row['club_loaned_from'])
                        positions.append(row['player_positions'])
                        transfer_values.append(row['value_eur'])
                        wages.append(row['wage_eur'])
                        urls.append(row['player_url'])
                        preferred_feet.append(row['preferred_foot'])

        elif c == '$parent_club':
            position_of_command = commands_name.index(c)
            starting_index = commands_index[commands_name.index('$parent_club')] + 13
            # print(starting_index)
            if position_of_command + 1 == num_commands:  # if this is the last command of the string
                ending_index = len(user_input)
            else:  # if there are more commands, then this string will end before the start of the next command
                ending_index = commands_index[position_of_command + 1]
            parent_club = user_input[starting_index:ending_index].strip()

            with open('players_22.csv', 'r', newline='', encoding="utf8") as csvDataFile:  # links to csv file
                csv_reader = csv.DictReader(csvDataFile)
                for index, row in enumerate(csv_reader):  # loops through csv file
                        long_names.append(row['long_name'])
                        short_names.append(row['short_name'])
                        ages.append(row['age'])
                        nationalities.append(row['nationality_name'])
                        overalls.append(row['overall'])
                        potentials.append(row['potential'])
                        current_clubs.append(row['club_name'])
                        if row['club_loaned_from'] == '':
                            parent_clubs.append("NA")
                        else:
                            parent_clubs.append(row['club_loaned_from'])
                        positions.append(row['player_positions'])
                        transfer_values.append(row['value_eur'])
                        wages.append(row['wage_eur'])
                        urls.append(row['player_url'])
                        preferred_feet.append(row['preferred_foot'])

        elif c == '$position':
            position_of_command = commands_name.index(c)
            starting_index = commands_index[commands_name.index('$position')] + 10
            if position_of_command + 1 == num_commands:  # if this is the last command of the string
                ending_index = len(user_input)
            else:  # if there are more commands, then this string will end before the start of the next command
                ending_index = commands_index[position_of_command + 1]
            position_string = user_input[starting_index:ending_index]
            position = position_string.strip().split()

            with open('players_22.csv', 'r', newline='', encoding="utf8") as csvDataFile:  # links to csv file
                csv_reader = csv.DictReader(csvDataFile)
                for index, row in enumerate(csv_reader):  # loops through csv file
                    for i in position:
                        if i in row['player_positions']:
                            long_names.append(row['long_name'])
                            short_names.append(row['short_name'])
                            ages.append(row['age'])
                            nationalities.append(row['nationality_name'])
                            overalls.append(row['overall'])
                            potentials.append(row['potential'])
                            current_clubs.append(row['club_name'])
                            if row['club_loaned_from'] == '':
                                parent_clubs.append("NA")
                            else:
                                parent_clubs.append(row['club_loaned_from'])
                            positions.append(row['player_positions'])
                            transfer_values.append(row['value_eur'])
                            wages.append(row['wage_eur'])
                            urls.append(row['player_url'])
                            preferred_feet.append(row['preferred_foot'])

        elif c == '$overall':
            position_of_command = commands_name.index(c)
            starting_index = commands_index[commands_name.index('$overall')] + 9
            # print(starting_index)
            if position_of_command + 1 == num_commands:  # if this is the last command of the string
                ending_index = len(user_input)
            else:  # if there are more commands, then this string will end before the start of the next command
                ending_index = commands_index[position_of_command + 1]
            overall_string = user_input[starting_index:ending_index]
            # print(overall_string)
            desired_overall = 0
            if '<' in overall_string:
                operator_occurrence = overall_string.index('<')
                desired_overall = overall_string[operator_occurrence+1:operator_occurrence+3]
                with open('players_22.csv', 'r', newline='', encoding="utf8") as csvDataFile:  # links to csv file
                    csv_reader = csv.DictReader(csvDataFile)
                    for index, row in enumerate(csv_reader):  # loops through csv file
                        if row['overall'] < desired_overall:
                            long_names.append(row['long_name'])
                            short_names.append(row['short_name'])
                            ages.append(row['age'])
                            nationalities.append(row['nationality_name'])
                            overalls.append(row['overall'])
                            potentials.append(row['potential'])
                            current_clubs.append(row['club_name'])
                            if row['club_loaned_from'] == '':
                                parent_clubs.append("NA")
                            else:
                                parent_clubs.append(row['club_loaned_from'])
                            positions.append(row['player_positions'])
                            transfer_values.append(row['value_eur'])
                            wages.append(row['wage_eur'])
                            urls.append(row['player_url'])
                            preferred_feet.append(row['preferred_foot'])
            elif '>' in overall_string:
                operator_occurrence = overall_string.index('>')
                desired_overall = overall_string[operator_occurrence+1:operator_occurrence+3]
                with open('players_22.csv', 'r', newline='', encoding="utf8") as csvDataFile:  # links to csv file
                    csv_reader = csv.DictReader(csvDataFile)
                    for index, row in enumerate(csv_reader):  # loops through csv file
                        if row['overall'] > desired_overall:
                            long_names.append(row['long_name'])
                            short_names.append(row['short_name'])
                            ages.append(row['age'])
                            nationalities.append(row['nationality_name'])
                            overalls.append(row['overall'])
                            preferred_feet.append(row['preferred_foot'])
                            potentials.append(row['potential'])
                            current_clubs.append(row['club_name'])
                            if row['club_loaned_from'] == '':
                                parent_clubs.append("NA")
                            else:
                                parent_clubs.append(row['club_loaned_from'])
                            positions.append(row['player_positions'])
                            transfer_values.append(row['value_eur'])
                            wages.append(row['wage_eur'])
                            urls.append(row['player_url'])
            if '-' in overall_string:
                operator_occurrence = overall_string.index('-')
                desired_min_overall = overall_string[operator_occurrence-2:operator_occurrence]
                desired_max_overall = overall_string[operator_occurrence+1:operator_occurrence+3]
                with open('players_22.csv', 'r', newline='', encoding="utf8") as csvDataFile:  # links to csv file
                    csv_reader = csv.DictReader(csvDataFile)
                    for index, row in enumerate(csv_reader):  # loops through csv file
                        if desired_min_overall <= row['overall'] <= desired_max_overall:
                            long_names.append(row['long_name'])
                            short_names.append(row['short_name'])
                            ages.append(row['age'])
                            nationalities.append(row['nationality_name'])
                            overalls.append(row['overall'])
                            potentials.append(row['potential'])
                            current_clubs.append(row['club_name'])
                            preferred_feet.append(row['preferred_foot'])
                            if row['club_loaned_from'] == '':
                                parent_clubs.append("NA")
                            else:
                                parent_clubs.append(row['club_loaned_from'])
                            positions.append(row['player_positions'])
                            transfer_values.append(row['value_eur'])
                            wages.append(row['wage_eur'])
                            urls.append(row['player_url'])
            else:
                desired_overall = overall_string[0:len(overall_string)].strip()
                print(desired_overall)
                with open('players_22.csv', 'r', newline='', encoding="utf8") as csvDataFile:  # links to csv file
                    csv_reader = csv.DictReader(csvDataFile)
                    for index, row in enumerate(csv_reader):  # loops through csv file
                        if row['overall'] == desired_overall:
                            long_names.append(row['long_name'])
                            short_names.append(row['short_name'])
                            preferred_feet.append(row['preferred_foot'])
                            ages.append(row['age'])
                            nationalities.append(row['nationality_name'])
                            overalls.append(row['overall'])
                            potentials.append(row['potential'])
                            current_clubs.append(row['club_name'])
                            if row['club_loaned_from'] == '':
                                parent_clubs.append("NA")
                            else:
                                parent_clubs.append(row['club_loaned_from'])
                            positions.append(row['player_positions'])
                            transfer_values.append(row['value_eur'])
                            wages.append(row['wage_eur'])
                            urls.append(row['player_url'])

        elif c == '$potential':
            position_of_command = commands_name.index(c)
            starting_index = commands_index[commands_name.index('$potential')] + 11
            # print(starting_index)
            if position_of_command + 1 == num_commands:  # if this is the last command of the string
                ending_index = len(user_input)
            else:  # if there are more commands, then this string will end before the start of the next command
                ending_index = commands_index[position_of_command + 1]
            potential_string = user_input[starting_index:ending_index]
            print(potential_string)
            desired_potential = 0
            if '<' in potential_string:
                operator_occurrence = potential_string.index('<')
                desired_potential = potential_string[operator_occurrence+1:operator_occurrence+3]
                with open('players_22.csv', 'r', newline='', encoding="utf8") as csvDataFile:  # links to csv file
                    csv_reader = csv.DictReader(csvDataFile)
                    for index, row in enumerate(csv_reader):  # loops through csv file
                        if row['potential'] < desired_potential:
                            long_names.append(row['long_name'])
                            short_names.append(row['short_name'])
                            ages.append(row['age'])
                            preferred_feet.append(row['preferred_foot'])
                            nationalities.append(row['nationality_name'])
                            overalls.append(row['overall'])
                            potentials.append(row['potential'])
                            current_clubs.append(row['club_name'])
                            if row['club_loaned_from'] == '':
                                parent_clubs.append("NA")
                            else:
                                parent_clubs.append(row['club_loaned_from'])
                            positions.append(row['player_positions'])
                            transfer_values.append(row['value_eur'])
                            wages.append(row['wage_eur'])
                            urls.append(row['player_url'])
            elif '>' in potential_string:
                operator_occurrence = potential_string.index('>')
                desired_potential = potential_string[operator_occurrence+1:operator_occurrence+3]
                with open('players_22.csv', 'r', newline='', encoding="utf8") as csvDataFile:  # links to csv file
                    csv_reader = csv.DictReader(csvDataFile)
                    for index, row in enumerate(csv_reader):  # loops through csv file
                        if row['potential'] > desired_potential:
                            long_names.append(row['long_name'])
                            preferred_feet.append(row['preferred_foot'])
                            short_names.append(row['short_name'])
                            ages.append(row['age'])
                            nationalities.append(row['nationality_name'])
                            overalls.append(row['overall'])
                            potentials.append(row['potential'])
                            current_clubs.append(row['club_name'])
                            if row['club_loaned_from'] == '':
                                parent_clubs.append("NA")
                            else:
                                parent_clubs.append(row['club_loaned_from'])
                            positions.append(row['player_positions'])
                            transfer_values.append(row['value_eur'])
                            wages.append(row['wage_eur'])
                            urls.append(row['player_url'])
            if '-' in potential_string:
                operator_occurrence = potential_string.index('-')
                desired_min_potential = potential_string[operator_occurrence-2:operator_occurrence]
                desired_max_potential = potential_string[operator_occurrence+1:operator_occurrence+3]
                with open('players_22.csv', 'r', newline='', encoding="utf8") as csvDataFile:  # links to csv file
                    csv_reader = csv.DictReader(csvDataFile)
                    for index, row in enumerate(csv_reader):  # loops through csv file
                        if desired_min_potential <= row['potential'] <= desired_max_potential:
                            long_names.append(row['long_name'])
                            short_names.append(row['short_name'])
                            ages.append(row['age'])
                            nationalities.append(row['nationality_name'])
                            overalls.append(row['overall'])
                            preferred_feet.append(row['preferred_foot'])
                            potentials.append(row['potential'])
                            current_clubs.append(row['club_name'])
                            if row['club_loaned_from'] == '':
                                parent_clubs.append("NA")
                            else:
                                parent_clubs.append(row['club_loaned_from'])
                            positions.append(row['player_positions'])
                            transfer_values.append(row['value_eur'])
                            wages.append(row['wage_eur'])
                            urls.append(row['player_url'])
            else:
                desired_potential = potential_string[0:len(potential_string)]
                with open('players_22.csv', 'r', newline='', encoding="utf8") as csvDataFile:  # links to csv file
                    csv_reader = csv.DictReader(csvDataFile)
                    for index, row in enumerate(csv_reader):  # loops through csv file
                        if row['potential'] == desired_potential:
                            long_names.append(row['long_name'])
                            preferred_feet.append(row['preferred_foot'])
                            short_names.append(row['short_name'])
                            ages.append(row['age'])
                            nationalities.append(row['nationality_name'])
                            overalls.append(row['overall'])
                            potentials.append(row['potential'])
                            current_clubs.append(row['club_name'])
                            if row['club_loaned_from'] == '':
                                parent_clubs.append("NA")
                            else:
                                parent_clubs.append(row['club_loaned_from'])
                            positions.append(row['player_positions'])
                            transfer_values.append(row['value_eur'])
                            wages.append(row['wage_eur'])
                            urls.append(row['player_url'])

        elif c == '$age':
            position_of_command = commands_name.index(c)
            starting_index = commands_index[commands_name.index('$age')] + 5
            # print(starting_index)
            if position_of_command + 1 == num_commands:  # if this is the last command of the string
                ending_index = len(user_input)
            else:  # if there are more commands, then this string will end before the start of the next command
                ending_index = commands_index[position_of_command + 1]
            age_string = user_input[starting_index:ending_index]
            print(age_string)
            desired_age = 0
            if '<' in age_string:
                operator_occurrence = age_string.index('<')
                desired_age = age_string[operator_occurrence + 1:operator_occurrence + 3]
                with open('players_22.csv', 'r', newline='', encoding="utf8") as csvDataFile:  # links to csv file
                    csv_reader = csv.DictReader(csvDataFile)
                    for index, row in enumerate(csv_reader):  # loops through csv file
                        if row['age'] < desired_age:
                            long_names.append(row['long_name'])
                            short_names.append(row['short_name'])
                            ages.append(row['age'])
                            nationalities.append(row['nationality_name'])
                            overalls.append(row['overall'])
                            potentials.append(row['potential'])
                            current_clubs.append(row['club_name'])
                            preferred_feet.append(row['preferred_foot'])
                            if row['club_loaned_from'] == '':
                                parent_clubs.append("NA")
                            else:
                                parent_clubs.append(row['club_loaned_from'])
                            positions.append(row['player_positions'])
                            transfer_values.append(row['value_eur'])
                            wages.append(row['wage_eur'])
                            urls.append(row['player_url'])
            elif '>' in age_string:
                operator_occurrence = age_string.index('>')
                desired_age = age_string[operator_occurrence + 1:operator_occurrence + 3]
                with open('players_22.csv', 'r', newline='', encoding="utf8") as csvDataFile:  # links to csv file
                    csv_reader = csv.DictReader(csvDataFile)
                    for index, row in enumerate(csv_reader):  # loops through csv file
                        if row['age'] > desired_age:
                            long_names.append(row['long_name'])
                            short_names.append(row['short_name'])
                            ages.append(row['age'])
                            preferred_feet.append(row['preferred_foot'])
                            nationalities.append(row['nationality_name'])
                            overalls.append(row['overall'])
                            potentials.append(row['potential'])
                            current_clubs.append(row['club_name'])
                            if row['club_loaned_from'] == '':
                                parent_clubs.append("NA")
                            else:
                                parent_clubs.append(row['club_loaned_from'])
                            positions.append(row['player_positions'])
                            transfer_values.append(row['value_eur'])
                            wages.append(row['wage_eur'])
                            urls.append(row['player_url'])
            if '-' in age_string:
                operator_occurrence = age_string.index('-')
                desired_min_age = age_string[operator_occurrence - 2:operator_occurrence]
                desired_max_age = age_string[operator_occurrence + 1:operator_occurrence + 3]
                with open('players_22.csv', 'r', newline='', encoding="utf8") as csvDataFile:  # links to csv file
                    csv_reader = csv.DictReader(csvDataFile)
                    for index, row in enumerate(csv_reader):  # loops through csv file
                        if desired_min_age <= row['age'] <= desired_max_age:
                            long_names.append(row['long_name'])
                            short_names.append(row['short_name'])
                            ages.append(row['age'])
                            nationalities.append(row['nationality_name'])
                            overalls.append(row['overall'])
                            potentials.append(row['potential'])
                            preferred_feet.append(row['preferred_foot'])
                            current_clubs.append(row['club_name'])
                            if row['club_loaned_from'] == '':
                                parent_clubs.append("NA")
                            else:
                                parent_clubs.append(row['club_loaned_from'])
                            positions.append(row['player_positions'])
                            transfer_values.append(row['value_eur'])
                            wages.append(row['wage_eur'])
                            urls.append(row['player_url'])
            else:
                desired_age = age_string[0:len(age_string)]
                with open('players_22.csv', 'r', newline='', encoding="utf8") as csvDataFile:  # links to csv file
                    csv_reader = csv.DictReader(csvDataFile)
                    for index, row in enumerate(csv_reader):  # loops through csv file
                        if row['age'] == desired_age:
                            long_names.append(row['long_name'])
                            short_names.append(row['short_name'])
                            ages.append(row['age'])
                            nationalities.append(row['nationality_name'])
                            overalls.append(row['overall'])
                            potentials.append(row['potential'])
                            preferred_feet.append(row['preferred_foot'])
                            current_clubs.append(row['club_name'])
                            if row['club_loaned_from'] == '':
                                parent_clubs.append("NA")
                            else:
                                parent_clubs.append(row['club_loaned_from'])
                            positions.append(row['player_positions'])
                            transfer_values.append(row['value_eur'])
                            wages.append(row['wage_eur'])
                            urls.append(row['player_url'])

        elif c == '$transfer_value':
            position_of_command = commands_name.index(c)
            starting_index = commands_index[commands_name.index('$transfer_value')] + 15
            # print(starting_index)
            if position_of_command + 1 == num_commands:  # if this is the last command of the string
                ending_index = len(user_input)
            else:  # if there are more commands, then this string will end before the start of the next command
                ending_index = commands_index[position_of_command + 1]
            transfer_value_string = user_input[starting_index:ending_index].strip()
            print(transfer_value_string)
            desired_transfer_value = 0
            if '<' in transfer_value_string:
                operator_occurrence = transfer_value_string.index('<')
                num_zeroes = int(str(transfer_value_string).count('0'))
                desired_transfer_value = transfer_value_string[operator_occurrence+1:operator_occurrence+num_zeroes+2]
                with open('players_22.csv', 'r', newline='', encoding="utf8") as csvDataFile:  # links to csv file
                    csv_reader = csv.DictReader(csvDataFile)
                    for index, row in enumerate(csv_reader):  # loops through csv file
                        if row['value_eur'] == '':
                            row['value_eur'] = 0
                        if int(row['value_eur']) < int(desired_transfer_value):
                            long_names.append(row['long_name'])
                            short_names.append(row['short_name'])
                            ages.append(row['age'])
                            preferred_feet.append(row['preferred_foot'])
                            nationalities.append(row['nationality_name'])
                            overalls.append(row['overall'])
                            potentials.append(row['potential'])
                            current_clubs.append(row['club_name'])
                            if row['club_loaned_from'] == '':
                                parent_clubs.append("NA")
                            else:
                                parent_clubs.append(row['club_loaned_from'])
                            positions.append(row['player_positions'])
                            transfer_values.append(row['value_eur'])
                            wages.append(row['wage_eur'])
                            urls.append(row['player_url'])
            elif '>' in transfer_value_string:
                operator_occurrence = transfer_value_string.index('>')
                num_zeroes = int(str(transfer_value_string).count('0'))
                desired_transfer_value = transfer_value_string[operator_occurrence + 1:operator_occurrence + num_zeroes + 2]
                print("desired transfer value: " + str(desired_transfer_value))
                with open('players_22.csv', 'r', newline='', encoding="utf8") as csvDataFile:  # links to csv file
                    csv_reader = csv.DictReader(csvDataFile)
                    for index, row in enumerate(csv_reader):  # loops through csv file
                        if row['value_eur'] == '':
                            row['value_eur'] = 0
                        if int(row['value_eur']) > int(desired_transfer_value):
                            long_names.append(row['long_name'])
                            short_names.append(row['short_name'])
                            ages.append(row['age'])
                            nationalities.append(row['nationality_name'])
                            preferred_feet.append(row['preferred_foot'])
                            overalls.append(row['overall'])
                            potentials.append(row['potential'])
                            current_clubs.append(row['club_name'])
                            if row['club_loaned_from'] == '':
                                parent_clubs.append("NA")
                            else:
                                parent_clubs.append(row['club_loaned_from'])
                            positions.append(row['player_positions'])
                            transfer_values.append(row['value_eur'])
                            wages.append(row['wage_eur'])
                            urls.append(row['player_url'])
            if '-' in transfer_value_string:
                operator_occurrence = transfer_value_string.index('-')
                num_zeroes = 0
                for char in transfer_value_string:
                    if char == '0':
                        num_zeroes += 1
                    if char == '-':
                        break
                # print(operator_occurrence)
                # print(num_zeroes)
                desired_min_transfer_value = transfer_value_string[operator_occurrence-(num_zeroes+1):operator_occurrence]
                num_zeroes = int(str(transfer_value_string).count('0'))
                desired_max_transfer_value = int(transfer_value_string[operator_occurrence+1:operator_occurrence+num_zeroes+2])
                # print("min: " + str(desired_min_transfer_value))
                # print("max: " + str(desired_max_transfer_value))
                with open('players_22.csv', 'r', newline='', encoding="utf8") as csvDataFile:  # links to csv file
                    csv_reader = csv.DictReader(csvDataFile)
                    for index, row in enumerate(csv_reader):  # loops through csv file
                        if row['value_eur'] == '':
                            row['value_eur'] = 0

                        if int(desired_min_transfer_value) <= int(row['value_eur']) <= int(desired_max_transfer_value):
                            long_names.append(row['long_name'])
                            short_names.append(row['short_name'])
                            preferred_feet.append(row['preferred_foot'])
                            ages.append(row['age'])
                            nationalities.append(row['nationality_name'])
                            overalls.append(row['overall'])
                            potentials.append(row['potential'])
                            current_clubs.append(row['club_name'])
                            if row['club_loaned_from'] == '':
                                parent_clubs.append("NA")
                            else:
                                parent_clubs.append(row['club_loaned_from'])
                            positions.append(row['player_positions'])
                            transfer_values.append(row['value_eur'])
                            wages.append(row['wage_eur'])
                            urls.append(row['player_url'])
            else:
                desired_transfer_value = transfer_value_string[0:len(transfer_value_string)]
                with open('players_22.csv', 'r', newline='', encoding="utf8") as csvDataFile:  # links to csv file
                    csv_reader = csv.DictReader(csvDataFile)
                    for index, row in enumerate(csv_reader):  # loops through csv file
                        if row['value_eur'] == desired_transfer_value:
                            long_names.append(row['long_name'])
                            short_names.append(row['short_name'])
                            ages.append(row['age'])
                            preferred_feet.append(row['preferred_foot'])
                            nationalities.append(row['nationality_name'])
                            overalls.append(row['overall'])
                            potentials.append(row['potential'])
                            current_clubs.append(row['club_name'])
                            if row['club_loaned_from'] == '':
                                parent_clubs.append("NA")
                            else:
                                parent_clubs.append(row['club_loaned_from'])
                            positions.append(row['player_positions'])
                            transfer_values.append(row['value_eur'])
                            wages.append(row['wage_eur'])
                            urls.append(row['player_url'])

        elif c == '$wage':
            position_of_command = commands_name.index(c)
            starting_index = commands_index[commands_name.index('$wage')] + 6
            # print(starting_index)
            if position_of_command + 1 == num_commands:  # if this is the last command of the string
                ending_index = len(user_input)
            else:  # if there are more commands, then this string will end before the start of the next command
                ending_index = commands_index[position_of_command + 1]
            wage_string = user_input[starting_index:ending_index].strip()
            print(wage_string)
            desired_wage = 0
            if '<' in wage_string:
                operator_occurrence = wage_string.index('<')
                num_zeroes = int(str(wage_string).count('0'))
                desired_wage = wage_string[operator_occurrence + 1:operator_occurrence + num_zeroes + 2]
                with open('players_22.csv', 'r', newline='', encoding="utf8") as csvDataFile:  # links to csv file
                    csv_reader = csv.DictReader(csvDataFile)
                    for index, row in enumerate(csv_reader):  # loops through csv file
                        if row['wage_eur'] == '':
                            row['wage_eur'] = 0
                        if int(row['wage_eur']) < int(desired_wage):
                            long_names.append(row['long_name'])
                            short_names.append(row['short_name'])
                            ages.append(row['age'])
                            nationalities.append(row['nationality_name'])
                            overalls.append(row['overall'])
                            potentials.append(row['potential'])
                            current_clubs.append(row['club_name'])
                            if row['club_loaned_from'] == '':
                                parent_clubs.append("NA")
                            else:
                                parent_clubs.append(row['club_loaned_from'])
                            positions.append(row['player_positions'])
                            transfer_values.append(row['value_eur'])
                            wages.append(row['wage_eur'])
                            urls.append(row['player_url'])
                            preferred_feet.append(row['preferred_foot'])
            elif '>' in wage_string:
                operator_occurrence = wage_string.index('>')
                num_zeroes = int(str(wage_string).count('0'))
                desired_wage = wage_string[operator_occurrence + 1:operator_occurrence + num_zeroes + 2]
                with open('players_22.csv', 'r', newline='', encoding="utf8") as csvDataFile:  # links to csv file
                    csv_reader = csv.DictReader(csvDataFile)
                    for index, row in enumerate(csv_reader):  # loops through csv file
                        if row['wage_eur'] == '':
                            row['wage_eur'] = 0
                        if int(row['wage_eur']) > int(desired_wage):
                            long_names.append(row['long_name'])
                            short_names.append(row['short_name'])
                            ages.append(row['age'])
                            nationalities.append(row['nationality_name'])
                            overalls.append(row['overall'])
                            potentials.append(row['potential'])
                            current_clubs.append(row['club_name'])
                            if row['club_loaned_from'] == '':
                                parent_clubs.append("NA")
                            else:
                                parent_clubs.append(row['club_loaned_from'])
                            positions.append(row['player_positions'])
                            transfer_values.append(row['value_eur'])
                            wages.append(row['wage_eur'])
                            urls.append(row['player_url'])
                            preferred_feet.append(row['preferred_foot'])
            if '-' in wage_string:
                operator_occurrence = wage_string.index('-')
                num_zeroes = 0
                for char in wage_string:
                    if char == '0':
                        num_zeroes += 1
                    if char == '-':
                        break
                # print(operator_occurrence)
                # print(num_zeroes)
                desired_min_wage = wage_string[operator_occurrence - (num_zeroes + 2):operator_occurrence]
                num_zeroes = int(str(wage_string).count('0'))
                desired_max_wage = int(wage_string[operator_occurrence + 1:operator_occurrence + num_zeroes + 2])
                print("min: " + str(desired_min_wage))
                print("max: " + str(desired_max_wage))
                with open('players_22.csv', 'r', newline='', encoding="utf8") as csvDataFile:  # links to csv file
                    csv_reader = csv.DictReader(csvDataFile)
                    for index, row in enumerate(csv_reader):  # loops through csv file
                        if row['wage_eur'] == '':
                            row['wage_eur'] = 0
                        if int(desired_min_wage) <= int(row['wage_eur']) <= int(desired_max_wage):
                            long_names.append(row['long_name'])
                            short_names.append(row['short_name'])
                            ages.append(row['age'])
                            nationalities.append(row['nationality_name'])
                            overalls.append(row['overall'])
                            potentials.append(row['potential'])
                            current_clubs.append(row['club_name'])
                            if row['club_loaned_from'] == '':
                                parent_clubs.append("NA")
                            else:
                                parent_clubs.append(row['club_loaned_from'])
                            positions.append(row['player_positions'])
                            transfer_values.append(row['value_eur'])
                            wages.append(row['wage_eur'])
                            urls.append(row['player_url'])
                            preferred_feet.append(row['preferred_foot'])
            else:
                desired_wage = wage_string[0:len(wage_string)]
                with open('players_22.csv', 'r', newline='', encoding="utf8") as csvDataFile:  # links to csv file
                    csv_reader = csv.DictReader(csvDataFile)
                    for index, row in enumerate(csv_reader):  # loops through csv file
                        if row['wage_eur'] == desired_wage:
                            long_names.append(row['long_name'])
                            short_names.append(row['short_name'])
                            ages.append(row['age'])
                            nationalities.append(row['nationality_name'])
                            overalls.append(row['overall'])
                            potentials.append(row['potential'])
                            current_clubs.append(row['club_name'])
                            if row['club_loaned_from'] == '':
                                parent_clubs.append("NA")
                            else:
                                parent_clubs.append(row['club_loaned_from'])
                            positions.append(row['player_positions'])
                            transfer_values.append(row['value_eur'])
                            wages.append(row['wage_eur'])
                            urls.append(row['player_url'])
                            preferred_feet.append(row['preferred_foot'])
                            wages.append(row['wage_eur'])
                            urls.append(row['player_url'])

    for name in long_names:
        if long_names.count(name) == len(commands_name):
            i = long_names.index(name)
            results.append(
                "Full Name: " + name + "\nShort name: " + short_names[i] + "\nAge: " + ages[i] + "\nNationality: " +
                nationalities[i] + "\nOverall: " +
                overalls[i]
                + "\nPotential: " + potentials[i] + "\nCurrent club: " + current_clubs[i]
                + "\nParent club: " + parent_clubs[i]
                + "\nPosition: " + positions[i] + "\nPreferred foot: " + preferred_feet[i] + "\nCurrent value (EUR): " + str(transfer_values[i])
                + "\nCurrent weekly wage (EUR): " + str(wages[i]) + '\nMore information: ' + urls[i])

    results_refined = []
    for i in results:
        if i not in results_refined:
            results_refined.append(i)

    for x in results_refined:
        await message.channel.send(x)

    # print(results)


token = 'OTg0ODExNTk4MzM2MTEwNjUy.GK92FW.GGjqAWgJkP0y4nrHfktn9Oq_tk2g-QseH2oXFY'
client.run(token)
